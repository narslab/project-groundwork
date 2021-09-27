# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 10:42:22 2021

@author: Mahsa
"""
###Import Network.py which includes variables and line segment class defenistion
import Network
import numpy as np
import pandas as pd
import random

###
#run simulation for calculating cost elemnts of statusQuo strategy and assign a data frame to them.
def run_cost_simulation_statusQuo_strategy(data):
    line_segment_array=[]
    line_segment_length_array=[]
    for i in range (data.parameter_dict['segment_number']):
        segment=Network.Line_segment(data)
        line_segment_array.append(segment)
        line_segment_length_array.append(segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    for t in range (data.parameter_dict['analysis_years']):
        for i in range (len(line_segment_array)):
            line_segment_array[i].update_underground_status()
            line_segment_array[i].update_age()
            line_segment_array[i].add_replcost_intrest_rate()
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
                                 'capex':[line_segment_array[i].capex[t]],
                                 'opex':[line_segment_array[i].opex[t]],
                                 'total infra':[line_segment_array[i].total_infra[t]],
                                 'environmental restoration':[line_segment_array[i].environmental_restoration[t]],
                                 'non fatal':[line_segment_array[i].non_fatal[t]],
                                 'fatal':[line_segment_array[i].fatal[t]],
                                 'total safety':[line_segment_array[i].total_safety[t]],
                                 'total cost':[line_segment_array[i].total[t]]})            
            df=df.append(df_new, ignore_index = True)
    df.to_csv(r'c:\\Users\\Mahsa\\NARS\\project-groundwork\\results\\outcomes\\Simulation output-StatusQuo strategy.csv', index = False)
    return(df.set_index(["year","segment number"]))


#run simulation for calculating cost elemnts of undergrounding after lifespan strategy and assign a data frame to them.
def run_cost_simulation_under_after_lifespan_strategy(data):
    line_segment_array=[]
    line_segment_length_array=[]
    for i in range (data.parameter_dict['segment_number']):
        segment=Network.Line_segment()
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
            line_segment_array[i].add_replcost_intrest_rate()
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
                                 'capex':[line_segment_array[i].capex[t]],
                                 'opex':[line_segment_array[i].opex[t]],
                                 'total infra':[line_segment_array[i].total_infra[t]],
                                 'environmental restoration':[line_segment_array[i].environmental_restoration[t]],
                                 'non fatal':[line_segment_array[i].non_fatal[t]],
                                 'fatal':[line_segment_array[i].fatal[t]],
                                 'total safety':[line_segment_array[i].total_safety[t]],
                                 'total cost':[line_segment_array[i].total[t]]})             
            df=df.append(df_new, ignore_index = True)    
    df.to_csv(r'c:\\Users\\Mahsa\\NARS\\project-groundwork\\results\\outcomes\\Simulation output-Undergrounding strategy.csv', index = False)
    return(df.set_index(["year","segment number"]))

    
    
