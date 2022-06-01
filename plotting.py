import xarray as xr
import cartopy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cmocean


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