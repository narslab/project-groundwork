# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 09:14:58 2021

@author: Mahsa
"""

import pandas as pd
import Network as network
import analyze_result
import Simulate


### Redefine analyze result cost function just for SQ
def calculate_cost_npv_S1(data, data_broadband):
    # S1
    df_output_S1=Simulate.run_cost_simulation_S1(data, data_broadband)
    df_analyze_result_S1=df_output_S1.groupby(level=[0])[['capex_el','opex_el','lifecycle_infrastructure_el','environmental_restoration_el','non_fatal_el','fatal_el','safety_el','total_cost_el','capex_br','opex_br','lifecycle_infrastructure_br','environmental_restoration_br','non_fatal_br','fatal_br','safety_br','total_cost_br']].sum()
    df_analyze_result_S1.insert(0, "year", range(data.parameter_dict['analysis_years']), True)    
      
    # NPV
    S1_npv_infrastructure_cost_el=[]
    S1_npv_environmental_cost_el=[]
    S1_npv_safety_cost_el=[]
    S1_npv_total_cost_el=[]
    S1_npv_infrastructure_cost_br=[]
    S1_npv_environmental_cost_br=[]
    S1_npv_safety_cost_br=[]
    S1_npv_total_cost_br=[]
    for index, row in df_analyze_result_S1.iterrows():
        S1_npv_infrastructure_cost_el.append(row['lifecycle_infrastructure_el']/(1+data.parameter_dict['r'])**index)
        S1_npv_environmental_cost_el.append(row['environmental_restoration_el']/(1+data.parameter_dict['r'])**index)
        S1_npv_safety_cost_el.append(row['safety_el']/(1+data.parameter_dict['r'])**index)
        S1_npv_total_cost_el.append(row['total_cost_el']/(1+data.parameter_dict['r'])**index)
        S1_npv_infrastructure_cost_br.append(row['lifecycle_infrastructure_br']/(1+data_broadband.parameter_dict['r'])**index)
        S1_npv_environmental_cost_br.append(row['environmental_restoration_br']/(1+data_broadband.parameter_dict['r'])**index)
        S1_npv_safety_cost_br.append(row['safety_br']/(1+data_broadband.parameter_dict['r'])**index)
        S1_npv_total_cost_br.append(row['total_cost_br']/(1+data_broadband.parameter_dict['r'])**index)
    S1_total_infrastructre_el=sum(S1_npv_infrastructure_cost_el)
    S1_total_environmental_el=sum(S1_npv_environmental_cost_el)
    S1_total_safety_el=sum(S1_npv_safety_cost_el)
    S1_total_cost_el=sum(S1_npv_total_cost_el)
    S1_total_infrastructre_br=sum(S1_npv_infrastructure_cost_br)
    S1_total_environmental_br=sum(S1_npv_environmental_cost_br)
    S1_total_safety_br=sum(S1_npv_safety_cost_br)
    S1_total_cost_br=sum(S1_npv_total_cost_br)
    S1_df_npv= pd.DataFrame({'lifecycle_infrastructure_el':[S1_total_infrastructre_el],
                             'environmental_restoration_el':[S1_total_environmental_el],
                             'safety_el':[S1_total_safety_el],
                             'total_cost_el':[S1_total_cost_el],
                             'lifecycle_infrastructure_br':[S1_total_infrastructre_br],
                             'environmental_restoration_br':[S1_total_environmental_br],
                             'safety_br':[S1_total_safety_br],
                             'total_cost_br':[S1_total_cost_br]},
                            )
    total_cost=S1_df_npv['total_cost_el']+S1_df_npv['total_cost_br']
    return(total_cost)


### run cost sensitivity analysis for a parameter
def run_sensitivity_cost_SQ(parameter1, percentage_change1,
                                                parameter2=None, percentage_change2=None, broadband=False):
    if broadband==True:
        data=network.Broadband_model_inputs()
        model_data=network.Electric_model_inputs()
        if  parameter2==None:           
            new_data1=network.Broadband_model_inputs()
            new_data1.modify_parameter(parameter1, percentage_change1)
            original_result=calculate_cost_npv_S1(data, model_data)
            new_result=calculate_cost_npv_S1(data, new_data1)
        else:
            new_data1=network.Broadband_model_inputs()
            new_data1.modify_parameter(parameter1, percentage_change1, parameter2)
            original_result=calculate_cost_npv_S1(data, model_data)
            new_result=calculate_cost_npv_S1(data, new_data1)
    else:
        data=network.Broadband_model_inputs()
        model_data=network.Electric_model_inputs()
        if  parameter2==None:
            new_data1=network.Electric_model_inputs()
            new_data1.modify_parameter(parameter1, percentage_change1)
            original_result=calculate_cost_npv_S1(model_data, data)
            new_result=calculate_cost_npv_S1(new_data1, data)
        else:
            new_data1=network.Electric_model_inputs()
            new_data1.modify_parameter(parameter1, percentage_change1, parameter2)
            original_result=calculate_cost_npv_S1(model_data, data)
            new_result=calculate_cost_npv_S1(new_data1, data)
    Percentage_change_result=(new_result-original_result)/original_result*100
    print(Percentage_change_result)
    return (Percentage_change_result)

## Redefine analyze result benefit function just for SQ
def calculate_benefit_npv_S1(data, data_broadband):
    # S1
    df_output_S1=Simulate.run_benefit_simulation_S1(data, data_broadband)
    df_analyze_result_S1=df_output_S1.groupby(level=[0])[['aesthetic_benefit_el','economic_losses_el','aesthetic_benefit_br','economic_loss_br']].sum()
    df_analyze_result_S1.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    df_analyze_result_S1.to_csv(r'../../results/outcomes/Benefit/Analyze result/benefit-analyze-result-S1.csv', index = False) 
    
    # NPV
    S1_npv_aesthetic_benefit_el=[]
    S1_npv_economic_losses_el=[]
    S1_npv_aesthetic_benefit_br=[]
    S1_npv_economic_loss_br=[]
    for index, row in df_analyze_result_S1.iterrows():
        S1_npv_aesthetic_benefit_el.append(row['aesthetic_benefit_el']/(1+data.parameter_dict['r'])**index)
        S1_npv_economic_losses_el.append(row['economic_losses_el']/(1+data.parameter_dict['r'])**index)
        S1_npv_aesthetic_benefit_br.append(row['aesthetic_benefit_br']/(1+data_broadband.parameter_dict['r'])**index)
        S1_npv_economic_loss_br.append(row['economic_loss_br']/(1+data_broadband.parameter_dict['r'])**index)
    S1_total_aesthetic_benefit_el=sum(S1_npv_aesthetic_benefit_el)
    S1_total_economic_losses_el=sum(S1_npv_economic_losses_el)
    S1_total_aesthetic_benefit_br=sum(S1_npv_aesthetic_benefit_br)
    S1_total_economic_loss_br=sum(S1_npv_economic_loss_br)
    S1_df_npv= pd.DataFrame({'aesthetic_benefit_el':[S1_total_aesthetic_benefit_el],
                             'economic_losses_el':[S1_total_economic_losses_el],
                             'aesthetic_benefit_br':[S1_total_aesthetic_benefit_br],
                             'economic_loss_br':[S1_total_economic_loss_br]},
                            )
    total_benefit=S1_df_npv['aesthetic_benefit_el']-S1_df_npv['economic_losses_el']+S1_df_npv['aesthetic_benefit_br']-S1_df_npv['economic_loss_br']
    return(total_benefit)

### run benefit sensitivity analysis for a parameter
def run_sensitivity_benefit_SQ(parameter1, percentage_change1,
                                                parameter2=None, percentage_change2=None, broadband=False):
    if broadband==True:
        data_br=network.Broadband_model_inputs()
        data_el=network.Electric_model_inputs()
        if  parameter2==None:           
            new_data1=network.Broadband_model_inputs()
            new_data1.modify_parameter(parameter1, percentage_change1)
            original_result=calculate_benefit_npv_S1(data_el, data_br)
            new_result=calculate_benefit_npv_S1(data_el, new_data1)
        else:
            new_data1=network.Broadband_model_inputs()
            new_data1.modify_parameter(parameter1, percentage_change1,parameter2)
            original_result=calculate_benefit_npv_S1(data_el, data_br)
            new_result=calculate_benefit_npv_S1(data_el, new_data1)
    else:
        data_br=network.Broadband_model_inputs()
        data_el=network.Electric_model_inputs()
        if  parameter2==None:
            new_data1=network.Electric_model_inputs()
            new_data1.modify_parameter(parameter1, percentage_change1)
            original_result=calculate_benefit_npv_S1(data_el, data_br)
            new_result=calculate_benefit_npv_S1(new_data1, data_br)
        else:
            new_data1=network.Electric_model_inputs()
            new_data1.modify_parameter(parameter1, percentage_change1, parameter2)
            original_result=calculate_benefit_npv_S1(data_el, data_br)
            new_result=calculate_benefit_npv_S1(new_data1, data_br)
    Percentage_change_result=(new_result-original_result)/original_result*100
    print(Percentage_change_result)
    return (Percentage_change_result)