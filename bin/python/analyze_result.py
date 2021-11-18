# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 09:42:52 2021

@author: Mahsa
"""
import pandas as pd
import network
import simulate

data  = network.model_inputs()

###Calculate aggregrated cost result of status-quo strategy based on each year for 40 years 
def aggregate_cost_through_years_statusQuo(data):
    df_output_statusQuo=simulate.run_cost_simulation_statusQuo_strategy(data)
    df_analyze_result_statusQuo=df_output_statusQuo.groupby(level=[0])[['capex','opex','lifecycle infrastructure','environmental restoration','non fatal','fatal','safety','total cost']].sum()
    df_analyze_result_statusQuo.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    df_analyze_result_statusQuo.to_csv(r'../../results/outcomes/cost-analyze-result-statusQuo-strategy.csv', index = False)
    return(df_analyze_result_statusQuo)

###Calculate aggregrated cost result of undergrounding after lifespan strategy based on each year for 40 years 
def aggregate_cost_through_years_under_after_lifespan(data):
    df_output_under=simulate.run_cost_simulation_under_after_lifespan_strategy(data)
    df_analyze_result_under=df_output_under.groupby(level=[0])[['capex','opex','lifecycle infrastructure','environmental restoration','non fatal','fatal','safety','total cost']].sum()
    df_analyze_result_under.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    df_analyze_result_under.to_csv(r'../../results/outcomes/cost-analyze-result-undergrounding-strategy.csv', index = False)
    return(df_analyze_result_under)

###Calculate additional cost due to undergrounding after lifespan strategy
def calculate_additional_cost_from_under_after_lifespan(data):
    df1=aggregate_cost_through_years_under_after_lifespan(data)
    df2=aggregate_cost_through_years_statusQuo(data)
    df_analyze_additional=df1.subtract(df2)
    del df_analyze_additional['year']
    df_analyze_additional.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    df_analyze_additional.to_csv(r'../../results/outcomes/cost-analyze-result-additional-cost.csv', index = False)
    return(df_analyze_additional)

###Calculate net present value of infrastructure, environmental, safety and total cost for statusQuo strategy
def calculate_cost_net_present_value_statusQuo(data):
    df_net_present_statusQuo=aggregate_cost_through_years_statusQuo(data)
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
def calculate_cost_net_present_value_under_after_lifespan(data):
    df_net_present_statusQuo=aggregate_cost_through_years_under_after_lifespan(data)
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
def calculate_net_present_value_of_additional_cost(data):
      list1=calculate_cost_net_present_value_under_after_lifespan(data)
      list2=calculate_cost_net_present_value_statusQuo(data)
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

###Calculate aggregrated benefit result of statusQuo strategy based on each year for 40 years 
def aggregate_benefit_through_years_statusQuo(data):
    df_output_statusQuo=simulate.run_benefit_simulation_statusQuo_strategy(data)
    df_analyze_result_statusQuo=df_output_statusQuo.groupby(level=[0])[['aesthetic losses','economic losses','total losses']].sum()
    df_analyze_result_statusQuo.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    df_analyze_result_statusQuo.to_csv(r'../../results/outcomes/benefit-analyze-result-statusQuo-strategy.csv', index = False)
    return(df_analyze_result_statusQuo)    

###Calculate aggregrated benefit result of undergrounding after lifespan strategy based on each year for 40 years 
def aggregate_benefit_through_years_under_after_lifespan(data):
    df_benefit_under=simulate.run_benefit_simulation_under_after_lifespan_strategy(data)
    df_analyze_benefit_under=df_benefit_under.groupby(level=[0])[['aesthetic losses','economic losses','total losses']].sum()
    df_analyze_benefit_under.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    df_analyze_benefit_under.to_csv(r'../../results/outcomes/benefit-analyze-undergrounding-strategy.csv', index = False)
    return(df_analyze_benefit_under)

###Calculate additional benefits due to undergrounding after lifespan strategy
def calculate_additional_benefit_from_under_after_lifespan(data):
    df1=aggregate_benefit_through_years_under_after_lifespan(data)
    df2=aggregate_benefit_through_years_statusQuo(data)
    df_analyze_additional=df2.subtract(df1)
    del df_analyze_additional['year']
    df_analyze_additional.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    df_analyze_additional.to_csv(r'../../results/outcomes/benefit-analyze-result-additional-cost.csv', index = False)
    return(df_analyze_additional)

###Calculate net present value of losses for statusQuo strategy
def calculate_benefit_net_present_value_statusQuo(data):
    df_net_present_statusQuo=aggregate_benefit_through_years_statusQuo(data)
    net_present_value_economic_benefit=[]
    net_present_value_aesthetic_benefit=[]
    net_present_value_total_benefit=[]
    for index, row in df_net_present_statusQuo.iterrows():
        net_present_value_aesthetic_benefit.append(row['aesthetic losses']/(1+data.parameter_dict['r'])**index)
        net_present_value_economic_benefit.append(row['economic losses']/(1+data.parameter_dict['r'])**index)
        net_present_value_total_benefit.append(row['total losses']/(1+data.parameter_dict['r'])**index)
    total_economic=sum(net_present_value_economic_benefit)
    total_aesthetic=sum(net_present_value_aesthetic_benefit)
    total_total=sum(net_present_value_total_benefit)
    df_net_present_value_statusQuo= pd.DataFrame({'aesthetic losses':[total_aesthetic],
                                                  'economic losses':[total_economic],
                                                  'total losses':[total_total]
                                                  })
    df_net_present_value_statusQuo.to_csv(r'../../results/outcomes/benefit-net-present-value-statusQuo.csv', index = False)
    return([total_aesthetic,total_economic,total_total])

###Calculate net present value of infrastructure, environmental, safety and total cost for undergrounding after lifespan strategy
def calculate_benefit_net_present_value_under_after_lifespan(data):
    df_net_present_statusQuo=aggregate_benefit_through_years_under_after_lifespan(data)
    net_present_value_economic=[]
    net_present_value_aesthetic=[]
    net_present_value_total=[]
    for index, row in df_net_present_statusQuo.iterrows():
        net_present_value_aesthetic.append(row['aesthetic losses']/(1+data.parameter_dict['r'])**index)
        net_present_value_economic.append(row['economic losses']/(1+data.parameter_dict['r'])**index)
        net_present_value_total.append(row['total losses']/(1+data.parameter_dict['r'])**index)
    total_aesthetic=sum(net_present_value_aesthetic)
    total_economic=sum(net_present_value_economic)
    total_total=sum(net_present_value_total)
    df_net_present_value_under= pd.DataFrame({'aesthetic losses':[total_aesthetic],
                                                  'economic losses':[total_economic],
                                                  'total losses':[total_total]})
    df_net_present_value_under.to_csv(r'../../results/outcomes/benefit-net-present-value-under.csv', index = False)
    return([total_aesthetic,total_economic,total_total])

###Calculate net present value for additional cost associate with undergrounding after lifespan strategy
def calculate_net_present_value_of_additional_benefit(data):
      list1=calculate_benefit_net_present_value_under_after_lifespan(data)
      list2=calculate_benefit_net_present_value_statusQuo(data)
      difference = []
      zip_object = zip(list1, list2)
      for list1_i, list2_i in zip_object:
          difference.append(list2_i-list1_i)
      df_net_present_value_additional= pd.DataFrame({'avoided aesthetic losses':[difference[0]],
                                                  'avoided economic losses':[difference[1]],
                                                  'avoided total losses':[difference[2]]})
      df_net_present_value_additional.to_csv(r'../../results/outcomes/benefit-net-present-value-additional.csv', index = False)
      return(difference)
