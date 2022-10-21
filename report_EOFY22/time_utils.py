import xarray as xr


def temporal_aggregation(
    ds,
    target_freq,
    agg_method,
    variables,
    input_freq=None,
    complete=False,
):
    """Temporal aggregation of data.
    
    Parameters
    ----------
    ds : xarray Dataset
    target_freq : {'A', 'Q-NOV', 'M'}
        Target frequency for the resampling
    agg_method : {'mean', 'min', 'max', 'sum'}
        Aggregation method
    variables : list
        Variables in the dataset to process
    input_freq : {'D', 'M', 'Q', 'A'}
        Temporal frequency of input data (daily, monthly or annual)
    complete : bool, default False
        Keep only complete time periods (e.g. complete years or months)
        
    Returns
    -------
    ds : xarray Dataset

    Notes
    -----
    target frequencies:
        A = annual, with date label being last day of year
    Q-NOV = seasonal (DJF, MAM, JJA, SON), with date label being last day of season
        M = monthly, with date label being last day of month
    """

    assert target_freq in ["A", "Q-NOV", "M"]

    if not input_freq:
        input_freq = xr.infer_freq(ds.indexes["time"])   
    assert input_freq in ["D", "M", "Q", "A"]

    counts = ds[variables[0]].resample(time=target_freq).count(dim="time")

    if input_freq == target_freq[0]:
        pass
    elif agg_method == "max":
        ds = ds.resample(time=target_freq).max(dim="time", keep_attrs=True)
    elif agg_method == "min":
        ds = ds.resample(time=target_freq).min(dim="time", keep_attrs=True)
    elif agg_method == "sum":
        ds = ds.resample(time=target_freq).sum(dim="time", keep_attrs=True)
    elif agg_method == "mean":
        if input_freq == "D":
            ds = ds.resample(time=target_freq).mean(dim="time", keep_attrs=True)
        elif input_freq == "M":
            ds = _monthly_downsample_mean(ds, target_freq, variables)
        else:
            raise ValueError(f"Unsupported input time frequency: {input_freq}")
    else:
        raise ValueError(f"Unsupported temporal aggregation method: {agg_method}")

    if complete:
        ds = _crop_to_complete_time_periods(ds, counts, input_freq, target_freq)

    return ds


def _crop_to_complete_time_periods(ds, counts, input_freq, output_freq):
    """Crop an aggregated xarray dataset to include only complete time periods.
    
    Parameters
    ----------
    ds : xarray DataArray or Dataset
        Temporally aggregated data
    counts : xarray DataArray
        Number of samples in each aggregation
    input_freq : {'D, 'M'}
        Time frequency before temporal aggregation
    output_freq : {'A', 'Q-NOV', 'M'}
        Time frequency after temporal aggregation

    Returns
    -------
    ds : xarray DataArray or Dataset
        Temporally aggregated data with only complete time periods retained
    """

    assert input_freq in ["D", "M"]
    assert output_freq in ["A", "Q-NOV", "M"]

    # to X from X
    count_dict = {
        ("A", "D"): 360,
        ("A", "M"): 12,
        ("M", "D"): 28,
        ("Q", "M"): 3,
        ("Q", "D"): 89,
    }
    min_sample = count_dict[(output_freq[0], input_freq)]
    ds = ds.where(counts.values >= min_sample)
    ds = ds.dropna("time")
    
    return ds


def ndays_weighted_mean(da, target_freq):
    """Calculate mean where each value is weighted by number of days"""
    
    days_in_month = da["time"].dt.days_in_month
    sum_weighted_by_days = (da * days_in_month).resample(time=target_freq).sum(dim="time", keep_attrs=True)
    n_days = days_in_month.resample(time=target_freq).sum(dim="time")
    weighted_mean = sum_weighted_by_days / n_days
    weighted_mean.attrs = da.attrs
    
    return weighted_mean


def _monthly_downsample_mean(ds, target_freq, variables):
    """Downsample monthly data (e.g. to seasonal or annual mean).

    Accounts for the different number of days in each month.
    """

    assert type(ds) == xr.core.dataset.Dataset
    var0 = variables[0]
    downsample_mean = ndays_weighted_mean(ds[var0], target_freq)
    downsample_mean = downsample_mean.to_dataset(name=var0)
    for var in variables[1:]:
        downsample_mean[var] = ndays_weighted_mean(ds[var], target_freq)
    downsample_mean.attrs = ds.attrs
        
    return downsample_mean