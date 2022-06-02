import calendar

import xarray as xr
import cartopy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cmocean
import geopandas as gp
import numpy as np

import spatial_selection


nrm_clusters = gp.read_file('/g/data/xv83/dbi599/shapefiles/NRM_clusters/NRM_clusters.shp')
nrm_sub_clusters = gp.read_file('/g/data/xv83/dbi599/shapefiles/NRM_sub_clusters/NRM_sub_clusters.shp')

def compare_agcd_gcm_rcm(
    agcd_da,
    parent_da,
    var_name,
    metric_name,
    parent_name,
    rcm_name,
    start_date,
    end_date,
    data_levels,
    diff_levels,
    rcm_da=None,
):
    """Creating a plot comparing RCM and parent GCM data to observations."""

    if var_name == 'pr':
        data_cmap = cmocean.cm.haline_r
        diff_cmap = 'BrBG'
        var_long_name = 'precipitation'
    elif var_name == 'tasmax':
        data_cmap = 'hot_r'
        diff_cmap = 'RdBu_r'
        var_long_name = 'daily maximum temperature'
    else:
        ValueError(f'Unrecognised variable {var_name}')
        
    if metric_name == 'annual-clim':
        metric_long_name = f'Annual mean {var_long_name}'
    else:
        ValueError(f'Unrecognised metric {metric}')
    
    fig = plt.figure(figsize=[20, 13])

    ax1 = fig.add_subplot(231, projection=ccrs.PlateCarree())
    agcd_da.plot(
        ax=ax1,
        transform=ccrs.PlateCarree(),
        cmap=data_cmap,
        levels=data_levels,
        extend='max',
        cbar_kwargs = {'orientation': 'horizontal', 'label': 'mm/year'}
    )
    ax1.set_title(f'{metric_long_name} (AGCD)')

    ax2 = fig.add_subplot(232, projection=ccrs.PlateCarree())
    parent_da.plot(
        ax=ax2,
        transform=ccrs.PlateCarree(),
        cmap=data_cmap,
        levels=data_levels,
        extend='max',
        cbar_kwargs = {'orientation': 'horizontal', 'label': 'mm/year'}
    )
    ax2.set_title(f'{metric_long_name} ({parent_name})')

    ax3 = fig.add_subplot(233, projection=ccrs.PlateCarree())
    parent_diff = parent_da - agcd_da
    parent_diff.plot(
        ax=ax3,
        transform=ccrs.PlateCarree(),
        cmap=diff_cmap,
        levels=diff_levels,
        extend='both',
        cbar_kwargs = {'orientation': 'horizontal', 'label': 'mm/year'}
    )
    ax3.set_title(f'Difference ({parent_name} - AGCD)')

    ax5 = fig.add_subplot(235, projection=ccrs.PlateCarree())
    if type(rcm_da) == xr.core.dataarray.DataArray:
        rcm_da.plot(
            ax=ax5,
            transform=ccrs.PlateCarree(),
            cmap=data_cmap,
            levels=data_levels,
            extend='max',
            cbar_kwargs = {'orientation': 'horizontal', 'label': 'mm/year'}
        )
    ax5.set_title(f'{metric_long_name} ({rcm_name}-{parent_name})')

    ax6 = fig.add_subplot(236, projection=ccrs.PlateCarree())
    if type(rcm_da) == xr.core.dataarray.DataArray:
        rcm_diff = rcm_da - agcd_da
        rcm_diff.plot(
            ax=ax6,
            transform=ccrs.PlateCarree(),
            cmap=diff_cmap,
            levels=diff_levels,
            extend='both',
            cbar_kwargs = {'orientation': 'horizontal', 'label': 'mm/year'}
        )
    ax6.set_title(f'Difference ({rcm_name}-{parent_name} - AGCD)')

    ax_list = [ax1, ax2, ax3]
    if type(rcm_da) == xr.core.dataarray.DataArray:
        ax_list = ax_list + [ax5, ax6]
    for ax in ax_list:
        ax.coastlines()
        ax.add_feature(cartopy.feature.STATES, linewidth=0.3)

    outfile = f'/g/data/xv83/dbi599/model-evaluation/{var_name}_{metric_name}_{rcm_name}-{parent_name}_{start_date}_{end_date}.png'
    plt.savefig(outfile, bbox_inches='tight', facecolor='white', dpi=300)
    print(outfile)

    
def temporal_evaluation(
    parent_monthly_clim,
    agcd_monthly_clim,
    var_name,
    parent_name,
    rcm_name,
    start_date,
    end_date,
    rcm_monthly_clim=None,
    clusters=False,
    std_ratio_levels=[0.25, 0.5, 0.67, 0.8, 1.0, 1.25, 1.5, 2.0, 4.0],
):
    """Plot assessment of phase and amplitude of seasonal cycle"""

    parent_corr = xr.corr(parent_monthly_clim, agcd_monthly_clim, dim='month') 
    parent_std = parent_monthly_clim.std(dim='month', keep_attrs=True)
    agcd_std = agcd_monthly_clim.std(dim='month', keep_attrs=True)
    parent_std_ratio = parent_std / agcd_std
    if type(rcm_monthly_clim) == xr.core.dataarray.DataArray:
        rcm_corr = xr.corr(rcm_monthly_clim, agcd_monthly_clim, dim='month') 
        rcm_std = rcm_monthly_clim.std(dim='month', keep_attrs=True)
        rcm_std_ratio = rcm_std / agcd_std
    
    fig = plt.figure(figsize=[14, 14])

    ax1 = fig.add_subplot(221, projection=ccrs.PlateCarree())
    parent_corr.plot(
        ax=ax1,
        transform=ccrs.PlateCarree(),
        cmap='RdBu_r',
        vmax=1,
        vmin=-1,
        cbar_kwargs = {'orientation': 'horizontal', 'label': 'corrrelation'}
    )
    ax1.set_title(f'Temporal correlation ({parent_name} vs. AGCD)')

    ax2 = fig.add_subplot(222, projection=ccrs.PlateCarree())
    parent_std_ratio.plot(
        ax=ax2,
        transform=ccrs.PlateCarree(),
        cmap='RdBu_r',
        levels=std_ratio_levels,
    extend='both',
    cbar_kwargs = {'orientation': 'horizontal', 'label': 'stdev ratio'}
    )
    ax2.set_title(f'Temporal standard deviation ratio ({parent_name} vs. AGCD)')
    
    ax3 = fig.add_subplot(223, projection=ccrs.PlateCarree())
    if type(rcm_monthly_clim) == xr.core.dataarray.DataArray:
        rcm_corr.plot(
            ax=ax3,
            transform=ccrs.PlateCarree(),
            cmap='RdBu_r',
            vmax=1,
            vmin=-1,
            cbar_kwargs = {'orientation': 'horizontal', 'label': 'corrrelation'}
        )   
    ax3.set_title(f'Temporal correlation ({rcm_name}-{parent_name} vs. AGCD)')

    ax4 = fig.add_subplot(224, projection=ccrs.PlateCarree())
    if type(rcm_monthly_clim) == xr.core.dataarray.DataArray:
        rcm_std_ratio.plot(
            ax=ax4,
            transform=ccrs.PlateCarree(),
            cmap='RdBu_r',
            levels=std_ratio_levels,
            extend='both',
            cbar_kwargs = {'orientation': 'horizontal', 'label': 'stdev ratio'}
        )
    ax4.set_title(f'Temporal standard deviation ratio ({rcm_name}-{parent_name} vs. AGCD)')

    ax_list = [ax1, ax2]
    if type(rcm_monthly_clim) == xr.core.dataarray.DataArray:
        ax_list = ax_list + [ax3, ax4]
    for ax in ax_list:
        ax.coastlines()
        if clusters:
            ax.add_geometries(nrm_sub_clusters.geometry, ccrs.PlateCarree(), facecolor='none', edgecolor='black')
        ax.add_feature(cartopy.feature.STATES, linewidth=0.3)
    #plt.suptitle(title)
    outfile = f'/g/data/xv83/dbi599/model-evaluation/{var_name}_seasonal-cycle_{rcm_name}-{parent_name}_{start_date}_{end_date}.png'
    plt.savefig(outfile, bbox_inches='tight', facecolor='white', dpi=300)
    print(outfile)
    

def seasonal_cycle(
    parent_monthly_clim,
    agcd_monthly_clim,
    parent_name,
    rcm_monthly_clim=None,
    rcm_name=None,
    cluster_name=None,
    latlon_point=None,
    latlon_name=None
):
    """Plot seasonal cycle for a given grid point or NRM cluster"""
    
    if cluster_name:
        if cluster_name in nrm_clusters['label'].values:
            cluster = nrm_clusters[nrm_clusters['label'] == cluster_name]
        elif cluster_name in nrm_sub_clusters['label'].values:
            cluster = nrm_sub_clusters[nrm_sub_clusters['label'] == cluster_name]
        else:
            raise ValueError(f'{cluster_name} is not valid cluster name')
        parent_cycle = spatial_selection.select_shapefile_regions(parent_monthly_clim, cluster, agg='weighted_mean')
        agcd_cycle = spatial_selection.select_shapefile_regions(agcd_monthly_clim, cluster, agg='weighted_mean')
        title = cluster_name
        if type(rcm_monthly_clim) == xr.core.dataarray.DataArray:
            rcm_cycle = spatial_selection.select_shapefile_regions(rcm_monthly_clim, cluster, agg='weighted_mean')
    elif latlon_point:
        parent_cycle = spatial_selection.select_point_region(parent_monthly_clim, latlon_point)
        agcd_cycle = spatial_selection.select_point_region(agcd_monthly_clim, latlon_point)
        title = latlon_name
        if type(rcm_monthly_clim) == xr.core.dataarray.DataArray:
            rcm_cycle = spatial_selection.select_point_region(rcm_monthly_clim, latlon_point)

    parent_cycle.plot(label=parent_name)
    agcd_cycle.plot(label='AGCD')
    if type(rcm_monthly_clim) == xr.core.dataarray.DataArray:
        rcm_cycle.plot(label=rcm_name)
    xticks = np.arange(1,13)
    xlabels = [calendar.month_abbr[i] for i in xticks]
    plt.xticks(xticks, xlabels)
    plt.legend()
    plt.ylabel('average precipitation (mm/month)')
    plt.title(title)
    plt.show()
