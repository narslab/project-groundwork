# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
###Importing required libraries
import numpy as np
import random
###

###Model Variables and Parameters
# Average ages in base year for underground and overhead distribution lines (in years)
average_age=20
# We selected age shape and scale in a way that age_shape*age_scale=average_age
age_shape=10
# We selected age shape and scale in a way that age_shape*age_scale=average_age
age_scale=2
# We selected length shape and scale in a way that length_shape*length_age=average_length
length_shape=2
#We selected age shape and scale in a way that length_shape*age scale=average_length
length_scale=0.25
# Average length for underground and overhead distribution lines (in miles)
average_length=0.5
# Numbers of line segments in the network (Shrewsbury has 191.5 miles overhead, 121.7 miles underground line, eaach segment's length is considered about 0.5 miles. So by dividing (91.5+121.7)/.5 we calculated this parameter.
segment_number= 625
#the year in which we are going to start conducting cost analysis
baseyear=2021
#Length of undergeound lines in miles in base year
underground_baseyear=121
#Length of overhead lines in miles in base year
overhead_baseyear=191
# Discount rate=10%
r=0.1
# per-acre price of a conservation easement
easment_value=3000
# Non-fatality incidence rates, number of accidents per 100000 workers
nfir=2100
# Fatality incidence rates, number of accidents per 100000 workers
fir=15
#The number of IOU employees
employees=8514/255
#A randomly determined annual injury cost, per accident
injurycost=130658
#The value of a statistical life
vsl=6900000
#Assigning overhead and underground line's specification (parameters) as a dictionary
overhead_line={'lifespan':60,'replcost':104000,'replcost_growth_rate':0,'om_growth_rate':0.05,'om_percentage_replcost':0.005,'corridor_length':60}
underground_line={'lifespan':40,'replcost':357000,'replcost_growth_rate':0,'om_growth_rate':0.05,'om_percentage_replcost':0.005,'corridor_length':120,'over_under_raplcost':357000}
#lifespan=Useful lifespan of overhead line and underground lines
#replcost=Cost associated with replacing a line with the same line type after it reaches its life span. 
#replcost_growth_rate= replacement cost annual growth/decay rate 
# om_percentage_replcost= percentage of the overall replacement costs which equals to annual O&M expenses (OPEX) for each type of line
# corridor_length= length of the corridor in feet needed for calculating environmental cost.
# over_under_raplcost= replacement cost associated with replacing an overhead line with an underground line.
###

###Defining Line segment class with required attributes and methods and these methods are going to be modified based on requirements for each strategies in the simulations.
class Line_segment:
    ## The __init__ function as the constructor, which assigns random length, age and underground status for the base year to each line segment.
    def __init__(self, age_shape, age_scale, length_shape, length_scale, overhead_proportion):        
        self.age = [np.random.gamma(age_shape, age_scale)] # set the age as a list, which can be dynamically expanded
        self.length = np.random.gamma(length_shape,length_scale) # we can assume the length is fixed over time
        overhead_probability = random.uniform(0,1)
        if overhead_probability > overhead_proportion: # if underground = 0, then segment is overhead.
            self.underground = [1] # again, a dynamic list.
        else:
            self.underground = [0]
        if self.underground[0]==1:
            self.replcost_rate=[underground_line['replcost']]
        else:
            self.replcost_rate=[overhead_line['replcost']]       
        self.capex=[0]
        self.opex=[self.calculate_opex()]
        self.total_infra=[0]
        self.environmental_restoration=[0]
        self.non_fatal=[0]
        self.fatal=[0]
        self.total_safety=[0]
        self.total=[0]
    ###Lifecycle Infrastructure Costs:
    # Add one year to the age of line segment,compare it to the lifespan, starts from 1 when reaches to lifespan and append this age to age list. Also append underground status to its list.
    def update_age_and_underground_statusQuo(self):
        if self.underground[-1]==1:
            lifespan_current= int(underground_line['lifespan'])
        else:
            lifespan_current= int(overhead_line['lifespan'])
        age_current=self.age[-1]
        if age_current<(lifespan_current-1):
            age_current+=1
            self.age.append(age_current)
            self.underground.append(self.underground[0])
        else:
            self.age.append(1)
            self.underground.append(self.underground[0])
            
    def update_age_and_underground_under_after_lifespan(self):
        underground=self.underground[-1]
        if underground==1:
            lifespan_x= int(underground_line['lifespan'])
        else:
            lifespan_x= int(overhead_line['lifespan'])
        age=(self.age[-1])
        if age<(lifespan_x-1):
            age+=1
            self.age.append(age)
            self.underground.append(self.underground[-1])
        else:
            self.age.append(1)
            self.underground.append(1)
    
    #Add interest rate to the replacement cost and also cansider different replacementcost rate when underground=1        
    def add_replcost_intrest_rate(self):
        underground_current=self.underground[-1]
        underground_baseyear=self.underground[0]
        if underground_current==1:
            replcost_growth_rate_current=underground_line['replcost_growth_rate']
        else:
            replcost_growth_rate_current=overhead_line['replcost_growth_rate']
        if underground_current==underground_baseyear:        
            replcost_new=(self.replcost_rate[-1])+((replcost_growth_rate_current)*(self.replcost_rate[-1]))
            self.replcost_rate.append(replcost_new)
        else:
            replcost_new=underground_line['replcost']*((1+replcost_growth_rate_current)**(len(self.underground)-1))
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
            om_percentage_replcost_current=underground_line['om_percentage_replcost']
        else:
            om_percentage_replcost_current=overhead_line['om_percentage_replcost']
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
            om_growth_rate=underground_line['om_growth_rate']
        else:
            om_growth_rate=overhead_line['om_growth_rate']
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
            lifespan_x=overhead_line['lifespan']
        elif underground==1:
            lifespan_x=underground_line['lifespan']
        first_retire=(lifespan_x)-(age_baseyear)
        return (np.ceil (first_retire))
 
    ###Environmental Costs:
    #Determin environmental restoration cost based on the length of overhead and underground lines. (1mile= 5280 foot, 1sqmile=640 Acre) 
    def calculate_environmental_restoration(self):
        environmental_restoration_current=0
        if self.underground[-1]==1:
            if self.underground[0]==1:
                corridor_length=overhead_line['corridor_length']
                self.environmental_restoration.append(environmental_restoration_current)
            else:
                corridor_length=underground_line['corridor_length']-overhead_line['corridor_length']
                environmental_restoration_current=((self.length)*(corridor_length)*640/5280*easment_value)
                self.environmental_restoration.append(environmental_restoration_current)
        else:
            corridor_length=underground_line['corridor_length']
            self.environmental_restoration.append(environmental_restoration_current)
        return(self.environmental_restoration)

    
    ###Safety and health Costs:
    #Return fatal cost which is one element of safety cost
    def calculate_non_fatal_cost(self):
        if self.underground[-1]==1:
            if self.underground[0]==1:
                self.non_fatal.append((self.length/(underground_baseyear+overhead_baseyear))*nfir*employees/100000*injurycost)
            else:
                self.non_fatal.append(((1+self.length)/1)*(self.length/(underground_baseyear+overhead_baseyear))*nfir*employees/100000*injurycost)
        else:
            self.non_fatal.append((self.length/(underground_baseyear+overhead_baseyear))*nfir*employees/100000*injurycost)
        return(self.non_fatal)
    
    #Return non-fatal cost which is one element of safety cost
    def calculate_fatal_cost(self):
        if self.underground[-1]==1:
            if self.underground[0]==1:
                self.fatal.append((self.length/(underground_baseyear+overhead_baseyear))*fir*employees/100000*vsl)
            else:
                self.fatal.append(((1+self.length)/1)*(self.length/(underground_baseyear+overhead_baseyear))*fir*employees/100000*vsl)
        else:
            self.fatal.append((self.length/(underground_baseyear+overhead_baseyear))*fir*employees/100000*vsl)
        return(self.fatal)
    
    #Return total safety cost which is summation of fatal and non fatal cost
    def calculate_total_safety(self):
        self.total_safety.append(self.non_fatal+self.fatal)
        return(self.total_safety)
    
    #Return total cost which is summation of lifecycle cost, environmental cost and safety cost
    def calculate_total_cost(self):
        self.total.append(self.total_infra+self.environmental_restoration+self.total_safety)
        return(self.total)