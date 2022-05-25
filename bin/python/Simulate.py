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


# Define S1 simulation function
def run_cost_simulation_S1(data, data_broadband):
    # SQ for electric line segments
    disaggregated_current=True
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
            el_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current)
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
            br_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current)
            br_line_segment_array[i].calculate_capex()
            br_line_segment_array[i].calculate_opex()
            br_line_segment_array[i].add_opex_interest_rate()
            br_line_segment_array[i].calculate_total_infrastructure_cost()
            br_line_segment_array[i].calculate_environmental_restoration()
            br_line_segment_array[i].calculate_non_fatal_cost()
            br_line_segment_array[i].calculate_fatal_cost()
            br_line_segment_array[i].calculate_total_safety()
            br_line_segment_array[i].calculate_total_cost()
                                        
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'capex_el':[el_line_segment_array[i].capex[t]],
                                 'opex_el':[el_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_el':[el_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_el':[el_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_el':[el_line_segment_array[i].non_fatal[t]],
                                 'fatal_el':[el_line_segment_array[i].fatal[t]],
                                 'safety_el':[el_line_segment_array[i].total_safety[t]],
                                 'total_cost_el':[el_line_segment_array[i].total_cost[t]],
                                 'capex_br':[br_line_segment_array[i].capex[t]],
                                 'opex_br':[br_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_br':[br_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_br':[br_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_br':[br_line_segment_array[i].non_fatal[t]],
                                 'fatal_br':[br_line_segment_array[i].fatal[t]],
                                 'safety_br':[br_line_segment_array[i].total_safety[t]],
                                 'total_cost_br':[br_line_segment_array[i].total_cost[t]],
                                 })            
            df1=df1.append(df_new, ignore_index = True)
    df1.to_csv(r'../../results/outcomes/Cost/Simulation/S1-cost-simulation.csv', index = False)
    return(df1.set_index(["year","segment number"]))
    #return(df1)

# Define S2 simulation function
def run_cost_simulation_S2(data, data_broadband):
    # SQ for electric line segments
    disaggregated_current=True
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
            el_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current)
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
            disaggregated_current=True
            lifespan_exceeded=br_line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if br_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            br_line_segment_array[i].update_underground_status(convert=convert_new)
            br_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current)
            br_line_segment_array[i].calculate_capex()
            br_line_segment_array[i].calculate_opex()
            br_line_segment_array[i].add_opex_interest_rate()
            br_line_segment_array[i].calculate_total_infrastructure_cost()
            br_line_segment_array[i].calculate_environmental_restoration()
            br_line_segment_array[i].calculate_non_fatal_cost()
            br_line_segment_array[i].calculate_fatal_cost()
            br_line_segment_array[i].calculate_total_safety()
            br_line_segment_array[i].calculate_total_cost()                                        
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'capex_el':[el_line_segment_array[i].capex[t]],
                                 'opex_el':[el_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_el':[el_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_el':[el_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_el':[el_line_segment_array[i].non_fatal[t]],
                                 'fatal_el':[el_line_segment_array[i].fatal[t]],
                                 'safety_el':[el_line_segment_array[i].total_safety[t]],
                                 'total_cost_el':[el_line_segment_array[i].total_cost[t]],
                                 'capex_br':[br_line_segment_array[i].capex[t]],
                                 'opex_br':[br_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_br':[br_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_br':[br_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_br':[br_line_segment_array[i].non_fatal[t]],
                                 'fatal_br':[br_line_segment_array[i].fatal[t]],
                                 'safety_br':[br_line_segment_array[i].total_safety[t]],
                                 'total_cost_br':[br_line_segment_array[i].total_cost[t]],
                                 })            
            df1=df1.append(df_new, ignore_index = True)
    df1.to_csv(r'../../results/outcomes/Cost/Simulation/S2-cost-simulation.csv', index = False)
    return(df1.set_index(["year","segment number"]))
    #return(df1)

# Define S3 simulation function
def run_cost_simulation_S3(data, data_broadband):
    # SQ for electric line segments
    disaggregated_current=True
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
            el_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current)
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
            disaggregated_current=True
            aggressive_current=True
            lifespan_exceeded=br_line_segment_array[i].update_age(aggressive=aggressive_current)
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if br_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            br_line_segment_array[i].update_underground_status(convert=convert_new)
            br_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current)
            br_line_segment_array[i].calculate_capex()
            br_line_segment_array[i].calculate_opex()
            br_line_segment_array[i].add_opex_interest_rate()
            br_line_segment_array[i].calculate_total_infrastructure_cost()
            br_line_segment_array[i].calculate_environmental_restoration()
            br_line_segment_array[i].calculate_non_fatal_cost()
            br_line_segment_array[i].calculate_fatal_cost()
            br_line_segment_array[i].calculate_total_safety()
            br_line_segment_array[i].calculate_total_cost()                                        
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'capex_el':[el_line_segment_array[i].capex[t]],
                                 'opex_el':[el_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_el':[el_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_el':[el_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_el':[el_line_segment_array[i].non_fatal[t]],
                                 'fatal_el':[el_line_segment_array[i].fatal[t]],
                                 'safety_el':[el_line_segment_array[i].total_safety[t]],
                                 'total_cost_el':[el_line_segment_array[i].total_cost[t]],
                                 'capex_br':[br_line_segment_array[i].capex[t]],
                                 'opex_br':[br_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_br':[br_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_br':[br_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_br':[br_line_segment_array[i].non_fatal[t]],
                                 'fatal_br':[br_line_segment_array[i].fatal[t]],
                                 'safety_br':[br_line_segment_array[i].total_safety[t]],
                                 'total_cost_br':[br_line_segment_array[i].total_cost[t]],
                                 })            
            df1=df1.append(df_new, ignore_index = True)
    df1.to_csv(r'../../results/outcomes/Cost/Simulation/S3-cost-simulation.csv', index = False)
    return(df1.set_index(["year","segment number"]))
    #return(df1)

# Define S4 simulation function
def run_cost_simulation_S4(data, data_broadband):
    # SQ for electric line segments
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
            convert_new=False
            disaggregated_current=True
            lifespan_exceeded=el_line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if el_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            el_line_segment_array[i].update_underground_status(convert=convert_new)
            el_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current)
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
    disaggregated_current=True
    br_line_segment_array=[]
    br_line_segment_length_array=[]
    for i in range (data_broadband.parameter_dict['segment_number']):
        br_segment=network.Broadband_line_segment(data)
        br_line_segment_array.append(br_segment)
        br_line_segment_length_array.append(br_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    for t in range (data_broadband.parameter_dict['analysis_years']):
        for i in range (len(br_line_segment_array)):
            br_line_segment_array[i].update_underground_status()
            br_line_segment_array[i].update_age()
            br_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current)
            br_line_segment_array[i].calculate_capex()
            br_line_segment_array[i].calculate_opex()
            br_line_segment_array[i].add_opex_interest_rate()
            br_line_segment_array[i].calculate_total_infrastructure_cost()
            br_line_segment_array[i].calculate_environmental_restoration()
            br_line_segment_array[i].calculate_non_fatal_cost()
            br_line_segment_array[i].calculate_fatal_cost()
            br_line_segment_array[i].calculate_total_safety()
            br_line_segment_array[i].calculate_total_cost()                                            
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'capex_el':[el_line_segment_array[i].capex[t]],
                                 'opex_el':[el_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_el':[el_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_el':[el_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_el':[el_line_segment_array[i].non_fatal[t]],
                                 'fatal_el':[el_line_segment_array[i].fatal[t]],
                                 'safety_el':[el_line_segment_array[i].total_safety[t]],
                                 'total_cost_el':[el_line_segment_array[i].total_cost[t]],
                                 'capex_br':[br_line_segment_array[i].capex[t]],
                                 'opex_br':[br_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_br':[br_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_br':[br_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_br':[br_line_segment_array[i].non_fatal[t]],
                                 'fatal_br':[br_line_segment_array[i].fatal[t]],
                                 'safety_br':[br_line_segment_array[i].total_safety[t]],
                                 'total_cost_br':[br_line_segment_array[i].total_cost[t]],
                                 })            
            df1=df1.append(df_new, ignore_index = True)
    df1.to_csv(r'../../results/outcomes/Cost/Simulation/S4-cost-simulation.csv', index = False)
    return(df1.set_index(["year","segment number"]))
    #return(df1)

# Define S5 simulation function
def run_cost_simulation_S5(data, data_broadband):
    # SQ for electric line segments
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
            convert_new=False
            disaggregated_current=True
            aggressive_current=True
            lifespan_exceeded=el_line_segment_array[i].update_age(aggressive=aggressive_current)
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if el_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            el_line_segment_array[i].update_underground_status(convert=convert_new)
            el_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current)
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
    disaggregated_current=True
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
            br_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current)
            br_line_segment_array[i].calculate_capex()
            br_line_segment_array[i].calculate_opex()
            br_line_segment_array[i].add_opex_interest_rate()
            br_line_segment_array[i].calculate_total_infrastructure_cost()
            br_line_segment_array[i].calculate_environmental_restoration()
            br_line_segment_array[i].calculate_non_fatal_cost()
            br_line_segment_array[i].calculate_fatal_cost()
            br_line_segment_array[i].calculate_total_safety()
            br_line_segment_array[i].calculate_total_cost()                                            
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'capex_el':[el_line_segment_array[i].capex[t]],
                                 'opex_el':[el_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_el':[el_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_el':[el_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_el':[el_line_segment_array[i].non_fatal[t]],
                                 'fatal_el':[el_line_segment_array[i].fatal[t]],
                                 'safety_el':[el_line_segment_array[i].total_safety[t]],
                                 'total_cost_el':[el_line_segment_array[i].total_cost[t]],
                                 'capex_br':[br_line_segment_array[i].capex[t]],
                                 'opex_br':[br_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_br':[br_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_br':[br_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_br':[br_line_segment_array[i].non_fatal[t]],
                                 'fatal_br':[br_line_segment_array[i].fatal[t]],
                                 'safety_br':[br_line_segment_array[i].total_safety[t]],
                                 'total_cost_br':[br_line_segment_array[i].total_cost[t]],
                                 })            
            df1=df1.append(df_new, ignore_index = True)
    df1.to_csv(r'../../results/outcomes/Cost/Simulation/S5-cost-simulation.csv', index = False)
    return(df1.set_index(["year","segment number"]))
    #return(df1)

# Define S6 simulation function
def run_cost_simulation_S6(data, data_broadband):
    # SQ for electric line segments
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
            convert_new=False
            disaggregated_current=True
            joint_trench_current=True
            lifespan_exceeded=el_line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if el_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            el_line_segment_array[i].update_underground_status(convert=convert_new)
            el_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current, joint_trench=joint_trench_current)
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
            disaggregated_current=True
            joint_trench_current=True
            lifespan_exceeded=br_line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if br_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            br_line_segment_array[i].update_underground_status(convert=convert_new)
            br_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current, joint_trench=joint_trench_current)
            br_line_segment_array[i].calculate_capex()
            br_line_segment_array[i].calculate_opex()
            br_line_segment_array[i].add_opex_interest_rate()
            br_line_segment_array[i].calculate_total_infrastructure_cost()
            br_line_segment_array[i].calculate_environmental_restoration()
            br_line_segment_array[i].calculate_non_fatal_cost()
            br_line_segment_array[i].calculate_fatal_cost()
            br_line_segment_array[i].calculate_total_safety()
            br_line_segment_array[i].calculate_total_cost()                                        
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'capex_el':[el_line_segment_array[i].capex[t]],
                                 'opex_el':[el_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_el':[el_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_el':[el_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_el':[el_line_segment_array[i].non_fatal[t]],
                                 'fatal_el':[el_line_segment_array[i].fatal[t]],
                                 'safety_el':[el_line_segment_array[i].total_safety[t]],
                                 'total_cost_el':[el_line_segment_array[i].total_cost[t]],
                                 'capex_br':[br_line_segment_array[i].capex[t]],
                                 'opex_br':[br_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_br':[br_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_br':[br_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_br':[br_line_segment_array[i].non_fatal[t]],
                                 'fatal_br':[br_line_segment_array[i].fatal[t]],
                                 'safety_br':[br_line_segment_array[i].total_safety[t]],
                                 'total_cost_br':[br_line_segment_array[i].total_cost[t]],
                                 })            
            df1=df1.append(df_new, ignore_index = True)
    df1.to_csv(r'../../results/outcomes/Cost/Simulation/S6-cost-simulation.csv', index = False)
    return(df1.set_index(["year","segment number"]))
    #return(df1)

# Define S7 simulation function
def run_cost_simulation_S7(data, data_broadband):
    # SQ for electric line segments
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
            convert_new=False
            disaggregated_current=True
            joint_trench_current=False
            lifespan_exceeded=el_line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if el_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            el_line_segment_array[i].update_underground_status(convert=convert_new)
            el_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current, joint_trench=joint_trench_current)
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
            disaggregated_current=True
            joint_trench_current=False
            lifespan_exceeded=br_line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if br_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            br_line_segment_array[i].update_underground_status(convert=convert_new)
            br_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current, joint_trench=joint_trench_current)
            br_line_segment_array[i].calculate_capex()
            br_line_segment_array[i].calculate_opex()
            br_line_segment_array[i].add_opex_interest_rate()
            br_line_segment_array[i].calculate_total_infrastructure_cost()
            br_line_segment_array[i].calculate_environmental_restoration()
            br_line_segment_array[i].calculate_non_fatal_cost()
            br_line_segment_array[i].calculate_fatal_cost()
            br_line_segment_array[i].calculate_total_safety()
            br_line_segment_array[i].calculate_total_cost()
                                        
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'capex_el':[el_line_segment_array[i].capex[t]],
                                 'opex_el':[el_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_el':[el_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_el':[el_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_el':[el_line_segment_array[i].non_fatal[t]],
                                 'fatal_el':[el_line_segment_array[i].fatal[t]],
                                 'safety_el':[el_line_segment_array[i].total_safety[t]],
                                 'total_cost_el':[el_line_segment_array[i].total_cost[t]],
                                 'capex_br':[br_line_segment_array[i].capex[t]],
                                 'opex_br':[br_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_br':[br_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_br':[br_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_br':[br_line_segment_array[i].non_fatal[t]],
                                 'fatal_br':[br_line_segment_array[i].fatal[t]],
                                 'safety_br':[br_line_segment_array[i].total_safety[t]],
                                 'total_cost_br':[br_line_segment_array[i].total_cost[t]],                                 
                                 })            
            df1=df1.append(df_new, ignore_index = True)
    df1.to_csv(r'../../results/outcomes/Cost/Simulation/S7-cost-simulation.csv', index = False)
    return(df1.set_index(["year","segment number"]))
    #return(df1)

# Define S8 simulation function
def run_cost_simulation_S8(data, data_broadband):
    # SQ for electric and broadband line segments
    el_line_segment_array=[]
    el_line_segment_length_array=[]
    br_line_segment_array=[]
    br_line_segment_length_array=[]
    for i in range (data.parameter_dict['segment_number']):
        el_segment=network.Electric_line_segment(data)
        el_line_segment_array.append(el_segment)
        el_line_segment_length_array.append(el_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    for i in range (data_broadband.parameter_dict['segment_number']):
        br_segment=network.Broadband_line_segment(data_broadband)
        br_line_segment_array.append(br_segment)
        br_line_segment_length_array.append(br_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df1=pd.DataFrame()
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(el_line_segment_array)):
            convert_new=False
            disaggregated_current=True
            joint_trench_current=True
            lifespan_exceeded=el_line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if el_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            el_line_segment_array[i].update_underground_status(convert=convert_new)
            el_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current, joint_trench=joint_trench_current)
            el_line_segment_array[i].calculate_capex()
            el_line_segment_array[i].calculate_opex()
            el_line_segment_array[i].add_opex_interest_rate()
            el_line_segment_array[i].calculate_total_infrastructure_cost()
            el_line_segment_array[i].calculate_environmental_restoration()
            el_line_segment_array[i].calculate_non_fatal_cost()
            el_line_segment_array[i].calculate_fatal_cost()
            el_line_segment_array[i].calculate_total_safety()
            el_line_segment_array[i].calculate_total_cost()

            br_line_segment_array[i].update_underground_status(convert=convert_new)
            br_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current, joint_trench=joint_trench_current)
            br_line_segment_array[i].calculate_capex()
            br_line_segment_array[i].calculate_opex()
            br_line_segment_array[i].add_opex_interest_rate()
            br_line_segment_array[i].calculate_total_infrastructure_cost()
            br_line_segment_array[i].calculate_environmental_restoration()
            br_line_segment_array[i].calculate_non_fatal_cost()
            br_line_segment_array[i].calculate_fatal_cost()
            br_line_segment_array[i].calculate_total_safety()
            br_line_segment_array[i].calculate_total_cost()
                                        
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'capex_el':[el_line_segment_array[i].capex[t]],
                                 'opex_el':[el_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_el':[el_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_el':[el_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_el':[el_line_segment_array[i].non_fatal[t]],
                                 'fatal_el':[el_line_segment_array[i].fatal[t]],
                                 'safety_el':[el_line_segment_array[i].total_safety[t]],
                                 'total_cost_el':[el_line_segment_array[i].total_cost[t]],
                                 'capex_br':[br_line_segment_array[i].capex[t]],
                                 'opex_br':[br_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_br':[br_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_br':[br_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_br':[br_line_segment_array[i].non_fatal[t]],
                                 'fatal_br':[br_line_segment_array[i].fatal[t]],
                                 'safety_br':[br_line_segment_array[i].total_safety[t]],
                                 'total_cost_br':[br_line_segment_array[i].total_cost[t]],
                                 })            
            df1=df1.append(df_new, ignore_index = True)
    df1.to_csv(r'../../results/outcomes/Cost/Simulation/S8-cost-simulation.csv', index = False)
    return(df1.set_index(["year","segment number"]))
    #return(df1)

# Define S9 simulation function
def run_cost_simulation_S9(data, data_broadband):
    # SQ for electric and broadband line segments
    el_line_segment_array=[]
    el_line_segment_length_array=[]
    br_line_segment_array=[]
    br_line_segment_length_array=[]
    for i in range (data.parameter_dict['segment_number']):
        el_segment=network.Electric_line_segment(data)
        el_line_segment_array.append(el_segment)
        el_line_segment_length_array.append(el_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    for i in range (data_broadband.parameter_dict['segment_number']):
        br_segment=network.Broadband_line_segment(data_broadband)
        br_line_segment_array.append(br_segment)
        br_line_segment_length_array.append(br_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df1=pd.DataFrame()
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(el_line_segment_array)):
            convert_new=False
            disaggregated_current=True
            joint_trench_current=False
            lifespan_exceeded=el_line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if el_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            el_line_segment_array[i].update_underground_status(convert=convert_new)
            el_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current, joint_trench=joint_trench_current)
            el_line_segment_array[i].calculate_capex()
            el_line_segment_array[i].calculate_opex()
            el_line_segment_array[i].add_opex_interest_rate()
            el_line_segment_array[i].calculate_total_infrastructure_cost()
            el_line_segment_array[i].calculate_environmental_restoration()
            el_line_segment_array[i].calculate_non_fatal_cost()
            el_line_segment_array[i].calculate_fatal_cost()
            el_line_segment_array[i].calculate_total_safety()
            el_line_segment_array[i].calculate_total_cost()

            br_line_segment_array[i].update_underground_status(convert=convert_new)
            br_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current, joint_trench=joint_trench_current)
            br_line_segment_array[i].calculate_capex()
            br_line_segment_array[i].calculate_opex()
            br_line_segment_array[i].add_opex_interest_rate()
            br_line_segment_array[i].calculate_total_infrastructure_cost()
            br_line_segment_array[i].calculate_environmental_restoration()
            br_line_segment_array[i].calculate_non_fatal_cost()
            br_line_segment_array[i].calculate_fatal_cost()
            br_line_segment_array[i].calculate_total_safety()
            br_line_segment_array[i].calculate_total_cost()
                                        
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'capex_el':[el_line_segment_array[i].capex[t]],
                                 'opex_el':[el_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_el':[el_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_el':[el_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_el':[el_line_segment_array[i].non_fatal[t]],
                                 'fatal_el':[el_line_segment_array[i].fatal[t]],
                                 'safety_el':[el_line_segment_array[i].total_safety[t]],
                                 'total_cost_el':[el_line_segment_array[i].total_cost[t]],
                                 'capex_br':[br_line_segment_array[i].capex[t]],
                                 'opex_br':[br_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_br':[br_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_br':[br_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_br':[br_line_segment_array[i].non_fatal[t]],
                                 'fatal_br':[br_line_segment_array[i].fatal[t]],
                                 'safety_br':[br_line_segment_array[i].total_safety[t]],
                                 'total_cost_br':[br_line_segment_array[i].total_cost[t]],
                                 })            
            df1=df1.append(df_new, ignore_index = True)
    df1.to_csv(r'../../results/outcomes/Cost/Simulation/S9-cost-simulation.csv', index = False)
    return(df1.set_index(["year","segment number"]))
    #return(df1)

# Define S10 simulation function
def run_cost_simulation_S10(data, data_broadband):
    # SQ for electric line segments
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
            convert_new=False
            disaggregated_current=True
            joint_trench_current=True
            aggressive_current=True
            lifespan_exceeded=el_line_segment_array[i].update_age(aggressive=aggressive_current)
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if el_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            el_line_segment_array[i].update_underground_status(convert=convert_new)
            el_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current, joint_trench=joint_trench_current)
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
            disaggregated_current=True
            joint_trench_current=True
            aggressive_current=True
            lifespan_exceeded=el_line_segment_array[i].update_age(aggressive=aggressive_current)
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if br_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            br_line_segment_array[i].update_underground_status(convert=convert_new)
            br_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current, joint_trench=joint_trench_current)
            br_line_segment_array[i].calculate_capex()
            br_line_segment_array[i].calculate_opex()
            br_line_segment_array[i].add_opex_interest_rate()
            br_line_segment_array[i].calculate_total_infrastructure_cost()
            br_line_segment_array[i].calculate_environmental_restoration()
            br_line_segment_array[i].calculate_non_fatal_cost()
            br_line_segment_array[i].calculate_fatal_cost()
            br_line_segment_array[i].calculate_total_safety()
            br_line_segment_array[i].calculate_total_cost()                                        
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'capex_el':[el_line_segment_array[i].capex[t]],
                                 'opex_el':[el_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_el':[el_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_el':[el_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_el':[el_line_segment_array[i].non_fatal[t]],
                                 'fatal_el':[el_line_segment_array[i].fatal[t]],
                                 'safety_el':[el_line_segment_array[i].total_safety[t]],
                                 'total_cost_el':[el_line_segment_array[i].total_cost[t]],
                                 'capex_br':[br_line_segment_array[i].capex[t]],
                                 'opex_br':[br_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_br':[br_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_br':[br_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_br':[br_line_segment_array[i].non_fatal[t]],
                                 'fatal_br':[br_line_segment_array[i].fatal[t]],
                                 'safety_br':[br_line_segment_array[i].total_safety[t]],
                                 'total_cost_br':[br_line_segment_array[i].total_cost[t]],
                                 })            
            df1=df1.append(df_new, ignore_index = True)
    df1.to_csv(r'../../results/outcomes/Cost/Simulation/S10-cost-simulation.csv', index = False)
    return(df1.set_index(["year","segment number"]))
    #return(df1)

# Define S11 simulation function
def run_cost_simulation_S11(data, data_broadband):
    # SQ for electric line segments
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
            convert_new=False
            disaggregated_current=True
            joint_trench_current=False
            lifespan_exceeded=el_line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if el_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            el_line_segment_array[i].update_underground_status(convert=convert_new)
            el_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current, joint_trench=joint_trench_current)
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
            disaggregated_current=True
            joint_trench_current=False
            lifespan_exceeded=br_line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if br_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            br_line_segment_array[i].update_underground_status(convert=convert_new)
            br_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current, joint_trench=joint_trench_current)
            br_line_segment_array[i].calculate_capex()
            br_line_segment_array[i].calculate_opex()
            br_line_segment_array[i].add_opex_interest_rate()
            br_line_segment_array[i].calculate_total_infrastructure_cost()
            br_line_segment_array[i].calculate_environmental_restoration()
            br_line_segment_array[i].calculate_non_fatal_cost()
            br_line_segment_array[i].calculate_fatal_cost()
            br_line_segment_array[i].calculate_total_safety()
            br_line_segment_array[i].calculate_total_cost()
                                        
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'capex_el':[el_line_segment_array[i].capex[t]],
                                 'opex_el':[el_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_el':[el_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_el':[el_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_el':[el_line_segment_array[i].non_fatal[t]],
                                 'fatal_el':[el_line_segment_array[i].fatal[t]],
                                 'safety_el':[el_line_segment_array[i].total_safety[t]],
                                 'total_cost_el':[el_line_segment_array[i].total_cost[t]],
                                 'capex_br':[br_line_segment_array[i].capex[t]],
                                 'opex_br':[br_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_br':[br_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_br':[br_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_br':[br_line_segment_array[i].non_fatal[t]],
                                 'fatal_br':[br_line_segment_array[i].fatal[t]],
                                 'safety_br':[br_line_segment_array[i].total_safety[t]],
                                 'total_cost_br':[br_line_segment_array[i].total_cost[t]],
                                 })            
            df1=df1.append(df_new, ignore_index = True)
    df1.to_csv(r'../../results/outcomes/Cost/Simulation/S11-cost-simulation.csv', index = False)
    return(df1.set_index(["year","segment number"]))
    #return(df1)

# Define S12 simulation function
def run_cost_simulation_S12(data, data_broadband):
    # SQ for electric and broadband line segments
    el_line_segment_array=[]
    el_line_segment_length_array=[]
    br_line_segment_array=[]
    br_line_segment_length_array=[]
    for i in range (data.parameter_dict['segment_number']):
        el_segment=network.Electric_line_segment(data)
        el_line_segment_array.append(el_segment)
        el_line_segment_length_array.append(el_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    for i in range (data_broadband.parameter_dict['segment_number']):
        br_segment=network.Broadband_line_segment(data_broadband)
        br_line_segment_array.append(br_segment)
        br_line_segment_length_array.append(br_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df1=pd.DataFrame()
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(el_line_segment_array)):
            convert_new=False
            disaggregated_current=True
            joint_trench_current=True
            aggressive_current=True
            lifespan_exceeded=el_line_segment_array[i].update_age(aggressive=aggressive_current)
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if el_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            el_line_segment_array[i].update_underground_status(convert=convert_new)
            el_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current, joint_trench=joint_trench_current)
            el_line_segment_array[i].calculate_capex()
            el_line_segment_array[i].calculate_opex()
            el_line_segment_array[i].add_opex_interest_rate()
            el_line_segment_array[i].calculate_total_infrastructure_cost()
            el_line_segment_array[i].calculate_environmental_restoration()
            el_line_segment_array[i].calculate_non_fatal_cost()
            el_line_segment_array[i].calculate_fatal_cost()
            el_line_segment_array[i].calculate_total_safety()
            el_line_segment_array[i].calculate_total_cost()

            br_line_segment_array[i].update_underground_status(convert=convert_new)
            br_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current, joint_trench=joint_trench_current)
            br_line_segment_array[i].calculate_capex()
            br_line_segment_array[i].calculate_opex()
            br_line_segment_array[i].add_opex_interest_rate()
            br_line_segment_array[i].calculate_total_infrastructure_cost()
            br_line_segment_array[i].calculate_environmental_restoration()
            br_line_segment_array[i].calculate_non_fatal_cost()
            br_line_segment_array[i].calculate_fatal_cost()
            br_line_segment_array[i].calculate_total_safety()
            br_line_segment_array[i].calculate_total_cost()
                                        
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'capex_el':[el_line_segment_array[i].capex[t]],
                                 'opex_el':[el_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_el':[el_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_el':[el_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_el':[el_line_segment_array[i].non_fatal[t]],
                                 'fatal_el':[el_line_segment_array[i].fatal[t]],
                                 'safety_el':[el_line_segment_array[i].total_safety[t]],
                                 'total_cost_el':[el_line_segment_array[i].total_cost[t]],
                                 'capex_br':[br_line_segment_array[i].capex[t]],
                                 'opex_br':[br_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_br':[br_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_br':[br_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_br':[br_line_segment_array[i].non_fatal[t]],
                                 'fatal_br':[br_line_segment_array[i].fatal[t]],
                                 'safety_br':[br_line_segment_array[i].total_safety[t]],
                                 'total_cost_br':[br_line_segment_array[i].total_cost[t]],
                                 })            
            df1=df1.append(df_new, ignore_index = True)
    df1.to_csv(r'../../results/outcomes/Cost/Simulation/S12-cost-simulation.csv', index = False)
    return(df1.set_index(["year","segment number"]))
    #return(df1)

# Define S13 simulation function
def run_cost_simulation_S13(data, data_broadband):
    # SQ for electric and broadband line segments
    el_line_segment_array=[]
    el_line_segment_length_array=[]
    br_line_segment_array=[]
    br_line_segment_length_array=[]
    for i in range (data.parameter_dict['segment_number']):
        el_segment=network.Electric_line_segment(data)
        el_line_segment_array.append(el_segment)
        el_line_segment_length_array.append(el_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    for i in range (data_broadband.parameter_dict['segment_number']):
        br_segment=network.Broadband_line_segment(data_broadband)
        br_line_segment_array.append(br_segment)
        br_line_segment_length_array.append(br_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df1=pd.DataFrame()
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(el_line_segment_array)):
            convert_new=False
            disaggregated_current=True
            joint_trench_current=False
            aggressive_current=True
            lifespan_exceeded=el_line_segment_array[i].update_age(aggressive=aggressive_current)
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if el_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            el_line_segment_array[i].update_underground_status(convert=convert_new)
            el_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current, joint_trench=joint_trench_current)
            el_line_segment_array[i].calculate_capex()
            el_line_segment_array[i].calculate_opex()
            el_line_segment_array[i].add_opex_interest_rate()
            el_line_segment_array[i].calculate_total_infrastructure_cost()
            el_line_segment_array[i].calculate_environmental_restoration()
            el_line_segment_array[i].calculate_non_fatal_cost()
            el_line_segment_array[i].calculate_fatal_cost()
            el_line_segment_array[i].calculate_total_safety()
            el_line_segment_array[i].calculate_total_cost()

            br_line_segment_array[i].update_underground_status(convert=convert_new)
            br_line_segment_array[i].calculate_replcost(disaggregated_function=disaggregated_current, joint_trench=joint_trench_current)
            br_line_segment_array[i].calculate_capex()
            br_line_segment_array[i].calculate_opex()
            br_line_segment_array[i].add_opex_interest_rate()
            br_line_segment_array[i].calculate_total_infrastructure_cost()
            br_line_segment_array[i].calculate_environmental_restoration()
            br_line_segment_array[i].calculate_non_fatal_cost()
            br_line_segment_array[i].calculate_fatal_cost()
            br_line_segment_array[i].calculate_total_safety()
            br_line_segment_array[i].calculate_total_cost()
                                        
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'capex_el':[el_line_segment_array[i].capex[t]],
                                 'opex_el':[el_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_el':[el_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_el':[el_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_el':[el_line_segment_array[i].non_fatal[t]],
                                 'fatal_el':[el_line_segment_array[i].fatal[t]],
                                 'safety_el':[el_line_segment_array[i].total_safety[t]],
                                 'total_cost_el':[el_line_segment_array[i].total_cost[t]],
                                 'capex_br':[br_line_segment_array[i].capex[t]],
                                 'opex_br':[br_line_segment_array[i].opex[t]],
                                 'lifecycle_infrastructure_br':[br_line_segment_array[i].total_infra[t]],
                                 'environmental_restoration_br':[br_line_segment_array[i].environmental_restoration[t]],
                                 'non_fatal_br':[br_line_segment_array[i].non_fatal[t]],
                                 'fatal_br':[br_line_segment_array[i].fatal[t]],
                                 'safety_br':[br_line_segment_array[i].total_safety[t]],
                                 'total_cost_br':[br_line_segment_array[i].total_cost[t]],
                                 })            
            df1=df1.append(df_new, ignore_index = True)
    df1.to_csv(r'../../results/outcomes/Cost/Simulation/S13-cost-simulation.csv', index = False)
    return(df1.set_index(["year","segment number"]))
    #return(df1)


### Benefits simulation functions

# S1 benefit simulation function 
def run_benefit_simulation_S1(data, data_broadband):
    #electric line segment
    el_line_segment_array=[]
    el_line_segment_length_array=[]
    el_total_mileage = data.parameter_dict['total_length']
    el_underground_mileage = 0 #data.parameter_dict['total_length_underground']
    el_underground_proportion = 1 - data.parameter_dict['overhead_proportion']
    for i in range (data.parameter_dict['segment_number']):
        el_segment=network.Electric_line_segment(data)
        el_line_segment_array.append(el_segment)
        el_line_segment_length_array.append(el_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    df1=pd.DataFrame()
    df2=pd.DataFrame()
    df_under_pro=pd.DataFrame()
    df_under_pro1=pd.DataFrame()
    df_under_pro2=pd.DataFrame()
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(el_line_segment_array)):
            if el_line_segment_array[i].underground[-1] == 1:
                el_underground_mileage += el_line_segment_array[i].length
            el_line_segment_array[i].update_underground_status()
            el_line_segment_array[i].update_age()
            el_line_segment_array[i].calculate_economic_loss() 
            el_line_segment_array[i].calculate_aesthetic_benefits()
            el_line_segment_array[i].add_aesthetic_benefits_interest_rate()
            el_line_segment_array[i].add_economic_loss_interest_rate()
            #el_line_segment_array[i].calculate_total_losses()    
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age_el': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'aesthetic_benefit_el':[el_line_segment_array[i].total_inflated_aesthetic_benefits[t]],
                                 'economic_losses_el':[el_line_segment_array[i].total_inflated_economic_losses[t]],
                                 #'total_losses_el':[el_line_segment_array[i].total_losses[t]],
                                 })   
            df_new['aesthetic_benefit_el']=df_new['aesthetic_benefit_el']*el_underground_proportion
            df1=df1.append(df_new, ignore_index = True)
        el_underground_proportion = el_underground_mileage/el_total_mileage
        print('el under proportion:',el_underground_proportion)
        el_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']    
        df_under_pro_new=pd.DataFrame({
            'el_underground_proportion': [el_underground_proportion],
            }) 
        df_under_pro1=df_under_pro1.append(df_under_pro_new, ignore_index = True)
 
    
    # Broadband line segment    
    br_line_segment_array=[]
    br_line_segment_length_array=[]
    br_total_mileage = data_broadband.parameter_dict['total_length']
    br_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']
    br_underground_proportion = 1 - data_broadband.parameter_dict['overhead_proportion']
    for i in range (data_broadband.parameter_dict['segment_number']):
        br_segment=network.Broadband_line_segment(data_broadband)
        br_line_segment_array.append(br_segment)
        br_line_segment_length_array.append(br_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    for t in range (data_broadband.parameter_dict['analysis_years']):
        for i in range (len(br_line_segment_array)):
            if br_line_segment_array[i].underground[-1] == 1:
                br_underground_mileage += br_line_segment_array[i].length
            br_line_segment_array[i].update_underground_status()
            br_line_segment_array[i].update_age()
            br_line_segment_array[i].calculate_economic_loss(proportion=br_underground_proportion)
            df_new2=pd.DataFrame({
                                 'age_br': [br_line_segment_array[i].age[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'economic_loss_br':[br_line_segment_array[i].total_economic_losses[t]]
                                 })            
            df2=df2.append(df_new2, ignore_index = True)
        br_underground_proportion = br_underground_mileage/br_total_mileage
        print('br under proportion:',br_underground_proportion)
        br_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']
        df_under_pro_new2=pd.DataFrame({
            'br_underground_proportion': [br_underground_proportion],
            }) 
        df_under_pro2=df_under_pro2.append(df_under_pro_new2, ignore_index = True)
    df=pd.concat([df1, df2], axis=1)
    df_under_pro=pd.concat([df_under_pro1, df_under_pro2], axis=1)
    df.to_csv(r'../../results/outcomes/Benefit/Simulation/S1-benefit-simulation.csv', index = False)
    df_under_pro.to_csv(r'../../results/outcomes/S1-under-proportion.csv', index = False)
    return(df.set_index(["year","segment number"]))
    #return(df)

# S2 benefit simulation function 
def run_benefit_simulation_S2(data, data_broadband):
    #electric line segment
    el_line_segment_array=[]
    el_line_segment_length_array=[]
    el_total_mileage = data.parameter_dict['total_length']
    el_underground_mileage = 0 #data.parameter_dict['total_length_underground']
    el_underground_proportion = 1 - data.parameter_dict['overhead_proportion']
    for i in range (data.parameter_dict['segment_number']):
        el_segment=network.Electric_line_segment(data)
        el_line_segment_array.append(el_segment)
        el_line_segment_length_array.append(el_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    df1=pd.DataFrame()
    df2=pd.DataFrame()
    df_under_pro=pd.DataFrame()
    df_under_pro1=pd.DataFrame()
    df_under_pro2=pd.DataFrame()
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(el_line_segment_array)):
            if el_line_segment_array[i].underground[-1] == 1:
                el_underground_mileage += el_line_segment_array[i].length
            el_line_segment_array[i].update_underground_status()
            el_line_segment_array[i].update_age()
            el_line_segment_array[i].calculate_economic_loss() 
            el_line_segment_array[i].calculate_aesthetic_benefits()
            el_line_segment_array[i].add_aesthetic_benefits_interest_rate()
            el_line_segment_array[i].add_economic_loss_interest_rate()
           #el_line_segment_array[i].calculate_total_losses()    
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age_el': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'aesthetic_benefit_el':[el_line_segment_array[i].total_inflated_aesthetic_benefits[t]],
                                 'economic_losses_el':[el_line_segment_array[i].total_inflated_economic_losses[t]],
                                 #'total_losses_el':[el_line_segment_array[i].total_losses[t]],
                                 })   
            df_new['aesthetic_benefit_el']=df_new['aesthetic_benefit_el']*el_underground_proportion
            df1=df1.append(df_new, ignore_index = True)
        el_underground_proportion = el_underground_mileage/el_total_mileage
        print('el under proportion:',el_underground_proportion)
        el_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']    
        df_under_pro_new=pd.DataFrame({
            'el_underground_proportion': [el_underground_proportion],
            }) 
        df_under_pro1=df_under_pro1.append(df_under_pro_new, ignore_index = True)
 
    
    # Broadband line segment    
    br_line_segment_array=[]
    br_line_segment_length_array=[]
    br_total_mileage = data_broadband.parameter_dict['total_length']
    br_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']
    br_underground_proportion = 1 - data_broadband.parameter_dict['overhead_proportion']
    for i in range (data_broadband.parameter_dict['segment_number']):
        br_segment=network.Broadband_line_segment(data_broadband)
        br_line_segment_array.append(br_segment)
        br_line_segment_length_array.append(br_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    for t in range (data_broadband.parameter_dict['analysis_years']):
        for i in range (len(br_line_segment_array)):
            if br_line_segment_array[i].underground[-1] == 1:
                br_underground_mileage += br_line_segment_array[i].length
            convert_new=False
            disaggregated_current=True
            lifespan_exceeded=br_line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if br_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            br_line_segment_array[i].update_underground_status(convert=convert_new)
            br_line_segment_array[i].calculate_economic_loss(proportion=br_underground_proportion)
            df_new2=pd.DataFrame({
                                 'age_br': [br_line_segment_array[i].age[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'economic_loss_br':[br_line_segment_array[i].total_economic_losses[t]]
                                 })            
            df2=df2.append(df_new2, ignore_index = True)
        br_underground_proportion = br_underground_mileage/br_total_mileage
        print('br under proportion:',br_underground_proportion)
        br_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']
        df_under_pro_new2=pd.DataFrame({
            'br_underground_proportion': [br_underground_proportion],
            }) 
        df_under_pro2=df_under_pro2.append(df_under_pro_new2, ignore_index = True)
    df=pd.concat([df1, df2], axis=1)
    df_under_pro=pd.concat([df_under_pro1, df_under_pro2], axis=1)
    df.to_csv(r'../../results/outcomes/Benefit/Simulation/S2-benefit-simulation.csv', index = False)
    df_under_pro.to_csv(r'../../results/outcomes/S2-under-proportion.csv', index = False)
    return(df.set_index(["year","segment number"]))
    #return(df)  



# S3 benefit simulation function 
def run_benefit_simulation_S3(data, data_broadband):
    #electric line segment
    el_line_segment_array=[]
    el_line_segment_length_array=[]
    el_total_mileage = data.parameter_dict['total_length']
    el_underground_mileage = 0 #data.parameter_dict['total_length_underground']
    el_underground_proportion = 1 - data.parameter_dict['overhead_proportion']
    for i in range (data.parameter_dict['segment_number']):
        el_segment=network.Electric_line_segment(data)
        el_line_segment_array.append(el_segment)
        el_line_segment_length_array.append(el_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    df1=pd.DataFrame()
    df2=pd.DataFrame()
    df_under_pro=pd.DataFrame()
    df_under_pro1=pd.DataFrame()
    df_under_pro2=pd.DataFrame()
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(el_line_segment_array)):
            if el_line_segment_array[i].underground[-1] == 1:
                el_underground_mileage += el_line_segment_array[i].length
            el_line_segment_array[i].update_underground_status()
            el_line_segment_array[i].update_age()
            el_line_segment_array[i].calculate_economic_loss() 
            el_line_segment_array[i].calculate_aesthetic_benefits()
            el_line_segment_array[i].add_aesthetic_benefits_interest_rate()
            el_line_segment_array[i].add_economic_loss_interest_rate()
            #el_line_segment_array[i].calculate_total_losses()    
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age_el': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'aesthetic_benefit_el':[el_line_segment_array[i].total_inflated_aesthetic_benefits[t]],
                                 'economic_losses_el':[el_line_segment_array[i].total_inflated_economic_losses[t]],
                                 #'total_losses_el':[el_line_segment_array[i].total_losses[t]],
                                 })   
            df_new['aesthetic_benefit_el']=df_new['aesthetic_benefit_el']*el_underground_proportion
            df1=df1.append(df_new, ignore_index = True)
        el_underground_proportion = el_underground_mileage/el_total_mileage
        print('el under proportion:',el_underground_proportion)
        el_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']    
        df_under_pro_new=pd.DataFrame({
            'el_underground_proportion': [el_underground_proportion],
            }) 
        df_under_pro1=df_under_pro1.append(df_under_pro_new, ignore_index = True)
     
    # Broadband line segment    
    br_line_segment_array=[]
    br_line_segment_length_array=[]
    br_total_mileage = data_broadband.parameter_dict['total_length']
    br_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']
    br_underground_proportion = 1 - data_broadband.parameter_dict['overhead_proportion']
    for i in range (data_broadband.parameter_dict['segment_number']):
        br_segment=network.Broadband_line_segment(data_broadband)
        br_line_segment_array.append(br_segment)
        br_line_segment_length_array.append(br_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    for t in range (data_broadband.parameter_dict['analysis_years']):
        for i in range (len(br_line_segment_array)):
            if br_line_segment_array[i].underground[-1] == 1:
                br_underground_mileage += br_line_segment_array[i].length
            convert_new=False
            disaggregated_current=True
            aggressive_current=True
            lifespan_exceeded=br_line_segment_array[i].update_age(aggressive=aggressive_current)
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if br_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            br_line_segment_array[i].update_underground_status(convert=convert_new)
            br_line_segment_array[i].calculate_economic_loss(proportion=br_underground_proportion)
            df_new2=pd.DataFrame({
                                 'age_br': [br_line_segment_array[i].age[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'economic_loss_br':[br_line_segment_array[i].total_economic_losses[t]]
                                 })            
            df2=df2.append(df_new2, ignore_index = True)
        br_underground_proportion = br_underground_mileage/br_total_mileage
        print('br under proportion:',br_underground_proportion)
        br_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']
        df_under_pro_new2=pd.DataFrame({
            'br_underground_proportion': [br_underground_proportion],
            }) 
        df_under_pro2=df_under_pro2.append(df_under_pro_new2, ignore_index = True)
    df=pd.concat([df1, df2], axis=1)
    df_under_pro=pd.concat([df_under_pro1, df_under_pro2], axis=1)
    df.to_csv(r'../../results/outcomes/Benefit/Simulation/S3-benefit-simulation.csv', index = False)
    df_under_pro.to_csv(r'../../results/outcomes/S3-under-proportion.csv', index = False)
    return(df.set_index(["year","segment number"]))
    #return(df)

# S4 benefit simulation function 
def run_benefit_simulation_S4(data, data_broadband):
    #electric line segment
    el_line_segment_array=[]
    el_line_segment_length_array=[]
    el_total_mileage = data.parameter_dict['total_length']
    el_underground_mileage = 0 #data.parameter_dict['total_length_underground']
    el_underground_proportion = 1 - data.parameter_dict['overhead_proportion']
    for i in range (data.parameter_dict['segment_number']):
        el_segment=network.Electric_line_segment(data)
        el_line_segment_array.append(el_segment)
        el_line_segment_length_array.append(el_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    df1=pd.DataFrame()
    df2=pd.DataFrame()
    df_under_pro=pd.DataFrame()
    df_under_pro1=pd.DataFrame()
    df_under_pro2=pd.DataFrame()
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(el_line_segment_array)):
            if el_line_segment_array[i].underground[-1] == 1:
                el_underground_mileage += el_line_segment_array[i].length
            convert_new=False
            lifespan_exceeded=el_line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if el_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            el_line_segment_array[i].update_underground_status(convert=convert_new)
            el_line_segment_array[i].calculate_economic_loss() 
            el_line_segment_array[i].calculate_aesthetic_benefits()
            el_line_segment_array[i].add_aesthetic_benefits_interest_rate()
            el_line_segment_array[i].add_economic_loss_interest_rate()
            #el_line_segment_array[i].calculate_total_losses()    
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age_el': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'aesthetic_benefit_el':[el_line_segment_array[i].total_inflated_aesthetic_benefits[t]],
                                 'economic_losses_el':[el_line_segment_array[i].total_inflated_economic_losses[t]],
                                 #'total_losses_el':[el_line_segment_array[i].total_losses[t]],
                                 })   
            df_new['aesthetic_benefit_el']=df_new['aesthetic_benefit_el']*el_underground_proportion
            df1=df1.append(df_new, ignore_index = True)
        el_underground_proportion = el_underground_mileage/el_total_mileage
        print('el under proportion:',el_underground_proportion)
        el_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']    
        df_under_pro_new=pd.DataFrame({
            'el_underground_proportion': [el_underground_proportion],
            }) 
        df_under_pro1=df_under_pro1.append(df_under_pro_new, ignore_index = True)
        
    # Broadband line segment    
    br_line_segment_array=[]
    br_line_segment_length_array=[]
    br_total_mileage = data_broadband.parameter_dict['total_length']
    br_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']
    br_underground_proportion = 1 - data_broadband.parameter_dict['overhead_proportion']
    for i in range (data_broadband.parameter_dict['segment_number']):
        br_segment=network.Broadband_line_segment(data_broadband)
        br_line_segment_array.append(br_segment)
        br_line_segment_length_array.append(br_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    for t in range (data_broadband.parameter_dict['analysis_years']):
        for i in range (len(br_line_segment_array)):
            if br_line_segment_array[i].underground[-1] == 1:
                br_underground_mileage += br_line_segment_array[i].length
            br_line_segment_array[i].update_underground_status()
            br_line_segment_array[i].update_age()
            br_line_segment_array[i].calculate_economic_loss(proportion=br_underground_proportion)
            df_new2=pd.DataFrame({
                                 'age_br': [br_line_segment_array[i].age[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'economic_loss_br':[br_line_segment_array[i].total_economic_losses[t]]
                                 })            
            df2=df2.append(df_new2, ignore_index = True)
        br_underground_proportion = br_underground_mileage/br_total_mileage
        print('br under proportion:',br_underground_proportion)
        br_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']
        df_under_pro_new2=pd.DataFrame({
            'br_underground_proportion': [br_underground_proportion],
            }) 
        df_under_pro2=df_under_pro2.append(df_under_pro_new2, ignore_index = True)
    df=pd.concat([df1, df2], axis=1)
    df_under_pro=pd.concat([df_under_pro1, df_under_pro2], axis=1)
    df.to_csv(r'../../results/outcomes/Benefit/Simulation/S4-benefit-simulation.csv', index = False)
    df_under_pro.to_csv(r'../../results/outcomes/S4-under-proportion.csv', index = False)
    return(df.set_index(["year","segment number"]))
    #return(df)

# S5 benefit simulation function 
def run_benefit_simulation_S5(data, data_broadband):
    #electric line segment
    el_line_segment_array=[]
    el_line_segment_length_array=[]
    el_total_mileage = data.parameter_dict['total_length']
    el_underground_mileage = 0 #data.parameter_dict['total_length_underground']
    el_underground_proportion = 1 - data.parameter_dict['overhead_proportion']
    for i in range (data.parameter_dict['segment_number']):
        el_segment=network.Electric_line_segment(data)
        el_line_segment_array.append(el_segment)
        el_line_segment_length_array.append(el_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    df1=pd.DataFrame()
    df2=pd.DataFrame()
    df_under_pro=pd.DataFrame()
    df_under_pro1=pd.DataFrame()
    df_under_pro2=pd.DataFrame()
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(el_line_segment_array)):
            if el_line_segment_array[i].underground[-1] == 1:
                el_underground_mileage += el_line_segment_array[i].length
            convert_new=False
            aggressive_current=True
            lifespan_exceeded=el_line_segment_array[i].update_age(aggressive=aggressive_current)
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if el_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            el_line_segment_array[i].update_underground_status(convert=convert_new)
            el_line_segment_array[i].calculate_economic_loss() 
            el_line_segment_array[i].calculate_aesthetic_benefits()
            el_line_segment_array[i].add_aesthetic_benefits_interest_rate()
            el_line_segment_array[i].add_economic_loss_interest_rate()
            #el_line_segment_array[i].calculate_total_losses()    
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age_el': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'aesthetic_benefit_el':[el_line_segment_array[i].total_inflated_aesthetic_benefits[t]],
                                 'economic_losses_el':[el_line_segment_array[i].total_inflated_economic_losses[t]],
                                 #'total_losses_el':[el_line_segment_array[i].total_losses[t]],
                                 })   
            df_new['aesthetic_benefit_el']=df_new['aesthetic_benefit_el']*el_underground_proportion
            df1=df1.append(df_new, ignore_index = True)
        el_underground_proportion = el_underground_mileage/el_total_mileage
        print('el under proportion:',el_underground_proportion)
        el_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']    
        df_under_pro_new=pd.DataFrame({
            'el_underground_proportion': [el_underground_proportion],
            }) 
        df_under_pro1=df_under_pro1.append(df_under_pro_new, ignore_index = True)
    
    # Broadband line segment    
    br_line_segment_array=[]
    br_line_segment_length_array=[]
    br_total_mileage = data_broadband.parameter_dict['total_length']
    br_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']
    br_underground_proportion = 1 - data_broadband.parameter_dict['overhead_proportion']
    for i in range (data_broadband.parameter_dict['segment_number']):
        br_segment=network.Broadband_line_segment(data_broadband)
        br_line_segment_array.append(br_segment)
        br_line_segment_length_array.append(br_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    for t in range (data_broadband.parameter_dict['analysis_years']):
        for i in range (len(br_line_segment_array)):
            if br_line_segment_array[i].underground[-1] == 1:
                br_underground_mileage += br_line_segment_array[i].length
            br_line_segment_array[i].update_underground_status()
            br_line_segment_array[i].update_age()
            br_line_segment_array[i].calculate_economic_loss(proportion=br_underground_proportion)
            df_new2=pd.DataFrame({
                                 'age_br': [br_line_segment_array[i].age[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'economic_loss_br':[br_line_segment_array[i].total_economic_losses[t]]
                                 })            
            df2=df2.append(df_new2, ignore_index = True)
        br_underground_proportion = br_underground_mileage/br_total_mileage
        print('br under proportion:',br_underground_proportion)
        br_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']
        df_under_pro_new2=pd.DataFrame({
            'br_underground_proportion': [br_underground_proportion],
            }) 
        df_under_pro2=df_under_pro2.append(df_under_pro_new2, ignore_index = True)
    df=pd.concat([df1, df2], axis=1)
    df_under_pro=pd.concat([df_under_pro1, df_under_pro2], axis=1)
    df.to_csv(r'../../results/outcomes/Benefit/Simulation/S5-benefit-simulation.csv', index = False)
    df_under_pro.to_csv(r'../../results/outcomes/S5-under-proportion.csv', index = False)
    return(df.set_index(["year","segment number"]))
    #return(df)

### S6 to S9 benefit simulation functions
def run_benefit_simulation_S6_to_s9(data, data_broadband):
    #electric line segment
    el_line_segment_array=[]
    el_line_segment_length_array=[]
    el_total_mileage = data.parameter_dict['total_length']
    el_underground_mileage = 0 #data.parameter_dict['total_length_underground']
    el_underground_proportion = 1 - data.parameter_dict['overhead_proportion']
    for i in range (data.parameter_dict['segment_number']):
        el_segment=network.Electric_line_segment(data)
        el_line_segment_array.append(el_segment)
        el_line_segment_length_array.append(el_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    df1=pd.DataFrame()
    df2=pd.DataFrame()
    df_under_pro=pd.DataFrame()
    df_under_pro1=pd.DataFrame()
    df_under_pro2=pd.DataFrame()
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(el_line_segment_array)):
            if el_line_segment_array[i].underground[-1] == 1:
                el_underground_mileage += el_line_segment_array[i].length
            convert_new=False
            lifespan_exceeded=el_line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if el_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            el_line_segment_array[i].update_underground_status(convert=convert_new)
            el_line_segment_array[i].calculate_economic_loss() 
            el_line_segment_array[i].calculate_aesthetic_benefits()
            el_line_segment_array[i].add_aesthetic_benefits_interest_rate()
            el_line_segment_array[i].add_economic_loss_interest_rate()
            #el_line_segment_array[i].calculate_total_losses()    
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age_el': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'aesthetic_benefit_el':[el_line_segment_array[i].total_inflated_aesthetic_benefits[t]],
                                 'economic_losses_el':[el_line_segment_array[i].total_inflated_economic_losses[t]],
                                 #'total_losses_el':[el_line_segment_array[i].total_losses[t]],
                                 })   
            df_new['aesthetic_benefit_el']=df_new['aesthetic_benefit_el']*el_underground_proportion
            df1=df1.append(df_new, ignore_index = True)
        el_underground_proportion = el_underground_mileage/el_total_mileage
        print('el under proportion:',el_underground_proportion)
        el_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']    
        df_under_pro_new=pd.DataFrame({
            'el_underground_proportion': [el_underground_proportion],
            }) 
        df_under_pro1=df_under_pro1.append(df_under_pro_new, ignore_index = True)
 
    
    # Broadband line segment    
    br_line_segment_array=[]
    br_line_segment_length_array=[]
    br_total_mileage = data_broadband.parameter_dict['total_length']
    br_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']
    br_underground_proportion = 1 - data_broadband.parameter_dict['overhead_proportion']
    for i in range (data_broadband.parameter_dict['segment_number']):
        br_segment=network.Broadband_line_segment(data_broadband)
        br_line_segment_array.append(br_segment)
        br_line_segment_length_array.append(br_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    for t in range (data_broadband.parameter_dict['analysis_years']):
        for i in range (len(br_line_segment_array)):
            if br_line_segment_array[i].underground[-1] == 1:
                br_underground_mileage += br_line_segment_array[i].length
            convert_new=False
            disaggregated_current=True
            lifespan_exceeded=br_line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if br_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            br_line_segment_array[i].update_underground_status(convert=convert_new)
            br_line_segment_array[i].calculate_economic_loss(proportion=br_underground_proportion)
            df_new2=pd.DataFrame({
                                 'age_br': [br_line_segment_array[i].age[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'economic_loss_br':[br_line_segment_array[i].total_economic_losses[t]]
                                 })            
            df2=df2.append(df_new2, ignore_index = True)
        br_underground_proportion = br_underground_mileage/br_total_mileage
        print('br under proportion:',br_underground_proportion)
        br_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']
        df_under_pro_new2=pd.DataFrame({
            'br_underground_proportion': [br_underground_proportion],
            }) 
        df_under_pro2=df_under_pro2.append(df_under_pro_new2, ignore_index = True)
    df=pd.concat([df1, df2], axis=1)
    df_under_pro=pd.concat([df_under_pro1, df_under_pro2], axis=1)
    df.to_csv(r'../../results/outcomes/Benefit/Simulation/S6-to-S9-benefit-simulation.csv', index = False)
    df_under_pro.to_csv(r'../../results/outcomes/S6-to-S9-under-proportion.csv', index = False)
    return(df.set_index(["year","segment number"]))
    #return(df)

### S10 to S13 benefit simulation functions
def run_benefit_simulation_S10_to_s13(data, data_broadband):
    #electric line segment
    el_line_segment_array=[]
    el_line_segment_length_array=[]
    el_total_mileage = data.parameter_dict['total_length']
    el_underground_mileage = 0 #data.parameter_dict['total_length_underground']
    el_underground_proportion = 1 - data.parameter_dict['overhead_proportion']
    for i in range (data.parameter_dict['segment_number']):
        el_segment=network.Electric_line_segment(data)
        el_line_segment_array.append(el_segment)
        el_line_segment_length_array.append(el_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    df1=pd.DataFrame()
    df2=pd.DataFrame()
    df_under_pro=pd.DataFrame()
    df_under_pro1=pd.DataFrame()
    df_under_pro2=pd.DataFrame()
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(el_line_segment_array)):
            if el_line_segment_array[i].underground[-1] == 1:
                el_underground_mileage += el_line_segment_array[i].length
            convert_new=False
            aggressive_current=True
            lifespan_exceeded=el_line_segment_array[i].update_age(aggressive=aggressive_current)
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if el_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            el_line_segment_array[i].update_underground_status(convert=convert_new)
            el_line_segment_array[i].calculate_economic_loss() 
            el_line_segment_array[i].calculate_aesthetic_benefits()
            el_line_segment_array[i].add_aesthetic_benefits_interest_rate()
            el_line_segment_array[i].add_economic_loss_interest_rate()
            #el_line_segment_array[i].calculate_total_losses()    
            df_new=pd.DataFrame({
                                 'year': [t],
                                 'segment number':[i],
                                 'length':[el_line_segment_array[i].length],
                                 'age_el': [el_line_segment_array[i].age[t]],
                                 'under_el': [el_line_segment_array[i].underground[t]],
                                 'aesthetic_benefit_el':[el_line_segment_array[i].total_inflated_aesthetic_benefits[t]],
                                 'economic_losses_el':[el_line_segment_array[i].total_inflated_economic_losses[t]],
                                 #'total_losses_el':[el_line_segment_array[i].total_losses[t]],
                                 })   
            df_new['aesthetic_benefit_el']=df_new['aesthetic_benefit_el']*el_underground_proportion
            df1=df1.append(df_new, ignore_index = True)
        el_underground_proportion = el_underground_mileage/el_total_mileage
        print('el under proportion:',el_underground_proportion)
        el_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']    
        df_under_pro_new=pd.DataFrame({
            'el_underground_proportion': [el_underground_proportion],
            }) 
        df_under_pro1=df_under_pro1.append(df_under_pro_new, ignore_index = True)
 

    
    # Broadband line segment    
    br_line_segment_array=[]
    br_line_segment_length_array=[]
    br_total_mileage = data_broadband.parameter_dict['total_length']
    br_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']
    br_underground_proportion = 1 - data_broadband.parameter_dict['overhead_proportion']
    for i in range (data_broadband.parameter_dict['segment_number']):
        br_segment=network.Broadband_line_segment(data_broadband)
        br_line_segment_array.append(br_segment)
        br_line_segment_length_array.append(br_segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    for t in range (data_broadband.parameter_dict['analysis_years']):
        for i in range (len(br_line_segment_array)):
            if br_line_segment_array[i].underground[-1] == 1:
                br_underground_mileage += br_line_segment_array[i].length
            convert_new=False
            disaggregated_current=True
            aggressive_current=True
            lifespan_exceeded=br_line_segment_array[i].update_age(aggressive=aggressive_current)
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if br_line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            br_line_segment_array[i].update_underground_status(convert=convert_new)
            br_line_segment_array[i].calculate_economic_loss(proportion=br_underground_proportion)
            df_new2=pd.DataFrame({
                                 'age_br': [br_line_segment_array[i].age[t]],
                                 'under_br': [br_line_segment_array[i].underground[t]],
                                 'economic_loss_br':[br_line_segment_array[i].total_economic_losses[t]]
                                 })            
            df2=df2.append(df_new2, ignore_index = True)
        br_underground_proportion = br_underground_mileage/br_total_mileage
        print('br under proportion:',br_underground_proportion)
        br_underground_mileage = 0#data_broadband.parameter_dict['total_length_underground']
        df_under_pro_new2=pd.DataFrame({
            'br_underground_proportion': [br_underground_proportion],
            }) 
        df_under_pro2=df_under_pro2.append(df_under_pro_new2, ignore_index = True)
    df=pd.concat([df1, df2], axis=1)
    df_under_pro=pd.concat([df_under_pro1, df_under_pro2], axis=1)
    df.to_csv(r'../../results/outcomes/Benefit/Simulation/S10-to-S13-benefit-simulation.csv', index = False)
    df_under_pro.to_csv(r'../../results/outcomes/S10-to-S13-under-proportion.csv', index = False)
    return(df.set_index(["year","segment number"]))
    #return(df)
