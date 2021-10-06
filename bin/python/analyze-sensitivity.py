# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 09:14:58 2021

@author: Mahsa
"""

import network
import analyze_result


### run sensitivity analysis for a parameter

def run_sensitivity_statusQuo(parameter1, percentage_change1,
                                                parameter2=None, percentage_change2=None):
    if  parameter2==None:
        model_data=network.model_inputs()
        new_data1=network.model_inputs()
        new_data1.modify_parameter(parameter1, percentage_change1)
        original_result=analyze_result.calculate_net_present_value_statusQuo(model_data)
        new_result=analyze_result.calculate_net_present_value_statusQuo(new_data1)
    else:
        #data=Network.model_inputs()
        model_data=network.model_inputs()
        new_data1=network.model_inputs()
        new_data1=new_data1.modify_parameter(parameter1, percentage_change1)
        new_data1=new_data1.modify_parameter(parameter2, percentage_change2)
        original_result=analyze_result.calculate_net_present_value_statusQuo(model_data)
        new_result=analyze_result.calculate_net_present_value_statusQuo(new_data1)
    Percentage_change_result=(new_result[-1]-original_result[-1])/original_result[-1]*100
    print(Percentage_change_result)
    return (Percentage_change_result)

def run_sensitivity_under(parameter1, percentage_change1,
                                                parameter2=None, percentage_change2=None):
    if  parameter2==None:
        model_data=network.model_inputs()
        data=model_data
        new_data1=network.model_inputs()
        new_data1.modify_parameter(parameter1, percentage_change1)
        original_result=analyze_result.calculate_net_present_value_under_after_lifespan(data)
        new_result=analyze_result.calculate_net_present_value_under_after_lifespan(new_data1)
    else:
        #data=Network.model_inputs()
        model_data=network.model_inputs()
        data=model_data
        new_data1=network.model_inputs()
        new_data1=new_data1.modify_parameter(parameter1, percentage_change1)
        new_data1=new_data1.modify_parameter(parameter2, percentage_change2)
        original_result=analyze_result.calculate_net_present_value_under_after_lifespan(data)
        new_result=analyze_result.calculate_net_present_value_under_after_lifespan(new_data1)
    Percentage_change_result=(new_result[-1]-original_result[-1])/original_result[-1]*100
    return (Percentage_change_result)
    



