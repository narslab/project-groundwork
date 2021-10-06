# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:00:33 2021

@author: Mahsa
"""

import analyze_sensitivity
import pandas as pd

#sensitivity results for statusQuo strategy
output1=analyze_sensitivity.run_sensitivity_statusQuo('r',10)
output2=analyze_sensitivity.run_sensitivity_statusQuo('r',-10)
output3=analyze_sensitivity.run_sensitivity_statusQuo('overhead_line',10,'corridor_length')
output4=analyze_sensitivity.run_sensitivity_statusQuo('overhead_line',-10,'corridor_length')
output5=analyze_sensitivity.run_sensitivity_statusQuo('underground_line',10,'corridor_length')
output6=analyze_sensitivity.run_sensitivity_statusQuo('underground_line',-10,'corridor_length')
output7=analyze_sensitivity.run_sensitivity_statusQuo('overhead_line',10,'replcost')
output8=analyze_sensitivity.run_sensitivity_statusQuo('overhead_line',-10,'replcost')
output9=analyze_sensitivity.run_sensitivity_statusQuo('underground_line',10,'replcost')
output10=analyze_sensitivity.run_sensitivity_statusQuo('underground_line',-10,'replcost')
output11=analyze_sensitivity.run_sensitivity_statusQuo('overhead_proportion',10)
output12=analyze_sensitivity.run_sensitivity_statusQuo('overhead_proportion',-10)
output13=analyze_sensitivity.run_sensitivity_statusQuo('overhead_line',10,'lifespan')
output14=analyze_sensitivity.run_sensitivity_statusQuo('overhead_line',-10,'lifespan')
output15=analyze_sensitivity.run_sensitivity_statusQuo('underground_line',10,'lifespan')
output16=analyze_sensitivity.run_sensitivity_statusQuo('underground_line',-10,'lifespan')
output17=analyze_sensitivity.run_sensitivity_statusQuo('overhead_line',10,'om_percentage_replcost')
output18=analyze_sensitivity.run_sensitivity_statusQuo('overhead_line',-10,'om_percentage_replcost')
output19=analyze_sensitivity.run_sensitivity_statusQuo('underground_line',10,'om_percentage_replcost')
output20=analyze_sensitivity.run_sensitivity_statusQuo('underground_line',-10,'om_percentage_replcost')
output21=analyze_sensitivity.run_sensitivity_statusQuo('length_shape',+10)
output22=analyze_sensitivity.run_sensitivity_statusQuo('length_shape',-10)
output23=analyze_sensitivity.run_sensitivity_statusQuo('length_scale',+10)
output24=analyze_sensitivity.run_sensitivity_statusQuo('length_scale',-10)
output25=analyze_sensitivity.run_sensitivity_statusQuo('age_shape',+10)
output26=analyze_sensitivity.run_sensitivity_statusQuo('age_shape',-10)
output27=analyze_sensitivity.run_sensitivity_statusQuo('age_scale',+10)
output28=analyze_sensitivity.run_sensitivity_statusQuo('age_scale',-10)


dataframe_sensitivity_statusQuo=pd.DataFrame({'Parameter':['r','over_corridor_length','under_corridor_length','over_replcost','under_replcost','overhead_proportion','over_lifespan','under_lifespan','over_om_percentage_replcost','under_om_percentage_replcost','length_shape','length_scale','age_shape','age_scale'],
                                 '%change in cost resulted from +%10 change in parameter': [output1,output3,output5,output7,output9,output11,output13,output15,output17,output19,output21,output23,output25,output27],
                                 '%change in cost resulted from -%10 change in parameter': [output2,output4,output6,output8,output10,output12,output14,output16,output18,output20,output22,output24,output26,output28]})

dataframe_sensitivity_statusQuo.to_csv(r'../../results/outcomes/sensitivity-result-statusquo.csv', index = False)

