# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 10:42:22 2021

@author: Mahsa
"""
###Import network.py which includes variables and line segment class defenistion
import Network as network
import numpy as np
import pandas as pd
import random

data = network.Electric_model_inputs()
data_broadband=network.Broadband_model_inputs()
###
#run simulation for calculating cost elemnts of statusQuo strategy and assign a data frame to them.
def run_cost_simulation_SQ_strategy_electric(data):
    line_segment_array=[]
    line_segment_length_array=[]
    for i in range (data.parameter_dict['segment_number']):
        segment=network.Electric_line_segment(data)
        line_segment_array.append(segment)
        line_segment_length_array.append(segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(line_segment_array)):
            disaggregated_function_new=True
            line_segment_array[i].update_underground_status()
            line_segment_array[i].update_age()
            line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_function_new)
            line_segment_array[i].calculate_capex()
            line_segment_array[i].calculate_opex()
            line_segment_array[i].add_opex_interest_rate()
            line_segment_array[i].calculate_total_infrastructure_cost()
            line_segment_array[i].calculate_environmental_restoration()
            line_segment_array[i].calculate_non_fatal_cost()
            line_segment_array[i].calculate_fatal_cost()
            line_segment_array[i].calculate_total_safety()
            line_segment_array[i].calculate_total_cost()
            df_new=pd.DataFrame({'year':[t],
                                 'segment number': [i],
                                 'length':[line_segment_array[i].length],
                                 'age': [line_segment_array[i].age[t]],
                                 'under': [line_segment_array[i].underground[t]],
                                 #'replecost': [line_segment_array[i].replcost[t]],
                                 'capex_electric':[line_segment_array[i].capex[t]],
                                 'opex_electric':[line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_electric':[line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_electric':[line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_electric':[line_segment_array[i].non_fatal[t]],
                                 'fatal_electric':[line_segment_array[i].fatal[t]],
                                 'safety_electric':[line_segment_array[i].total_safety[t]],
                                 'total_cost_electric':[line_segment_array[i].total_cost[t]],
                                 })            
            df=df.append(df_new, ignore_index = True)
    df.to_csv(r'../../results/outcomes/cost-simulation-output-statusQuo-strategy.csv', index = False)
    #return(df.set_index(["year","segment number"]))
    return(df)


#run simulation for calculating cost elemnts of undergrounding after lifespan strategy and assign a data frame to them.
def run_cost_simulation_UL_strategy_electric(data, joint_trench):
    line_segment_array=[]
    line_segment_length_array=[]
    for i in range (data.parameter_dict['segment_number']):
        segment=network.Electric_line_segment(data)
        line_segment_array.append(segment)
        line_segment_length_array.append(segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(line_segment_array)):
            convert_new=False
            disaggregated_function_new=True
            lifespan_exceeded=line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            line_segment_array[i].update_underground_status(convert=convert_new)
            line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_function_new)
            line_segment_array[i].calculate_capex()
            line_segment_array[i].calculate_opex()
            line_segment_array[i].add_opex_interest_rate()
            line_segment_array[i].calculate_total_infrastructure_cost()
            line_segment_array[i].calculate_environmental_restoration()
            line_segment_array[i].calculate_non_fatal_cost()
            line_segment_array[i].calculate_fatal_cost()
            line_segment_array[i].calculate_total_safety()
            line_segment_array[i].calculate_total_cost()
            #print(line_segment_array[i].conversion_cost)
            df_new=pd.DataFrame({'year':[t],
                                 'segment number': [i],
                                 'length':[line_segment_array[i].length],
                                 'age': [line_segment_array[i].age[t]],
                                 'under': [line_segment_array[i].underground[t]],
                                 #'replecost': [line_segment_array[i].replcost[t]],
                                 #'conversioncost': [line_segment_array[i].conversion_cost[t]],
                                 'capex_electric':[line_segment_array[i].capex[t]],
                                 'opex_electric':[line_segment_array[i].opex[t]],
                                 'lifecycle infrastructure_electric':[line_segment_array[i].total_infra[t]],
                                 'environmental restoration_electric':[line_segment_array[i].environmental_restoration[t]],
                                 'non fatal_electric':[line_segment_array[i].non_fatal[t]],
                                 'fatal_electric':[line_segment_array[i].fatal[t]],
                                 'safety_electric':[line_segment_array[i].total_safety[t]],
                                 'total cost_electric':[line_segment_array[i].total_cost[t]]})             
            df=df.append(df_new, ignore_index = True) 
    df.to_csv(r'../../results/outcomes/cost-simulation-output-undergrounding-strategy.csv', index = False)
    #return(df.set_index(["year","segment number"]))
    return(df)

def run_benefit_simulation_SQ_strategy_electric(data):
    line_segment_array=[]
    line_segment_length_array=[]
    for i in range (data.parameter_dict['segment_number']):
        segment=network.Electric_line_segment(data)
        line_segment_array.append(segment)
        line_segment_length_array.append(segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(line_segment_array)):
            line_segment_array[i].update_underground_status()
            line_segment_array[i].update_age()
            line_segment_array[i].calculate_economic_benefits()
            line_segment_array[i].calculate_aesthetic_benefits()
            line_segment_array[i].add_aesthetic_benefits_interest_rate()
            line_segment_array[i].calculate_aesthetic_losses()
            line_segment_array[i].add_aesthetic_losses_interest_rate()
            line_segment_array[i].calculate_economic_outage_losses()
            line_segment_array[i].add_economic_outage_losses_interest_rate()
            line_segment_array[i].calculate_total_losses()
            df_new=pd.DataFrame({'year':[t],
                                 'segment number': [i],
                                 'length':[line_segment_array[i].length],
                                 'age': [line_segment_array[i].age[t]],
                                 'under': [line_segment_array[i].underground[t]],                            
                                 'economic benefits':[line_segment_array[i].total_economic_benefits[t]],            
                                 'aesthetic benefits':[line_segment_array[i].total_aesthetic_benefits[t]], 
                                 'aesthetic losses':[line_segment_array[i].total_inflated_aesthetic_losses[t]],
                                 'economic losses':[line_segment_array[i].total_inflated_economic_losses[t]],
                                 'total losses':[line_segment_array[i].total_losses[t]]
                                 }) 
            df=df.append(df_new, ignore_index = True)
    df.to_csv(r'../../results/outcomes/benefit-simulation-output-statusQuo-strategy.csv', index = False)
    #return(df.set_index(["year","segment number"]))
    return(df)       


def run_benefit_simulation_UL_strategy_electric(data,p):
    line_segment_array=[]
    line_segment_length_array=[]
    total_mileage = 0
    underground_mileage = 0
    underground_proportion = 1 - data.parameter_dict['overhead_proportion']
    for i in range (data.parameter_dict['segment_number']):
        segment=network.Electric_line_segment(data)
        line_segment_array.append(segment)
        line_segment_length_array.append(segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(line_segment_array)):
            total_mileage += line_segment_array[i].length
            if line_segment_array[i].underground[-1] == 1:
                  underground_mileage += line_segment_array[i].length
            convert_new=False
            lifespan_exceeded=line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            line_segment_array[i].update_underground_status(convert=convert_new)
            line_segment_array[i].calculate_economic_benefits()
            line_segment_array[i].calculate_aesthetic_benefits()
            line_segment_array[i].add_aesthetic_benefits_interest_rate()
            line_segment_array[i].calculate_aesthetic_losses()
            line_segment_array[i].add_aesthetic_losses_interest_rate()
            line_segment_array[i].calculate_economic_outage_losses()
            line_segment_array[i].add_economic_outage_losses_interest_rate()
            line_segment_array[i].calculate_total_losses()
            line_segment_array[i].calculate_economic_loss(p)
            df_new=pd.DataFrame({'year':[t],
                                 'segment number': [i],
                                 'length':[line_segment_array[i].length],
                                 'age': [line_segment_array[i].age[t]],
                                 'under': [line_segment_array[i].underground[t]],  
                                 'under_proportion': underground_proportion,
                                 'economic benefits':[line_segment_array[i].total_economic_benefits[t]],            
                                 'aesthetic benefits':[line_segment_array[i].total_inflated_aesthetic_benefits[t]],
                                 'aesthetic losses':[line_segment_array[i].total_inflated_aesthetic_losses[t]],
                                 'economic losses':[line_segment_array[i].total_inflated_economic_losses[t]],
                                 'total losses':[line_segment_array[i].total_losses[t]],
                                 'economic_cost_outages':[line_segment_array[i].total_economic_losses[t]]
                                 }) 
            df=df.append(df_new, ignore_index = True)
        underground_proportion = underground_mileage/total_mileage
    df.to_csv(r'../../results/outcomes/benefit-simulation-output-under-strategy-90-10-20seg.csv', index = False)
    print("Undergroung proportion at Year 40:" + str(underground_proportion))
    #return(df.set_index(["year","segment number"]))   
    return(df)
# calculate total length of underground line on each year
def calculate_percentage_underground_UL_strategy_electric(data):    
    line_segment_array=[]
    line_segment_length_array=[]
    for i in range (data.parameter_dict['segment_number']):
        segment=network.Electric_line_segment(data)
        line_segment_array.append(segment)
        line_segment_length_array.append(segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    underground_length=[0]
    total_length=0
    for t in range (data.parameter_dict['analysis_years']-1):
        underground_length.append(0)
    for i in range (len(line_segment_array)):
        total_length+=line_segment_array[i].length
        if line_segment_array[i].underground[0]==1:
          underground_length[0]+=line_segment_array[i].length
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(line_segment_array)):
            convert_new=False
            lifespan_exceeded=line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            line_segment_array[i].update_underground_status(convert=convert_new)
            retire_age=line_segment_array[i].determine_first_retire()
            if line_segment_array[i].underground[0]==0:
                if t==retire_age:
                    underground_length[t]+=underground_length[t-1]+line_segment_array[i].length
                else:
                    pass
        df_new=pd.DataFrame({'year':[t],
                             'underground_length': underground_length[t]})             
        df=df.append(df_new, ignore_index = True)    
    df.to_csv(r'../../results/outcomes/under-length-undergrounding-strategy.csv', index = False)
    return(df)

#run simulation for calculating broadband cost elemnts of statusQuo strategy and assign a data frame to them.
def run_cost_simulation_SQ_strategy_calculate_economic_loss(data_broadband):
    disaggregated_function=True
    line_segment_array=[]
    line_segment_length_array=[]
    total_mileage = data_broadband.parameter_dict['total_length']
    underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']
    underground_proportion = 1 - data_broadband.parameter_dict['overhead_proportion']
    for i in range (data_broadband.parameter_dict['segment_number']):
        segment=network.Broadband_line_segment(data_broadband)
        line_segment_array.append(segment)
        line_segment_length_array.append(segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    for t in range (data_broadband.parameter_dict['analysis_years']):
        for i in range (len(line_segment_array)):
            if line_segment_array[i].underground[-1] == 1:
                underground_mileage += line_segment_array[i].length
            line_segment_array[i].update_underground_status()
            line_segment_array[i].update_age()
            line_segment_array[i].calculate_replcost()
            line_segment_array[i].calculate_capex()
            line_segment_array[i].calculate_opex()
            line_segment_array[i].add_opex_interest_rate()
            line_segment_array[i].calculate_total_infrastructure_cost()
            #line_segment_array[i].calculate_economic_loss(underground_proportion) #0.2
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'capex_broadband':[line_segment_array[i].capex[t]],
                                 'opex_broadband':[line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_broadband':[line_segment_array[i].total_infra[t]],
                                 #'economic loss':[line_segment_array[i].total_economic_losses[t]]
                                 })            
            df=df.append(df_new, ignore_index = True)
        underground_proportion = underground_mileage/total_mileage
        print('Underground proportion: ', underground_proportion)
        underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']
    print("Undergroung proportion at Year 40:" + str(underground_proportion))
    df.to_csv(r'../../results/outcomes/cost-simulation-output-SQ-broadband-econ-loss.csv', index = False)
    #return(df.set_index(["year","segment number"]))
    return(df)

#run simulation for calculating cost elemnts of undergrounding after lifespan strategy and assign a data frame to them.
def run_cost_simulation_UL_strategy_broadband(data_broadband, joint_trench):
    disaggregated_function=True
    line_segment_array=[]
    line_segment_length_array=[]
    total_mileage = 0
    underground_mileage = 0
    underground_proportion = 1 - data.parameter_dict['overhead_proportion']
    for i in range (data_broadband.parameter_dict['segment_number']):
        segment=network.Broadband_line_segment(data_broadband)
        line_segment_array.append(segment)
        line_segment_length_array.append(segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    for t in range (data_broadband.parameter_dict['analysis_years']):
        for i in range (len(line_segment_array)):
            total_mileage += line_segment_array[i].length
            if line_segment_array[i].underground[-1] == 1:
                  underground_mileage += line_segment_array[i].length
            line_segment_array[i].update_underground_status()
            line_segment_array[i].update_age()
            line_segment_array[i].calculate_replcost()
            line_segment_array[i].calculate_capex()
            line_segment_array[i].calculate_opex()
            line_segment_array[i].add_opex_interest_rate()
            line_segment_array[i].calculate_total_infrastructure_cost()
            line_segment_array[i].calculate_economic_loss(0.2)
            df_new=pd.DataFrame({
                                 'capex_broadband':[line_segment_array[i].capex[t]],
                                 'opex_broadband':[line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_broadband':[line_segment_array[i].total_infra[t]],
                                 })             
            df=df.append(df_new, ignore_index = True)    
    
    underground_proportion = underground_mileage/total_mileage
    print("Undergroung proportion at Year 40:" + str(underground_proportion))
    #df.to_csv(r'../../results/outcomes/cost-simulation-output-UL-broadband.csv', index = False)
    #return(df.set_index(["year","segment number"]))
    return(df)

def run_cost_simulation_UL_jointtrench_strategy_broadband(data_broadband,joint_trench):
    disaggregated_function=True
    line_segment_array=[]
    line_segment_length_array=[]
    for i in range (data_broadband.parameter_dict['segment_number']):
        segment=network.Broadband_line_segment(data_broadband)
        line_segment_array.append(segment)
        line_segment_length_array.append(segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    for t in range (data_broadband.parameter_dict['analysis_years']):
        for i in range (len(line_segment_array)):
            convert_new=False
            lifespan_exceeded=line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            line_segment_array[i].update_underground_status(convert=convert_new)
            line_segment_array[i].calculate_disaggregated_conversion_cost()
            line_segment_array[i].calculate_replcost(joint_trench=True)
            line_segment_array[i].calculate_capex()
            line_segment_array[i].calculate_opex()
            line_segment_array[i].add_opex_interest_rate()
            line_segment_array[i].calculate_total_infrastructure_cost()
            #print(line_segment_array[i].conversion_cost)
            df_new=pd.DataFrame({
                                 'capex_broadband':[line_segment_array[i].capex[t]],
                                 'opex_broadband':[line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_broadband':[line_segment_array[i].total_infra[t]],
                                 })             
            df=df.append(df_new, ignore_index = True)    
    #df.to_csv(r'../../results/outcomes/cost-simulation-output-ULjoint-broadband.csv', index = False)
    #return(df.set_index(["year","segment number"]))
    return(df)

def run_cost_ST1_SQ_electric_SQ_broadband_simulate(data, data_broadband):
    df_electric=run_cost_simulation_SQ_strategy_electric(data)
    df_broadband=run_cost_simulation_SQ_strategy_broadband(data_broadband)
    df_joint=pd.concat([df_electric, df_broadband], axis=1)
    df_joint.to_csv(r'../../results/outcomes/ST1_results.csv', index = False)
    return(df_joint)

def run_cost_ST2_UL_electric_SQ_broadband_simulate(data, data_broadband):
    df_electric=run_cost_simulation_UL_strategy_electric(data, joint_trench=False)
    df_broadband=run_cost_simulation_SQ_strategy_broadband(data_broadband)
    df_joint=pd.concat([df_electric, df_broadband], axis=1)
    df_joint.to_csv(r'../../results/outcomes/ST2_results.csv', index = False)
    return(df_joint)

def run_cost_ST3_SQ_electric_UL_broadband_simulate(data, data_broadband, joint_trench=False):
    df_electric=run_cost_simulation_SQ_strategy_electric(data)
    df_broadband=run_cost_simulation_UL_strategy_broadband(data_broadband, joint_trench=False)
    df_joint=pd.concat([df_electric, df_broadband], axis=1)
    df_joint.to_csv(r'../../results/outcomes/ST3_results.csv', index = False)
    return(df_joint)


def run_cost_ST4_UL_electric_UL_broadband_simulate(data, data_broadband, joint_trench=False):
    df_electric=run_cost_simulation_UL_strategy_electric(data, joint_trench=False)
    df_broadband=run_cost_simulation_UL_strategy_broadband(data_broadband, joint_trench=False)
    df_joint=pd.concat([df_electric, df_broadband], axis=1)
    df_joint.to_csv(r'../../results/outcomes/ST4_results.csv', index = False)
    return(df_joint)

def run_ST5_UL_electric_UL_joint_trench_broadband_simulate(data, data_broadband, joint_trench=True):
    df_electric=run_cost_simulation_UL_strategy_electric(data, joint_trench=True)
    df_broadband=run_cost_simulation_UL_jointtrench_strategy_broadband(data_broadband, joint_trench=True)
    df_joint=pd.concat([df_electric, df_broadband], axis=1)
    df_joint.to_csv(r'../../results/outcomes/ST5_results.csv', index = False)
    return(df_joint)

# Define S1 simulation function
def run_cost_simulation_S1(data, data_broadband):
    # SQ for electric line segments
    disaggregated_function=True
    el_line_segment_array=[]
    el_line_segment_length_array=[]
    for i in range (data.parameter_dict['segment_number']):
        el_segment=network.Electric_line_segment(data)
        el_line_segment_array.append(el_segment)
        el_line_segment_length_array.append(el_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df1=pd.DataFrame()
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(el_line_segment_array)):
            el_line_segment_array[i].update_underground_status()
            el_line_segment_array[i].update_age()
            el_line_segment_array[i].calculate_replcost(disaggregated_function)
            el_line_segment_array[i].calculate_capex()
            el_line_segment_array[i].calculate_opex()
            el_line_segment_array[i].add_opex_interest_rate()
            el_line_segment_array[i].calculate_total_infrastructure_cost()
            el_line_segment_array[i].calculate_environmental_restoration()
            el_line_segment_array[i].calculate_non_fatal_cost()
            el_line_segment_array[i].calculate_fatal_cost()
            el_line_segment_array[i].calculate_total_safety()
            el_line_segment_array[i].calculate_total_cost()
    # SQ for broadband line segment
    br_line_segment_array=[]
    br_line_segment_length_array=[]
    for i in range (data_broadband.parameter_dict['segment_number']):
        br_segment=network.Broadband_line_segment(data_broadband)
        br_line_segment_array.append(br_segment)
        br_line_segment_length_array.append(br_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    for t in range (data_broadband.parameter_dict['analysis_years']):
        for i in range (len(br_line_segment_array)):
            br_line_segment_array[i].update_underground_status()
            br_line_segment_array[i].update_age()
            br_line_segment_array[i].calculate_replcost(disaggregated_function)
            br_line_segment_array[i].calculate_capex()
            br_line_segment_array[i].calculate_opex()
            br_line_segment_array[i].add_opex_interest_rate()
            br_line_segment_array[i].calculate_total_infrastructure_cost()
                                        
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age': [el_line_segment_array[i].age[t]],
                                 'under': [el_line_segment_array[i].underground[t]],  
                                 'capex_electric':[el_line_segment_array[i].capex[t]],
                                 'opex_electric':[el_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_electric':[el_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_electric':[el_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_electric':[el_line_segment_array[i].non_fatal[t]],
                                 'fatal_electric':[el_line_segment_array[i].fatal[t]],
                                 'safety_electric':[el_line_segment_array[i].total_safety[t]],
                                 'total_cost_electric':[el_line_segment_array[i].total_cost[t]],
                                 'capex_broadband':[br_line_segment_array[i].capex[t]],
                                 'opex_broadband':[br_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_broadband':[br_line_segment_array[i].total_infra[t]],
                                 })            
            df1=df1.append(df_new, ignore_index = True)
    df1.to_csv(r'../../results/outcomes/Cost/Simulation/S1-cost-simulation.csv', index = False)
    return(df1.set_index(["year","segment number"]))
    #return(df1)

# Define S2 simulation function
def run_cost_simulation_S2(data, data_broadband):
    # SQ for electric line segments
    disaggregated_function=True
    el_line_segment_array=[]
    el_line_segment_length_array=[]
    for i in range (data.parameter_dict['segment_number']):
        el_segment=network.Electric_line_segment(data)
        el_line_segment_array.append(el_segment)
        el_line_segment_length_array.append(el_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df1=pd.DataFrame()
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(el_line_segment_array)):
            el_line_segment_array[i].update_underground_status()
            el_line_segment_array[i].update_age()
            el_line_segment_array[i].calculate_replcost(disaggregated_function)
            el_line_segment_array[i].calculate_capex()
            el_line_segment_array[i].calculate_opex()
            el_line_segment_array[i].add_opex_interest_rate()
            el_line_segment_array[i].calculate_total_infrastructure_cost()
            el_line_segment_array[i].calculate_environmental_restoration()
            el_line_segment_array[i].calculate_non_fatal_cost()
            el_line_segment_array[i].calculate_fatal_cost()
            el_line_segment_array[i].calculate_total_safety()
            el_line_segment_array[i].calculate_total_cost()
    # SQ for broadband line segment
    br_line_segment_array=[]
    br_line_segment_length_array=[]
    for i in range (data_broadband.parameter_dict['segment_number']):
        br_segment=network.Broadband_line_segment(data_broadband)
        br_line_segment_array.append(br_segment)
        br_line_segment_length_array.append(br_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    for t in range (data_broadband.parameter_dict['analysis_years']):
        for i in range (len(br_line_segment_array)):
            convert_new=False
            disaggregated_function=True
            lifespan_exceeded=br_line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if br_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            br_line_segment_array[i].update_underground_status()
            br_line_segment_array[i].calculate_replcost(disaggregated_function)
            br_line_segment_array[i].calculate_capex()
            br_line_segment_array[i].calculate_opex()
            br_line_segment_array[i].add_opex_interest_rate()
            br_line_segment_array[i].calculate_total_infrastructure_cost()
                                        
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age': [el_line_segment_array[i].age[t]],
                                 'under': [el_line_segment_array[i].underground[t]],  
                                 'capex_electric':[el_line_segment_array[i].capex[t]],
                                 'opex_electric':[el_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_electric':[el_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_electric':[el_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_electric':[el_line_segment_array[i].non_fatal[t]],
                                 'fatal_electric':[el_line_segment_array[i].fatal[t]],
                                 'safety_electric':[el_line_segment_array[i].total_safety[t]],
                                 'total_cost_electric':[el_line_segment_array[i].total_cost[t]],
                                 'capex_broadband':[br_line_segment_array[i].capex[t]],
                                 'opex_broadband':[br_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_broadband':[br_line_segment_array[i].total_infra[t]],
                                 })            
            df1=df1.append(df_new, ignore_index = True)
    df1.to_csv(r'../../results/outcomes/Cost/Simulation/S1-cost-simulation.csv', index = False)
    return(df1.set_index(["year","segment number"]))
    #return(df1)
