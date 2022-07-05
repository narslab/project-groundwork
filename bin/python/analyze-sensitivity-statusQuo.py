# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:00:33 2021

@author: Mahsa
"""

import analyze_sensitivity
import pandas as pd

#cost sensitivity results for SQ
# =============================================================================
# output1=analyze_sensitivity.run_sensitivity_cost_SQ('r',10)
# output2=analyze_sensitivity.run_sensitivity_cost_SQ('r',-10)
# output3=analyze_sensitivity.run_sensitivity_cost_SQ('overhead_line',10,'corridor_width')
# output4=analyze_sensitivity.run_sensitivity_cost_SQ('overhead_line',-10,'corridor_width')
# output5=analyze_sensitivity.run_sensitivity_cost_SQ('underground_line',10,'corridor_width')
# output6=analyze_sensitivity.run_sensitivity_cost_SQ('underground_line',-10,'corridor_width')
# output7=analyze_sensitivity.run_sensitivity_cost_SQ('overhead_line',10,'replcost')
# output8=analyze_sensitivity.run_sensitivity_cost_SQ('overhead_line',-10,'replcost')
# output9=analyze_sensitivity.run_sensitivity_cost_SQ('underground_line',10,'replcost')
# output10=analyze_sensitivity.run_sensitivity_cost_SQ('underground_line',-10,'replcost')
# 
# 
# dataframe_sensitivity_statusQuo=pd.DataFrame({'Parameter':['r','over_corridor_width','under_corridor_width','over_replcost_el','under_replcost_el'],
#                                  '%change in cost resulted from +%10 change in parameter': [output1,output3,output5,output7,output9],
#                                  '%change in cost resulted from -%10 change in parameter': [output2,output4,output6,output8,output10]})
# 
# dataframe_sensitivity_statusQuo.to_csv(r'../../results/outcomes/sensitivity-cost-result-SQ-part1.csv', index = False)
# 
# output11=analyze_sensitivity.run_sensitivity_cost_SQ('overhead_proportion',10)
# output12=analyze_sensitivity.run_sensitivity_cost_SQ('overhead_proportion',-10)
# output13=analyze_sensitivity.run_sensitivity_cost_SQ('overhead_line',10,'lifespan')
# output14=analyze_sensitivity.run_sensitivity_cost_SQ('overhead_line',-10,'lifespan')
# output15=analyze_sensitivity.run_sensitivity_cost_SQ('underground_line',10,'lifespan')
# output16=analyze_sensitivity.run_sensitivity_cost_SQ('underground_line',-10,'lifespan')
# output17=analyze_sensitivity.run_sensitivity_cost_SQ('overhead_line',10,'om_proportion_replcost')
# output18=analyze_sensitivity.run_sensitivity_cost_SQ('overhead_line',-10,'om_proportion_replcost')
# output19=analyze_sensitivity.run_sensitivity_cost_SQ('underground_line',10,'om_proportion_replcost')
# output20=analyze_sensitivity.run_sensitivity_cost_SQ('underground_line',-10,'om_proportion_replcost')
# 
# 
# dataframe_sensitivity_statusQuo=pd.DataFrame({'Parameter':['overhead_proportion','over_lifespan','under_lifespan','over_om_percentage_replcost_el','under_om_percentage_replcost_el'],
#                                  '%change in cost resulted from +%10 change in parameter': [output11,output13,output15,output17,output19],
#                                  '%change in cost resulted from -%10 change in parameter': [output12,output14,output16,output18,output20]})
# 
# dataframe_sensitivity_statusQuo.to_csv(r'../../results/outcomes/sensitivity-cost-result-SQ-part2.csv', index = False)
# =============================================================================

output21=analyze_sensitivity.run_sensitivity_cost_SQ('length_s',+10)
output22=analyze_sensitivity.run_sensitivity_cost_SQ('length_s',-10)
output23=analyze_sensitivity.run_sensitivity_cost_SQ('length_scale',+10)
output24=analyze_sensitivity.run_sensitivity_cost_SQ('length_scale',-10)
output25=analyze_sensitivity.run_sensitivity_cost_SQ('age_shape',+10)
output26=analyze_sensitivity.run_sensitivity_cost_SQ('age_shape',-10)
output27=analyze_sensitivity.run_sensitivity_cost_SQ('age_scale',+10)
output28=analyze_sensitivity.run_sensitivity_cost_SQ('age_scale',-10)
output29=analyze_sensitivity.run_sensitivity_cost_SQ('average_length',+10)
output30=analyze_sensitivity.run_sensitivity_cost_SQ('average_length',-10)

dataframe_sensitivity_statusQuo=pd.DataFrame({'Parameter':['length_shape','length_scale','age_shape','age_scale','average_length'],
                                 '%change in cost resulted from +%10 change in parameter': [output21,output23,output25,output27,output29],
                                 '%change in cost resulted from -%10 change in parameter': [output22,output24,output26,output28, output30]})

dataframe_sensitivity_statusQuo.to_csv(r'../../results/outcomes/sensitivity-cost-result-SQ-part3.csv', index = False)

#output31=analyze_sensitivity.run_sensitivity_cost_SQ('segment_number',+10)
#output32=analyze_sensitivity.run_sensitivity_cost_SQ('segment_number',-10)
output33=analyze_sensitivity.run_sensitivity_cost_SQ('overhead_line',10,'replcost', broadband=True)
output34=analyze_sensitivity.run_sensitivity_cost_SQ('overhead_line',-10,'replcost', broadband=True)
output35=analyze_sensitivity.run_sensitivity_cost_SQ('underground_line',10,'replcost', broadband=True)
output36=analyze_sensitivity.run_sensitivity_cost_SQ('underground_line',-10,'replcost', broadband=True)
output37=analyze_sensitivity.run_sensitivity_cost_SQ('overhead_line',10,'om_proportion_replcost', broadband=True)
output38=analyze_sensitivity.run_sensitivity_cost_SQ('overhead_line',-10,'om_proportion_replcost', broadband=True)
output39=analyze_sensitivity.run_sensitivity_cost_SQ('underground_line',10,'om_proportion_replcost', broadband=True)
output40=analyze_sensitivity.run_sensitivity_cost_SQ('underground_line',-10,'om_proportion_replcost', broadband=True)
output41=analyze_sensitivity.run_sensitivity_cost_SQ('underground_line',10,'over_under_joint_proportion_convertcost', broadband=True)
output42=analyze_sensitivity.run_sensitivity_cost_SQ('underground_line',-10,'over_under_joint_proportion_convertcost', broadband=True)
output43=analyze_sensitivity.run_sensitivity_cost_SQ('joint_trench_additional',10)
output44=analyze_sensitivity.run_sensitivity_cost_SQ('joint_trench_additional',-10)



dataframe_sensitivity_statusQuo=pd.DataFrame({'Parameter':['over_replcost_br','under_replcost_br','over_om_percentage_replcost_br','under_om_percentage_replcost_br','over_under_joint_proportion_convertcost','joint_trench_additional'],
                                 '%change in cost resulted from +%10 change in parameter': [output33, output35, output37, output39, output41, output43],
                                 '%change in cost resulted from -%10 change in parameter': [output34, output36, output38, output40, output42, output44]})

dataframe_sensitivity_statusQuo.to_csv(r'../../results/outcomes/sensitivity-cost-result-SQ-part4.csv', index = False)

