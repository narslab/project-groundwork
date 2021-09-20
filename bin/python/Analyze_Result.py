# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 09:42:52 2021

@author: Mahsa
"""

import Simulate

###Calculate aggregrated cost resutl of status-quo strategy based on each year for 40 years 
df_output_statusQuo=Simulate.run_cost_simulation_statusQuo_strategy(40)
df_analyze_result_statusQuo=df_output_statusQuo.groupby(level=[0])[['capex','opex','total infra','environmental restoration','non fatal','fatal','total safety','total cost']].sum()
df_analyze_result_statusQuo.insert(0, "year", range(40), True)
df_analyze_result_statusQuo.to_csv(r'c:\\Users\\Mahsa\\NARS\\project-groundwork\\results\\outcomes\\Analyze result-StatusQuo strategy.csv', index = False)


###Calculate aggregrated cost resutl of undergrounding after lifespan strategy based on each year for 40 years 
df_output_under=Simulate.run_cost_simulation_under_after_lifespan_strategy(40)
df_analyze_result_under=df_output_under.groupby(level=[0])[['capex','opex','total infra','environmental restoration','non fatal','fatal','total safety','total cost']].sum()
df_analyze_result_under.insert(0, "year", range(40), True)
df_analyze_result_under.to_csv(r'c:\\Users\\Mahsa\\NARS\\project-groundwork\\results\\outcomes\\Analyze result-Undergrounding strategy.csv', index = False)


###Calculate additional cost due to undergrounding after lifespan strategy
df_analyze_additional=df_analyze_result_under.subtract(df_analyze_result_statusQuo)
#df_analyze_additional.drop("year")
del df_analyze_additional['year']
df_analyze_additional.insert(0, "year", range(40), True)
df_analyze_additional.to_csv(r'c:\\Users\\Mahsa\\NARS\\project-groundwork\\results\\outcomes\\Analyze result-Additional cost.csv', index = False)
