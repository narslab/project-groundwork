# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 08:18:26 2021

@author: Mahsa
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from scipy import stats
concord_projects_dict={'project_name':["2011_ug_conversion_project","west_concord_business_district","2010_ug_conversion_project","minuteman_heights_utility_project","emerson_underground_utility_project"],"cost":[741945.60,495950.40,503712,496161.60,1338849.60],"single_phase":[0,0,1,1,0]}
df_concord_projects=pd.DataFrame(concord_projects_dict)
print(df_concord_projects)
x = np.array([0,0,1,1,0]).reshape((-1, 1))
y = np.array([741945.60,495950.40,503712,496161.60,1338849.60])
#model = LinearRegression().fit(x, y)
#r_sq = model.score(x, y)
#print('coefficient of determination:', r_sq)
#%matplotlib inline
plt.xlabel('single phase status')
plt.ylabel('cost(M$)')
plt.scatter(df_concord_projects.single_phase, df_concord_projects.cost, color='red',marker='+')