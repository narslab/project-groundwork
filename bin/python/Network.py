# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
###Importing required libraries
import numpy as np
import random
###

class model_inputs:
    ###Model Variables and Parameters
    def __init__(self):
        self.parameter_dict = {
            "analysis_years":40, #Analysis_years
            "average_age":20, # Average ages in base year for underground and overhead distribution lines (in years)
            "age_shape":10, # We selected age shape and scale in a way that age_shape*age_scale=average_age
            "age_scale":2,  # We selected age shape and scale in a way that length_shape*age scale=average_length
            "length_shape":2, # We selected length shape and scale in a way that length_shape*length_age=average_length
            "length_scale":0.25, # We selected length shape and scale in a way that length_shape*length_age=average_length
            "average_length":0.5, # Average length for underground and overhead distribution lines (in miles)
            "segment_number":625, # Numbers of line segments in the network (Shrewsbury has 191.5 miles overhead, 121.7 miles underground line, eaach segment's length is considered about 0.5 miles. So by dividing (91.5+121.7)/.5 we calculated this parameter.
            "baseyear":2021, #the year in which we are going to start conducting cost analysis 
            "underground_baseyear":121, #Length of undergeound lines in miles in base year
            "overhead_baseyear":191, #Length of overhead lines in miles in base year
            "r":0.1, # Discount rate=10%
            "easment_value":3000, # per-acre price of a conservation easement
            "nfir":2100, # Non-fatality incidence rates, number of accidents per 100000 workers
            "fir":15, # Fatality incidence rates, number of accidents per 100000 workers 
            "employees":8514/255, #The number of IOU employees
            "injurycost":130658, # A randomly determined annual injury cost, per accident
            "vsl":6900000,#The value of a statistical life
            "overhead_proportion":0.66, #The value showing the proportion of underground lines in Shrewsbury
            "overhead_line":{'lifespan':60,'replcost':104000,'replcost_growth_rate':0,'om_growth_rate':0.05,'om_percentage_replcost':0.005,'corridor_length':60},
            "underground_line":{'lifespan':40,'replcost':357000,'replcost_growth_rate':0,'om_growth_rate':0.05,'om_percentage_replcost':0.005,'corridor_length':120,'over_under_raplcost':357000},
            "SAIDI_overhead": 5.72, #in hours #0.66x + 0.34y = 4.17, and y = 0.2x --> which is the current SAIDI for MASS according to patch.com
            "SAIDI_underground": 1.15, #0.66 is the percentage of overhead lines in Shrewsbury, MA and 0.34 is the percentage of undergrounded lines, taking into consideration our assumption that 80% of outages happen via overhead lines and 20% due to unerground lines
            #Dollar Amount Lost per Customer Hour Interruption in Shrewsbury in 2019, costs from 2.1 Estimating customer interruption costs using customer interruption cost surveys, page 21: https://eta-publications.lbl.gov/sites/default/files/hybrid_paper_final_22feb2021.pdf
            "USD_per_Customer_Hour_Interruption_Residential":4.2,
            "USD_per_Customer_Hour_Interruption_Commercial":1260,
            "USD_per_Customer_Hour_Interruption_Industry":42600,

            #Number of Customers in Each Sector in Shrewsbury Municipal Electric (SELCO) in 2019
            "Total_Customers_Residential_Shrewsbury":14633,
            "Total_Customers_Commercial_Shrewsbury":1541,
            "Total_Customers_Industry_Shrewsbury":122,
            "total_length":326.21997, #summation of underground and overhead miles generated based on gamma simulation
            "total_length_overhead":227.3577026, #summation of overhead miles generated based on gamma simulation
            "total_length_underground":98.86226968, #summation of underground miles generated based on gamma simulation}
            "Shrewsbury_tax_levy_2021": 85713912.0,
            "aesthetic_benefit_percentage":0.03
            }
    #Assigning overhead and underground line's specification (parameters) as a dictionary
    
    #lifespan=Useful lifespan of overhead line and underground lines
    #replcost=Cost associated with replacing a line with the same line type after it reaches its life span. 
    #replcost_growth_rate= replacement cost annual growth/decay rate 
    # om_percentage_replcost= percentage of the overall replacement costs which equals to annual O&M expenses (OPEX) for each type of line
    # corridor_length= length of the corridor in feet needed for calculating environmental cost.
    # over_under_raplcost= replacement cost associated with replacing an overhead line with an underground line.
    ###   
    
    #def modify_parameter(self,parameter, percentage_change):
    #    original_param = self.parameter_dict[parameter]
    #    new_param=self.parameter_dict[parameter] = (1+percentage_change) * (original_param)
    #    return (new_param)
    
    def modify_parameter(self,parameter,percentage_change, required_key=None):
        new_param=0
        if isinstance(self.parameter_dict[parameter], dict):
            original_param = self.parameter_dict[parameter][required_key]
            new_param= (1+(percentage_change/100))*(original_param)
            self.parameter_dict[parameter][required_key] = new_param
        else:
            original_param = self.parameter_dict[parameter]
            new_param=(1+(percentage_change/100.)) * (original_param)
            self.parameter_dict[parameter] = new_param      
        print("Original parameter: ", original_param)
        print("New parameter: ", new_param)  
        return (new_param)
        #if k == required_key:
        #    d[k] = new_value
    


###Defining Line segment class with required attributes and methods and these methods are going to be modified based on requirements for each strategies in the simulations.
class Line_segment:
    ## The __init__ function as the constructor, which assigns random length, age and underground status for the base year to each line segment.
    #data=model_inputs()
    def __init__(self, inputs): 
        self.inputs = inputs
        self.age = [np.random.gamma(self.inputs.parameter_dict['age_shape'], self.inputs.parameter_dict['age_scale'])] # set the age as a list, which can be dynamically expanded
        self.length = np.random.gamma(self.inputs.parameter_dict['length_shape'],self.inputs.parameter_dict['length_scale']) # we can assume the length is fixed over time
        overhead_probability = random.uniform(0,1)
        if overhead_probability > self.inputs.parameter_dict['overhead_proportion']: # if underground = 0, then segment is overhead.
            self.underground = [1] # again, a dynamic list.
        else:
            self.underground = [0]
        if self.underground[0]==1:
            self.replcost_rate=[self.inputs.parameter_dict['underground_line']['replcost']]
        else:
            self.replcost_rate=[self.inputs.parameter_dict['overhead_line']['replcost']]       
        self.capex=[0]
        self.opex=[self.calculate_opex()]
        self.total_infra=[self.calculate_opex()]
        self.environmental_restoration=[0]
        self.non_fatal=[0]
        self.fatal=[0]
        self.total_safety=[0]
        self.total=[self.calculate_opex()]
        self.residential_benefit=[0]
        self.commercial_benefit=[0]
        self.industry_benefit=[0]
        self.total_economic_benefits = [0]
        self.total_aesthetic_benefits=[0]
        
    ###Lifecycle Infrastructure Costs:
    # Add one year to the age of line segment,compare it to the lifespan, starts from 1 when reaches to lifespan and append this age to age list.                  
    def update_age(self,replace=False):
        if self.underground[-1]==1:
            lifespan_current= int(self.inputs.parameter_dict['underground_line']['lifespan'])
        else:
            lifespan_current= int(self.inputs.parameter_dict['overhead_line']['lifespan'])
        age_current=self.age[-1]
        if age_current>lifespan_current:
            self.age.append(1)
            replace=True
        else:
            age_current+=1
            self.age.append(age_current)
            replace=False
        return(replace)
    
    # Add underground status based on if convert is true or not to self.underground list.                  
    def update_underground_status(self,convert=False):
        status=self.underground[0]
        if convert==True:
            if status==0:
                status+=1
            else:
                status=self.underground[0]
        else:
            status=self.underground[0]
        self.underground.append(status)
            
        
    #Add interest rate to the replacement cost and also cansider different replacementcost rate when underground=1        
    def add_replcost_intrest_rate(self):
        underground_current=self.underground[-1]
        underground_baseyear=self.underground[0]
        if underground_current==1:
            replcost_growth_rate_current=self.inputs.parameter_dict['underground_line']['replcost_growth_rate']
        else:
            replcost_growth_rate_current=self.inputs.parameter_dict['overhead_line']['replcost_growth_rate']
        if underground_current==underground_baseyear:        
            replcost_new=(self.replcost_rate[-1])+((replcost_growth_rate_current)*(self.replcost_rate[-1]))
            self.replcost_rate.append(replcost_new)
        else:
            replcost_new=self.inputs.parameter_dict['underground_line']['replcost']*((1+replcost_growth_rate_current)**(len(self.underground)-1))
            self.replcost_rate.append(replcost_new)
        return(self.replcost_rate)
    
    #Determine capital expenses which is replacement cost for each line segment based on the rate of replacement cost in that year and length of the circuit.
    def calculate_capex(self):
        if (self.age[-1])==1:
            length_current=self.length
            replcost_rate_current=self.replcost_rate[-1]
            replcost_new=(replcost_rate_current)*(length_current)
            self.capex.append(replcost_new)
        else:
            replcost_new=0
            self.capex.append(replcost_new)
        return(self.capex)
    
    #Determin operation and maintanace expenses which is a fraction of replacement rate for each circuit.
    def calculate_opex(self):
        underground_current=self.underground[-1]
        if underground_current==1:
            om_percentage_replcost_current=self.inputs.parameter_dict['underground_line']['om_percentage_replcost']
        else:
            om_percentage_replcost_current=self.inputs.parameter_dict['overhead_line']['om_percentage_replcost']
        length_current=self.length
        replcost_rate_current=self.replcost_rate[-1]
        opex=(om_percentage_replcost_current)*(length_current)*(replcost_rate_current)
        #opex_new=opex[-1]+om_growth_rate*opex[-1]
        #self.opex.append(opex)
        return(opex) 
  
    #Add interest rate to opex.
    def add_opex_interest_rate(self):
        underground_current=self.underground[-1]
        if underground_current==1:
            om_growth_rate=self.inputs.parameter_dict['underground_line']['om_growth_rate']
        else:
            om_growth_rate=self.inputs.parameter_dict['overhead_line']['om_growth_rate']
        opex_new=self.opex[-1]+(self.opex[-1]*om_growth_rate)
        self.opex.append(opex_new)
        return(self.opex)
    
    #Sum capex and opex.
    def calculate_total_infrastructure_cost(self):
        total_infra_new=self.capex[-1]+self.opex[-1]
        self.total_infra.append(total_infra_new)
        return (self.total_infra)

    #Determin the first retirement year
    def determine_first_retire(self):
        age_baseyear=self.age[0]
        underground=self.underground[0]
        if underground==0:
            lifespan_x=self.inputs.parameter_dict['overhead_line']['lifespan']
        elif underground==1:
            lifespan_x=self.inputs.parameter_dict['underground_line']['lifespan']
        first_retire=(lifespan_x)-(age_baseyear)
        return (np.ceil (first_retire))
 
    ###Environmental Costs:
    #Determin environmental restoration cost based on the length of overhead and underground lines. (1mile= 5280 foot, 1sqmile=640 Acre) 
    def calculate_environmental_restoration(self):
        environmental_restoration_current=0
        if self.underground[-1]==1:
            if self.underground[0]==1:
                corridor_length=self.inputs.parameter_dict['overhead_line']['corridor_length']
                self.environmental_restoration.append(environmental_restoration_current)
            else:
                corridor_length=self.inputs.parameter_dict['underground_line']['corridor_length']-self.inputs.parameter_dict['overhead_line']['corridor_length']
                environmental_restoration_current=((self.length)*(corridor_length)*640/5280*self.inputs.parameter_dict['easment_value'])
                self.environmental_restoration.append(environmental_restoration_current)
        else:
            corridor_length=self.inputs.parameter_dict['underground_line']['corridor_length']
            self.environmental_restoration.append(environmental_restoration_current)
        return(self.environmental_restoration)

    
    ###Safety and health Costs:
    #Return fatal cost which is one element of safety cost
    def calculate_non_fatal_cost(self):
        if self.underground[-1]==1:
            if self.underground[0]==1:
                self.non_fatal.append((self.length/(self.inputs.parameter_dict['underground_baseyear']+self.inputs.parameter_dict['overhead_baseyear']))*(self.inputs.parameter_dict['nfir'])*(self.inputs.parameter_dict['employees']/100000)*(self.inputs.parameter_dict['injurycost']))
            else:
                self.non_fatal.append(((1+self.length)/1)*(self.length/(self.inputs.parameter_dict['underground_baseyear']+self.inputs.parameter_dict['overhead_baseyear']))*(self.inputs.parameter_dict['nfir'])*(self.inputs.parameter_dict['employees']/100000)*(self.inputs.parameter_dict['injurycost']))
        else:
            self.non_fatal.append((self.length/(self.inputs.parameter_dict['underground_baseyear']+self.inputs.parameter_dict['overhead_baseyear']))*(self.inputs.parameter_dict['nfir'])*(self.inputs.parameter_dict['employees']/100000)*(self.inputs.parameter_dict['injurycost']))
        return(self.non_fatal)
    
    #Return non-fatal cost which is one element of safety cost
    def calculate_fatal_cost(self):
        if self.underground[-1]==1:
            if self.underground[0]==1:
                self.fatal.append((self.length/(self.inputs.parameter_dict['underground_baseyear']+self.inputs.parameter_dict['overhead_baseyear']))*self.inputs.parameter_dict['fir']*self.inputs.parameter_dict['employees']/100000*self.inputs.parameter_dict['vsl'])
            else:
                self.fatal.append(((1+self.length)/1)*(self.length/(self.inputs.parameter_dict['underground_baseyear']+self.inputs.parameter_dict['overhead_baseyear']))*self.inputs.parameter_dict['fir']*self.inputs.parameter_dict['employees']/100000*self.inputs.parameter_dict['vsl'])
        else:
            self.fatal.append((self.length/(self.inputs.parameter_dict['underground_baseyear']+self.inputs.parameter_dict['overhead_baseyear']))*self.inputs.parameter_dict['fir']*self.inputs.parameter_dict['employees']/100000*self.inputs.parameter_dict['vsl'])
        return(self.fatal)
    
    #Return total safety cost which is summation of fatal and non fatal cost
    def calculate_total_safety(self):
        self.total_safety.append(self.non_fatal[-1]+self.fatal[-1])
        return(self.total_safety)
    
    #Return total cost which is summation of lifecycle cost, environmental cost and safety cost
    def calculate_total_cost(self):
        self.total.append(self.total_infra[-1]+self.environmental_restoration[-1]+self.total_safety[-1])
        return(self.total)
    
    #Calculation of Total Dollar Amount of Revenue lost per Customer Hour Interruption in Shrewsbury, MA based on SAIDI for MA in the Residential, Commercial and Industry sectors in 2019, for overhead
    
    def calculate_economic_benefits(self):
        SAIDI_Current=0
        total_length_current=0
        total_economic_benefit_current= 0
        if self.underground[-1]==1:
            SAIDI_Current=self.inputs.parameter_dict['SAIDI_underground']
            total_length_current=self.inputs.parameter_dict['total_length_underground']            
        else:
            SAIDI_Current=self.inputs.parameter_dict['SAIDI_overhead']
            total_length_current=self.inputs.parameter_dict['total_length_overhead']
        if self.underground[-1]==1:
            if self.underground[0]==0:
                residential_benefit_current=SAIDI_Current*(self.inputs.parameter_dict['USD_per_Customer_Hour_Interruption_Residential'])*(self.inputs.parameter_dict['Total_Customers_Residential_Shrewsbury'])
                commercial_benefit_current=SAIDI_Current*(self.inputs.parameter_dict['USD_per_Customer_Hour_Interruption_Commercial'])*(self.inputs.parameter_dict['Total_Customers_Commercial_Shrewsbury'])
                industry_benefit_current=SAIDI_Current*(self.inputs.parameter_dict['USD_per_Customer_Hour_Interruption_Industry'])*(self.inputs.parameter_dict['Total_Customers_Industry_Shrewsbury'])
                self.residential_benefit.append(residential_benefit_current)
                self.commercial_benefit.append(commercial_benefit_current)
                self.industry_benefit.append(industry_benefit_current)
            else:
                residential_benefit_current=0
                commercial_benefit_current=0
                industry_benefit_current=0
                self.residential_benefit.append(residential_benefit_current)
                self.commercial_benefit.append(commercial_benefit_current)
                self.industry_benefit.append(industry_benefit_current)
        else:
            residential_benefit_current=0
            commercial_benefit_current=0
            industry_benefit_current=0
            self.residential_benefit.append(residential_benefit_current)
            self.commercial_benefit.append(commercial_benefit_current)
            self.industry_benefit.append(industry_benefit_current)
        total_economic_benefit_current = (self.length/total_length_current) * (residential_benefit_current + commercial_benefit_current + industry_benefit_current)
        self.total_economic_benefits.append(total_economic_benefit_current)
        return(self.total_economic_benefits)  
    
    def calculate_aesthetic_benefits(self):
        if self.underground[-1]==1:
            if self.underground[0]==0:
                self.total_aesthetic_benefits.append((self.inputs.parameter_dict['Shrewsbury_tax_levy_2021']/self.inputs.parameter_dict['total_length'])*self.inputs.parameter_dict['aesthetic_benefit_percentage'])
            else:
                self.total_aesthetic_benefits.append(0)
        else:
            self.total_aesthetic_benefits.append(0)
        return(self.total_aesthetic_benefits)              

def test():
    model_data=model_inputs()
    model_data.modify_parameter('r',10)