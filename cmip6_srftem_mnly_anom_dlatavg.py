#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:41:55 2022

@author: jayanthikishore
"""

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import numpy.ma as ma
from scipy.optimize import curve_fit
import netCDF4 as nC4
import sys
import os
import re
import glob
from os import path
from netCDF4 import Dataset
from pylab import *
import statsmodels.api as sm
import fnmatch
from numpy import percentile
from scipy.interpolate import griddata
from datetime import datetime, timedelta
# ************************************************************************
prgname = 'cmip6_srftem_mnly_anom_dlatavg.py'
def pause():
    programPause = input("Press the <ENTER> key to continue...")
    
#CMIP6 surface temp. monthly
dirpath = '/home/jayanthikishore/Downloads/Preetham_work/Surface_temp/Results/'
ncfile = dirpath + 'CESM2_srftem_monthly_185001-201412_1x1_py.nc'

#loading netcdf file
nc = Dataset(ncfile)
# print(nc.variables)

lon = nc.variables['lon'][:]
lat = nc.variables['lat'][:]
dmonths = nc.variables['decmonths'][:]
srftem = nc.variables['srft'][:]
print(srftem.shape,lon.shape,lat.shape)

nln = len(lon)
nlt = len(lat)
mns = len(dmonths)
print(nln,nlt,mns)
print(dmonths)

#Date convesion (digital to year and month)
date1 = ['' for x in range(len(dmonths))]
for mn in range(mns):
    yrmndec = dmonths[mn]
    
    year = int(yrmndec)
    rem = yrmndec - year
    
    base = datetime(year, 1, 1)
    result = base + timedelta(seconds=(base.replace(year=base.year + 1) - base).total_seconds() * rem)
    date1[mn] = result.strftime('%Y-%m-%d')
    # print(mn+1,year,result, '    ',date1[mn])
# pause()    

print(date1)