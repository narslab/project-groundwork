# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 10:42:22 2021

@author: Mahsa
"""
###Import network.py which includes variables and line segment class defenistion
import network
import numpy as np
import pandas as pd
import random

data = network.model_inputs()
###
#run simulation for calculating cost elemnts of statusQuo strategy and assign a data frame to them.
def run_cost_simulation_statusQuo_strategy(data):
    line_segment_array=[]
    line_segment_length_array=[]
    for i in range (data.parameter_dict['segment_number']):
        segment=network.Line_segment(data)
        line_segment_array.append(segment)
        line_segment_length_array.append(segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(line_segment_array)):
            #disaggregated_function=True
            line_segment_array[i].update_underground_status()
            line_segment_array[i].update_age()
            line_segment_array[i].calculate_replcost(disaggregated_function=True)
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
                                 'capex':[line_segment_array[i].capex[t]],
                                 'opex':[line_segment_array[i].opex[t]],
                                 'lifecycle infrastructure':[line_segment_array[i].total_infra[t]],
                                 'environmental restoration':[line_segment_array[i].environmental_restoration[t]],
                                 'non fatal':[line_segment_array[i].non_fatal[t]],
                                 'fatal':[line_segment_array[i].fatal[t]],
                                 'safety':[line_segment_array[i].total_safety[t]],
                                 'total cost':[line_segment_array[i].total_cost[t]],
                                 })            
            df=df.append(df_new, ignore_index = True)
    df.to_csv(r'../../results/outcomes/cost-simulation-output-statusQuo-strategy.csv', index = False)
    return(df.set_index(["year","segment number"]))


#run simulation for calculating cost elemnts of undergrounding after lifespan strategy and assign a data frame to them.
def run_cost_simulation_under_after_lifespan_strategy(data):
    line_segment_array=[]
    line_segment_length_array=[]
    for i in range (data.parameter_dict['segment_number']):
        segment=network.Line_segment(data)
        line_segment_array.append(segment)
        line_segment_length_array.append(segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    #underground_length=[]
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(line_segment_array)):
            convert_new=False
            #disaggregated_function=True
            lifespan_exceeded=line_segment_array[i].update_age()
            if lifespan_exceeded==True:
                convert_new+=True
            else:
                if line_segment_array[i].underground[-1]==1:
                    convert_new=True
                else:
                    convert_new=False
            line_segment_array[i].update_underground_status(convert=convert_new)
            line_segment_array[i].calculate_replcost(disaggregated_function=True)
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
                                 #'conversioncost': [line_segment_array[i].conversion_cost[t]],
                                 'capex':[line_segment_array[i].capex[t]],
                                 'opex':[line_segment_array[i].opex[t]],
                                 'lifecycle infrastructure':[line_segment_array[i].total_infra[t]],
                                 'environmental restoration':[line_segment_array[i].environmental_restoration[t]],
                                 'non fatal':[line_segment_array[i].non_fatal[t]],
                                 'fatal':[line_segment_array[i].fatal[t]],
                                 'safety':[line_segment_array[i].total_safety[t]],
                                 'total cost':[line_segment_array[i].total_cost[t]]})             
            df=df.append(df_new, ignore_index = True)    
    df.to_csv(r'../../results/outcomes/cost-simulation-output-undergrounding-strategy.csv', index = False)
    return(df.set_index(["year","segment number"]))

def run_benefit_simulation_statusQuo_strategy(data):
    line_segment_array=[]
    line_segment_length_array=[]
    for i in range (data.parameter_dict['segment_number']):
        segment=network.Line_segment(data)
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
    return(df.set_index(["year","segment number"]))       


def run_benefit_simulation_under_after_lifespan_strategy(data):
    line_segment_array=[]
    line_segment_length_array=[]
    for i in range (data.parameter_dict['segment_number']):
        segment=network.Line_segment(data)
        line_segment_array.append(segment)
        line_segment_length_array.append(segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
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
                                 'aesthetic benefits':[line_segment_array[i].total_inflated_aesthetic_benefits[t]],
                                 'aesthetic losses':[line_segment_array[i].total_inflated_aesthetic_losses[t]],
                                 'economic losses':[line_segment_array[i].total_inflated_economic_losses[t]],
                                 'total losses':[line_segment_array[i].total_losses[t]]
                                 }) 
            df=df.append(df_new, ignore_index = True)
    df.to_csv(r'../../results/outcomes/benefit-simulation-output-under-strategy.csv', index = False)
    return(df.set_index(["year","segment number"]))   

# calculate total length of underground line on each year
def calculate_percentage_underground_UL_strategy(data):    
    line_segment_array=[]
    line_segment_length_array=[]
    for i in range (data.parameter_dict['segment_number']):
        segment=network.Line_segment(data)
        line_segment_array.append(segment)
        line_segment_length_array.append(segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    underground_length=[0]
    underground_percentage=[]
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