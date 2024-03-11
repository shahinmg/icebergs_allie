#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:10:21 2024

@author: laserglaciers
"""

import polars as pl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

path = '../out_geoparquet/'
file_list = [file for file in os.listdir(path) if file.endswith('parquet')] 

os.chdir(path)
fig, ax = plt.subplots(figsize=(10,8))
labels =[]
csv_path = '/media/laserglaciers/upernavik/sid_data/icebergs_allie/filter_count_len_csvs/'
# for each file lazily evaulate each parquet. Groupby date and get the sum.
# Then turn to pandas data frame and plot
filter_size = 10000
for file in file_list:
    label = file[:3]
    labels.append(label)
    # df = pl.scan_parquet(file) # scan parquet file reads large data faster
    q = (
        pl.scan_parquet(file) # scan parquet file reads large data faster
        .lazy() #https://towardsdatascience.com/what-is-lazy-evaluation-in-python-9efb1d3bfed0#:~:text=If%20you've%20never%20heard,strategy%20to%20optimize%20your%20code.
        .filter(pl.col("AreaRF_m2")>=filter_size)
        .group_by('date').agg(pl.len().alias('gt_value'))
        ) 
    df_group = q.collect()
    
    df_pd = df_group.to_pandas()
    df_pd.set_index('date',inplace=True)
    df_pd.sort_index(inplace=True)
    df_pd.plot(ax=ax,label=label,legend=False)
    
    csv_out_file = f'{csv_path}/{label}_gte_{filter_size}.csv'
    df_pd.to_csv(csv_out_file)
    
ax.legend(labels)
ax.set_ylabel('iceberg count')
ax.grid(linestyle='--')
ax.set_title('Number of icebergs >= {filter_size}')

plt.savefig(f'../figs/icebergs_gte_{filter_size}',dpi=300)
