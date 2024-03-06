#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:00:38 2024

@author: laserglaciers
"""

import geopandas as gpd
import os
import matplotlib.pyplot as plt
import gc

path = '../geo_parquets/'
file_list = sorted([file for file in os.listdir(path) if file.endswith('parquet')])

fig, ax = plt.subplots()

os.chdir(path)
for file in file_list:
    label = file[:3]
    df = gpd.read_parquet(file)

    # df.groupby(['date'])['AreaRF_m2'].sum()
    
    df.groupby(['date'])['AreaRF_m2'].sum().plot(ax=ax,label=label)
    # # Delete the old DataFrame
    # del df
     
    # # Perform garbage collection
    # gc.collect()

ax.legend()
ax.set_title('NW1 Iceberg Area')
ax.set_ylabel=('m$^2$')
fig_path = '..figs/'
plt.savefig(f'{fig_path}iceberg_area_time_series.png', dpi=300)