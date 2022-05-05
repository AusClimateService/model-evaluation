import glob

import xarray as xr
import numpy as np
import xesmf as xe


# /g/data/ia39/aus-ref-clim-data-nci/cmip6-etccdi/data/v1-0/ for parent model indices


start_date = '1995-01-01'
end_date = '2014-12-31'

# NorESM2-MM

noresm_dates = ['19900101-19991231', '20000101-20091231', '20100101-20141231']
noresm_tmax_files = [f'/g/data/oi10/replicas/CMIP6/CMIP/NCC/NorESM2-MM/historical/r1i1p1f1/day/tasmax/gn/v20191108/tasmax_day_NorESM2-MM_historical_r1i1p1f1_gn_{dates}.nc' for dates in noresm_dates]
noresm_ds = xr.open_mfdataset(noresm_tmax_files)
noresm_ds = noresm_ds['tasmax'].sel({'time': slice(start_date, end_date)})

noresm_annual_clim = noresm_ds.mean('time', keep_attrs=True)
noresm_seasonal_clim = noresm_ds.groupby('time.season').mean('time', keep_attrs=True)
noresm_monthly_clim = noresm_ds.groupby('time.month').mean('time', keep_attrs=True)

# AGCD

agcd_years = np.arange(1995, 2015, 1)
agcd_tmax_files = [f'/g/data/xv83/agcd-csiro/tmax/tmax_AGCD-CSIRO_r005_{year}0101-{year}1231_daily.nc' for year in agcd_years]
agcd_ds = xr.open_mfdataset(agcd_tmax_files)
agcd_ds = agcd_ds['tmax'].sel({'time': slice(start_date, end_date)})

agcd_annual_clim = agcd_ds.mean('time', keep_attrs=True)
agcd_seasonal_clim = agcd_ds.groupby('time.season').mean('time', keep_attrs=True)
agcd_monthly_clim = agcd_ds.groupby('time.month').mean('time', keep_attrs=True)


noresm_regridder = xe.Regridder(noresm_ds, agcd_ds, "conservative")
noresm_annual_clim = regridder(noresm_annual_clim)
noresm_seasonal_clim = regridder(noresm_seasonal_clim)
noresm_monthly_clim = regridder(noresm_monthly_clim)

