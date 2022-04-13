# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 09:14:58 2021

@author: Mahsa
"""

import network
import analyze_result


### run sensitivity analysis for a parameter

def run_cost_sensitivity_SQ_electric(parameter1, percentage_change1,
                                                parameter2=None, percentage_change2=None):
    if  parameter2==None:
        model_data=network.Electric_model_inputs()
        new_data1=network.Electric_model_inputs()
        new_data1.modify_parameter(parameter1, percentage_change1)
        original_result=analyze_result.calculate_net_present_value_SQ_electric(model_data)
        new_result=analyze_result.calculate_net_present_value_SQ_electric(new_data1)
    else:
        #data=Network.Electric_model_inputs()
        model_data=network.Electric_model_inputs()
        new_data1=network.Electric_model_inputs()
        new_data1=new_data1.modify_parameter(parameter1, percentage_change1)
        new_data1=new_data1.modify_parameter(parameter2, percentage_change2)
        original_result=analyze_result.calculate_net_present_value_SQ_electric(model_data)
        new_result=analyze_result.calculate_net_present_value_SQ_electric(new_data1)
    Percentage_change_result=(new_result[-1]-original_result[-1])/original_result[-1]*100
    print(Percentage_change_result)
    return (Percentage_change_result)

def run_cost_sensitivity_UL_electric(parameter1, percentage_change1,
                                                parameter2=None, percentage_change2=None):
    if  parameter2==None:
        model_data=network.Electric_model_inputs()
        data=model_data
        new_data1=network.Electric_model_inputs()
        new_data1.modify_parameter(parameter1, percentage_change1)
        original_result=analyze_result.calculate_net_present_value_UL_electric(data)
        new_result=analyze_result.calculate_net_present_value_UL_electric(new_data1)
    else:
        #data=Network.Electric_model_inputs()
        model_data=network.Electric_model_inputs()
        data=model_data
        new_data1=network.Electric_model_inputs()
        new_data1=new_data1.modify_parameter(parameter1, percentage_change1)
        new_data1=new_data1.modify_parameter(parameter2, percentage_change2)
        original_result=analyze_result.calculate_net_present_value_UL_electric(data)
        new_result=analyze_result.calculate_net_present_value_UL_electric(new_data1)
    Percentage_change_result=(new_result[-1]-original_result[-1])/original_result[-1]*100
    return (Percentage_change_result)
    



