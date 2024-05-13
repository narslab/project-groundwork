###Importing required libraries
import numpy as np
import random
###

class Electric_model_inputs:
    ###Model Variables and Parameters for Electric line segments
    def __init__(self):
        #np.random.seed(10101)  # Ensuring deterministic initialization
        #random.seed(10102)
        self.parameter_dict = {
            "analysis_years":40, #Analysis_years
            "average_age":27, # Average ages in base year for underground and overhead distribution lines (in years)=0.5(0.66*60+0.36*40)
            "age_shape":13.5, # We selected age shape and scale in a way that age_shape*age_scale=average_age
            "age_scale":2,  # We selected age shape and scale in a way that age_shape*age scale=average_length
            #"length_shape":2, # We selected length shape and scale in a way that length_shape*length_scale=average_length
            #"length_scale":0.25, # We selected length shape and scale in a way that length_shape*length_scale=average_length
            "average_length":0.21, # Average length for underground and overhead distribution lines (in miles)
            "segment_number":2299, # Numbers of line segments in the network (Shrewsbury has 191.5 miles overhead, 121.7 miles underground line, eaach segment's length is considered about 0.5 miles. So by dividing (91.5+121.7)/.5 we calculated this parameter.
            "baseyear":2021, #the year in which we are going to start conducting cost analysis 
            "underground_baseyear":167, #Length of undergeound lines in miles in base year
            "overhead_baseyear":325, #Length of overhead lines in miles in base year
            "r":0.1, # Discount rate=10%
            "easment_value":2692, # per-acre price of a conservation easement in MA
            "nfir":2100, # Non-fatality incidence rates, number of accidents per 100000 workers
            "fir":10, # Fatality incidence rates, number of accidents per 100000 workers 
            "employees":40, #The number of IOU employees
            "injurycost":130658, # A randomly determined annual injury cost, per accident
            "vsl":7600000,#The value of a statistical life
            "overhead_proportion":0.66, #The value showing the proportion of underground lines in Shrewsbury
            #Assigning overhead and underground line's specification (parameters) as a dictionary
            "overhead_line":{'lifespan':40,'replcost':51000,'replcost_growth_rate':0.01,'om_growth_rate':0.01,'om_proportion_replcost':0.003,'corridor_width':7.5},
            "underground_line":{'lifespan':50,'replcost':154000,'replcost_growth_rate':0.01 ,'om_growth_rate':0.01,'om_proportion_replcost':0.003,'corridor_width':15 ,'over_under_convertcost':378000},
            #lifespan=Useful lifespan of overhead line and underground lines
            #replcost=Cost associated with replacing a line with the same line type after it reaches its life span. 
            #replcost_growth_rate= replacement cost annual growth/decay rate 
            # om_proportion_replcost= percentage of the overall replacement costs which equals to annual O&M expenses (OPEX) for each type of line
            # corridor_width= length of the corridor in feet needed for calculating environmental cost.
            # over_under_convertcost= replacement cost associated with replacing an overhead line with an underground line.
            ###
            "service_area": 21.7,
            #"SAIDI_overhead": 5.72, #in hours #0.66x + 0.34y = 4.17, and y = 0.2x --> which is the current SAIDI for MASS according to patch.com
            #"SAIDI_underground": 1.15, #0.66 is the percentage of overhead lines in Shrewsbury, MA and 0.34 is the percentage of undergrounded lines, taking into consideration our assumption that 80% of outages happen via overhead lines and 20% due to unerground lines
            "joint_trench_additional":0.022, # 2.2% additioanal cost for bigger trench (0.22*10%=0.022)
            "SAIDI":1.38,
            #Dollar Amount Lost per Customer Hour Interruption in Shrewsbury in 2019, costs from 2.1 Estimating customer interruption costs using customer interruption cost surveys, page 21: https://eta-publications.lbl.gov/sites/default/files/hybrid_paper_final_22feb2021.pdf
            "USD_per_Customer_Hour_Interruption_Residential": 10,
            "USD_per_Customer_Hour_Interruption_Commercial":205.70,
            "USD_per_Customer_Hour_Interruption_Industry":15048,
            #Number of Customers in Each Sector in Shrewsbury Municipal Electric (SELCO) in 2019
            #"Total_Customers_Residential_Shrewsbury":6400,
            #"Total_Customers_Commercial_Shrewsbury":8000,
            #"Total_Customers_Industry_Shrewsbury":1600,
            "Total_Customers_Residential_Shrewsbury":14424,
            "Total_Customers_Commercial_Shrewsbury":838,
            "Total_Customers_Industry_Shrewsbury":269,
            "total_length":55.43, #summation of underground and overhead miles generated based on gamma simulation
            "total_length_overhead":36.68, #summation of overhead miles generated based on gamma simulation
            "total_length_underground":18.75, #summation of underground miles generated based on gamma simulation}
            #"Shrewsbury_tax_levy_2021": 85713912.0,
            "Shrewsbury_tax_levy_2021": 6873609623,#85713912.0/(12.47/1000) the tax levy is $85,713,912 and the tax rate is $12.47 per $1,000 of assessed value
            #"aesthetic_benefit_proportion":0.03,
            "aesthetic_benefit_proportion":0.05,
            "inflation_rate_benefit":0,
            "shrewsbury_population":38325,
            "residential_percentage":0.8,
            "industrial_percentage":0.1,
            "commercial_percentage":0.1,
            "outage_overhead":0.8,
            "outage_underground":0.2,
            "single_phase_probability":0.6,
            "log_clay_probabiliy":[0.0004,0.1649,0.0202,0.0002,0.0667,0.0078,0.397,0.2282,0.0401,0.0714,0.003],
            "log_clay":[0,0.301,0.602,0.663,0.732,0.778,0.845,0.863,0.903,0.954,0.978],
            "log_density_mu": -1.55,
            "log_density_sigma": 0.76,
            "length_s": 0.711,
            "length_scale": 0.019,
            "length_loc": -0.004,
            "alpha":0.3
            }
    
    
    #defining a function to modify parameters for sensitivity anlysis based on percentage change
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
    
###Model Variables and Parameters for Broadband line segments
class Broadband_model_inputs:
    ###Model Variables and Parameters
    def __init__(self):
        self.parameter_dict = {
            "analysis_years":40, #Analysis_years
            "average_age":27, # Average ages in base year for underground and overhead distribution lines (in years)=0.5(0.66*60+0.36*40)
            "age_shape":13.5, # We selected age shape and scale in a way that age_shape*age_scale=average_age
            "age_scale":2,  # We selected age shape and scale in a way that age_shape*age scale=average_length
            #"length_shape":2, # We selected length shape and scale in a way that length_shape*length_scale=average_length
            #"length_scale":0.25, # We selected length shape and scale in a way that length_shape*length_scale=average_length
            "average_length":0.21, # Average length for underground and overhead distribution lines (in miles)
            "total_length":55.43,
            "total_length_overhead":36.68, #summation of overhead miles generated based on gamma simulation
            "total_length_underground":18.75, #summation of underground miles generated based on gamma simulation}
            "segment_number":2299, # Numbers of line segments in the network (Shrewsbury has 191.5 miles overhead, 121.7 miles underground line, eaach segment's length is considered about 0.5 miles. So by dividing (91.5+121.7)/.5 we calculated this parameter.
            "baseyear":2021, #the year in which we are going to start conducting cost analysis 
            "underground_baseyear":167, #Length of undergeound lines in miles in base year
            "overhead_baseyear":325, #Length of overhead lines in miles in base year
            "r":0.1, # Discount rate=10%
            "easment_value":2692, # per-acre price of a conservation easement
            "nfir":2100, # Non-fatality incidence rates, number of accidents per 100000 workers
            "fir":10, # Fatality incidence rates, number of accidents per 100000 workers 
            "employees":40, #The number of IOU employees
            "injurycost":130658, # A randomly determined annual injury cost, per accident
            "vsl":7600000,#The value of a statistical life
            "overhead_proportion":0.66, #The value showing the proportion of underground lines in Shrewsbury
            #Assigning overhead and underground line's specification (parameters) as a dictionary
            "overhead_line":{'lifespan':40,'replcost':27720,'replcost_growth_rate':0.01,'om_growth_rate':0.01,'om_proportion_replcost':0.003,'corridor_width':7.5},
            "underground_line":{'lifespan':50,'replcost':83160,'replcost_growth_rate':0.01,'om_growth_rate':0.01,'om_proportion_replcost':0.003,'corridor_width':15 ,'over_under_convertcost':378000, 'over_under_joint_proportion_convertcost':0.28},
            #lifespan=Useful lifespan of overhead line and underground lines
            #replcost=Cost associated with replacing a line with the same line type after it reaches its life span. 
            #replcost_growth_rate= replacement cost annual growth/decay rate 
            # om_proportion_replcost= percentage of the overall replacement costs which equals to annual O&M expenses (OPEX) for each type of line
            # corridor_width= length of the corridor in feet needed for calculating environmental cost.
            # over_under_convertcost= replacement cost associated with replacing an overhead line with an underground line.
            "aesthetic_benefit_proportion":0.05,
            #"Shrewsbury_tax_levy_2021": 85713912.0,
            "Shrewsbury_tax_levy_2021": 6873609623,#85713912.0/(12.47/1000) the tax levy is $85,713,912 and the tax rate is $12.47 per $1,000 of assessed value
            "inflation_rate_benefit":0,
            "service_area": 21.7, # square mile (town of Shrewsbury area)
            "single_phase_probability":0.6,
            "log_clay_probabiliy":[0.0004,0.1649,0.0202,0.0002,0.0667,0.0078,0.397,0.2282,0.0401,0.0714,0.003],
            "log_clay":[0,0.301,0.602,0.663,0.732,0.778,0.845,0.863,0.903,0.954,0.978],
            "log_density_mu": -1.55,
            "log_density_sigma": 0.76,
            "length_s": 0.711,
            "length_scale": 0.019,
            "length_loc": -0.004,
            #"total_employees":3000,
            "total_employees":24834, # total population * employment rate = 38,325 * 64.8%
            "affected_employees": 0.25,
            "cost_per_hour_residential": 20.07,
            "affected_Customers_Residential_Shrewsbury":18396,# total_population*residential%*work_from_home%=38325*0.8*0.6=18396
            #"cost_per_hour": 24,
            "cost_per_hour_commercial_residencial": 830, # Average lost per minute= (137+17244)/2=8690, Average lost per hour= 8690 *60 = 521430, 521430/(0.25*24834)
            "outage_hours": 40,
            "SAIDI":1.38,
            "outage_overhead":0.8,
            "outage_underground":0.2,
            "USD_per_Customer_Hour_Interruption_Residential": 15,
            "USD_per_Customer_Hour_Interruption_Commercial":205.70,
            "USD_per_Customer_Hour_Interruption_Industry":8220,
            #Number of Customers in Each Sector in Shrewsbury Municipal Electric (SELCO) in 2019
            #"Total_Customers_Residential_Shrewsbury":6400,
            #"Total_Customers_Commercial_Shrewsbury":8000,
            #"Total_Customers_Industry_Shrewsbury":1600,
            "Total_Customers_Residential_Shrewsbury":6449,
            "Total_Customers_Commercial_Shrewsbury":838,
            "Total_Customers_Industry_Shrewsbury":135,
            "alpha":0.3
            }
        
    #defining a function to modify parameters for sensitivity anlysis based on percentage change
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


###Defining Electric Line segment class with required attributes and methods and these methods are going to be modified based on requirements for each strategies in the simulations.
class Electric_line_segment:
    ## The __init__ function as the constructor, which assigns random length, age and underground status for the base year to each line segment.
    #data=Electric_model_inputs()
    def __init__(self, inputs): 
        #np.random.seed(10101)  # Ensuring deterministic initialization
        #random.seed(10102)
        self.inputs = inputs
        self.age = [np.random.gamma(self.inputs.parameter_dict['age_shape'], self.inputs.parameter_dict['age_scale'])] # set the age as a list, which can be dynamically expanded
        #self.length = np.random.gamma(self.inputs.parameter_dict['length_shape'],self.inputs.parameter_dict['length_scale']) # we can assume the length is fixed over time
        self.length = np.random.lognormal(np.log(self.inputs.parameter_dict['length_scale']),self.inputs.parameter_dict['length_s'])
        overhead_probability = random.uniform(0,1)
        if overhead_probability > self.inputs.parameter_dict['overhead_proportion']: # if underground = 0, then segment is overhead.
            self.underground = [1] # again, a dynamic list.
        else:
            self.underground = [0]
        if self.underground[0]==1:
            self.replcost=[self.inputs.parameter_dict['underground_line']['replcost']]
        else:
            self.replcost=[self.inputs.parameter_dict['overhead_line']['replcost']]       
        self.capex=[0]
        self.opex=[0]
        self.total_infra=[0]
        self.environmental_restoration=[0]
        self.non_fatal=[0]
        self.fatal=[0]
        self.total_safety=[0]
        self.total_cost=[0]
        self.residential_benefit=[0]
        self.residential_loss=[0]
        self.commercial_benefit=[0]
        self.commercial_loss=[0]
        self.industry_benefit=[0]
        self.industry_loss=[0]
        self.total_economic_benefits = [0]
        self.total_inflated_economic_benefits=[0]
        self.total_aesthetic_benefits=[0]
        self.total_inflated_aesthetic_benefits=[0]
        self.total_aesthetic_losses=[0]
        self.total_inflated_aesthetic_losses=[0]
        self.total_economic_losses=[0]
        self.total_inflated_economic_losses=[0]
        self.total_losses=[0]
        single_phase_probability = random.uniform(0,1)
        if single_phase_probability > self.inputs.parameter_dict['single_phase_probability']: # if underground = 0, then segment is overhead.
            self.single_phase = [1] 
        else:
            self.single_phase = [0]
        log_clay = random.uniform(0,1)    
        if log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:1]): 
            self.log_clay=[self.inputs.parameter_dict['log_clay'][0]]
        elif sum(self.inputs.parameter_dict['log_clay_probabiliy'][:1])< log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:2]):
            self.log_clay=[self.inputs.parameter_dict['log_clay'][1]]
        elif sum(self.inputs.parameter_dict['log_clay_probabiliy'][:2])< log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:3]):
            self.log_clay=[self.inputs.parameter_dict['log_clay'][2]]
        elif sum(self.inputs.parameter_dict['log_clay_probabiliy'][:3])< log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:4]):
            self.log_clay=[self.inputs.parameter_dict['log_clay'][3]]
        elif sum(self.inputs.parameter_dict['log_clay_probabiliy'][:4])< log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:5]):
            self.log_clay=[self.inputs.parameter_dict['log_clay'][4]]
        elif sum(self.inputs.parameter_dict['log_clay_probabiliy'][:5])< log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:6]):
            self.log_clay=[self.inputs.parameter_dict['log_clay'][5]]
        elif sum(self.inputs.parameter_dict['log_clay_probabiliy'][:6])< log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:7]):
            self.log_clay=[self.inputs.parameter_dict['log_clay'][6]]
        elif sum(self.inputs.parameter_dict['log_clay_probabiliy'][:7])< log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:8]):
            self.log_clay=[self.inputs.parameter_dict['log_clay'][7]]
        elif sum(self.inputs.parameter_dict['log_clay_probabiliy'][:8])< log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:9]):
            self.log_clay=[self.inputs.parameter_dict['log_clay'][8]]
        elif sum(self.inputs.parameter_dict['log_clay_probabiliy'][:9])< log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:10]):
            self.log_clay=[self.inputs.parameter_dict['log_clay'][9]]
        else:
            self.log_clay=[self.inputs.parameter_dict['log_clay'][10]]
            
        self.log_density=[np.random.normal(self.inputs.parameter_dict['log_density_mu'], self.inputs.parameter_dict['log_density_sigma'])]
        self.conversion_cost=[0]
        
    ###Lifecycle Infrastructure Costs:
    # Add one year to the age of line segment,compare it to the lifespan, starts from 1 when reaches to lifespan and append this age to age list.                  
    #def update_age_and_check_replacement(self, aggressive=False):
        """
        Updates the age and determines whether it should be replaced.
    
        This function increments the age of a line segment based on its current age and lifespan. 
        It also checks if it has replaced from overhead (0) to underground (1).
    
        :param aggressive: Boolean indicating if the aggressive replacement policy is used.
        :return: Boolean indicating if the asset was marked for replacement.
        """
    #    age_current = self.age[-1]
    #    lifespan_dict = 'underground_line' if self.underground[-1] == 1 else 'overhead_line'
    #    lifespan_current = int(self.inputs.parameter_dict[lifespan_dict]['lifespan'])
    
    #    replace = False
    #    if aggressive and len(self.underground) > 1 and self.underground[-2] == 0 and self.underground[-1] == 1:
    #        threshold = 0.5 * lifespan_current
    #        if age_current > threshold:
    #            self.age.append(1)
    #            replace = True
    #        else:
    #            age_current += 1
    #    else:
    #        if age_current > lifespan_current:
    #            self.age.append(1)
    #            replace = True
    #        else:
    #            age_current += 1
    
    #    self.age.append(age_current)
    #    return replace


        
# Add one year to the age of line segment,compare it to the lifespan, starts from 1 when reaches to lifespan and append this age to age list.                  
    #def update_age_and_check_replacement(self,replace=False, aggressive=False):
    #    if aggressive==False:
    #        if self.underground[-1]==1:
    #            treshhold= int(self.inputs.parameter_dict['underground_line']['lifespan'])
    #        else:
    #            treshhold= int(self.inputs.parameter_dict['overhead_line']['lifespan'])
    #    else:
    #        if self.underground[:-1]==[0]*len(self.underground[:-1]):
    #            if self.underground[-1]==1:
    #                treshhold= 0.5*int(self.inputs.parameter_dict['underground_line']['lifespan'])
    #            else:
    #                treshhold= int(self.inputs.parameter_dict['overhead_line']['lifespan'])
    #        else:
    #            if self.underground[-1]==1:
    #                treshhold= int(self.inputs.parameter_dict['underground_line']['lifespan'])
    #            else:
    #                treshhold= int(self.inputs.parameter_dict['overhead_line']['lifespan'])                 
    #    age_current=self.age[-1]
    #    if age_current>treshhold:
    #        self.age.append(1)
    #        replace=True
    #    else:
    #        age_current+=1
    #        self.age.append(age_current)
    #        replace=False
    #    return(replace)
    
    # Add one year to the age of line segment,compare it to the lifespan, starts from 1 when reaches to lifespan and append this age to age list.                  
    def update_age_and_check_replacement(self, aggressive=False):
        if self.underground[-1] == 1:
            threshold = int(self.inputs.parameter_dict['underground_line']['lifespan'])
        else:
            threshold = int(self.inputs.parameter_dict['overhead_line']['lifespan'])
    
        if aggressive and self.underground[-1] == 0:
            threshold = 0.5 * int(self.inputs.parameter_dict['overhead_line']['lifespan'])
    
        age_current = self.age[-1]
        if age_current > threshold:
            self.age.append(1)
            replace = True
        else:
            age_current += 1
            self.age.append(age_current)
            replace = False
    
        return replace
    
    def update_underground_status(self,convert=False):
        """
        Updates the underground status of the asset.
    
        If conversion is indicated (convert=True), the method changes the status from overhead (0) 
        to underground (1). Otherwise, the status remains unchanged.
    
        :param convert: Boolean indicating if a conversion from overhead to underground should occur.
        """
        # Get the current underground status
        status = self.underground[-1]
    
        # Convert from 0 to 1 if necessary
        if convert and status == 0:
            status = 1
    
        # Append the (possibly updated) status to the underground list
        self.underground.append(status)
            
    #Disaggregated cost model
    def calculate_disaggregated_conversion_cost(self):
        if self.underground[-1]==0:
            conversion_cost_current=0
            self.conversion_cost.append(conversion_cost_current)
        else:
            if self.underground[:-1]==[0]*len(self.underground[:-1]):
                conversion_cost_current=5280*((-61*self.log_density[-1])-(64*self.single_phase[-1])+(137*self.log_clay[-1]))
                self.conversion_cost.append(conversion_cost_current)
            else:
                conversion_cost_current=0
                self.conversion_cost.append(conversion_cost_current)
        return(self.conversion_cost)
        
    #Add interest rate to the replacement cost and also cansider different replacementcost rate when underground=1        
    def calculate_replcost(self,disaggregated_function=False, joint_trench=False):
        if disaggregated_function==True:
            if joint_trench==True:
                conversion_cost_current=self.calculate_disaggregated_conversion_cost()[-1]*(1+self.inputs.parameter_dict['joint_trench_additional'])
            else:
                conversion_cost_current=self.calculate_disaggregated_conversion_cost()[-1]
        else:
            if joint_trench==True:
                conversion_cost_current=self.inputs.parameter_dict['underground_line']['over_under_convertcost']*(1+self.inputs.parameter_dict['joint_trench_additional'])
            else:
                conversion_cost_current=self.inputs.parameter_dict['underground_line']['over_under_convertcost']
        underground_current=self.underground[-1]
        underground_baseyear=self.underground[0]
        if underground_current==1:
            replcost_growth_rate_current=self.inputs.parameter_dict['underground_line']['replcost_growth_rate']
        else:
            replcost_growth_rate_current=self.inputs.parameter_dict['overhead_line']['replcost_growth_rate']
        if underground_current==underground_baseyear:        
            replcost_new=(self.replcost[-1])+((replcost_growth_rate_current)*(self.replcost[-1]))
            self.replcost.append(replcost_new)
        else:
            if self.underground[:-1]==[0]*len(self.underground[:-1]):
                replcost_new=conversion_cost_current*((1+replcost_growth_rate_current)**(len(self.underground)-1))
                self.replcost.append(replcost_new)
            else:
                replcost_new=self.inputs.parameter_dict['underground_line']['replcost']*((1+replcost_growth_rate_current)**(len(self.underground)-1))
                self.replcost.append(replcost_new)
        return(self.replcost)
        
    
    #Determine capital expenses which is replacement cost for each line segment based on the rate of replacement cost in that year and length of the circuit.
    def calculate_capex(self):
        if (self.age[-1])==1:
            length_current=self.length
            replcost_rate_current=self.replcost[-1]
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
            om_proportion_replcost_current=self.inputs.parameter_dict['underground_line']['om_proportion_replcost']
        else:
            om_proportion_replcost_current=self.inputs.parameter_dict['overhead_line']['om_proportion_replcost']
        length_current=self.length
        replcost_rate_current=self.replcost[-1]
        opex=(om_proportion_replcost_current)*(length_current)*(replcost_rate_current)
        self.opex.append(opex)
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
            corridor_width=self.inputs.parameter_dict['underground_line']['corridor_width']
            if self.underground[0]==1:
                self.environmental_restoration.append(environmental_restoration_current)
            else:
                environmental_restoration_current=((self.length)*(corridor_width)*640/5280*self.inputs.parameter_dict['easment_value'])
                self.environmental_restoration.append(environmental_restoration_current)
        else:
            corridor_width=self.inputs.parameter_dict['overhead_line']['corridor_width']
            self.environmental_restoration.append(environmental_restoration_current)
        return(self.environmental_restoration)

    
    ###Safety and health Costs:
    #Return fatal cost which is one element of safety cost
    def calculate_non_fatal_cost(self,under_len_pro=1):
        self.non_fatal.append(under_len_pro*(self.length/self.inputs.parameter_dict['total_length'])*(self.inputs.parameter_dict['nfir'])*(self.inputs.parameter_dict['employees']/100000)*(self.inputs.parameter_dict['injurycost']))
        #print("under_len_pro_el:", under_len_pro)
        return(self.non_fatal)
    
    #Return non-fatal cost which is one element of safety cost
    def calculate_fatal_cost(self, under_len_pro=1):
        self.fatal.append(under_len_pro*(self.length/self.inputs.parameter_dict['total_length'])*self.inputs.parameter_dict['fir']*(self.inputs.parameter_dict['employees']/100000)*self.inputs.parameter_dict['vsl'])
        #print("under_len_pro_el:", under_len_pro)
        return(self.fatal)
    
    #Return total safety cost which is summation of fatal and non fatal cost
    def calculate_total_safety(self):
        self.total_safety.append(self.non_fatal[-1]+self.fatal[-1])       
        return(self.total_safety)
    
    #Return total cost which is summation of lifecycle cost, environmental cost and safety cost
    def calculate_total_cost(self):
        self.total_cost.append(self.total_infra[-1]+self.environmental_restoration[-1]+self.total_safety[-1])
        return(self.total_cost)
    
### Ver01
# =============================================================================
#     def calculate_economic_loss(self):
#         SAIDI_Current=self.inputs.parameter_dict['SAIDI']
#         if self.underground[-1]==1:
#             outage_percentage_current=self.inputs.parameter_dict['outage_underground']
#             #percentage=proportion
#         else:
#             outage_percentage_current=self.inputs.parameter_dict['outage_overhead']
#             #percentage=1-proportion
#         residential_loss_current=self.length/self.inputs.parameter_dict["total_length"]*self.inputs.parameter_dict["Total_Customers_Residential_Shrewsbury"]*outage_percentage_current*SAIDI_Current*(self.inputs.parameter_dict['USD_per_Customer_Hour_Interruption_Residential'])
#         commercial_loss_current=self.length/self.inputs.parameter_dict["total_length"]*self.inputs.parameter_dict["Total_Customers_Commercial_Shrewsbury"]*outage_percentage_current*SAIDI_Current*(self.inputs.parameter_dict['USD_per_Customer_Hour_Interruption_Commercial'])
#         industry_loss_current=self.length/self.inputs.parameter_dict["total_length"]*self.inputs.parameter_dict["Total_Customers_Industry_Shrewsbury"]*outage_percentage_current*SAIDI_Current*(self.inputs.parameter_dict['USD_per_Customer_Hour_Interruption_Industry'])
#         self.residential_loss.append(residential_loss_current)
#         self.commercial_loss.append(commercial_loss_current)
#         self.industry_loss.append(industry_loss_current)
#         total_economic_loss_current = (residential_loss_current + commercial_loss_current + industry_loss_current)
#         self.total_economic_losses.append(total_economic_loss_current)
#         return(self.total_economic_losses)      
# =============================================================================

### Ver02
    def calculate_economic_loss(self,lam):
        SAIDI_init=self.inputs.parameter_dict['SAIDI']
        lamb_current=lam
        SAIDI_current=SAIDI_init*(self.inputs.parameter_dict['alpha']+lamb_current*(1-self.inputs.parameter_dict['alpha']))
        residential_loss_current=self.inputs.parameter_dict["Total_Customers_Residential_Shrewsbury"]*SAIDI_current*(self.inputs.parameter_dict['USD_per_Customer_Hour_Interruption_Residential'])
        commercial_loss_current=self.inputs.parameter_dict["Total_Customers_Commercial_Shrewsbury"]*SAIDI_current*(self.inputs.parameter_dict['USD_per_Customer_Hour_Interruption_Commercial'])
        industry_loss_current=self.inputs.parameter_dict["Total_Customers_Industry_Shrewsbury"]*SAIDI_current*(self.inputs.parameter_dict['USD_per_Customer_Hour_Interruption_Industry'])
        self.residential_loss.append(residential_loss_current)
        self.commercial_loss.append(commercial_loss_current)
        self.industry_loss.append(industry_loss_current)
        total_economic_loss_current = (residential_loss_current + commercial_loss_current + industry_loss_current)
        self.total_economic_losses.append(total_economic_loss_current)
        return(self.total_economic_losses)      


    #Add interest rate to economic benefit.
    def add_economic_loss_interest_rate(self):
        economic_loss_new=self.total_economic_losses[-1]*((1+self.inputs.parameter_dict['inflation_rate_benefit'])**(len(self.underground)-1))
        self.total_inflated_economic_losses.append(economic_loss_new)
        return(self.total_inflated_economic_losses)    


    # Calculate aesthetic benefit
    def calculate_aesthetic_benefits(self):
        if self.underground[-1]==1:
            corridor_width_current=self.inputs.parameter_dict['overhead_line']['corridor_width']
        else:
            corridor_width_current=self.inputs.parameter_dict['underground_line']['corridor_width']
        if self.underground[-1]==1:
            if self.underground[:-1]==[0]*len(self.underground[:-1]):
                aesthetic_benefit_current=corridor_width_current/5280*self.length/self.inputs.parameter_dict["service_area"]*self.inputs.parameter_dict['Shrewsbury_tax_levy_2021']*self.inputs.parameter_dict['aesthetic_benefit_proportion']
                self.total_aesthetic_benefits.append(aesthetic_benefit_current)
            else:
                self.total_aesthetic_benefits.append(0)
        else:
            self.total_aesthetic_benefits.append(0)
        return(self.total_aesthetic_benefits) 

    #Add interest rate to aesthetic benefit.
    def add_aesthetic_benefits_interest_rate(self):
        aesthetic_benefit_new=self.total_aesthetic_benefits[-1]*((1+self.inputs.parameter_dict['inflation_rate_benefit'])**(len(self.underground)-1))
        self.total_inflated_aesthetic_benefits.append(aesthetic_benefit_new)
        return(self.total_inflated_aesthetic_benefits)




###Defining Broadband Line segment class with required attributes and methods and these methods are going to be modified based on requirements for each strategies in the simulations.
class Broadband_line_segment:
    ## The __init__ function as the constructor, which assigns random length, age and underground status for the base year to each line segment.
    #data=Broadband_model_inputs()
    def __init__(self, inputs): 
        self.inputs = inputs
        self.age = [np.random.gamma(self.inputs.parameter_dict['age_shape'], self.inputs.parameter_dict['age_scale'])] # set the age as a list, which can be dynamically expanded
        #self.length = np.random.gamma(self.inputs.parameter_dict['length_shape'],self.inputs.parameter_dict['length_scale']) # we can assume the length is fixed over time
        self.length = np.random.lognormal(np.log(self.inputs.parameter_dict['length_scale']),self.inputs.parameter_dict['length_s'])
        overhead_probability = random.uniform(0,1)
        if overhead_probability > self.inputs.parameter_dict['overhead_proportion']: # if underground = 0, then segment is overhead.
            self.underground = [1] # again, a dynamic list.
        else:
            self.underground = [0]
        if self.underground[0]==1:
            self.replcost=[self.inputs.parameter_dict['underground_line']['replcost']]
        else:
            self.replcost=[self.inputs.parameter_dict['overhead_line']['replcost']]       
        self.capex=[0]
        self.opex=[0]
        self.total_infra=[0]
        self.environmental_restoration=[0]
        self.non_fatal=[0]
        self.fatal=[0]
        self.total_safety=[0]
        self.total_cost=[0]
        self.residential_benefit=[0]
        self.residential_loss=[0]
        self.commercial_benefit=[0]
        self.commercial_loss=[0]
        self.industry_benefit=[0]
        self.industry_loss=[0]
        self.total_economic_benefits = [0]
        self.total_inflated_economic_benefits=[0]
        self.total_aesthetic_benefits=[0]
        self.total_inflated_aesthetic_benefits=[0]
        self.total_aesthetic_losses=[0]
        self.total_inflated_aesthetic_losses=[0]
        self.total_economic_losses=[0]
        self.total_inflated_economic_losses=[0]
        self.total_aesthetic_benefits=[0]
        self.total_inflated_aesthetic_benefits=[0]
        self.total_losses=[0]
        single_phase_probability = random.uniform(0,1)
        if single_phase_probability > self.inputs.parameter_dict['single_phase_probability']: # if underground = 0, then segment is overhead.
            self.single_phase = [1] 
        else:
            self.single_phase = [0]
        log_clay = random.uniform(0,1)    
        if log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:1]): 
            self.log_clay=[self.inputs.parameter_dict['log_clay'][0]]
        elif sum(self.inputs.parameter_dict['log_clay_probabiliy'][:1])< log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:2]):
            self.log_clay=[self.inputs.parameter_dict['log_clay'][1]]
        elif sum(self.inputs.parameter_dict['log_clay_probabiliy'][:2])< log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:3]):
            self.log_clay=[self.inputs.parameter_dict['log_clay'][2]]
        elif sum(self.inputs.parameter_dict['log_clay_probabiliy'][:3])< log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:4]):
            self.log_clay=[self.inputs.parameter_dict['log_clay'][3]]
        elif sum(self.inputs.parameter_dict['log_clay_probabiliy'][:4])< log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:5]):
            self.log_clay=[self.inputs.parameter_dict['log_clay'][4]]
        elif sum(self.inputs.parameter_dict['log_clay_probabiliy'][:5])< log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:6]):
            self.log_clay=[self.inputs.parameter_dict['log_clay'][5]]
        elif sum(self.inputs.parameter_dict['log_clay_probabiliy'][:6])< log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:7]):
            self.log_clay=[self.inputs.parameter_dict['log_clay'][6]]
        elif sum(self.inputs.parameter_dict['log_clay_probabiliy'][:7])< log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:8]):
            self.log_clay=[self.inputs.parameter_dict['log_clay'][7]]
        elif sum(self.inputs.parameter_dict['log_clay_probabiliy'][:8])< log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:9]):
            self.log_clay=[self.inputs.parameter_dict['log_clay'][8]]
        elif sum(self.inputs.parameter_dict['log_clay_probabiliy'][:9])< log_clay <= sum(self.inputs.parameter_dict['log_clay_probabiliy'][:10]):
            self.log_clay=[self.inputs.parameter_dict['log_clay'][9]]
        else:
            self.log_clay=[self.inputs.parameter_dict['log_clay'][10]]
            
        self.log_density=[np.random.normal(self.inputs.parameter_dict['log_density_mu'], self.inputs.parameter_dict['log_density_sigma'])]
        self.conversion_cost=[0]
        
    ###Lifecycle Infrastructure Costs:
    #def update_age_and_check_replacement(self, aggressive=False):
        """
        Updates the age and determines whether it should be replaced.
    
        This function increments the age of a line segment based on its current age and lifespan. 
        It also checks if it has replaced from overhead (0) to underground (1).
    
        :param aggressive: Boolean indicating if the aggressive replacement policy is used.
        :return: Boolean indicating if the asset was marked for replacement.
        """
    #    age_current = self.age[-1]
    #    lifespan_dict = 'underground_line' if self.underground[-1] == 1 else 'overhead_line'
    #    lifespan_current = int(self.inputs.parameter_dict[lifespan_dict]['lifespan'])
    
    #    replace = False
    #    if aggressive and len(self.underground) > 1 and self.underground[-2] == 0 and self.underground[-1] == 1:
    #        threshold = 0.5 * lifespan_current
    #        if age_current > threshold:
    #            self.age.append(1)
    #            replace = True
    #        else:
    #            age_current += 1
    #    else:
    #        if age_current > lifespan_current:
    #            self.age.append(1)
    #            replace = True
    #        else:
    #            age_current += 1
    
    #    self.age.append(age_current)
    #    return replace
    

    # Add one year to the age of line segment,compare it to the lifespan, starts from 1 when reaches to lifespan and append this age to age list.                  
    #def update_age_and_check_replacement(self,replace=False, aggressive=False):
    #    if aggressive==False:
    #        if self.underground[-1]==1:
    #            treshhold= int(self.inputs.parameter_dict['underground_line']['lifespan'])
    #        else:
    #            treshhold= int(self.inputs.parameter_dict['overhead_line']['lifespan'])
    #    else:
    #        if self.underground[:-1]==[0]*len(self.underground[:-1]):
    #            if self.underground[-1]==1:
    #                treshhold= 0.5*int(self.inputs.parameter_dict['underground_line']['lifespan'])
    #            else:
    #                treshhold= int(self.inputs.parameter_dict['overhead_line']['lifespan'])
    #        else:
    #            if self.underground[-1]==1:
    #                treshhold= int(self.inputs.parameter_dict['underground_line']['lifespan'])
    #            else:
    #                treshhold= int(self.inputs.parameter_dict['overhead_line']['lifespan'])                 
    #    age_current=self.age[-1]
    #    if age_current>treshhold:
    #        self.age.append(1)
    #        replace=True
    #    else:
    #        age_current+=1
    #        self.age.append(age_current)
    #        replace=False
    #    return(replace)


    # Add one year to the age of line segment,compare it to the lifespan, starts from 1 when reaches to lifespan and append this age to age list.                  
    def update_age_and_check_replacement(self, aggressive=False):
        if self.underground[-1] == 1:
            threshold = int(self.inputs.parameter_dict['underground_line']['lifespan'])
        else:
            threshold = int(self.inputs.parameter_dict['overhead_line']['lifespan'])
    
        if aggressive and self.underground[-1] == 0:
            threshold = 0.5 * int(self.inputs.parameter_dict['overhead_line']['lifespan'])
    
        age_current = self.age[-1]
        if age_current > threshold:
            self.age.append(1)
            replace = True
        else:
            age_current += 1
            self.age.append(age_current)
            replace = False
    
        return replace

    # Add underground status based on if convert is true or not to self.underground list.  
                
    def update_underground_status(self,convert=False):
        """
        Updates the underground status of the asset.
    
        If conversion is indicated (convert=True), the method changes the status from overhead (0) 
        to underground (1). Otherwise, the status remains unchanged.
    
        :param convert: Boolean indicating if a conversion from overhead to underground should occur.
        """
        # Get the current underground status
        status = self.underground[-1]
    
        # Convert from 0 to 1 if necessary
        if convert and status == 0:
            status = 1
    
        # Append the (possibly updated) status to the underground list
        self.underground.append(status)
    
    #Disaggregated cost model
    def calculate_disaggregated_conversion_cost(self):
        if self.underground[-1]==0:
            conversion_cost_current=0
            self.conversion_cost.append(conversion_cost_current)
        else:
            if self.underground[:-1]==[0]*len(self.underground[:-1]):
                conversion_cost_current=5280*((-61*self.log_density[-1])-(64*self.single_phase[-1])+(137*self.log_clay[-1]))
                self.conversion_cost.append(conversion_cost_current)
            else:
                conversion_cost_current=0
                self.conversion_cost.append(conversion_cost_current)
        return(self.conversion_cost)
        
    
    #Add interest rate to the replacement cost and also cansider different replacementcost rate when underground=1        
    def calculate_replcost(self,disaggregated_function=False, joint_trench=False):
        if disaggregated_function==True:
            conversion_cost_current=self.calculate_disaggregated_conversion_cost()[-1]
        else:
            conversion_cost_current=self.inputs.parameter_dict['underground_line']['over_under_convertcost']
        if joint_trench==True:
            conversion_cost_current=conversion_cost_current*self.inputs.parameter_dict['underground_line']['over_under_joint_proportion_convertcost']
        else:
            pass
        underground_current=self.underground[-1]
        underground_baseyear=self.underground[0]
        if underground_current==1:
            replcost_growth_rate_current=self.inputs.parameter_dict['underground_line']['replcost_growth_rate']
        else:
            replcost_growth_rate_current=self.inputs.parameter_dict['overhead_line']['replcost_growth_rate']
        if underground_current==underground_baseyear:        
            replcost_new=(self.replcost[-1])+((replcost_growth_rate_current)*(self.replcost[-1]))
            self.replcost.append(replcost_new)
        else:
            if self.underground[:-1]==[0]*len(self.underground[:-1]):
                replcost_new=conversion_cost_current*((1+replcost_growth_rate_current)**(len(self.underground)-1))
                self.replcost.append(replcost_new)
            else:
                replcost_new=self.inputs.parameter_dict['underground_line']['replcost']*((1+replcost_growth_rate_current)**(len(self.underground)-1))
                self.replcost.append(replcost_new)
        return(self.replcost)   
    
    
    
    #Determine capital expenses which is replacement cost for each line segment based on the rate of replacement cost in that year and length of the circuit.
    def calculate_capex(self):
        if (self.age[-1])==1:
            length_current=self.length
            replcost_rate_current=self.replcost[-1]
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
            om_proportion_replcost_current=self.inputs.parameter_dict['underground_line']['om_proportion_replcost']
        else:
            om_proportion_replcost_current=self.inputs.parameter_dict['overhead_line']['om_proportion_replcost']
        length_current=self.length
        replcost_rate_current=self.replcost[-1]
        opex=(om_proportion_replcost_current)*(length_current)*(replcost_rate_current)
        self.opex.append(opex)
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
            corridor_width=self.inputs.parameter_dict['underground_line']['corridor_width']
            if self.underground[0]==1:
                self.environmental_restoration.append(environmental_restoration_current)
            else:
                environmental_restoration_current=((self.length)*(corridor_width)*640/5280*self.inputs.parameter_dict['easment_value'])
                self.environmental_restoration.append(environmental_restoration_current)
        else:
            corridor_width=self.inputs.parameter_dict['overhead_line']['corridor_width']
            self.environmental_restoration.append(environmental_restoration_current)
        return(self.environmental_restoration)

    
    ###Safety and health Costs:
    #Return fatal cost which is one element of safety cost
    def calculate_non_fatal_cost(self,under_len_pro=1):
        self.non_fatal.append(under_len_pro*(self.length/self.inputs.parameter_dict['total_length'])*(self.inputs.parameter_dict['nfir'])*(self.inputs.parameter_dict['employees']/100000)*(self.inputs.parameter_dict['injurycost']))
        #print("under_len_pro_el:", under_len_pro)
        return(self.non_fatal)
    
    #Return non-fatal cost which is one element of safety cost
    def calculate_fatal_cost(self, under_len_pro=1):
        self.fatal.append(under_len_pro*(self.length/self.inputs.parameter_dict['total_length'])*self.inputs.parameter_dict['fir']*(self.inputs.parameter_dict['employees']/100000)*self.inputs.parameter_dict['vsl'])
        #print("under_len_pro_el:", under_len_pro)
        return(self.fatal)
    
    #Return total safety cost which is summation of fatal and non fatal cost
    def calculate_total_safety(self):
        self.total_safety.append(self.non_fatal[-1]+self.fatal[-1])       
        return(self.total_safety)
    
    ###Total cost
    #Return total cost which is summation of lifecycle cost, environmental cost and safety cost
    def calculate_total_cost(self):
        self.total_cost.append(self.total_infra[-1]+self.environmental_restoration[-1]+self.total_safety[-1])
        return(self.total_cost)

### Ver001
# =============================================================================
#     def calculate_economic_loss(self): 
#         """A method to quantify employee productivity cost based on line segment status"""    
#         status = self.underground[-1]
#         residential_loss = (self.length/self.inputs.parameter_dict["total_length"])*self.inputs.parameter_dict['affected_Customers_Residential_Shrewsbury']*self.inputs.parameter_dict['cost_per_hour_residential']*self.inputs.parameter_dict['outage_hours']
#         commercial_industrial_loss = (self.length/self.inputs.parameter_dict["total_length"])*self.inputs.parameter_dict['affected_employees']*self.inputs.parameter_dict['total_employees']*self.inputs.parameter_dict['cost_per_hour_commercial_residencial']*self.inputs.parameter_dict['outage_hours']
#         economic_loss = residential_loss + commercial_industrial_loss
#         if status==1: #underground line
#             outage_probability=self.inputs.parameter_dict['outage_underground']
#             #percentage=proportion
#         else:
#             outage_probability=self.inputs.parameter_dict['outage_overhead']
#             #percentage=1-proportion
#         self.total_economic_losses.append(economic_loss*outage_probability)
#         return (self.total_economic_losses)
# =============================================================================

### Ver02
    def calculate_economic_loss(self,lam):
        SAIDI_init=self.inputs.parameter_dict['SAIDI']
        lamb_current=lam
        SAIDI_current=SAIDI_init*(self.inputs.parameter_dict['alpha']+lamb_current*(1-self.inputs.parameter_dict['alpha']))
        residential_loss_current=self.inputs.parameter_dict["Total_Customers_Residential_Shrewsbury"]*SAIDI_current*(self.inputs.parameter_dict['USD_per_Customer_Hour_Interruption_Residential'])
        commercial_loss_current=self.inputs.parameter_dict["Total_Customers_Commercial_Shrewsbury"]*SAIDI_current*(self.inputs.parameter_dict['USD_per_Customer_Hour_Interruption_Commercial'])
        industry_loss_current=self.inputs.parameter_dict["Total_Customers_Industry_Shrewsbury"]*SAIDI_current*(self.inputs.parameter_dict['USD_per_Customer_Hour_Interruption_Industry'])
        self.residential_loss.append(residential_loss_current)
        self.commercial_loss.append(commercial_loss_current)
        self.industry_loss.append(industry_loss_current)
        total_economic_loss_current = (residential_loss_current + commercial_loss_current + industry_loss_current)
        self.total_economic_losses.append(total_economic_loss_current)
        return(self.total_economic_losses)    
    
    #Add interest rate to economic benefit.
    def add_economic_loss_interest_rate(self):
        economic_loss_new=self.total_economic_losses[-1]*((1+self.inputs.parameter_dict['inflation_rate_benefit'])**(len(self.underground)-1))
        self.total_inflated_economic_losses.append(economic_loss_new)
        return(self.total_inflated_economic_losses)    


    #Define a function to calculate aesthetic benefit
    def calculate_aesthetic_benefits(self):
        if self.underground[-1]==1:
            corridor_width_current=self.inputs.parameter_dict['overhead_line']['corridor_width']
        else:
            corridor_width_current=self.inputs.parameter_dict['underground_line']['corridor_width']
        if self.underground[-1]==1:
            if self.underground[:-1]==[0]*len(self.underground[:-1]):
                aesthetic_benefit_current=corridor_width_current/5280*self.length/self.inputs.parameter_dict["service_area"]*self.inputs.parameter_dict['Shrewsbury_tax_levy_2021']*self.inputs.parameter_dict['aesthetic_benefit_proportion']
                self.total_aesthetic_benefits.append(aesthetic_benefit_current)
            else:
                self.total_aesthetic_benefits.append(0)
        else:
            self.total_aesthetic_benefits.append(0)
        return(self.total_aesthetic_benefits) 
    
    #Add interest rate to aesthetic benefit.
    def add_aesthetic_benefits_interest_rate(self):
        aesthetic_benefit_new=self.total_aesthetic_benefits[-1]*((1+self.inputs.parameter_dict['inflation_rate_benefit'])**(len(self.underground)-1))
        self.total_inflated_aesthetic_benefits.append(aesthetic_benefit_new)
        return(self.total_inflated_aesthetic_benefits)


    
def test():
    model_data=Electric_model_inputs()
    model_data.modify_parameter('r',10)
