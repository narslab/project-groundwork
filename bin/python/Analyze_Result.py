# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 09:42:52 2021

@author: Mahsa
"""

import Simulate


df_output_statusQuo=Simulate.run_cost_simulation_statusQuo_strategy(40)
df_analyze_result_statusQuo=df_output_statusQuo.groupby(level=[0])[['capex','opex','total infra','environmental restoration','non fatal','fatal','total safety','total cost']].sum()
print (df_analyze_result_statusQuo)

df_output_under=Simulate.run_cost_simulation_under_after_lifespan_strategy(40)
df_analyze_result_under=df_output_under.groupby(level=[0])[['capex','opex','total infra','environmental restoration','non fatal','fatal','total safety','total cost']].sum()
print (df_analyze_result_under)