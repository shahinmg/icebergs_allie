### allie icebergs

I have saved Sid's iceberg data as [geoparquet](https://geoparquet.org/) files due to their speed and storage efficiency. These can be read with [geopandas](https://geopandas.org/en/stable/) and in QGIS. Though to use with QGIS, you need to have it compiled with a version of GDAL > 3.6 and the libgdal-arrow-parquet plugin. I created two yml files that will create two seperate conda environments. One for QGIS and one for geopandas. I try not to mess with my conda environments where QGIS is installed which is why we are installing two environments. To make these environemts, you first need to install [anaconda](https://www.anaconda.com/download) if you don't already have it installed.

## 1) Clone the repo
Open a terminal or anaconda prompt if on Windows then follow the commands below

```
git clone https://github.com/shahinmg/icebergs_allie.git
```
and cd to the directory 
```
cd icebergs_allie
```
## Create QGIS environment

Note: Be patient. These may take some time
```
conda env create --file qgis_environment.yml
```

to run the new qgis install first activate the environment

```
conda activate qgis
```

then run the qgis command
```
qgis
```

## Create geopandas environment
Now we need to make a seperate environment to work with the data in python. Run the command below to creat the new environment 

```
conda env create --file icebergs.yml
```

```
conda activate icebergs
```



## Visualize the data

Since the data is quite large, we should use the library [polars](https://docs.pola.rs/). We will use the `scan_parquet` method to read our data, use grouby to sort the data by date and then take the sum of the area. Use the `polars_plot.py` to make the figure in the `figs` directory. Place the parquet files in the `geo_parquets` directory to run the script.

