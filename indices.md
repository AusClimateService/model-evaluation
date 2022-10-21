# Indices

This file maintains a list of the xclim/icclim/climpact indices required for CCAM evaluation.

#### List of indicators for each package
- xclim indices: https://xclim.readthedocs.io/en/stable/indicators.html
- icclim indices: https://icclim.readthedocs.io/en/stable/explanation/climate_indices.html#icclim-capabilities
- climpact indices: https://github.com/ARCCSS-extremes/climpact/blob/master/www/user_guide/Climpact_user_guide.md#appendixa

(Note: view raw to see markdown table formatting.)

### Temperature indices
| Index | Description | xclim | icclim | Climpact | Hazard | Notes |
| - | - | - | - | - | - | - |
| txn | Coldest daily maximum temperature | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - | - |
| txx | Warmest daily maximum temperature | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | Heatwaves, bushfires, extreme temperature | - |
| txm | Mean daily maximum temperature | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - | Defined as ```tx``` in icclim |
| tx10p | Percentage of days when daily maximum temperature is less than 10th percentile | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - | xclim doesn't calculate percentiles, percentile needs to be pre-calculated as a DataArray and fed into function. <br>xclim defines ```tx10p``` as number of days, climpact defines it as percentage, need to check icclim output |
| tx90p | Percentage of days when daily maximum temperature is greater than 90th percentile | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | Heatwaves, bushfires, extreme temperature | xclim doesn't calculate percentiles, percentile needs to be pre-calculated as a DataArray and fed into function. <br>xclim defines ```tx90p``` as number of days, climpact defines it as percentage, need to check icclim output |
| tnn | Coldest daily minimum temperature | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - | - |
| tnx | Warmest daily minimum temperature | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - | - |
| tnm | Mean daily minimum temperature | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - | Defined as ```tn``` in icclim |
| tn10p | Percentage of days when daily minimum temperature is less than 10th percentile | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - | xclim doesn't calculate percentiles, percentile needs to be pre-calculated as a DataArray and fed into function. <br>xclim defines ```tn10p``` as number of days, climpact defines it as percentage, need to check icclim output |
| tn90p | Percentage of days when daily minimum temperature is greater than 90th percentile | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - | xclim doesn't calculate percentiles, percentile needs to be pre-calculated as a DataArray and fed into function. <br>xclim defines ```tn90p``` as number of days, climpact defines it as percentage, need to check icclim output |
| tmm | Mean daily mean temperature | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - | Defined as ```tg``` in icclim |
| dtr | Daily temperature range | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - | - |
| hwn | Heatwave number | :heavy_check_mark: | - | :heavy_check_mark: | Heatwaves | Defined as ```heat wave frequency``` in xclim. xclim uses absolute values, climpact uses 90th percentile or excess heat factor |
| hwf | Heatwave frequency | - | - | :heavy_check_mark: | Heatwaves | - |
| hwd | Heatwave duration | :heavy_check_mark: | - | :heavy_check_mark: | Heatwaves | Defined as ```heat wave max length``` in xclim |
| hwm | Heatwave magnitude | - | - | :heavy_check_mark: | Heatwaves | - |
| hwa | Heatwave amplitude | - | - | :heavy_check_mark: | Heatwaves | - |

### Rainfall indices
| Index | Description | xclim | icclim | Climpact | Hazard | Notes |
| - | - | - | - | - | - | - |
| rx1day | Maximum 1 day precipitation | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | Heavy rainfall, floods | - |
| rx5day | Maximum 5 day precipitation | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | Heavy rainfall, floods | Some differences between xclim & climpact due to centering of 5-day period. By definition the window should be on the last day, need to use ```fclimdex.compatible=TRUE``` in ```climpact.ncdf.wrapper.r``` to get the same result in climpact as xclim. See also: https://search.r-project.org/CRAN/refmans/climdex.pcic/html/climdex.rx5day.html |
| r10mm | Number of days when rainfall is greater than or equal to 10mm | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | Heavy rainfall, floods | - |
| r20mm | Number of days when rainfall is greater than or equal to 20mm | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | Heavy rainfall, floods | - |
| r95p | Amount of rainfall from very wet days  | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | Heavy rainfall, floods | xclim doesn't calculate percentiles, percentile needs to be pre-calculated as a DataArray and fed into function |
| r99p | Amount of rainfall from extremely wet days  | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | Heavy rainfall, floods | As above |
| r95ptot | Fraction of total wet-day rainfall that comes from very wet days | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | Heavy rainfall, floods | As above |
| r99ptot | Fraction of total wet-day rainfall that comes from extremely wet days | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | Heavy rainfall, floods | As above |
| prcptot | Total precipitation | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - | - |
| cdd | Consecutive Dry Days | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | Drought | - |
| cwd | Consecutive Wet Days | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | Floods | - |
| sdii | Average daily wet-day rainfall intensity | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | - | - |


### Compound indices
| Index | Description | xclim | icclim | Climpact | Hazard | Notes |
| - | - | - | - | - | - | - |
| cd | Cold and dry days | :heavy_check_mark: | :heavy_check_mark: | - | - | Days with TG\tmm < 25th percentile of daily mean temperature and RR <25th percentile of daily precipitation sum (cold/dry days) |
| cw | Cold and wet days | :heavy_check_mark: | :heavy_check_mark: | - | - | Days with TG\tmm < 25th percentile of daily mean temperature and RR >75th percentile of daily precipitation sum (cold/wet days) |
| wd | Warm and dry days | :heavy_check_mark: | :heavy_check_mark: | - | - | Days with TG\tmm > 75th percentile of daily mean temperature and RR <25th percentile of daily precipitation sum (warm/dry days) |
| ww | Warm and wet days | :heavy_check_mark: | :heavy_check_mark: | - | - | Days with TG\tmm > 75th percentile of daily mean temperature and RR >75th percentile of daily precipitation sum (warm/wet days) |

... and so on.

---
### References
Below are some references for xclim, icclim, and climpact indices. Please see the [three indices lists](#list-of-indicators-for-each-package) above for specific index references

#### xclim
- European Climate Assessment & Dataset, https://www.ecad.eu/
- https://www.ecad.eu/documents/atbd.pdf

#### icclim
- https://icclim.readthedocs.io/en/stable/references/index.html

#### Climpact
- McKee T B, Doesken N J and Kleist J 1993 The relationship of drought frequency and duration to time scales Proceedings of the 8th Conference on Applied Climatology vol 17 (American Meteorological Society Boston, MA, USA) pp 179–83
- Nairn J R and Fawcett R G 2013 Defining heatwaves: heatwave defined as a heat-impact event servicing all community and business sectors in Australia (Centre for Australian Weather and Climate Research) Online: http://www.cawcr.gov.au/technical-reports/CTR_060.pdf
- Perkins S E and Alexander L V 2013 On the Measurement of heatwaves J. Clim. 26 4500–17 Online: http://dx.doi.org/10.1175/JCLI-D-12-00383.1
- Vicente-Serrano S M, Beguería S and López-Moreno J I 2010 A Multiscalar Drought Index Sensitive to Global Warming: The Standardized Precipitation Evapotranspiration Index J. Clim. 23 1696–718 Online: http://dx.doi.org/10.1175/2009JCLI2909.1
- WMO 2012 Standardized Precipitation Index User Guide (7 bis, avenue de la Paix – P.O. Box 2300 – CH 1211 Geneva 2 – Switzerland) Online: http://www.wamis.org/agm/pubs/SPI/WMO_1090_EN.pdf
- Zhang X, Alexander L, Hegerl G C, Jones P, Tank A K, Peterson T C, Trewin B and Zwiers F W 2011 Indices for monitoring changes in extremes based on daily temperature and precipitation data Wiley Interdiscip. Rev. Clim. Chang. 2 851–70 Online: https://onlinelibrary.wiley.com/doi/full/10.1002/wcc.147
