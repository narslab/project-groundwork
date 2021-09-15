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
def run_cost_simulation_statusQuo_strategy(years_of_analysis):
    line_segment_array=[]
    line_segment_length_array=[]
    for i in range (Network.segment_number):
        segment=Network.Line_segment(Network.age_shape, Network.age_scale, Network.length_shape, Network.length_scale, 0.66)
        line_segment_array.append(segment)
        line_segment_length_array.append(segment.length)
    np.random.seed(10101)
    random.seed(10102)
    df=pd.DataFrame()
    for t in range (years_of_analysis):
        for i in range (len(line_segment_array)):
            line_segment_array[i].update_age_and_underground_statusQuo()
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
            df_new=pd.DataFrame({'segment number': [i],
                                 'year':[t],
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
    return(df.set_index(["year","segment number"]))


#run simulation for calculating cost elemnts of undergrounding after lifespan strategy and assign a data frame to them.
def run_cost_simulation_under_after_lifespan_strategy(years_of_analysis):
    line_segment_array=[]
    line_segment_length_array=[]
    line_segment_age_array=[]
    line_segment_underground_array=[]
    line_segment_underground_length_total_array=[0 for t in range (years_of_analysis)]
    for i in range (Network.segment_number):
        segment=Network.Line_segment(Network.age_shape, Network.age_scale, Network.length_shape, Network.length_scale, 0.66)
        line_segment_array.append(segment)
        line_segment_length_array.append(segment.length)
        line_segment_age_array.append(segment.age[0])
        line_segment_underground_array.append(segment.underground[0])
        line_segment_underground_length_total_array[0]+=line_segment_array[i].underground[0]
    np.random.seed(10101)
    random.seed(10102)
    #df_line_segment_array=pd.DataFrame([line_segment_length_array, line_segment_age_array,line_segment_underground_array]).transpose()
    #df_line_segment_array.columns=['length','base year age','base year underground']
    #underground_length_new=[]
    df=pd.DataFrame()
    #environmental_cost=[]
    for t in range (years_of_analysis):
        for i in range (len(line_segment_array)):
            line_segment_array[i].update_age_and_underground_under_after_lifespan()
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
            #if t==0:
            #    environmental_cost=0
            #    safety_rate=1
            #    non_fatal_safety_cost= safety_rate * line_segment_array[i].calculate_non_fatal_cost()
            #    fatal_safety_cost= safety_rate * line_segment_array[i].calculate_fatal_cost()
            #    total_safety_cost= safety_rate * line_segment_array[i].calculate_total_safety()
            #else: 
            #    if line_segment_array[i].underground[t]==line_segment_array[i].underground[t-1]:
            #       environmental_cost=0
            #       safety_rate=1
            #        non_fatal_safety_cost= safety_rate * line_segment_array[i].calculate_non_fatal_cost()
            #        fatal_safety_cost= safety_rate * line_segment_array[i].calculate_fatal_cost()
            #        total_safety_cost= safety_rate * line_segment_array[i].calculate_total_safety()
            #    else:
            #        environmental_cost=line_segment_array[i].calculate_environmental_restoration()
            #       safety_rate=(1+line_segment_array[i].length)
            #       non_fatal_safety_cost= safety_rate * line_segment_array[i].calculate_non_fatal_cost()
            #       fatal_safety_cost= safety_rate * line_segment_array[i].calculate_fatal_cost()
            #       total_safety_cost= safety_rate * line_segment_array[i].calculate_total_safety()
                    
                
            #line_segment_array[i].calculate_environmental_restoration()
            #line_segment_capex_array[t]+=line_segment_array[i].capex[t]
            #line_segment_opex_array[t]+=line_segment_array[i].opex[t]
            #line_segment_environmental_restoration_cost_array[t]+=line_segment_array[i].environmental_restoration[t]     
            df_new=pd.DataFrame({'segment number': [i],
                                 'year':[t],
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
    return(df.set_index(["year","segment number"]))

# run sensitivity analysis for a parameter
#def sensitivity_analysis_statusQuo_strategy(parameter_name,parameter_value,years_of_analysis):
#    output1=run_cost_simulation_statusQuo_strategy(years_of_analysis)
#    parameter_name=parameter_value
#    output2=run_cost_simulation_statusQuo_strategy(years_of_analysis)
    
    
