import pandas as pd
import Network
import Simulate
import random
import numpy as np


data  = Network.Electric_model_inputs()
data_broadband  = Network.Broadband_model_inputs()

## Costs
# Analyze result functions based on S1 to S13 results
def aggregate_costs_S1_to_S13(data, data_broadband):
    # S1
    df_output_S1=Simulate.run_cost_simulation_S1(data, data_broadband)
    df_analyze_result_S1=df_output_S1.groupby(level=[0])[['capex_el','opex_el','lifecycle_infrastructure_el','environmental_restoration_el','non_fatal_el','fatal_el','safety_el','total_cost_el','capex_br','opex_br','lifecycle_infrastructure_br','environmental_restoration_br','non_fatal_br','fatal_br','safety_br','total_cost_br']].sum()
    df_analyze_result_S1.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S1.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-analyze-result-S1.csv', index = False)
    print("Done aggregating costs of S1")
    
    # S2
    df_output_S2=Simulate.run_cost_simulation_S2(data, data_broadband)
    df_analyze_result_S2=df_output_S2.groupby(level=[0])[['capex_el','opex_el','lifecycle_infrastructure_el','environmental_restoration_el','non_fatal_el','fatal_el','safety_el','total_cost_el','capex_br','opex_br','lifecycle_infrastructure_br','environmental_restoration_br','non_fatal_br','fatal_br','safety_br','total_cost_br']].sum()
    df_analyze_result_S2.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S2.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-analyze-result-S2.csv', index = False)
    print("Done aggregating costs of S2")

    # S3
    df_output_S3=Simulate.run_cost_simulation_S3(data, data_broadband)
    df_analyze_result_S3=df_output_S3.groupby(level=[0])[['capex_el','opex_el','lifecycle_infrastructure_el','environmental_restoration_el','non_fatal_el','fatal_el','safety_el','total_cost_el','capex_br','opex_br','lifecycle_infrastructure_br','environmental_restoration_br','non_fatal_br','fatal_br','safety_br','total_cost_br']].sum()
    df_analyze_result_S3.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S3.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-analyze-result-S3.csv', index = False)
    print("Done aggregating costs of S3")

    # S4
    df_output_S4=Simulate.run_cost_simulation_S4(data, data_broadband)
    df_analyze_result_S4=df_output_S4.groupby(level=[0])[['capex_el','opex_el','lifecycle_infrastructure_el','environmental_restoration_el','non_fatal_el','fatal_el','safety_el','total_cost_el','capex_br','opex_br','lifecycle_infrastructure_br','environmental_restoration_br','non_fatal_br','fatal_br','safety_br','total_cost_br']].sum()
    df_analyze_result_S4.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S4.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-analyze-result-S4.csv', index = False)
    print("Done aggregating costs of S4")

    # S5
    df_output_S5=Simulate.run_cost_simulation_S5(data, data_broadband)
    df_analyze_result_S5=df_output_S5.groupby(level=[0])[['capex_el','opex_el','lifecycle_infrastructure_el','environmental_restoration_el','non_fatal_el','fatal_el','safety_el','total_cost_el','capex_br','opex_br','lifecycle_infrastructure_br','environmental_restoration_br','non_fatal_br','fatal_br','safety_br','total_cost_br']].sum()
    df_analyze_result_S5.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S5.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-analyze-result-S5.csv', index = False)
    print("Done aggregating costs of S5")
    
    # S6
    df_output_S6=Simulate.run_cost_simulation_S6(data, data_broadband)
    df_analyze_result_S6=df_output_S6.groupby(level=[0])[['capex_el','opex_el','lifecycle_infrastructure_el','environmental_restoration_el','non_fatal_el','fatal_el','safety_el','total_cost_el','capex_br','opex_br','lifecycle_infrastructure_br','environmental_restoration_br','non_fatal_br','fatal_br','safety_br','total_cost_br']].sum()
    df_analyze_result_S6.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S6.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-analyze-result-S6.csv', index = False)
    print("Done aggregating costs of S6")
    
    # S7
    df_output_S7=Simulate.run_cost_simulation_S7(data, data_broadband)
    df_analyze_result_S7=df_output_S7.groupby(level=[0])[['capex_el','opex_el','lifecycle_infrastructure_el','environmental_restoration_el','non_fatal_el','fatal_el','safety_el','total_cost_el','capex_br','opex_br','lifecycle_infrastructure_br','environmental_restoration_br','non_fatal_br','fatal_br','safety_br','total_cost_br']].sum()
    df_analyze_result_S7.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S7.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-analyze-result-S7.csv', index = False)
    print("Done aggregating costs of S7")

    # S8
    df_output_S8=Simulate.run_cost_simulation_S8(data, data_broadband)
    df_analyze_result_S8=df_output_S8.groupby(level=[0])[['capex_el','opex_el','lifecycle_infrastructure_el','environmental_restoration_el','non_fatal_el','fatal_el','safety_el','total_cost_el','capex_br','opex_br','lifecycle_infrastructure_br','environmental_restoration_br','non_fatal_br','fatal_br','safety_br','total_cost_br']].sum()
    df_analyze_result_S8.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S8.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-analyze-result-S8.csv', index = False)
    print("Done aggregating costs of S8")

    # S9
    df_output_S9=Simulate.run_cost_simulation_S9(data, data_broadband)
    df_analyze_result_S9=df_output_S9.groupby(level=[0])[['capex_el','opex_el','lifecycle_infrastructure_el','environmental_restoration_el','non_fatal_el','fatal_el','safety_el','total_cost_el','capex_br','opex_br','lifecycle_infrastructure_br','environmental_restoration_br','non_fatal_br','fatal_br','safety_br','total_cost_br']].sum()
    df_analyze_result_S9.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S9.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-analyze-result-S9.csv', index = False)
    print("Done aggregating costs of S9")

    # S10
    df_output_S10=Simulate.run_cost_simulation_S10(data, data_broadband)
    df_analyze_result_S10=df_output_S10.groupby(level=[0])[['capex_el','opex_el','lifecycle_infrastructure_el','environmental_restoration_el','non_fatal_el','fatal_el','safety_el','total_cost_el','capex_br','opex_br','lifecycle_infrastructure_br','environmental_restoration_br','non_fatal_br','fatal_br','safety_br','total_cost_br']].sum()
    df_analyze_result_S10.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S10.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-analyze-result-S10.csv', index = False)
    print("Done aggregating costs of S10")
    
    # S11
    df_output_S11=Simulate.run_cost_simulation_S11(data, data_broadband)
    df_analyze_result_S11=df_output_S11.groupby(level=[0])[['capex_el','opex_el','lifecycle_infrastructure_el','environmental_restoration_el','non_fatal_el','fatal_el','safety_el','total_cost_el','capex_br','opex_br','lifecycle_infrastructure_br','environmental_restoration_br','non_fatal_br','fatal_br','safety_br','total_cost_br']].sum()
    df_analyze_result_S11.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S11.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-analyze-result-S11.csv', index = False)
    print("Done aggregating costs of S11")
    
    # S12
    df_output_S12=Simulate.run_cost_simulation_S12(data, data_broadband)
    df_analyze_result_S12=df_output_S12.groupby(level=[0])[['capex_el','opex_el','lifecycle_infrastructure_el','environmental_restoration_el','non_fatal_el','fatal_el','safety_el','total_cost_el','capex_br','opex_br','lifecycle_infrastructure_br','environmental_restoration_br','non_fatal_br','fatal_br','safety_br','total_cost_br']].sum()
    df_analyze_result_S12.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S12.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-analyze-result-S12.csv', index = False)
    print("Done aggregating costs of S12")
    
    # S13
    df_output_S13=Simulate.run_cost_simulation_S13(data, data_broadband)
    df_analyze_result_S13=df_output_S13.groupby(level=[0])[['capex_el','opex_el','lifecycle_infrastructure_el','environmental_restoration_el','non_fatal_el','fatal_el','safety_el','total_cost_el','capex_br','opex_br','lifecycle_infrastructure_br','environmental_restoration_br','non_fatal_br','fatal_br','safety_br','total_cost_br']].sum()
    df_analyze_result_S13.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S13.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-analyze-result-S13.csv', index = False)
    print("Done aggregating costs of S13")
    return(df_analyze_result_S1, df_analyze_result_S2, df_analyze_result_S3, df_analyze_result_S4, df_analyze_result_S5, df_analyze_result_S6, df_analyze_result_S7, df_analyze_result_S8, df_analyze_result_S9, df_analyze_result_S10, df_analyze_result_S11, df_analyze_result_S12, df_analyze_result_S13)


# Calculate net present values for S1 to S13
def calculate_cost_npv_S1_to_S13(data, data_broadband):
    df_analyze_result_S1, df_analyze_result_S2, df_analyze_result_S3, df_analyze_result_S4, df_analyze_result_S5, df_analyze_result_S6, df_analyze_result_S7, df_analyze_result_S8, df_analyze_result_S9, df_analyze_result_S10, df_analyze_result_S11, df_analyze_result_S12, df_analyze_result_S13=aggregate_costs_S1_to_S13(data, data_broadband)    
    # S1
    S1_npv_infrastructure_cost_el=[]
    S1_npv_environmental_cost_el=[]
    S1_npv_safety_cost_el=[]
    S1_npv_total_cost_el=[]
    S1_npv_infrastructure_cost_br=[]
    S1_npv_environmental_cost_br=[]
    S1_npv_safety_cost_br=[]
    S1_npv_total_cost_br=[]
    for index, row in df_analyze_result_S1.iterrows():
        S1_npv_infrastructure_cost_el.append(row['lifecycle_infrastructure_el']/(1+data.parameter_dict['r'])**index)
        S1_npv_environmental_cost_el.append(row['environmental_restoration_el']/(1+data.parameter_dict['r'])**index)
        S1_npv_safety_cost_el.append(row['safety_el']/(1+data.parameter_dict['r'])**index)
        S1_npv_total_cost_el.append(row['total_cost_el']/(1+data.parameter_dict['r'])**index)
        S1_npv_infrastructure_cost_br.append(row['lifecycle_infrastructure_br']/(1+data_broadband.parameter_dict['r'])**index)
        S1_npv_environmental_cost_br.append(row['environmental_restoration_br']/(1+data_broadband.parameter_dict['r'])**index)
        S1_npv_safety_cost_br.append(row['safety_br']/(1+data_broadband.parameter_dict['r'])**index)
        S1_npv_total_cost_br.append(row['total_cost_br']/(1+data_broadband.parameter_dict['r'])**index)
    S1_total_infrastructre_el=sum(S1_npv_infrastructure_cost_el)
    S1_total_environmental_el=sum(S1_npv_environmental_cost_el)
    S1_total_safety_el=sum(S1_npv_safety_cost_el)
    S1_total_cost_el=sum(S1_npv_total_cost_el)
    S1_total_infrastructre_br=sum(S1_npv_infrastructure_cost_br)
    S1_total_environmental_br=sum(S1_npv_environmental_cost_br)
    S1_total_safety_br=sum(S1_npv_safety_cost_br)
    S1_total_cost_br=sum(S1_npv_total_cost_br)
    S1_df_npv= pd.DataFrame({'lifecycle_infrastructure_el':[S1_total_infrastructre_el],
                             'environmental_restoration_el':[S1_total_environmental_el],
                             'safety_el':[S1_total_safety_el],
                             'total_cost_el':[S1_total_cost_el],
                             'lifecycle_infrastructure_br':[S1_total_infrastructre_br],
                             'environmental_restoration_br':[S1_total_environmental_br],
                             'safety_br':[S1_total_safety_br],
                             'total_cost_br':[S1_total_cost_br]},
                            )
    #S1_df_npv.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-npv-S1.csv', index = False)
    # S2
    S2_npv_infrastructure_cost_el=[]
    S2_npv_environmental_cost_el=[]
    S2_npv_safety_cost_el=[]
    S2_npv_total_cost_el=[]
    S2_npv_infrastructure_cost_br=[]
    S2_npv_environmental_cost_br=[]
    S2_npv_safety_cost_br=[]
    S2_npv_total_cost_br=[]
    for index, row in df_analyze_result_S2.iterrows():
        S2_npv_infrastructure_cost_el.append(row['lifecycle_infrastructure_el']/(1+data.parameter_dict['r'])**index)
        S2_npv_environmental_cost_el.append(row['environmental_restoration_el']/(1+data.parameter_dict['r'])**index)
        S2_npv_safety_cost_el.append(row['safety_el']/(1+data.parameter_dict['r'])**index)
        S2_npv_total_cost_el.append(row['total_cost_el']/(1+data.parameter_dict['r'])**index)
        S2_npv_infrastructure_cost_br.append(row['lifecycle_infrastructure_br']/(1+data_broadband.parameter_dict['r'])**index)
        S2_npv_environmental_cost_br.append(row['environmental_restoration_br']/(1+data_broadband.parameter_dict['r'])**index)
        S2_npv_safety_cost_br.append(row['safety_br']/(1+data_broadband.parameter_dict['r'])**index)
        S2_npv_total_cost_br.append(row['total_cost_br']/(1+data_broadband.parameter_dict['r'])**index)
    S2_total_infrastructre_el=sum(S2_npv_infrastructure_cost_el)
    S2_total_environmental_el=sum(S2_npv_environmental_cost_el)
    S2_total_safety_el=sum(S2_npv_safety_cost_el)
    S2_total_cost_el=sum(S2_npv_total_cost_el)
    S2_total_infrastructre_br=sum(S2_npv_infrastructure_cost_br)
    S2_total_environmental_br=sum(S2_npv_environmental_cost_br)
    S2_total_safety_br=sum(S2_npv_safety_cost_br)
    S2_total_cost_br=sum(S2_npv_total_cost_br)
    S2_df_npv= pd.DataFrame({'lifecycle_infrastructure_el':[S2_total_infrastructre_el],
                             'environmental_restoration_el':[S2_total_environmental_el],
                             'safety_el':[S2_total_safety_el],
                             'total_cost_el':[S2_total_cost_el],
                             'lifecycle_infrastructure_br':[S2_total_infrastructre_br],
                             'environmental_restoration_br':[S2_total_environmental_br],
                             'safety_br':[S2_total_safety_br],
                             'total_cost_br':[S2_total_cost_br]},
                            )
    #S2_df_npv.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-npv-S2.csv', index = False)
    # S3
    S3_npv_infrastructure_cost_el=[]
    S3_npv_environmental_cost_el=[]
    S3_npv_safety_cost_el=[]
    S3_npv_total_cost_el=[]
    S3_npv_infrastructure_cost_br=[]
    S3_npv_environmental_cost_br=[]
    S3_npv_safety_cost_br=[]
    S3_npv_total_cost_br=[]
    for index, row in df_analyze_result_S3.iterrows():
        S3_npv_infrastructure_cost_el.append(row['lifecycle_infrastructure_el']/(1+data.parameter_dict['r'])**index)
        S3_npv_environmental_cost_el.append(row['environmental_restoration_el']/(1+data.parameter_dict['r'])**index)
        S3_npv_safety_cost_el.append(row['safety_el']/(1+data.parameter_dict['r'])**index)
        S3_npv_total_cost_el.append(row['total_cost_el']/(1+data.parameter_dict['r'])**index)
        S3_npv_infrastructure_cost_br.append(row['lifecycle_infrastructure_br']/(1+data_broadband.parameter_dict['r'])**index)
        S3_npv_environmental_cost_br.append(row['environmental_restoration_br']/(1+data_broadband.parameter_dict['r'])**index)
        S3_npv_safety_cost_br.append(row['safety_br']/(1+data_broadband.parameter_dict['r'])**index)
        S3_npv_total_cost_br.append(row['total_cost_br']/(1+data_broadband.parameter_dict['r'])**index)
    S3_total_infrastructre_el=sum(S3_npv_infrastructure_cost_el)
    S3_total_environmental_el=sum(S3_npv_environmental_cost_el)
    S3_total_safety_el=sum(S3_npv_safety_cost_el)
    S3_total_cost_el=sum(S3_npv_total_cost_el)
    S3_total_infrastructre_br=sum(S3_npv_infrastructure_cost_br)
    S3_total_environmental_br=sum(S3_npv_environmental_cost_br)
    S3_total_safety_br=sum(S3_npv_safety_cost_br)
    S3_total_cost_br=sum(S3_npv_total_cost_br)
    S3_df_npv= pd.DataFrame({'lifecycle_infrastructure_el':[S3_total_infrastructre_el],
                             'environmental_restoration_el':[S3_total_environmental_el],
                             'safety_el':[S3_total_safety_el],
                             'total_cost_el':[S3_total_cost_el],
                             'lifecycle_infrastructure_br':[S3_total_infrastructre_br],
                             'environmental_restoration_br':[S3_total_environmental_br],
                             'safety_br':[S3_total_safety_br],
                             'total_cost_br':[S3_total_cost_br]},
                            )
    #S3_df_npv.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-npv-S3.csv', index = False)    
    # S4
    S4_npv_infrastructure_cost_el=[]
    S4_npv_environmental_cost_el=[]
    S4_npv_safety_cost_el=[]
    S4_npv_total_cost_el=[]
    S4_npv_infrastructure_cost_br=[]
    S4_npv_environmental_cost_br=[]
    S4_npv_safety_cost_br=[]
    S4_npv_total_cost_br=[]
    for index, row in df_analyze_result_S4.iterrows():
        S4_npv_infrastructure_cost_el.append(row['lifecycle_infrastructure_el']/(1+data.parameter_dict['r'])**index)
        S4_npv_environmental_cost_el.append(row['environmental_restoration_el']/(1+data.parameter_dict['r'])**index)
        S4_npv_safety_cost_el.append(row['safety_el']/(1+data.parameter_dict['r'])**index)
        S4_npv_total_cost_el.append(row['total_cost_el']/(1+data.parameter_dict['r'])**index)
        S4_npv_infrastructure_cost_br.append(row['lifecycle_infrastructure_br']/(1+data_broadband.parameter_dict['r'])**index)
        S4_npv_environmental_cost_br.append(row['environmental_restoration_br']/(1+data_broadband.parameter_dict['r'])**index)
        S4_npv_safety_cost_br.append(row['safety_br']/(1+data_broadband.parameter_dict['r'])**index)
        S4_npv_total_cost_br.append(row['total_cost_br']/(1+data_broadband.parameter_dict['r'])**index)
    S4_total_infrastructre_el=sum(S4_npv_infrastructure_cost_el)
    S4_total_environmental_el=sum(S4_npv_environmental_cost_el)
    S4_total_safety_el=sum(S4_npv_safety_cost_el)
    S4_total_cost_el=sum(S4_npv_total_cost_el)
    S4_total_infrastructre_br=sum(S4_npv_infrastructure_cost_br)
    S4_total_environmental_br=sum(S4_npv_environmental_cost_br)
    S4_total_safety_br=sum(S4_npv_safety_cost_br)
    S4_total_cost_br=sum(S4_npv_total_cost_br)
    S4_df_npv= pd.DataFrame({'lifecycle_infrastructure_el':[S4_total_infrastructre_el],
                             'environmental_restoration_el':[S4_total_environmental_el],
                             'safety_el':[S4_total_safety_el],
                             'total_cost_el':[S4_total_cost_el],
                             'lifecycle_infrastructure_br':[S4_total_infrastructre_br],
                             'environmental_restoration_br':[S4_total_environmental_br],
                             'safety_br':[S4_total_safety_br],
                             'total_cost_br':[S4_total_cost_br]},
                            )
    #S4_df_npv.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-npv-S4.csv', index = False) 
    # S5
    S5_npv_infrastructure_cost_el=[]
    S5_npv_environmental_cost_el=[]
    S5_npv_safety_cost_el=[]
    S5_npv_total_cost_el=[]
    S5_npv_infrastructure_cost_br=[]
    S5_npv_environmental_cost_br=[]
    S5_npv_safety_cost_br=[]
    S5_npv_total_cost_br=[]
    for index, row in df_analyze_result_S5.iterrows():
        S5_npv_infrastructure_cost_el.append(row['lifecycle_infrastructure_el']/(1+data.parameter_dict['r'])**index)
        S5_npv_environmental_cost_el.append(row['environmental_restoration_el']/(1+data.parameter_dict['r'])**index)
        S5_npv_safety_cost_el.append(row['safety_el']/(1+data.parameter_dict['r'])**index)
        S5_npv_total_cost_el.append(row['total_cost_el']/(1+data.parameter_dict['r'])**index)
        S5_npv_infrastructure_cost_br.append(row['lifecycle_infrastructure_br']/(1+data_broadband.parameter_dict['r'])**index)
        S5_npv_environmental_cost_br.append(row['environmental_restoration_br']/(1+data_broadband.parameter_dict['r'])**index)
        S5_npv_safety_cost_br.append(row['safety_br']/(1+data_broadband.parameter_dict['r'])**index)
        S5_npv_total_cost_br.append(row['total_cost_br']/(1+data_broadband.parameter_dict['r'])**index)
    S5_total_infrastructre_el=sum(S5_npv_infrastructure_cost_el)
    S5_total_environmental_el=sum(S5_npv_environmental_cost_el)
    S5_total_safety_el=sum(S5_npv_safety_cost_el)
    S5_total_cost_el=sum(S5_npv_total_cost_el)
    S5_total_infrastructre_br=sum(S5_npv_infrastructure_cost_br)
    S5_total_environmental_br=sum(S5_npv_environmental_cost_br)
    S5_total_safety_br=sum(S5_npv_safety_cost_br)
    S5_total_cost_br=sum(S5_npv_total_cost_br)
    S5_df_npv= pd.DataFrame({'lifecycle_infrastructure_el':[S5_total_infrastructre_el],
                             'environmental_restoration_el':[S5_total_environmental_el],
                             'safety_el':[S5_total_safety_el],
                             'total_cost_el':[S5_total_cost_el],
                             'lifecycle_infrastructure_br':[S5_total_infrastructre_br],
                             'environmental_restoration_br':[S5_total_environmental_br],
                             'safety_br':[S5_total_safety_br],
                             'total_cost_br':[S5_total_cost_br]},
                            )
    #S5_df_npv.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-npv-S5.csv', index = False) 
    # S6
    S6_npv_infrastructure_cost_el=[]
    S6_npv_environmental_cost_el=[]
    S6_npv_safety_cost_el=[]
    S6_npv_total_cost_el=[]
    S6_npv_infrastructure_cost_br=[]
    S6_npv_environmental_cost_br=[]
    S6_npv_safety_cost_br=[]
    S6_npv_total_cost_br=[]
    for index, row in df_analyze_result_S6.iterrows():
        S6_npv_infrastructure_cost_el.append(row['lifecycle_infrastructure_el']/(1+data.parameter_dict['r'])**index)
        S6_npv_environmental_cost_el.append(row['environmental_restoration_el']/(1+data.parameter_dict['r'])**index)
        S6_npv_safety_cost_el.append(row['safety_el']/(1+data.parameter_dict['r'])**index)
        S6_npv_total_cost_el.append(row['total_cost_el']/(1+data.parameter_dict['r'])**index)
        S6_npv_infrastructure_cost_br.append(row['lifecycle_infrastructure_br']/(1+data_broadband.parameter_dict['r'])**index)
        S6_npv_environmental_cost_br.append(row['environmental_restoration_br']/(1+data_broadband.parameter_dict['r'])**index)
        S6_npv_safety_cost_br.append(row['safety_br']/(1+data_broadband.parameter_dict['r'])**index)
        S6_npv_total_cost_br.append(row['total_cost_br']/(1+data_broadband.parameter_dict['r'])**index)
    S6_total_infrastructre_el=sum(S6_npv_infrastructure_cost_el)
    S6_total_environmental_el=sum(S6_npv_environmental_cost_el)
    S6_total_safety_el=sum(S6_npv_safety_cost_el)
    S6_total_cost_el=sum(S6_npv_total_cost_el)
    S6_total_infrastructre_br=sum(S6_npv_infrastructure_cost_br)
    S6_total_environmental_br=sum(S6_npv_environmental_cost_br)
    S6_total_safety_br=sum(S6_npv_safety_cost_br)
    S6_total_cost_br=sum(S6_npv_total_cost_br)
    S6_df_npv= pd.DataFrame({'lifecycle_infrastructure_el':[S6_total_infrastructre_el],
                             'environmental_restoration_el':[S6_total_environmental_el],
                             'safety_el':[S6_total_safety_el],
                             'total_cost_el':[S6_total_cost_el],
                             'lifecycle_infrastructure_br':[S6_total_infrastructre_br],
                             'environmental_restoration_br':[S6_total_environmental_br],
                             'safety_br':[S6_total_safety_br],
                             'total_cost_br':[S6_total_cost_br]},
                            )
    #S6_df_npv.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-npv-S6.csv', index = False) 
    # S7
    S7_npv_infrastructure_cost_el=[]
    S7_npv_environmental_cost_el=[]
    S7_npv_safety_cost_el=[]
    S7_npv_total_cost_el=[]
    S7_npv_infrastructure_cost_br=[]
    S7_npv_environmental_cost_br=[]
    S7_npv_safety_cost_br=[]
    S7_npv_total_cost_br=[]
    for index, row in df_analyze_result_S7.iterrows():
        S7_npv_infrastructure_cost_el.append(row['lifecycle_infrastructure_el']/(1+data.parameter_dict['r'])**index)
        S7_npv_environmental_cost_el.append(row['environmental_restoration_el']/(1+data.parameter_dict['r'])**index)
        S7_npv_safety_cost_el.append(row['safety_el']/(1+data.parameter_dict['r'])**index)
        S7_npv_total_cost_el.append(row['total_cost_el']/(1+data.parameter_dict['r'])**index)
        S7_npv_infrastructure_cost_br.append(row['lifecycle_infrastructure_br']/(1+data_broadband.parameter_dict['r'])**index)
        S7_npv_environmental_cost_br.append(row['environmental_restoration_br']/(1+data_broadband.parameter_dict['r'])**index)
        S7_npv_safety_cost_br.append(row['safety_br']/(1+data_broadband.parameter_dict['r'])**index)
        S7_npv_total_cost_br.append(row['total_cost_br']/(1+data_broadband.parameter_dict['r'])**index)
    S7_total_infrastructre_el=sum(S7_npv_infrastructure_cost_el)
    S7_total_environmental_el=sum(S7_npv_environmental_cost_el)
    S7_total_safety_el=sum(S7_npv_safety_cost_el)
    S7_total_cost_el=sum(S7_npv_total_cost_el)
    S7_total_infrastructre_br=sum(S7_npv_infrastructure_cost_br)
    S7_total_environmental_br=sum(S7_npv_environmental_cost_br)
    S7_total_safety_br=sum(S7_npv_safety_cost_br)
    S7_total_cost_br=sum(S7_npv_total_cost_br)
    S7_df_npv= pd.DataFrame({'lifecycle_infrastructure_el':[S7_total_infrastructre_el],
                             'environmental_restoration_el':[S7_total_environmental_el],
                             'safety_el':[S7_total_safety_el],
                             'total_cost_el':[S7_total_cost_el],
                             'lifecycle_infrastructure_br':[S7_total_infrastructre_br],
                             'environmental_restoration_br':[S7_total_environmental_br],
                             'safety_br':[S7_total_safety_br],
                             'total_cost_br':[S7_total_cost_br]},
                            )
    #S7_df_npv.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-npv-S7.csv', index = False) 
    # S8
    S8_npv_infrastructure_cost_el=[]
    S8_npv_environmental_cost_el=[]
    S8_npv_safety_cost_el=[]
    S8_npv_total_cost_el=[]
    S8_npv_infrastructure_cost_br=[]
    S8_npv_environmental_cost_br=[]
    S8_npv_safety_cost_br=[]
    S8_npv_total_cost_br=[]
    for index, row in df_analyze_result_S8.iterrows():
        S8_npv_infrastructure_cost_el.append(row['lifecycle_infrastructure_el']/(1+data.parameter_dict['r'])**index)
        S8_npv_environmental_cost_el.append(row['environmental_restoration_el']/(1+data.parameter_dict['r'])**index)
        S8_npv_safety_cost_el.append(row['safety_el']/(1+data.parameter_dict['r'])**index)
        S8_npv_total_cost_el.append(row['total_cost_el']/(1+data.parameter_dict['r'])**index)
        S8_npv_infrastructure_cost_br.append(row['lifecycle_infrastructure_br']/(1+data_broadband.parameter_dict['r'])**index)
        S8_npv_environmental_cost_br.append(row['environmental_restoration_br']/(1+data_broadband.parameter_dict['r'])**index)
        S8_npv_safety_cost_br.append(row['safety_br']/(1+data_broadband.parameter_dict['r'])**index)
        S8_npv_total_cost_br.append(row['total_cost_br']/(1+data_broadband.parameter_dict['r'])**index)
    S8_total_infrastructre_el=sum(S8_npv_infrastructure_cost_el)
    S8_total_environmental_el=sum(S8_npv_environmental_cost_el)
    S8_total_safety_el=sum(S8_npv_safety_cost_el)
    S8_total_cost_el=sum(S8_npv_total_cost_el)
    S8_total_infrastructre_br=sum(S8_npv_infrastructure_cost_br)
    S8_total_environmental_br=sum(S8_npv_environmental_cost_br)
    S8_total_safety_br=sum(S8_npv_safety_cost_br)
    S8_total_cost_br=sum(S8_npv_total_cost_br)
    S8_df_npv= pd.DataFrame({'lifecycle_infrastructure_el':[S8_total_infrastructre_el],
                             'environmental_restoration_el':[S8_total_environmental_el],
                             'safety_el':[S8_total_safety_el],
                             'total_cost_el':[S8_total_cost_el],
                             'lifecycle_infrastructure_br':[S8_total_infrastructre_br],
                             'environmental_restoration_br':[S8_total_environmental_br],
                             'safety_br':[S8_total_safety_br],
                             'total_cost_br':[S8_total_cost_br]},
                            )
    #S8_df_npv.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-npv-S8.csv', index = False)     
    # S9
    S9_npv_infrastructure_cost_el=[]
    S9_npv_environmental_cost_el=[]
    S9_npv_safety_cost_el=[]
    S9_npv_total_cost_el=[]
    S9_npv_infrastructure_cost_br=[]
    S9_npv_environmental_cost_br=[]
    S9_npv_safety_cost_br=[]
    S9_npv_total_cost_br=[]
    for index, row in df_analyze_result_S9.iterrows():
        S9_npv_infrastructure_cost_el.append(row['lifecycle_infrastructure_el']/(1+data.parameter_dict['r'])**index)
        S9_npv_environmental_cost_el.append(row['environmental_restoration_el']/(1+data.parameter_dict['r'])**index)
        S9_npv_safety_cost_el.append(row['safety_el']/(1+data.parameter_dict['r'])**index)
        S9_npv_total_cost_el.append(row['total_cost_el']/(1+data.parameter_dict['r'])**index)
        S9_npv_infrastructure_cost_br.append(row['lifecycle_infrastructure_br']/(1+data_broadband.parameter_dict['r'])**index)
        S9_npv_environmental_cost_br.append(row['environmental_restoration_br']/(1+data_broadband.parameter_dict['r'])**index)
        S9_npv_safety_cost_br.append(row['safety_br']/(1+data_broadband.parameter_dict['r'])**index)
        S9_npv_total_cost_br.append(row['total_cost_br']/(1+data_broadband.parameter_dict['r'])**index)
    S9_total_infrastructre_el=sum(S9_npv_infrastructure_cost_el)
    S9_total_environmental_el=sum(S9_npv_environmental_cost_el)
    S9_total_safety_el=sum(S9_npv_safety_cost_el)
    S9_total_cost_el=sum(S9_npv_total_cost_el)
    S9_total_infrastructre_br=sum(S9_npv_infrastructure_cost_br)
    S9_total_environmental_br=sum(S9_npv_environmental_cost_br)
    S9_total_safety_br=sum(S9_npv_safety_cost_br)
    S9_total_cost_br=sum(S9_npv_total_cost_br)
    S9_df_npv= pd.DataFrame({'lifecycle_infrastructure_el':[S9_total_infrastructre_el],
                             'environmental_restoration_el':[S9_total_environmental_el],
                             'safety_el':[S9_total_safety_el],
                             'total_cost_el':[S9_total_cost_el],
                             'lifecycle_infrastructure_br':[S9_total_infrastructre_br],
                             'environmental_restoration_br':[S9_total_environmental_br],
                             'safety_br':[S9_total_safety_br],
                             'total_cost_br':[S9_total_cost_br]},
                            )
    #S9_df_npv.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-npv-S9.csv', index = False) 
    # S10
    S10_npv_infrastructure_cost_el=[]
    S10_npv_environmental_cost_el=[]
    S10_npv_safety_cost_el=[]
    S10_npv_total_cost_el=[]
    S10_npv_infrastructure_cost_br=[]
    S10_npv_environmental_cost_br=[]
    S10_npv_safety_cost_br=[]
    S10_npv_total_cost_br=[]
    for index, row in df_analyze_result_S10.iterrows():
        S10_npv_infrastructure_cost_el.append(row['lifecycle_infrastructure_el']/(1+data.parameter_dict['r'])**index)
        S10_npv_environmental_cost_el.append(row['environmental_restoration_el']/(1+data.parameter_dict['r'])**index)
        S10_npv_safety_cost_el.append(row['safety_el']/(1+data.parameter_dict['r'])**index)
        S10_npv_total_cost_el.append(row['total_cost_el']/(1+data.parameter_dict['r'])**index)
        S10_npv_infrastructure_cost_br.append(row['lifecycle_infrastructure_br']/(1+data_broadband.parameter_dict['r'])**index)
        S10_npv_environmental_cost_br.append(row['environmental_restoration_br']/(1+data_broadband.parameter_dict['r'])**index)
        S10_npv_safety_cost_br.append(row['safety_br']/(1+data_broadband.parameter_dict['r'])**index)
        S10_npv_total_cost_br.append(row['total_cost_br']/(1+data_broadband.parameter_dict['r'])**index)
    S10_total_infrastructre_el=sum(S10_npv_infrastructure_cost_el)
    S10_total_environmental_el=sum(S10_npv_environmental_cost_el)
    S10_total_safety_el=sum(S10_npv_safety_cost_el)
    S10_total_cost_el=sum(S10_npv_total_cost_el)
    S10_total_infrastructre_br=sum(S10_npv_infrastructure_cost_br)
    S10_total_environmental_br=sum(S10_npv_environmental_cost_br)
    S10_total_safety_br=sum(S10_npv_safety_cost_br)
    S10_total_cost_br=sum(S10_npv_total_cost_br)
    S10_df_npv= pd.DataFrame({'lifecycle_infrastructure_el':[S10_total_infrastructre_el],
                             'environmental_restoration_el':[S10_total_environmental_el],
                             'safety_el':[S10_total_safety_el],
                             'total_cost_el':[S10_total_cost_el],
                             'lifecycle_infrastructure_br':[S10_total_infrastructre_br],
                             'environmental_restoration_br':[S10_total_environmental_br],
                             'safety_br':[S10_total_safety_br],
                             'total_cost_br':[S10_total_cost_br]},
                            )
    #S10_df_npv.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-npv-S10.csv', index = False) 
    # S11
    S11_npv_infrastructure_cost_el=[]
    S11_npv_environmental_cost_el=[]
    S11_npv_safety_cost_el=[]
    S11_npv_total_cost_el=[]
    S11_npv_infrastructure_cost_br=[]
    S11_npv_environmental_cost_br=[]
    S11_npv_safety_cost_br=[]
    S11_npv_total_cost_br=[]
    for index, row in df_analyze_result_S11.iterrows():
        S11_npv_infrastructure_cost_el.append(row['lifecycle_infrastructure_el']/(1+data.parameter_dict['r'])**index)
        S11_npv_environmental_cost_el.append(row['environmental_restoration_el']/(1+data.parameter_dict['r'])**index)
        S11_npv_safety_cost_el.append(row['safety_el']/(1+data.parameter_dict['r'])**index)
        S11_npv_total_cost_el.append(row['total_cost_el']/(1+data.parameter_dict['r'])**index)
        S11_npv_infrastructure_cost_br.append(row['lifecycle_infrastructure_br']/(1+data_broadband.parameter_dict['r'])**index)
        S11_npv_environmental_cost_br.append(row['environmental_restoration_br']/(1+data_broadband.parameter_dict['r'])**index)
        S11_npv_safety_cost_br.append(row['safety_br']/(1+data_broadband.parameter_dict['r'])**index)
        S11_npv_total_cost_br.append(row['total_cost_br']/(1+data_broadband.parameter_dict['r'])**index)
    S11_total_infrastructre_el=sum(S11_npv_infrastructure_cost_el)
    S11_total_environmental_el=sum(S11_npv_environmental_cost_el)
    S11_total_safety_el=sum(S11_npv_safety_cost_el)
    S11_total_cost_el=sum(S11_npv_total_cost_el)
    S11_total_infrastructre_br=sum(S11_npv_infrastructure_cost_br)
    S11_total_environmental_br=sum(S11_npv_environmental_cost_br)
    S11_total_safety_br=sum(S11_npv_safety_cost_br)
    S11_total_cost_br=sum(S11_npv_total_cost_br)
    S11_df_npv= pd.DataFrame({'lifecycle_infrastructure_el':[S11_total_infrastructre_el],
                             'environmental_restoration_el':[S11_total_environmental_el],
                             'safety_el':[S11_total_safety_el],
                             'total_cost_el':[S11_total_cost_el],
                             'lifecycle_infrastructure_br':[S11_total_infrastructre_br],
                             'environmental_restoration_br':[S11_total_environmental_br],
                             'safety_br':[S11_total_safety_br],
                             'total_cost_br':[S11_total_cost_br]},
                            )
    #S11_df_npv.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-npv-S11.csv', index = False) 
    # S12
    S12_npv_infrastructure_cost_el=[]
    S12_npv_environmental_cost_el=[]
    S12_npv_safety_cost_el=[]
    S12_npv_total_cost_el=[]
    S12_npv_infrastructure_cost_br=[]
    S12_npv_environmental_cost_br=[]
    S12_npv_safety_cost_br=[]
    S12_npv_total_cost_br=[]
    for index, row in df_analyze_result_S12.iterrows():
        S12_npv_infrastructure_cost_el.append(row['lifecycle_infrastructure_el']/(1+data.parameter_dict['r'])**index)
        S12_npv_environmental_cost_el.append(row['environmental_restoration_el']/(1+data.parameter_dict['r'])**index)
        S12_npv_safety_cost_el.append(row['safety_el']/(1+data.parameter_dict['r'])**index)
        S12_npv_total_cost_el.append(row['total_cost_el']/(1+data.parameter_dict['r'])**index)
        S12_npv_infrastructure_cost_br.append(row['lifecycle_infrastructure_br']/(1+data_broadband.parameter_dict['r'])**index)
        S12_npv_environmental_cost_br.append(row['environmental_restoration_br']/(1+data_broadband.parameter_dict['r'])**index)
        S12_npv_safety_cost_br.append(row['safety_br']/(1+data_broadband.parameter_dict['r'])**index)
        S12_npv_total_cost_br.append(row['total_cost_br']/(1+data_broadband.parameter_dict['r'])**index)
    S12_total_infrastructre_el=sum(S12_npv_infrastructure_cost_el)
    S12_total_environmental_el=sum(S12_npv_environmental_cost_el)
    S12_total_safety_el=sum(S12_npv_safety_cost_el)
    S12_total_cost_el=sum(S12_npv_total_cost_el)
    S12_total_infrastructre_br=sum(S12_npv_infrastructure_cost_br)
    S12_total_environmental_br=sum(S12_npv_environmental_cost_br)
    S12_total_safety_br=sum(S12_npv_safety_cost_br)
    S12_total_cost_br=sum(S12_npv_total_cost_br)
    S12_df_npv= pd.DataFrame({'lifecycle_infrastructure_el':[S12_total_infrastructre_el],
                             'environmental_restoration_el':[S12_total_environmental_el],
                             'safety_el':[S12_total_safety_el],
                             'total_cost_el':[S12_total_cost_el],
                             'lifecycle_infrastructure_br':[S12_total_infrastructre_br],
                             'environmental_restoration_br':[S12_total_environmental_br],
                             'safety_br':[S12_total_safety_br],
                             'total_cost_br':[S12_total_cost_br]},
                            )
    #S12_df_npv.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-npv-S12.csv', index = False) 
    # S13
    S13_npv_infrastructure_cost_el=[]
    S13_npv_environmental_cost_el=[]
    S13_npv_safety_cost_el=[]
    S13_npv_total_cost_el=[]
    S13_npv_infrastructure_cost_br=[]
    S13_npv_environmental_cost_br=[]
    S13_npv_safety_cost_br=[]
    S13_npv_total_cost_br=[]
    for index, row in df_analyze_result_S13.iterrows():
        S13_npv_infrastructure_cost_el.append(row['lifecycle_infrastructure_el']/(1+data.parameter_dict['r'])**index)
        S13_npv_environmental_cost_el.append(row['environmental_restoration_el']/(1+data.parameter_dict['r'])**index)
        S13_npv_safety_cost_el.append(row['safety_el']/(1+data.parameter_dict['r'])**index)
        S13_npv_total_cost_el.append(row['total_cost_el']/(1+data.parameter_dict['r'])**index)
        S13_npv_infrastructure_cost_br.append(row['lifecycle_infrastructure_br']/(1+data_broadband.parameter_dict['r'])**index)
        S13_npv_environmental_cost_br.append(row['environmental_restoration_br']/(1+data_broadband.parameter_dict['r'])**index)
        S13_npv_safety_cost_br.append(row['safety_br']/(1+data_broadband.parameter_dict['r'])**index)
        S13_npv_total_cost_br.append(row['total_cost_br']/(1+data_broadband.parameter_dict['r'])**index)
    S13_total_infrastructre_el=sum(S13_npv_infrastructure_cost_el)
    S13_total_environmental_el=sum(S13_npv_environmental_cost_el)
    S13_total_safety_el=sum(S13_npv_safety_cost_el)
    S13_total_cost_el=sum(S13_npv_total_cost_el)
    S13_total_infrastructre_br=sum(S13_npv_infrastructure_cost_br)
    S13_total_environmental_br=sum(S13_npv_environmental_cost_br)
    S13_total_safety_br=sum(S13_npv_safety_cost_br)
    S13_total_cost_br=sum(S13_npv_total_cost_br)
    S13_df_npv= pd.DataFrame({'lifecycle_infrastructure_el':[S13_total_infrastructre_el],
                             'environmental_restoration_el':[S13_total_environmental_el],
                             'safety_el':[S13_total_safety_el],
                             'total_cost_el':[S13_total_cost_el],
                             'lifecycle_infrastructure_br':[S13_total_infrastructre_br],
                             'environmental_restoration_br':[S13_total_environmental_br],
                             'safety_br':[S13_total_safety_br],
                             'total_cost_br':[S13_total_cost_br]},
                            )
    #S13_df_npv.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-npv-S13.csv', index = False) 

    #npv_cost= pd.DataFrame({'Strategy':['S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11','S12','S13'],
    #                        'lifecycle_infrastructure_el':[S1_df_npv['lifecycle_infrastructure_el'],S2_df_npv['lifecycle_infrastructure_el'],S3_df_npv['lifecycle_infrastructure_el'],S4_df_npv['lifecycle_infrastructure_el'],S5_df_npv['lifecycle_infrastructure_el'],S6_df_npv['lifecycle_infrastructure_el'],S7_df_npv['lifecycle_infrastructure_el'],S8_df_npv['lifecycle_infrastructure_el'],S9_df_npv['lifecycle_infrastructure_el'],S10_df_npv['lifecycle_infrastructure_el'],S11_df_npv['lifecycle_infrastructure_el'],S12_df_npv['lifecycle_infrastructure_el'],S13_df_npv['lifecycle_infrastructure_el']],
    #                        'environmental_restoration_el':[S1_df_npv['environmental_restoration_el'],S2_df_npv['environmental_restoration_el'],S3_df_npv['environmental_restoration_el'],S4_df_npv['environmental_restoration_el'],S5_df_npv['environmental_restoration_el'],S6_df_npv['environmental_restoration_el'],S7_df_npv['environmental_restoration_el'],S8_df_npv['environmental_restoration_el'],S9_df_npv['environmental_restoration_el'],S10_df_npv['environmental_restoration_el'],S11_df_npv['environmental_restoration_el'],S12_df_npv['environmental_restoration_el'],S13_df_npv['environmental_restoration_el']],
    #                        'safety_el':[S1_df_npv['safety_el'],S2_df_npv['safety_el'],S3_df_npv['safety_el'],S4_df_npv['safety_el'],S5_df_npv['safety_el'],S6_df_npv['safety_el'],S7_df_npv['safety_el'],S8_df_npv['safety_el'],S9_df_npv['safety_el'],S10_df_npv['safety_el'],S11_df_npv['safety_el'],S12_df_npv['safety_el'],S13_df_npv['safety_el']],
    #                        'total_cost_el':[S1_df_npv['total_cost_el'],S2_df_npv['total_cost_el'],S3_df_npv['total_cost_el'],S4_df_npv['total_cost_el'],S5_df_npv['total_cost_el'],S6_df_npv['total_cost_el'],S7_df_npv['total_cost_el'],S8_df_npv['total_cost_el'],S9_df_npv['total_cost_el'],S10_df_npv['total_cost_el'],S11_df_npv['total_cost_el'],S12_df_npv['total_cost_el'],S13_df_npv['total_cost_el']],
    #                        'lifecycle_infrastructure_br':[S1_df_npv['lifecycle_infrastructure_br'],S2_df_npv['lifecycle_infrastructure_br'],S3_df_npv['lifecycle_infrastructure_br'],S4_df_npv['lifecycle_infrastructure_br'],S5_df_npv['lifecycle_infrastructure_br'],S6_df_npv['lifecycle_infrastructure_br'],S7_df_npv['lifecycle_infrastructure_br'],S8_df_npv['lifecycle_infrastructure_br'],S9_df_npv['lifecycle_infrastructure_br'],S10_df_npv['lifecycle_infrastructure_br'],S11_df_npv['lifecycle_infrastructure_br'],S12_df_npv['lifecycle_infrastructure_br'],S13_df_npv['lifecycle_infrastructure_br']],
    #                        'environmental_restoration_br':[S1_df_npv['environmental_restoration_br'],S2_df_npv['environmental_restoration_br'],S3_df_npv['environmental_restoration_br'],S4_df_npv['environmental_restoration_br'],S5_df_npv['environmental_restoration_br'],S6_df_npv['environmental_restoration_br'],S7_df_npv['environmental_restoration_br'],S8_df_npv['environmental_restoration_br'],S9_df_npv['environmental_restoration_br'],S10_df_npv['environmental_restoration_br'],S11_df_npv['environmental_restoration_br'],S12_df_npv['environmental_restoration_br'],S13_df_npv['environmental_restoration_br']],
    #                        'safety_br':[S1_df_npv['safety_br'],S2_df_npv['safety_br'],S3_df_npv['safety_br'],S4_df_npv['safety_br'],S5_df_npv['safety_br'],S6_df_npv['safety_br'],S7_df_npv['safety_br'],S8_df_npv['safety_br'],S9_df_npv['safety_br'],S10_df_npv['safety_br'],S11_df_npv['safety_br'],S12_df_npv['safety_br'],S13_df_npv['safety_br']],
    #                        'total_cost_br':[S1_df_npv['total_cost_br'],S2_df_npv['total_cost_br'],S3_df_npv['total_cost_br'],S4_df_npv['total_cost_br'],S5_df_npv['total_cost_br'],S6_df_npv['total_cost_br'],S7_df_npv['total_cost_br'],S8_df_npv['total_cost_br'],S9_df_npv['total_cost_br'],S10_df_npv['total_cost_br'],S11_df_npv['total_cost_br'],S12_df_npv['total_cost_br'],S13_df_npv['total_cost_br']]},
    #                        )
    
    npv_cost = pd.DataFrame({
    'Strategy': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'],
    'lifecycle_infrastructure_el': [
        S1_df_npv['lifecycle_infrastructure_el'].iloc[0],
        S2_df_npv['lifecycle_infrastructure_el'].iloc[0],
        S3_df_npv['lifecycle_infrastructure_el'].iloc[0],
        S4_df_npv['lifecycle_infrastructure_el'].iloc[0],
        S5_df_npv['lifecycle_infrastructure_el'].iloc[0],
        S6_df_npv['lifecycle_infrastructure_el'].iloc[0],
        S7_df_npv['lifecycle_infrastructure_el'].iloc[0],
        S8_df_npv['lifecycle_infrastructure_el'].iloc[0],
        S9_df_npv['lifecycle_infrastructure_el'].iloc[0],
        S10_df_npv['lifecycle_infrastructure_el'].iloc[0],
        S11_df_npv['lifecycle_infrastructure_el'].iloc[0],
        S12_df_npv['lifecycle_infrastructure_el'].iloc[0],
        S13_df_npv['lifecycle_infrastructure_el'].iloc[0]
    ],
    'environmental_restoration_el': [
        S1_df_npv['environmental_restoration_el'].iloc[0],
        S2_df_npv['environmental_restoration_el'].iloc[0],
        S3_df_npv['environmental_restoration_el'].iloc[0],
        S4_df_npv['environmental_restoration_el'].iloc[0],
        S5_df_npv['environmental_restoration_el'].iloc[0],
        S6_df_npv['environmental_restoration_el'].iloc[0],
        S7_df_npv['environmental_restoration_el'].iloc[0],
        S8_df_npv['environmental_restoration_el'].iloc[0],
        S9_df_npv['environmental_restoration_el'].iloc[0],
        S10_df_npv['environmental_restoration_el'].iloc[0],
        S11_df_npv['environmental_restoration_el'].iloc[0],
        S12_df_npv['environmental_restoration_el'].iloc[0],
        S13_df_npv['environmental_restoration_el'].iloc[0]
    ],
    'safety_el': [
        S1_df_npv['safety_el'].iloc[0],
        S2_df_npv['safety_el'].iloc[0],
        S3_df_npv['safety_el'].iloc[0],
        S4_df_npv['safety_el'].iloc[0],
        S5_df_npv['safety_el'].iloc[0],
        S6_df_npv['safety_el'].iloc[0],
        S7_df_npv['safety_el'].iloc[0],
        S8_df_npv['safety_el'].iloc[0],
        S9_df_npv['safety_el'].iloc[0],
        S10_df_npv['safety_el'].iloc[0],
        S11_df_npv['safety_el'].iloc[0],
        S12_df_npv['safety_el'].iloc[0],
        S13_df_npv['safety_el'].iloc[0]
    ],
    'total_cost_el': [
        S1_df_npv['total_cost_el'].iloc[0],
        S2_df_npv['total_cost_el'].iloc[0],
        S3_df_npv['total_cost_el'].iloc[0],
        S4_df_npv['total_cost_el'].iloc[0],
        S5_df_npv['total_cost_el'].iloc[0],
        S6_df_npv['total_cost_el'].iloc[0],
        S7_df_npv['total_cost_el'].iloc[0],
        S8_df_npv['total_cost_el'].iloc[0],
        S9_df_npv['total_cost_el'].iloc[0],
        S10_df_npv['total_cost_el'].iloc[0],
        S11_df_npv['total_cost_el'].iloc[0],
        S12_df_npv['total_cost_el'].iloc[0],
        S13_df_npv['total_cost_el'].iloc[0]
    ],
    'lifecycle_infrastructure_br': [
        S1_df_npv['lifecycle_infrastructure_br'].iloc[0],
        S2_df_npv['lifecycle_infrastructure_br'].iloc[0],
        S3_df_npv['lifecycle_infrastructure_br'].iloc[0],
        S4_df_npv['lifecycle_infrastructure_br'].iloc[0],
        S5_df_npv['lifecycle_infrastructure_br'].iloc[0],
        S6_df_npv['lifecycle_infrastructure_br'].iloc[0],
        S7_df_npv['lifecycle_infrastructure_br'].iloc[0],
        S8_df_npv['lifecycle_infrastructure_br'].iloc[0],
        S9_df_npv['lifecycle_infrastructure_br'].iloc[0],
        S10_df_npv['lifecycle_infrastructure_br'].iloc[0],
        S11_df_npv['lifecycle_infrastructure_br'].iloc[0],
        S12_df_npv['lifecycle_infrastructure_br'].iloc[0],
        S13_df_npv['lifecycle_infrastructure_br'].iloc[0]
    ],
    'environmental_restoration_br': [
        S1_df_npv['environmental_restoration_br'].iloc[0],
        S2_df_npv['environmental_restoration_br'].iloc[0],
        S3_df_npv['environmental_restoration_br'].iloc[0],
        S4_df_npv['environmental_restoration_br'].iloc[0],
        S5_df_npv['environmental_restoration_br'].iloc[0],
        S6_df_npv['environmental_restoration_br'].iloc[0],
        S7_df_npv['environmental_restoration_br'].iloc[0],
        S8_df_npv['environmental_restoration_br'].iloc[0],
        S9_df_npv['environmental_restoration_br'].iloc[0],
        S10_df_npv['environmental_restoration_br'].iloc[0],
        S11_df_npv['environmental_restoration_br'].iloc[0],
        S12_df_npv['environmental_restoration_br'].iloc[0],
        S13_df_npv['environmental_restoration_br'].iloc[0]
    ],
    'safety_br': [
        S1_df_npv['safety_br'].iloc[0],
        S2_df_npv['safety_br'].iloc[0],
        S3_df_npv['safety_br'].iloc[0],
        S4_df_npv['safety_br'].iloc[0],
        S5_df_npv['safety_br'].iloc[0],
        S6_df_npv['safety_br'].iloc[0],
        S7_df_npv['safety_br'].iloc[0],
        S8_df_npv['safety_br'].iloc[0],
        S9_df_npv['safety_br'].iloc[0],
        S10_df_npv['safety_br'].iloc[0],
        S11_df_npv['safety_br'].iloc[0],
        S12_df_npv['safety_br'].iloc[0],
        S13_df_npv['safety_br'].iloc[0]
    ],
    'total_cost_br': [
        S1_df_npv['total_cost_br'].iloc[0],
        S2_df_npv['total_cost_br'].iloc[0],
        S3_df_npv['total_cost_br'].iloc[0],
        S4_df_npv['total_cost_br'].iloc[0],
        S5_df_npv['total_cost_br'].iloc[0],
        S6_df_npv['total_cost_br'].iloc[0],
        S7_df_npv['total_cost_br'].iloc[0],
        S8_df_npv['total_cost_br'].iloc[0],
        S9_df_npv['total_cost_br'].iloc[0],
        S10_df_npv['total_cost_br'].iloc[0],
        S11_df_npv['total_cost_br'].iloc[0],
        S12_df_npv['total_cost_br'].iloc[0],
        S13_df_npv['total_cost_br'].iloc[0]
    ]
})
    
    npv_cost.to_csv(r'../../results/outcomes/Cost/Analyze result/ npv_cost_inflation1percent.csv', index = False) 
    return([S1_total_infrastructre_el, S1_total_environmental_el, S1_total_safety_el, S1_total_cost_el, S1_total_infrastructre_br, S1_total_environmental_br, S1_total_safety_br, S1_total_cost_br])

## Benefits and losses
# Analyze result functions for benefits and losses based on S1 to S13 results
def aggregate_benefits_S1_to_S13(data, data_broadband):
    # S1
    df_output_S1=Simulate.run_benefit_simulation_S1(data, data_broadband)
    df_analyze_result_S1=df_output_S1.groupby(level=[0])[['aesthetic_benefit_el','economic_losses_el','aesthetic_benefit_br','economic_loss_br']].sum()
    df_analyze_result_S1.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S1.to_csv(r'../../results/outcomes/Benefit/Analyze result/benefit-analyze-result-S1.csv', index = False)
    # S2
    df_output_S2=Simulate.run_benefit_simulation_S2(data, data_broadband)
    df_analyze_result_S2=df_output_S2.groupby(level=[0])[['aesthetic_benefit_el','economic_losses_el','aesthetic_benefit_br','economic_loss_br']].sum()
    df_analyze_result_S2.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S2.to_csv(r'../../results/outcomes/Benefit/Analyze result/benefit-analyze-result-S2.csv', index = False)
    # S3
    df_output_S3=Simulate.run_benefit_simulation_S3(data, data_broadband)
    df_analyze_result_S3=df_output_S3.groupby(level=[0])[['aesthetic_benefit_el','economic_losses_el','aesthetic_benefit_br','economic_loss_br']].sum()
    df_analyze_result_S3.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S3.to_csv(r'../../results/outcomes/Benefit/Analyze result/benefit-analyze-result-S3.csv', index = False)
    # S4
    df_output_S4=Simulate.run_benefit_simulation_S4(data, data_broadband)
    df_analyze_result_S4=df_output_S4.groupby(level=[0])[['aesthetic_benefit_el','economic_losses_el','aesthetic_benefit_br','economic_loss_br']].sum()
    df_analyze_result_S4.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S4.to_csv(r'../../results/outcomes/Benefit/Analyze result/benefit-analyze-result-S4.csv', index = False)
    # S5
    df_output_S5=Simulate.run_benefit_simulation_S5(data, data_broadband)
    df_analyze_result_S5=df_output_S5.groupby(level=[0])[['aesthetic_benefit_el','economic_losses_el','aesthetic_benefit_br','economic_loss_br']].sum()
    df_analyze_result_S5.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S5.to_csv(r'../../results/outcomes/Benefit/Analyze result/benefit-analyze-result-S5.csv', index = False)
    # S6-S9
    df_output_S6=Simulate.run_benefit_simulation_S6_to_s9(data, data_broadband)
    df_analyze_result_S6=df_output_S6.groupby(level=[0])[['aesthetic_benefit_el','economic_losses_el','aesthetic_benefit_br','economic_loss_br']].sum()
    df_analyze_result_S6.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S6.to_csv(r'../../results/outcomes/Benefit/Analyze result/benefit-analyze-result-S6.csv', index = False)
    # S10-S13
    df_output_S10=Simulate.run_benefit_simulation_S10_to_s13(data, data_broadband)
    df_analyze_result_S10=df_output_S10.groupby(level=[0])[['aesthetic_benefit_el','economic_losses_el','aesthetic_benefit_br','economic_loss_br']].sum()
    df_analyze_result_S10.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    #df_analyze_result_S10.to_csv(r'../../results/outcomes/Benefit/Analyze result/benefit-analyze-result-S10.csv', index = False)
    return(df_analyze_result_S1, df_analyze_result_S2, df_analyze_result_S3, df_analyze_result_S4, df_analyze_result_S5, df_analyze_result_S6, df_analyze_result_S10)


# Calculate net present values of benefits and losses for S1 to S13
def calculate_benefits_npv_S1_to_S13(data, data_broadband):
    df_analyze_result_S1, df_analyze_result_S2, df_analyze_result_S3, df_analyze_result_S4, df_analyze_result_S5, df_analyze_result_S6, df_analyze_result_S10=aggregate_benefits_S1_to_S13(data, data_broadband)    
    # S1
    S1_npv_aesthetic_benefit_el=[]
    S1_npv_economic_losses_el=[]
    S1_npv_aesthetic_benefit_br=[]
    S1_npv_economic_loss_br=[]
    for index, row in df_analyze_result_S1.iterrows():
        S1_npv_aesthetic_benefit_el.append(row['aesthetic_benefit_el']/(1+data.parameter_dict['r'])**index)
        S1_npv_economic_losses_el.append(row['economic_losses_el']/(1+data.parameter_dict['r'])**index)
        S1_npv_aesthetic_benefit_br.append(row['aesthetic_benefit_br']/(1+data_broadband.parameter_dict['r'])**index)
        S1_npv_economic_loss_br.append(row['economic_loss_br']/(1+data_broadband.parameter_dict['r'])**index)
    S1_total_aesthetic_benefit_el=sum(S1_npv_aesthetic_benefit_el)
    S1_total_economic_losses_el=sum(S1_npv_economic_losses_el)
    S1_total_aesthetic_benefit_br=sum(S1_npv_aesthetic_benefit_br)
    S1_total_economic_loss_br=sum(S1_npv_economic_loss_br)
    S1_df_npv= pd.DataFrame({'aesthetic_benefit_el':[S1_total_aesthetic_benefit_el],
                             'economic_losses_el':[S1_total_economic_losses_el],
                             'aesthetic_benefit_br':[S1_total_aesthetic_benefit_br],
                             'economic_loss_br':[S1_total_economic_loss_br]},
                            )
    #S1_df_npv.to_csv(r'../../results/outcomes/Benefit/Analyze result/benefit-npv-S1.csv', index = False)
    # S2
    S2_npv_aesthetic_benefit_el=[]
    S2_npv_economic_losses_el=[]
    S2_npv_aesthetic_benefit_br=[]
    S2_npv_economic_loss_br=[]
    for index, row in df_analyze_result_S2.iterrows():
        S2_npv_aesthetic_benefit_el.append(row['aesthetic_benefit_el']/(1+data.parameter_dict['r'])**index)
        S2_npv_economic_losses_el.append(row['economic_losses_el']/(1+data.parameter_dict['r'])**index)
        S2_npv_aesthetic_benefit_br.append(row['aesthetic_benefit_br']/(1+data_broadband.parameter_dict['r'])**index)
        S2_npv_economic_loss_br.append(row['economic_loss_br']/(1+data_broadband.parameter_dict['r'])**index)
    S2_total_aesthetic_benefit_el=sum(S2_npv_aesthetic_benefit_el)
    S2_total_economic_losses_el=sum(S2_npv_economic_losses_el)
    S2_total_aesthetic_benefit_br=sum(S2_npv_aesthetic_benefit_br)
    S2_total_economic_loss_br=sum(S2_npv_economic_loss_br)
    S2_df_npv= pd.DataFrame({'aesthetic_benefit_el':[S2_total_aesthetic_benefit_el],
                             'economic_losses_el':[S2_total_economic_losses_el],
                             'aesthetic_benefit_br':[S2_total_aesthetic_benefit_br],
                             'economic_loss_br':[S2_total_economic_loss_br]},
                            )
    #S2_df_npv.to_csv(r'../../results/outcomes/Benefit/Analyze result/benefit-npv-S2.csv', index = False)
    # S3
    S3_npv_aesthetic_benefit_el=[]
    S3_npv_economic_losses_el=[]
    S3_npv_aesthetic_benefit_br=[]
    S3_npv_economic_loss_br=[]
    for index, row in df_analyze_result_S3.iterrows():
        S3_npv_aesthetic_benefit_el.append(row['aesthetic_benefit_el']/(1+data.parameter_dict['r'])**index)
        S3_npv_economic_losses_el.append(row['economic_losses_el']/(1+data.parameter_dict['r'])**index)
        S3_npv_aesthetic_benefit_br.append(row['aesthetic_benefit_br']/(1+data_broadband.parameter_dict['r'])**index)
        S3_npv_economic_loss_br.append(row['economic_loss_br']/(1+data_broadband.parameter_dict['r'])**index)
    S3_total_aesthetic_benefit_el=sum(S3_npv_aesthetic_benefit_el)
    S3_total_economic_losses_el=sum(S3_npv_economic_losses_el)
    S3_total_aesthetic_benefit_br=sum(S3_npv_aesthetic_benefit_br)
    S3_total_economic_loss_br=sum(S3_npv_economic_loss_br)
    S3_df_npv= pd.DataFrame({'aesthetic_benefit_el':[S3_total_aesthetic_benefit_el],
                             'economic_losses_el':[S3_total_economic_losses_el],
                             'aesthetic_benefit_br':[S3_total_aesthetic_benefit_br],
                             'economic_loss_br':[S3_total_economic_loss_br]},
                            )
    #S3_df_npv.to_csv(r'../../results/outcomes/Benefit/Analyze result/benefit-npv-S3.csv', index = False)
    # S4
    S4_npv_aesthetic_benefit_el=[]
    S4_npv_economic_losses_el=[]
    S4_npv_aesthetic_benefit_br=[]
    S4_npv_economic_loss_br=[]
    for index, row in df_analyze_result_S4.iterrows():
        S4_npv_aesthetic_benefit_el.append(row['aesthetic_benefit_el']/(1+data.parameter_dict['r'])**index)
        S4_npv_economic_losses_el.append(row['economic_losses_el']/(1+data.parameter_dict['r'])**index)
        S4_npv_aesthetic_benefit_br.append(row['aesthetic_benefit_br']/(1+data_broadband.parameter_dict['r'])**index)
        S4_npv_economic_loss_br.append(row['economic_loss_br']/(1+data_broadband.parameter_dict['r'])**index)
    S4_total_aesthetic_benefit_el=sum(S4_npv_aesthetic_benefit_el)
    S4_total_economic_losses_el=sum(S4_npv_economic_losses_el)
    S4_total_aesthetic_benefit_br=sum(S4_npv_aesthetic_benefit_br)
    S4_total_economic_loss_br=sum(S4_npv_economic_loss_br)
    S4_df_npv= pd.DataFrame({'aesthetic_benefit_el':[S4_total_aesthetic_benefit_el],
                             'economic_losses_el':[S4_total_economic_losses_el],
                             'aesthetic_benefit_br':[S4_total_aesthetic_benefit_br],
                             'economic_loss_br':[S4_total_economic_loss_br]},
                            )
    #S4_df_npv.to_csv(r'../../results/outcomes/Benefit/Analyze result/benefit-npv-S4.csv', index = False)
    # S5
    S5_npv_aesthetic_benefit_el=[]
    S5_npv_economic_losses_el=[]
    S5_npv_aesthetic_benefit_br=[]
    S5_npv_economic_loss_br=[]
    for index, row in df_analyze_result_S5.iterrows():
        S5_npv_aesthetic_benefit_el.append(row['aesthetic_benefit_el']/(1+data.parameter_dict['r'])**index)
        S5_npv_economic_losses_el.append(row['economic_losses_el']/(1+data.parameter_dict['r'])**index)
        S5_npv_aesthetic_benefit_br.append(row['aesthetic_benefit_br']/(1+data_broadband.parameter_dict['r'])**index)
        S5_npv_economic_loss_br.append(row['economic_loss_br']/(1+data_broadband.parameter_dict['r'])**index)
    S5_total_aesthetic_benefit_el=sum(S5_npv_aesthetic_benefit_el)
    S5_total_economic_losses_el=sum(S5_npv_economic_losses_el)
    S5_total_aesthetic_benefit_br=sum(S5_npv_aesthetic_benefit_br)
    S5_total_economic_loss_br=sum(S5_npv_economic_loss_br)
    S5_df_npv= pd.DataFrame({'aesthetic_benefit_el':[S5_total_aesthetic_benefit_el],
                             'economic_losses_el':[S5_total_economic_losses_el],
                             'aesthetic_benefit_br':[S5_total_aesthetic_benefit_br],
                             'economic_loss_br':[S5_total_economic_loss_br]},
                            )
    #S5_df_npv.to_csv(r'../../results/outcomes/Benefit/Analyze result/benefit-npv-S5.csv', index = False)
    # S6
    S6_npv_aesthetic_benefit_el=[]
    S6_npv_economic_losses_el=[]
    S6_npv_aesthetic_benefit_br=[]
    S6_npv_economic_loss_br=[]
    for index, row in df_analyze_result_S6.iterrows():
        S6_npv_aesthetic_benefit_el.append(row['aesthetic_benefit_el']/(1+data.parameter_dict['r'])**index)
        S6_npv_economic_losses_el.append(row['economic_losses_el']/(1+data.parameter_dict['r'])**index)
        S6_npv_aesthetic_benefit_br.append(row['aesthetic_benefit_br']/(1+data_broadband.parameter_dict['r'])**index)
        S6_npv_economic_loss_br.append(row['economic_loss_br']/(1+data_broadband.parameter_dict['r'])**index)
    S6_total_aesthetic_benefit_el=sum(S6_npv_aesthetic_benefit_el)
    S6_total_economic_losses_el=sum(S6_npv_economic_losses_el)
    S6_total_aesthetic_benefit_br=sum(S6_npv_aesthetic_benefit_br)
    S6_total_economic_loss_br=sum(S6_npv_economic_loss_br)
    S6_df_npv= pd.DataFrame({'aesthetic_benefit_el':[S6_total_aesthetic_benefit_el],
                             'economic_losses_el':[S6_total_economic_losses_el],
                             'aesthetic_benefit_br':[S6_total_aesthetic_benefit_br],
                             'economic_loss_br':[S6_total_economic_loss_br]},
                            )
    #S6_df_npv.to_csv(r'../../results/outcomes/Benefit/Analyze result/benefit-npv-S6.csv', index = False)
    # S10
    S10_npv_aesthetic_benefit_el=[]
    S10_npv_economic_losses_el=[]
    S10_npv_aesthetic_benefit_br=[]
    S10_npv_economic_loss_br=[]
    for index, row in df_analyze_result_S10.iterrows():
        S10_npv_aesthetic_benefit_el.append(row['aesthetic_benefit_el']/(1+data.parameter_dict['r'])**index)
        S10_npv_economic_losses_el.append(row['economic_losses_el']/(1+data.parameter_dict['r'])**index)
        S10_npv_aesthetic_benefit_br.append(row['aesthetic_benefit_br']/(1+data_broadband.parameter_dict['r'])**index)
        S10_npv_economic_loss_br.append(row['economic_loss_br']/(1+data_broadband.parameter_dict['r'])**index)
    S10_total_aesthetic_benefit_el=sum(S10_npv_aesthetic_benefit_el)
    S10_total_economic_losses_el=sum(S10_npv_economic_losses_el)
    S10_total_aesthetic_benefit_br=sum(S10_npv_aesthetic_benefit_br)
    S10_total_economic_loss_br=sum(S10_npv_economic_loss_br)
    S10_df_npv= pd.DataFrame({'aesthetic_benefit_el':[S10_total_aesthetic_benefit_el],
                             'economic_losses_el':[S10_total_economic_losses_el],
                             'aesthetic_benefit_br':[S10_total_aesthetic_benefit_br],
                             'economic_loss_br':[S10_total_economic_loss_br]},
                            )
    #S10_df_npv.to_csv(r'../../results/outcomes/Benefit/Analyze result/benefit-npv-S10.csv', index = False)

    npv_benefit = pd.DataFrame({
    'Strategy': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S10'],
    'aesthetic_benefit_el': [
        S1_df_npv['aesthetic_benefit_el'].iloc[0],
        S2_df_npv['aesthetic_benefit_el'].iloc[0],
        S3_df_npv['aesthetic_benefit_el'].iloc[0],
        S4_df_npv['aesthetic_benefit_el'].iloc[0],
        S5_df_npv['aesthetic_benefit_el'].iloc[0],
        S6_df_npv['aesthetic_benefit_el'].iloc[0],
        S10_df_npv['aesthetic_benefit_el'].iloc[0]
    ],
    'economic_losses_el': [
        S1_df_npv['economic_losses_el'].iloc[0],
        S2_df_npv['economic_losses_el'].iloc[0],
        S3_df_npv['economic_losses_el'].iloc[0],
        S4_df_npv['economic_losses_el'].iloc[0],
        S5_df_npv['economic_losses_el'].iloc[0],
        S6_df_npv['economic_losses_el'].iloc[0],
        S10_df_npv['economic_losses_el'].iloc[0]
    ],
    'aesthetic_benefit_br': [
        S1_df_npv['aesthetic_benefit_br'].iloc[0],
        S2_df_npv['aesthetic_benefit_br'].iloc[0],
        S3_df_npv['aesthetic_benefit_br'].iloc[0],
        S4_df_npv['aesthetic_benefit_br'].iloc[0],
        S5_df_npv['aesthetic_benefit_br'].iloc[0],
        S6_df_npv['aesthetic_benefit_br'].iloc[0],
        S10_df_npv['aesthetic_benefit_br'].iloc[0]
    ],
    'economic_loss_br': [
        S1_df_npv['economic_loss_br'].iloc[0],
        S2_df_npv['economic_loss_br'].iloc[0],
        S3_df_npv['economic_loss_br'].iloc[0],
        S4_df_npv['economic_loss_br'].iloc[0],
        S5_df_npv['economic_loss_br'].iloc[0],
        S6_df_npv['economic_loss_br'].iloc[0],
        S10_df_npv['economic_loss_br'].iloc[0]
    ]
})

    npv_benefit.to_csv(r'../../results/outcomes/Benefit/Analyze result/ npv_benefit_VLL_B_R7.csv', index = False) 
    return([S10_total_aesthetic_benefit_el, S10_total_economic_losses_el, S10_total_aesthetic_benefit_br, S10_total_economic_loss_br])





### Test
def test1(data, data_broadband):
   # S3
    df_output_S3=Simulate.run_cost_simulation_S3(data, data_broadband)
    df_analyze_result_S3=df_output_S3.groupby(level=[0])[['capex_el','opex_el','lifecycle_infrastructure_el','environmental_restoration_el','non_fatal_el','fatal_el','safety_el','total_cost_el','capex_br','opex_br','lifecycle_infrastructure_br','environmental_restoration_br','non_fatal_br','fatal_br','safety_br','total_cost_br']].sum()
    df_analyze_result_S3.insert(0, "year", range(data.parameter_dict['analysis_years']), True)
    df_analyze_result_S3.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-analyze-result-S3.csv', index = False)
    return df_analyze_result_S3





def test2(data, data_broadband):
    df_analyze_result_S12,  df_analyze_result_S13=test1(data, data_broadband)    
    # S12
    S12_npv_infrastructure_cost_el=[]
    S12_npv_environmental_cost_el=[]
    S12_npv_safety_cost_el=[]
    S12_npv_total_cost_el=[]
    S12_npv_infrastructure_cost_br=[]
    S12_npv_environmental_cost_br=[]
    S12_npv_safety_cost_br=[]
    S12_npv_total_cost_br=[]
    for index, row in df_analyze_result_S12.iterrows():
        S12_npv_infrastructure_cost_el.append(row['lifecycle_infrastructure_el']/(1+data.parameter_dict['r'])**index)
        S12_npv_environmental_cost_el.append(row['environmental_restoration_el']/(1+data.parameter_dict['r'])**index)
        S12_npv_safety_cost_el.append(row['safety_el']/(1+data.parameter_dict['r'])**index)
        S12_npv_total_cost_el.append(row['total_cost_el']/(1+data.parameter_dict['r'])**index)
        S12_npv_infrastructure_cost_br.append(row['lifecycle_infrastructure_br']/(1+data_broadband.parameter_dict['r'])**index)
        S12_npv_environmental_cost_br.append(row['environmental_restoration_br']/(1+data_broadband.parameter_dict['r'])**index)
        S12_npv_safety_cost_br.append(row['safety_br']/(1+data_broadband.parameter_dict['r'])**index)
        S12_npv_total_cost_br.append(row['total_cost_br']/(1+data_broadband.parameter_dict['r'])**index)
    S12_total_infrastructre_el=sum(S12_npv_infrastructure_cost_el)
    S12_total_environmental_el=sum(S12_npv_environmental_cost_el)
    S12_total_safety_el=sum(S12_npv_safety_cost_el)
    S12_total_cost_el=sum(S12_npv_total_cost_el)
    S12_total_infrastructre_br=sum(S12_npv_infrastructure_cost_br)
    S12_total_environmental_br=sum(S12_npv_environmental_cost_br)
    S12_total_safety_br=sum(S12_npv_safety_cost_br)
    S12_total_cost_br=sum(S12_npv_total_cost_br)
    S12_df_npv= pd.DataFrame({'lifecycle_infrastructure_el':[S12_total_infrastructre_el],
                             'environmental_restoration_el':[S12_total_environmental_el],
                             'safety_el':[S12_total_safety_el],
                             'total_cost_el':[S12_total_cost_el],
                             'lifecycle_infrastructure_br':[S12_total_infrastructre_br],
                             'environmental_restoration_br':[S12_total_environmental_br],
                             'safety_br':[S12_total_safety_br],
                             'total_cost_br':[S12_total_cost_br]},
                            )
    S12_df_npv.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-npv-S12.csv', index = False) 
    # S13
    S13_npv_infrastructure_cost_el=[]
    S13_npv_environmental_cost_el=[]
    S13_npv_safety_cost_el=[]
    S13_npv_total_cost_el=[]
    S13_npv_infrastructure_cost_br=[]
    S13_npv_environmental_cost_br=[]
    S13_npv_safety_cost_br=[]
    S13_npv_total_cost_br=[]
    for index, row in df_analyze_result_S13.iterrows():
        S13_npv_infrastructure_cost_el.append(row['lifecycle_infrastructure_el']/(1+data.parameter_dict['r'])**index)
        S13_npv_environmental_cost_el.append(row['environmental_restoration_el']/(1+data.parameter_dict['r'])**index)
        S13_npv_safety_cost_el.append(row['safety_el']/(1+data.parameter_dict['r'])**index)
        S13_npv_total_cost_el.append(row['total_cost_el']/(1+data.parameter_dict['r'])**index)
        S13_npv_infrastructure_cost_br.append(row['lifecycle_infrastructure_br']/(1+data_broadband.parameter_dict['r'])**index)
        S13_npv_environmental_cost_br.append(row['environmental_restoration_br']/(1+data_broadband.parameter_dict['r'])**index)
        S13_npv_safety_cost_br.append(row['safety_br']/(1+data_broadband.parameter_dict['r'])**index)
        S13_npv_total_cost_br.append(row['total_cost_br']/(1+data_broadband.parameter_dict['r'])**index)
    S13_total_infrastructre_el=sum(S13_npv_infrastructure_cost_el)
    S13_total_environmental_el=sum(S13_npv_environmental_cost_el)
    S13_total_safety_el=sum(S13_npv_safety_cost_el)
    S13_total_cost_el=sum(S13_npv_total_cost_el)
    S13_total_infrastructre_br=sum(S13_npv_infrastructure_cost_br)
    S13_total_environmental_br=sum(S13_npv_environmental_cost_br)
    S13_total_safety_br=sum(S13_npv_safety_cost_br)
    S13_total_cost_br=sum(S13_npv_total_cost_br)
    S13_df_npv= pd.DataFrame({'lifecycle_infrastructure_el':[S13_total_infrastructre_el],
                             'environmental_restoration_el':[S13_total_environmental_el],
                             'safety_el':[S13_total_safety_el],
                             'total_cost_el':[S13_total_cost_el],
                             'lifecycle_infrastructure_br':[S13_total_infrastructre_br],
                             'environmental_restoration_br':[S13_total_environmental_br],
                             'safety_br':[S13_total_safety_br],
                             'total_cost_br':[S13_total_cost_br]},
                            )
    S13_df_npv.to_csv(r'../../results/outcomes/Cost/Analyze result/cost-npv-S13.csv', index = False) 

    return([S12_total_infrastructre_el, ])