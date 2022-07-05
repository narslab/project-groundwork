# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 07:58:22 2021

@author: Mahsa
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:00:33 2021

@author: Mahsa
"""
import analyze_sensitivity
import pandas as pd

# =============================================================================
# #cost sensitivity results for SQ
# output1=analyze_sensitivity.run_sensitivity_benefit_SQ('r',10)
# output2=analyze_sensitivity.run_sensitivity_benefit_SQ('r',-10)
# output3=analyze_sensitivity.run_sensitivity_benefit_SQ('overhead_line',10,'corridor_width')
# output4=analyze_sensitivity.run_sensitivity_benefit_SQ('overhead_line',-10,'corridor_width')
# output5=analyze_sensitivity.run_sensitivity_benefit_SQ('underground_line',10,'corridor_width')
# output6=analyze_sensitivity.run_sensitivity_benefit_SQ('underground_line',-10,'corridor_width')
# output7=analyze_sensitivity.run_sensitivity_benefit_SQ('overhead_proportion',10)
# output8=analyze_sensitivity.run_sensitivity_benefit_SQ('overhead_proportion',-10)
# output9=analyze_sensitivity.run_sensitivity_benefit_SQ('overhead_line',10,'lifespan')
# output10=analyze_sensitivity.run_sensitivity_benefit_SQ('overhead_line',-10,'lifespan')
# 
# dataframe_sensitivity_statusQuo=pd.DataFrame({'Parameter':['r','over_corridor_width','under_corridor_width','overhead_proportion','over_lifespan'],
#                                  '%change in benefit resulted from +%10 change in parameter': [output1,output3,output5,output7,output9],
#                                  '%change in benefit resulted from -%10 change in parameter': [output2,output4,output6,output8,output10]})
# 
# dataframe_sensitivity_statusQuo.to_csv(r'../../results/outcomes/sensitivity-result-benefit-SQ-part1.csv', index = False)
# 
# output11=analyze_sensitivity.run_sensitivity_benefit_SQ('underground_line',10,'lifespan')
# output12=analyze_sensitivity.run_sensitivity_benefit_SQ('underground_line',-10,'lifespan')
# output13=analyze_sensitivity.run_sensitivity_benefit_SQ('length_s',+10)
# output14=analyze_sensitivity.run_sensitivity_benefit_SQ('length_s',-10)
# output15=analyze_sensitivity.run_sensitivity_benefit_SQ('length_scale',+10)
# output16=analyze_sensitivity.run_sensitivity_benefit_SQ('length_scale',-10)
# output17=analyze_sensitivity.run_sensitivity_benefit_SQ('age_shape',+10)
# output18=analyze_sensitivity.run_sensitivity_benefit_SQ('age_shape',-10)
# output19=analyze_sensitivity.run_sensitivity_benefit_SQ('age_scale',+10)
# output20=analyze_sensitivity.run_sensitivity_benefit_SQ('age_scale',-10)
# 
# dataframe_sensitivity_statusQuo=pd.DataFrame({'Parameter':['under_lifespan','length_shape','length_scale','age_shape','age_scale'],
#                                  '%change in benefit resulted from +%10 change in parameter': [output11,output13,output15,output17,output19],
#                                  '%change in benefit resulted from -%10 change in parameter': [output12,output14,output16,output18,output20]})
# =============================================================================

# =============================================================================
# # dataframe_sensitivity_statusQuo.to_csv(r'../../results/outcomes/sensitivity-result-benefit-SQ-part2.csv', index = False)
# 
# #output21=analyze_sensitivity.run_sensitivity_benefit_SQ('average_length',+10)
# #output22=analyze_sensitivity.run_sensitivity_benefit_SQ('average_length',-10)
# output23=analyze_sensitivity.run_sensitivity_benefit_SQ('service_area',+10)
# output24=analyze_sensitivity.run_sensitivity_benefit_SQ('service_area',-10)
# output25=analyze_sensitivity.run_sensitivity_benefit_SQ('SAIDI',+10)
# output26=analyze_sensitivity.run_sensitivity_benefit_SQ('SAIDI',-10)
# output27=analyze_sensitivity.run_sensitivity_benefit_SQ('USD_per_Customer_Hour_Interruption_Residential',+10)
# output28=analyze_sensitivity.run_sensitivity_benefit_SQ('USD_per_Customer_Hour_Interruption_Residential',-10)
# output29=analyze_sensitivity.run_sensitivity_benefit_SQ('USD_per_Customer_Hour_Interruption_Commercial',+10)
# output30=analyze_sensitivity.run_sensitivity_benefit_SQ('USD_per_Customer_Hour_Interruption_Commercial',-10)
# 
# dataframe_sensitivity_statusQuo=pd.DataFrame({'Parameter':['service_area','SAIDI','USD_per_Customer_Hour_Interruption_Residential','USD_per_Customer_Hour_Interruption_Commercial'],
#                                  '%change in benefit resulted from +%10 change in parameter': [output23,output25,output27,output29],
#                                  '%change in benefit resulted from -%10 change in parameter': [output24,output26,output28, output30]})
# 
# dataframe_sensitivity_statusQuo.to_csv(r'../../results/outcomes/sensitivity-result-benefit-SQ-part3.csv', index = False)
# =============================================================================

# =============================================================================
# output31=analyze_sensitivity.run_sensitivity_benefit_SQ('USD_per_Customer_Hour_Interruption_Industry',+10)
# output32=analyze_sensitivity.run_sensitivity_benefit_SQ('USD_per_Customer_Hour_Interruption_Industry',-10)
# output33=analyze_sensitivity.run_sensitivity_benefit_SQ('Shrewsbury_tax_levy_2021',+10)
# output34=analyze_sensitivity.run_sensitivity_benefit_SQ('Shrewsbury_tax_levy_2021',-10)
# 
# 
# dataframe_sensitivity_statusQuo=pd.DataFrame({'Parameter':['USD_per_Customer_Hour_Interruption_Industrial','Shrewsbury_tax_levy_2021'],
#                                  '%change in benefit resulted from +%10 change in parameter': [output31, output33],
#                                  '%change in benefit resulted from -%10 change in parameter': [output32, output34]})
# 
# dataframe_sensitivity_statusQuo.to_csv(r'../../results/outcomes/sensitivity-result-benefit-SQ-part4.csv', index = False)
# =============================================================================


output35=analyze_sensitivity.run_sensitivity_benefit_SQ('total_employees',+10, broadband=True)
output36=analyze_sensitivity.run_sensitivity_benefit_SQ('total_employees',-10, broadband=True)
output37=analyze_sensitivity.run_sensitivity_benefit_SQ('affected_employees',+10, broadband=True)
output38=analyze_sensitivity.run_sensitivity_benefit_SQ('affected_employees',-10, broadband=True)

dataframe_sensitivity_statusQuo=pd.DataFrame({'Parameter':['total_employees','affected_employees'],
                                 '%change in benefit resulted from +%10 change in parameter': [output35, output37],
                                 '%change in benefit resulted from -%10 change in parameter': [output36, output38]})

dataframe_sensitivity_statusQuo.to_csv(r'../../results/outcomes/sensitivity-result-benefit-SQ-part5.csv', index = False)


output39=analyze_sensitivity.run_sensitivity_benefit_SQ('cost_per_hour',+10, broadband=True)
output40=analyze_sensitivity.run_sensitivity_benefit_SQ('cost_per_hour',-10, broadband=True)
output41=analyze_sensitivity.run_sensitivity_benefit_SQ('outage_hours',+10, broadband=True)
output42=analyze_sensitivity.run_sensitivity_benefit_SQ('outage_hours',-10, broadband=True)

dataframe_sensitivity_statusQuo=pd.DataFrame({'Parameter':['cost_per_hour','outage_hours'],
                                 '%change in benefit resulted from +%10 change in parameter': [output39, output41],
                                 '%change in benefit resulted from -%10 change in parameter': [output40, output42]})

dataframe_sensitivity_statusQuo.to_csv(r'../../results/outcomes/sensitivity-result-benefit-SQ-part6.csv', index = False)


