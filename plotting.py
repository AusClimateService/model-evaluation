import calendar
import string

import xarray as xr
import cartopy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cmocean
import geopandas as gp
import numpy as np
import matplotlib as mpl
from matplotlib import gridspec

import spatial_selection


mpl.rcParams['axes.labelsize'] = 'x-large'
mpl.rcParams['axes.titlesize'] = 'xx-large'
mpl.rcParams['xtick.labelsize'] = 'large'
mpl.rcParams['ytick.labelsize'] = 'x-large'
mpl.rcParams['legend.fontsize'] = 'x-large'

nrm_clusters = gp.read_file('/g/data/xv83/dbi599/shapefiles/NRM_clusters/NRM_clusters.shp')
nrm_sub_clusters = gp.read_file('/g/data/xv83/dbi599/shapefiles/NRM_sub_clusters/NRM_sub_clusters.shp')

data_cmap_dict = {
    ('tasmax', 'annual-clim'): 'hot_r',
    ('tasmax', 'txx'): 'hot_r',
    ('tasmax', 'txn'): cmocean.cm.ice,
    ('tasmax', 'wsdi'): 'hot_r',
    ('tasmin', 'tr'): 'hot_r',
    ('tasmin', 'annual-clim'): cmocean.cm.ice,
    ('tasmin', 'csdi'): cmocean.cm.ice_r,
    ('tasmin', 'fd'): cmocean.cm.ice_r,
    ('pr', 'annual-clim'): cmocean.cm.haline_r,
    ('pr', 'rx1day'): cmocean.cm.haline_r,
    ('pr', 'r95ptot'): cmocean.cm.haline_r,
    ('pr', 'r10mm'): cmocean.cm.haline_r,
    ('pr', 'cdd'): cmocean.cm.haline,
    ('pr', 'cwd'): cmocean.cm.haline_r,
}

diff_cmap_dict = {
    ('tasmax', 'annual-clim'): 'RdBu_r',
    ('tasmax', 'txx'): 'RdBu_r',
    ('tasmax', 'txn'): 'RdBu_r',
    ('tasmax', 'wsdi'): 'RdBu_r',
    ('tasmin', 'annual-clim'): 'RdBu_r',
    ('tasmin', 'tr'): 'RdBu_r',
    ('tasmin', 'csdi'): 'RdBu',
    ('tasmin', 'fd'): 'RdBu',
    ('pr', 'annual-clim'): 'BrBG',
    ('pr', 'rx1day'): 'BrBG',
    ('pr', 'r95ptot'): 'BrBG',
    ('pr', 'cdd'): 'BrBG_r',
    ('pr', 'cwd'): 'BrBG',
    ('pr', 'r10mm'): 'BrBG',
}

units_dict = {
    ('tasmax', 'annual-clim'): 'degrees (C)',
    ('tasmax', 'txx'): 'degrees (C)',
    ('tasmax', 'txn'): 'degrees (C)',
    ('tasmax', 'wsdi'): 'days',
    ('tasmin', 'annual-clim'): 'degrees (C)',
    ('tasmin', 'tr'): 'days',
    ('tasmin', 'csdi'): 'days',
    ('tasmin', 'fd'): 'days',
    ('pr', 'annual-clim'): 'mm/year',
    ('pr', 'rx1day'): 'mm/day',
    ('pr', 'r95ptot'): '%',
    ('pr', 'r10mm'): 'days',
    ('pr', 'cdd'): 'days',
    ('pr', 'cwd'): 'days',
}

title_dict = {
    ('tasmax', 'annual-clim'): 'Annual mean daily maximum temperature',
    ('tasmax', 'txx'): 'Annual mean maximum daily maximum temperature (TXx)',
    ('tasmax', 'txn'): 'Annual mean minimum daily maximum temperature (TXn)',
    ('tasmax', 'wsdi'): 'Warm spell duration index (WSDI)',
    ('tasmin', 'annual-clim'): 'Annual mean daily minimum temperature',
    ('tasmin', 'csdi'): 'Cold spell duration index (WSDI)',
    ('tasmin', 'fd'): 'Annual mean number of frost days (Tmin < 0C; FD)',
    ('tasmin', 'tr'): 'Annual mean number of tropical nights (Tmin > 20C; TR)',
    ('pr', 'annual-clim'): 'Total annual precipitation',
    ('pr', 'rx1day'): 'Annual mean maximum 1-day precipitation (RX1day)',
    ('pr', 'r95ptot'): 'Annual mean total precipitation from heavy rain (r95ptot)',
    ('pr', 'r10mm'): 'Annual mean number of heavy rainfall days (r10mm)',
    ('pr', 'cdd'): 'Annual mean maximum consecutive dry days (<1mm; CDD)',
    ('pr', 'cwd'): 'Annual mean maximum consecutive wet days (>1mm; CWD)',
}

sub_cluster_list = [
    'Monsoonal North (West)', 'Wet Tropics', 'Monsoonal North (East)', 'East Coast (North)',
    'Rangelands (North)', 'Rangelands (South)', 'Central Slopes', 'East Coast (South)',
    'Southern and South Western Flatlands (West)', 'Southern and South Western Flatlands (East)', 'Murray Basin', '',
    'Southern Slopes (Vic West)', 'Southern Slopes (Vic/NSW East)', 'Southern Slopes (Tas West)', 'Southern Slopes (Tas East)'
]


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

    data_cmap = data_cmap_dict[(var_name, metric_name)]
    diff_cmap = diff_cmap_dict[(var_name, metric_name)]
    units = units_dict[(var_name, metric_name)]
    title = title_dict[(var_name, metric_name)]
        
    fig = plt.figure(figsize=[20, 13])

    ax1 = fig.add_subplot(231, projection=ccrs.PlateCarree())
    agcd_da.plot(
        ax=ax1,
        transform=ccrs.PlateCarree(),
        cmap=data_cmap,
        levels=data_levels,
        extend='max',
        cbar_kwargs = {'orientation': 'horizontal', 'label': units}
    )
    ax1.set_title('(a) AGCD')

    ax2 = fig.add_subplot(232, projection=ccrs.PlateCarree())
    parent_da.plot(
        ax=ax2,
        transform=ccrs.PlateCarree(),
        cmap=data_cmap,
        levels=data_levels,
        extend='max',
        cbar_kwargs = {'orientation': 'horizontal', 'label': units}
    )
    ax2.set_title(f'(b) {parent_name}')

    ax3 = fig.add_subplot(233, projection=ccrs.PlateCarree())
    parent_diff = parent_da - agcd_da
    parent_diff.plot(
        ax=ax3,
        transform=ccrs.PlateCarree(),
        cmap=diff_cmap,
        levels=diff_levels,
        extend='both',
        cbar_kwargs = {'orientation': 'horizontal', 'label': units}
    )
    ax3.set_title(f'Difference:\n(c) {parent_name} - AGCD')

    ax5 = fig.add_subplot(235, projection=ccrs.PlateCarree())
    if type(rcm_da) == xr.core.dataarray.DataArray:
        rcm_da.plot(
            ax=ax5,
            transform=ccrs.PlateCarree(),
            cmap=data_cmap,
            levels=data_levels,
            extend='max',
            cbar_kwargs = {'orientation': 'horizontal', 'label': units}
        )
    ax5.set_title(f'(d) {rcm_name}-{parent_name}')

    ax6 = fig.add_subplot(236, projection=ccrs.PlateCarree())
    if type(rcm_da) == xr.core.dataarray.DataArray:
        rcm_diff = rcm_da - agcd_da
        rcm_diff.plot(
            ax=ax6,
            transform=ccrs.PlateCarree(),
            cmap=diff_cmap,
            levels=diff_levels,
            extend='both',
            cbar_kwargs = {'orientation': 'horizontal', 'label': units}
        )
    ax6.set_title(f'Difference:\n(e) {rcm_name}-{parent_name} - AGCD')

    ax_list = [ax1, ax2, ax3]
    if type(rcm_da) == xr.core.dataarray.DataArray:
        ax_list = ax_list + [ax5, ax6]
    for ax in ax_list:
        ax.coastlines()
        ax.add_feature(cartopy.feature.STATES, linewidth=0.3)
    plt.suptitle(title, fontsize='xx-large', y=0.95)
        
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
    ax1.set_title(f'(a) Temporal correlation:\n{parent_name} vs. AGCD')

    ax2 = fig.add_subplot(222, projection=ccrs.PlateCarree())
    parent_std_ratio.plot(
        ax=ax2,
        transform=ccrs.PlateCarree(),
        cmap='RdBu_r',
        levels=std_ratio_levels,
    extend='both',
    cbar_kwargs = {'orientation': 'horizontal', 'label': 'stdev ratio'}
    )
    ax2.set_title(f'(b) Temporal standard deviation ratio:\n{parent_name} vs. AGCD')
    
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
    ax3.set_title(f'(c) Temporal correlation:\n{rcm_name}-{parent_name} vs. AGCD')

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
    ax4.set_title(f'(d) Temporal standard deviation ratio:\n{rcm_name}-{parent_name} vs. AGCD')

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
    

def seasonal_clusters(
    var_name,
    parent_monthly_clim,
    agcd_monthly_clim,
    rcm_monthly_clim,
    start_date,
    end_date,
):
    """Plot seasonal cycle for eahc NRM sub-cluster"""

    if var_name == 'pr':
        ylabel = 'average precipitation (mm/month)'
    elif var_name == 'tasmax':
        ylabel = 'average daily maximum temperature (C)'
    elif var_name == 'tasmin':
        ylabel = 'average daily minimum temperature (C)'
    else:
        raise ValueError(f'No defaults defined for variable {var}')
    
    parent_cycle = spatial_selection.select_shapefile_regions(
        parent_monthly_clim,
        nrm_sub_clusters,
        header='label',
        agg='weighted_mean'
    )

    agcd_cycle = spatial_selection.select_shapefile_regions(
        agcd_monthly_clim,
        nrm_sub_clusters,
        header='label',
        agg='weighted_mean',
    )

    rcm_cycle = spatial_selection.select_shapefile_regions(
        rcm_monthly_clim,
        nrm_sub_clusters,
        header='label',
        agg='weighted_mean'
    )
    
    xticks = np.arange(1,13)
    xlabels = [calendar.month_abbr[i] for i in xticks]

    fig = plt.figure(figsize=[38, 30])
    gs = gridspec.GridSpec(4, 4)
    for plot_num, cluster_name in enumerate(sub_cluster_list):
        if cluster_name:
            ax = plt.subplot(gs[plot_num])
            agcd_cycle.sel({'region': cluster_name}).plot(ax=ax, label='AGCD', color='black')
            parent_cycle.sel({'region': cluster_name}).plot(ax=ax, label='ACCESS-CM2')
            rcm_cycle.sel({'region': cluster_name}).plot(ax=ax, label='BARPA')
            ax.set_xticks(xticks, xlabels)
            ax.legend()
            ax.set_ylabel(ylabel)
            letter = string.ascii_lowercase[plot_num]
            ax.set_title(f'({letter}) {cluster_name}')
    outfile = f'/g/data/xv83/dbi599/model-evaluation/{var_name}_seasonal-cycle-nrm_BARPA-ACCESS-CM2_{start_date}_{end_date}.png'
    plt.savefig(outfile, bbox_inches='tight', facecolor='white', dpi=300)
    print(outfile)
