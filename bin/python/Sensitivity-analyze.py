# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 09:14:58 2021

@author: Mahsa
"""

import Network
import Analyze_Result


### run sensitivity analysis for a parameter

def run_sensitivity_statusQuo(parameter1, percentage_change1,
                                                parameter2=None, percentage_change2=None,data=Network.data):
    if  parameter2==None:
        model_data=Network.model_inputs()
        data=model_data
        new_data1=Network.model_inputs()
        new_data1.modify_parameter(parameter1, percentage_change1)
        original_result=Analyze_Result.calculate_net_present_value_statusQuo(data)
        new_result=Analyze_Result.calculate_net_present_value_statusQuo(new_data1)
    else:
        #data=Network.model_inputs()
        model_data=Network.model_inputs()
        data=model_data
        new_data1=Network.model_inputs()
        new_data1=new_data1.modify_parameter(parameter1, percentage_change1)
        new_data1=new_data1.modify_parameter(parameter2, percentage_change2)
        original_result=Analyze_Result.calculate_net_present_value_statusQuo(data)
        new_result=Analyze_Result.calculate_net_present_value_statusQuo(new_data1)
    Percentage_change_result=(new_result-original_result[-1])/original_result[-1]*100
    return (Percentage_change_result)

def run_sensitivity_under(parameter1, percentage_change1,
                                                parameter2=None, percentage_change2=None,data=Network.data):
    if  parameter2==None:
        model_data=Network.model_inputs()
        data=model_data
        new_data1=Network.model_inputs()
        new_data1.modify_parameter(parameter1, percentage_change1)
        original_result=Analyze_Result.calculate_net_present_value_under_after_lifespan(data)
        new_result=Analyze_Result.calculate_net_present_value_under_after_lifespan(new_data1)
    else:
        #data=Network.model_inputs()
        model_data=Network.model_inputs()
        data=model_data
        new_data1=Network.model_inputs()
        new_data1=new_data1.modify_parameter(parameter1, percentage_change1)
        new_data1=new_data1.modify_parameter(parameter2, percentage_change2)
        original_result=Analyze_Result.calculate_net_present_value_under_after_lifespan(data)
        new_result=Analyze_Result.calculate_net_present_value_under_after_lifespan(new_data1)
    Percentage_change_result=(new_result-original_result[-1])/original_result[-1]*100
    return (Percentage_change_result)
    
    #data=Network.model_inputs()
    #data_plus = data.modify_parameter(parameter1, percentage_change1)
    #data_minus= data.modify_parameter(parameter, -percentage_change)
    
    #return Simulate.run_cost_simulation_statusQuo_strategy(data)
    


