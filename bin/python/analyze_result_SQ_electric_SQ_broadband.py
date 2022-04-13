# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 08:18:22 2022

@author: Mahsa
"""

import pandas as pd
import network
import simulate

data  = network.Electric_model_inputs()
data_broadband  = network.Broadband_model_inputs()

###Calculate aggregrated cost result of status-quo strategy based on each year for 40 years 
def aggregate_cost_through_years_SQ_electric_SQ_broadband(data, data_broadband):
    df_output_statusQuo=simulate.run_cost_simulation_SQ_strategy_electric(data)
    df_analyze_result_statusQuo=df_output_statusQuo.groupby(level=[0])[['capex','opex','lifecycle infrastructure','environmental restoration','non fatal','fatal','safety','total cost']].sum()
    df_analyze_result_statusQuo.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    df_analyze_result_statusQuo.to_csv(r'../../results/outcomes/cost-analyze-result-statusQuo-strategy.csv', index = False)
    return(df_analyze_result_statusQuo)

###Calculate aggregrated cost result of undergrounding after lifespan strategy based on each year for 40 years 
def aggregate_cost_through_years_UL_electric(data, data_broadband):
    df_output_under=simulate.run_cost_simulation_UL_strategy_electric(data)
    df_analyze_result_under=df_output_under.groupby(level=[0])[['capex','opex','lifecycle infrastructure','environmental restoration','non fatal','fatal','safety','total cost']].sum()
    df_analyze_result_under.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    df_analyze_result_under.to_csv(r'../../results/outcomes/cost-analyze-result-undergrounding-strategy.csv', index = False)
    return(df_analyze_result_under)

###Calculate additional cost due to undergrounding after lifespan strategy
def calculate_additional_cost_from_UL_electric(data, data_broadband):
    df1=aggregate_cost_through_years_UL_electric(data)
    df2=aggregate_cost_through_years_SQ_electric(data)
    df_analyze_additional=df1.subtract(df2)
    del df_analyze_additional['year']
    df_analyze_additional.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    df_analyze_additional.to_csv(r'../../results/outcomes/cost-analyze-result-additional-cost.csv', index = False)
    return(df_analyze_additional)

###Calculate net present value of infrastructure, environmental, safety and total cost for statusQuo strategy
def calculate_cost_net_present_value_SQ_electric(data, data_broadband):
    df_net_present_statusQuo=aggregate_cost_through_years_SQ_electric(data)
    net_present_value_lifecycle_infrastructure_cost=[]
    net_present_value_environmental_cost=[]
    net_present_value_safety_cost=[]
    net_present_value_total_under_after_lifespan_strategy_cost=[]
    for index, row in df_net_present_statusQuo.iterrows():
        net_present_value_lifecycle_infrastructure_cost.append(row['lifecycle infrastructure']/(1+data.parameter_dict['r'])**index)
        net_present_value_environmental_cost.append(row['environmental restoration']/(1+data.parameter_dict['r'])**index)
        net_present_value_safety_cost.append(row['safety']/(1+data.parameter_dict['r'])**index)
        net_present_value_total_under_after_lifespan_strategy_cost.append(row['total cost']/(1+data.parameter_dict['r'])**index)
    total_infrastructre=sum(net_present_value_lifecycle_infrastructure_cost)
    total_environmental=sum(net_present_value_environmental_cost)
    total_safety=sum(net_present_value_safety_cost)
    total_total=sum(net_present_value_total_under_after_lifespan_strategy_cost)
    df_net_present_value_statusQuo= pd.DataFrame({'lifecycle infrastructure':[total_infrastructre],
                                                  'environmental restoration':[total_environmental],
                                                  'safety':[total_safety],
                                                  'total cost':[total_total]})
    df_net_present_value_statusQuo.to_csv(r'../../results/outcomes/cost-net-present-value-statusQuo.csv', index = False)
    return([total_infrastructre,total_environmental,total_safety,total_total])

###Calculate net present value of infrastructure, environmental, safety and total cost for undergrounding after lifespan strategy
def calculate_cost_net_present_value_UL_electric(data, data_broadband):
    df_net_present_statusQuo=aggregate_cost_through_years_UL_electric(data)
    net_present_value_lifecycle_infrastructure_cost=[]
    net_present_value_environmental_cost=[]
    net_present_value_safety_cost=[]
    net_present_value_total_under_after_lifespan_strategy_cost=[]
    for index, row in df_net_present_statusQuo.iterrows():
        net_present_value_lifecycle_infrastructure_cost.append(row['lifecycle infrastructure']/(1+data.parameter_dict['r'])**index)
        net_present_value_environmental_cost.append(row['environmental restoration']/(1+data.parameter_dict['r'])**index)
        net_present_value_safety_cost.append(row['safety']/(1+data.parameter_dict['r'])**index)
        net_present_value_total_under_after_lifespan_strategy_cost.append(row['total cost']/(1+data.parameter_dict['r'])**index)
    total_infrastructre=sum(net_present_value_lifecycle_infrastructure_cost)
    total_environmental=sum(net_present_value_environmental_cost)
    total_safety=sum(net_present_value_safety_cost)
    total_total=sum(net_present_value_total_under_after_lifespan_strategy_cost)
    df_net_present_value_under= pd.DataFrame({'lifecycle infrastructure':[total_infrastructre],
                                                  'environmental restoration':[total_environmental],
                                                  'safety':[total_safety],
                                                  'total cost':[total_total]})
    df_net_present_value_under.to_csv(r'../../results/outcomes/cost-net-present-value-under.csv', index = False)
    return([total_infrastructre,total_environmental,total_safety,total_total])

###Calculate net present value for additional cost associate with undergrounding after lifespan strategy
def calculate_net_present_value_of_additional_cost_electric(data, data_broadband):
      list1=calculate_cost_net_present_value_UL_electric(data)
      list2=calculate_cost_net_present_value_SQ_electric(data)
      difference = []
      zip_object = zip(list1, list2)
      for list1_i, list2_i in zip_object:
          difference.append(list1_i-list2_i)
      df_net_present_value_additional= pd.DataFrame({'lifecycle infrastructure':[difference[0]],
                                                  'environmental restoration':[difference[1]],
                                                  'safety':[difference[2]],
                                                  'total cost':[difference[3]]})
      df_net_present_value_additional.to_csv(r'../../results/outcomes/cost-net-present-value-additional.csv', index = False)
      return(difference)
