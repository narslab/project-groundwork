# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 09:42:52 2021

@author: Mahsa
"""
import Network
import Simulate

###Calculate aggregrated cost result of status-quo strategy based on each year for 40 years 
def aggregate_through_years_statusQuo(data=Network.data):
    df_output_statusQuo=Simulate.run_cost_simulation_statusQuo_strategy(data=Network.data)
    df_analyze_result_statusQuo=df_output_statusQuo.groupby(level=[0])[['capex','opex','total infra','environmental restoration','non fatal','fatal','total safety','total cost']].sum()
    df_analyze_result_statusQuo.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    df_analyze_result_statusQuo.to_csv(r'c:\\Users\\Mahsa\\NARS\\project-groundwork\\results\\outcomes\\Analyze result-StatusQuo strategy.csv', index = False)
    return(df_analyze_result_statusQuo)

###Calculate aggregrated cost result of undergrounding after lifespan strategy based on each year for 40 years 
def aggregate_through_years_under_after_lifespan(data=Network.data):
    df_output_under=Simulate.run_cost_simulation_under_after_lifespan_strategy(data=Network.data)
    df_analyze_result_under=df_output_under.groupby(level=[0])[['capex','opex','total infra','environmental restoration','non fatal','fatal','total safety','total cost']].sum()
    df_analyze_result_under.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    df_analyze_result_under.to_csv(r'c:\\Users\\Mahsa\\NARS\\project-groundwork\\results\\outcomes\\Analyze result-Undergrounding strategy.csv', index = False)
    return(df_analyze_result_under)

###Calculate additional cost due to undergrounding after lifespan strategy
def calculate_additional_cost_from_under_after_lifespan(data=Network.data):
    df1=aggregate_through_years_under_after_lifespan(data=Network.data)
    df2=aggregate_through_years_statusQuo(data=Network.data)
    df_analyze_additional=df1.subtract(df2)
    del df_analyze_additional['year']
    df_analyze_additional.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    df_analyze_additional.to_csv(r'c:\\Users\\Mahsa\\NARS\\project-groundwork\\results\\outcomes\\Analyze result-Additional cost.csv', index = False)
    return(df_analyze_additional)

###Calculate net present value of infrastructure, environmental, safety and total cost for statusQuo strategy
def calculate_net_present_value_statusQuo(data=Network.data):
    df_net_present_statusQuo=aggregate_through_years_statusQuo(data=Network.data)
    net_present_value_lifecycle_infrastructure_cost=[]
    net_present_value_environmental_cost=[]
    net_present_value_safety_cost=[]
    net_present_value_total_under_after_lifespan_strategy_cost=[]
    for index, row in df_net_present_statusQuo.iterrows():
        net_present_value_lifecycle_infrastructure_cost.append(row['total infra']/(1+data.parameter_dict['r'])**index)
        net_present_value_environmental_cost.append(row['environmental restoration']/(1+data.parameter_dict['r'])**index)
        net_present_value_safety_cost.append(row['total safety']/(1+data.parameter_dict['r'])**index)
        net_present_value_total_under_after_lifespan_strategy_cost.append(row['total cost']/(1+data.parameter_dict['r'])**index)
    total_infrastructre=sum(net_present_value_lifecycle_infrastructure_cost)
    total_environmental=sum(net_present_value_environmental_cost)
    total_safety=sum(net_present_value_safety_cost)
    total_total=sum(net_present_value_total_under_after_lifespan_strategy_cost)
    return([total_infrastructre,total_environmental,total_safety,total_total])

###Calculate net present value of infrastructure, environmental, safety and total cost for undergrounding after lifespan strategy
def calculate_net_present_value_under_after_lifespan(data=Network.data):
    df_net_present_statusQuo=aggregate_through_years_under_after_lifespan(data=Network.data)
    net_present_value_lifecycle_infrastructure_cost=[]
    net_present_value_environmental_cost=[]
    net_present_value_safety_cost=[]
    net_present_value_total_under_after_lifespan_strategy_cost=[]
    for index, row in df_net_present_statusQuo.iterrows():
        net_present_value_lifecycle_infrastructure_cost.append(row['total infra']/(1+data.parameter_dict['r'])**index)
        net_present_value_environmental_cost.append(row['environmental restoration']/(1+data.parameter_dict['r'])**index)
        net_present_value_safety_cost.append(row['total safety']/(1+Network.data.r)**index)
        net_present_value_total_under_after_lifespan_strategy_cost.append(row['total cost']/(1+data.parameter_dict['r'])**index)
    total_infrastructre=sum(net_present_value_lifecycle_infrastructure_cost)
    total_environmental=sum(net_present_value_environmental_cost)
    total_safety=sum(net_present_value_safety_cost)
    total_total=sum(net_present_value_total_under_after_lifespan_strategy_cost)
    return([total_infrastructre,total_environmental,total_safety,total_total])

###Calculate net present value for additional cost associate with undergrounding after lifespan strategy
def calculate_net_present_value_of_additional_cost(years_of_analysis):
      list1=calculate_net_present_value_under_after_lifespan(years_of_analysis)
      list2=calculate_net_present_value_statusQuo(years_of_analysis)
      difference = []
      zip_object = zip(list1, list2)
      for list1_i, list2_i in zip_object:
          difference.append(list1_i-list2_i)
      return(difference)