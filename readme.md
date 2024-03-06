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

## Create geopandas environment
```
conda env create --file icebergs.yml
```
