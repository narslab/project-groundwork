import sensitivity as analyze_sensitivity
import pandas as pd

#cost sensitivity results for JAA
# =============================================================================
# output1=analyze_sensitivity.run_sensitivity_cost_JAA('r',10)
# output2=analyze_sensitivity.run_sensitivity_cost_JAA('r',-10)
# output3=analyze_sensitivity.run_sensitivity_cost_JAA('overhead_line',10,'corridor_width')
# output4=analyze_sensitivity.run_sensitivity_cost_JAA('overhead_line',-10,'corridor_width')
# output5=analyze_sensitivity.run_sensitivity_cost_JAA('underground_line',10,'corridor_width')
# output6=analyze_sensitivity.run_sensitivity_cost_JAA('underground_line',-10,'corridor_width')
# output7=analyze_sensitivity.run_sensitivity_cost_JAA('overhead_line',10,'replcost')
# output8=analyze_sensitivity.run_sensitivity_cost_JAA('overhead_line',-10,'replcost')
# output9=analyze_sensitivity.run_sensitivity_cost_JAA('underground_line',10,'replcost')
# output10=analyze_sensitivity.run_sensitivity_cost_JAA('underground_line',-10,'replcost')
# 
#  
# dataframe_sensitivity_JAA_part1=pd.DataFrame({'Parameter':['r','over_corridor_width','under_corridor_width','over_replcost_el','under_replcost_el'],
#                                   '%change in cost resulted from +%10 change in parameter': [output1,output3,output5,output7,output9],
#                                   '%change in cost resulted from -%10 change in parameter': [output2,output4,output6,output8,output10]})
#  
# dataframe_sensitivity_JAA_part1.to_csv(r'../../results/outcomes/sensitivity-cost-result-JAA-part1.csv', index = False)
# print("Done part1")
#  
# output11=analyze_sensitivity.run_sensitivity_cost_JAA('overhead_proportion',10)
# output12=analyze_sensitivity.run_sensitivity_cost_JAA('overhead_proportion',-10)
# output13=analyze_sensitivity.run_sensitivity_cost_JAA('overhead_line',10,'lifespan')
# output14=analyze_sensitivity.run_sensitivity_cost_JAA('overhead_line',-10,'lifespan')
# output15=analyze_sensitivity.run_sensitivity_cost_JAA('underground_line',10,'lifespan')
# output16=analyze_sensitivity.run_sensitivity_cost_JAA('underground_line',-10,'lifespan')
# output17=analyze_sensitivity.run_sensitivity_cost_JAA('overhead_line',10,'om_proportion_replcost')
# output18=analyze_sensitivity.run_sensitivity_cost_JAA('overhead_line',-10,'om_proportion_replcost')
# output19=analyze_sensitivity.run_sensitivity_cost_JAA('underground_line',10,'om_proportion_replcost')
# output20=analyze_sensitivity.run_sensitivity_cost_JAA('underground_line',-10,'om_proportion_replcost')
#  
#  
# dataframe_sensitivity_JAA_part2=pd.DataFrame({'Parameter':['overhead_proportion','over_lifespan','under_lifespan','over_om_percentage_replcost_el','under_om_percentage_replcost_el'],
#                                   '%change in cost resulted from +%10 change in parameter': [output11,output13,output15,output17,output19],
#                                   '%change in cost resulted from -%10 change in parameter': [output12,output14,output16,output18,output20]})
#  
# dataframe_sensitivity_JAA_part2.to_csv(r'../../results/outcomes/sensitivity-cost-result-JAA-part2.csv', index = False)
# print("Done part2")
# 
# output21=analyze_sensitivity.run_sensitivity_cost_JAA('length_s',+10)
# output22=analyze_sensitivity.run_sensitivity_cost_JAA('length_s',-10)
# output23=analyze_sensitivity.run_sensitivity_cost_JAA('length_scale',+10)
# output24=analyze_sensitivity.run_sensitivity_cost_JAA('length_scale',-10)
# output25=analyze_sensitivity.run_sensitivity_cost_JAA('age_shape',+10)
# output26=analyze_sensitivity.run_sensitivity_cost_JAA('age_shape',-10)
# output27=analyze_sensitivity.run_sensitivity_cost_JAA('age_scale',+10)
# output28=analyze_sensitivity.run_sensitivity_cost_JAA('age_scale',-10)
# output29=analyze_sensitivity.run_sensitivity_cost_JAA('average_length',+10)
# output30=analyze_sensitivity.run_sensitivity_cost_JAA('average_length',-10)
# 
# dataframe_sensitivity_JAA_part3=pd.DataFrame({'Parameter':['length_shape','length_scale','age_shape','age_scale','average_length'],
#                                  '%change in cost resulted from +%10 change in parameter': [output21,output23,output25,output27,output29],
#                                  '%change in cost resulted from -%10 change in parameter': [output22,output24,output26,output28, output30]})
# 
# dataframe_sensitivity_JAA_part3.to_csv(r'../../results/outcomes/sensitivity-cost-result-JAA-part3.csv', index = False)
# print("Done part3")
# =============================================================================

#output31=analyze_sensitivity.run_sensitivity_cost_SQ('segment_number',+10)
#output32=analyze_sensitivity.run_sensitivity_cost_SQ('segment_number',-10)


output33=analyze_sensitivity.run_sensitivity_cost_JAA('overhead_line',10,'replcost', broadband=True)
output34=analyze_sensitivity.run_sensitivity_cost_JAA('overhead_line',-10,'replcost', broadband=True)
output35=analyze_sensitivity.run_sensitivity_cost_JAA('underground_line',10,'replcost', broadband=True)
output36=analyze_sensitivity.run_sensitivity_cost_JAA('underground_line',-10,'replcost', broadband=True)
output37=analyze_sensitivity.run_sensitivity_cost_JAA('overhead_line',10,'om_proportion_replcost', broadband=True)
output38=analyze_sensitivity.run_sensitivity_cost_JAA('overhead_line',-10,'om_proportion_replcost', broadband=True)
output39=analyze_sensitivity.run_sensitivity_cost_JAA('underground_line',10,'om_proportion_replcost', broadband=True)
output40=analyze_sensitivity.run_sensitivity_cost_JAA('underground_line',-10,'om_proportion_replcost', broadband=True)
output41=analyze_sensitivity.run_sensitivity_cost_JAA('underground_line',10,'over_under_joint_proportion_convertcost', broadband=True)
output42=analyze_sensitivity.run_sensitivity_cost_JAA('underground_line',-10,'over_under_joint_proportion_convertcost', broadband=True)
output43=analyze_sensitivity.run_sensitivity_cost_JAA('joint_trench_additional',10)
output44=analyze_sensitivity.run_sensitivity_cost_JAA('joint_trench_additional',-10)




dataframe_sensitivity_JAA_part4=pd.DataFrame({'Parameter':['over_replcost_br','under_replcost_br','over_om_percentage_replcost_br','under_om_percentage_replcost_br','over_under_joint_proportion_convertcost','joint_trench_additional'],
                                 '%change in cost resulted from +%10 change in parameter': [output33, output35, output37, output39, output41, output43],
                                 '%change in cost resulted from -%10 change in parameter': [output34, output36, output38, output40, output42, output44]})

dataframe_sensitivity_JAA_part4.to_csv(r'../../results/outcomes/sensitivity-cost-result-JAA-part4.csv', index = False)
print("Done part4")


output45=analyze_sensitivity.run_sensitivity_cost_JAA('vsl',10)
output46=analyze_sensitivity.run_sensitivity_cost_JAA('vsl',-10)
output47=analyze_sensitivity.run_sensitivity_cost_JAA('employees',10)
output48=analyze_sensitivity.run_sensitivity_cost_JAA('employees',-10)
output49=analyze_sensitivity.run_sensitivity_cost_JAA('fir',10)
output50=analyze_sensitivity.run_sensitivity_cost_JAA('fir',-10)
output51=analyze_sensitivity.run_sensitivity_cost_JAA('nfir',10)
output52=analyze_sensitivity.run_sensitivity_cost_JAA('nfir',-10)
output53=analyze_sensitivity.run_sensitivity_cost_JAA('r',10)
output54=analyze_sensitivity.run_sensitivity_cost_JAA('r',-10)



dataframe_sensitivity_JAA_part5=pd.DataFrame({'Parameter':['vsl_el','employees_el','fir_el','nfir_el','r_el'],
                                 '%change in cost resulted from +%10 change in parameter': [output45, output47, output49, output51, output53],
                                 '%change in cost resulted from -%10 change in parameter': [output46, output48, output50, output52, output54]})

dataframe_sensitivity_JAA_part5.to_csv(r'../../results/outcomes/sensitivity-cost-result-JAA-part5.csv', index = False)
print("Done part5")


output55=analyze_sensitivity.run_sensitivity_cost_JAA('vsl',10, broadband=True)
output56=analyze_sensitivity.run_sensitivity_cost_JAA('vsl',-10, broadband=True)
output57=analyze_sensitivity.run_sensitivity_cost_JAA('employees',10, broadband=True)
output58=analyze_sensitivity.run_sensitivity_cost_JAA('employees',-10, broadband=True)
output59=analyze_sensitivity.run_sensitivity_cost_JAA('fir',10, broadband=True)
output60=analyze_sensitivity.run_sensitivity_cost_JAA('fir',-10, broadband=True)
output61=analyze_sensitivity.run_sensitivity_cost_JAA('nfir',10, broadband=True)
output62=analyze_sensitivity.run_sensitivity_cost_JAA('nfir',-10, broadband=True)
output63=analyze_sensitivity.run_sensitivity_cost_JAA('r',10, broadband=True)
output64=analyze_sensitivity.run_sensitivity_cost_JAA('r',-10, broadband=True)



dataframe_sensitivity_JAA_part6=pd.DataFrame({'Parameter':['vsl_el','employees_el','fir_el','nfir_el','r_el'],
                                 '%change in cost resulted from +%10 change in parameter': [output55, output57, output59, output61, output63],
                                 '%change in cost resulted from -%10 change in parameter': [output56, output58, output60, output62, output64]})

dataframe_sensitivity_JAA_part6.to_csv(r'../../results/outcomes/sensitivity-cost-result-JAA-part6.csv', index = False)
print("Done part6")

