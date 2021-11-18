# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 14:19:46 2021

@author: Mahsa
"""

import osmnx as ox
import networkx as nx
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
#ox.config(log_console=True, use_cache=True)
#ox.__version__
# Place name which is used to retrieve data from OSM
place_name = "Concord,MA, US"
#Retrieve the street network
graph = ox.graph_from_place(place_name)
type(graph)