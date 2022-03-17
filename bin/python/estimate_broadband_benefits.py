#!/usr/bin/env python
# coding: utf-8
#author: Nasko

# Sample employee model data
EMPLOYEE_DATA = {'outage_id': 'test1',
                 'total_employees': 500,
                 'affected_employees': 125,
                 'cost_per_hour': 45,
                 'downtime_hours': 3}

# Sample residential model data
RESIDENTIAL_DATA = {'outage_id': 'test1',
                    'total_residents': 827,
                    'median_income': 50000,
                    'downtime_hours': 1.5}

def estimateResidentialProductivity(residential_dict):
    """A method to quantify residential productivity cost.
       Assume all residents in a given area are impacted.
    """    
    hourly_wage = residential_dict['median_income'] / 2080 # determine median hourly wage based on annual salary
    return residential_dict['total_residents']*hourly_wage*residential_dict['downtime_hours']

def estimateEmployeeProductivity(employee_dict):
    """A method to quantify employee productivity cost"""    
    percentage_affected = employee_dict['affected_employees']/employee_dict['total_employees'] # percentage of the affected employees
    return employee_dict['total_employees']*percentage_affected*employee_dict['cost_per_hour']*employee_dict['downtime_hours']

def estimateBroadbandBenefits(residential, commercial):
    """Broadband benefit estimation based on residential and commercial data"""
    return estimateResidentialProductivity(residential) + estimateEmployeeProductivity(commercial)

def main():
    employee_productivity = estimateEmployeeProductivity(EMPLOYEE_DATA)
    broadbandbenefits = estimateBroadbandBenefits(RESIDENTIAL_DATA, EMPLOYEE_DATA)
    print('Employee productivity cost for internet outage', EMPLOYEE_DATA['outage_id'] ,'is estimated at:', '$'+str(employee_productivity))
    print('Total community cost for internet outage', EMPLOYEE_DATA['outage_id'] ,'is estimated at:', "$"+str(broadbandbenefits))
    
if __name__ == "__main__":
    main()