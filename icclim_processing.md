# ICCLIM processing

This file maintains a list of Obs (AGCDv1), reanalysis (ERA5), GCMs and downscaled runs which have been or are being processed using [icclim](https://github.com/AusClimateService/indices)

For historical GCM/RCM data, period used is 19790101-20141231

For AGCD/ERA5 and CCAM-ERA5, period used is 19790101-20211231

For percentile indices (#16: TX10p, TX90p, TN10p, TN90p, TG10p, TG90p, R75p, R75pTOT, R95p, R95pTOT, R99p, R99pTOT, CD, CW, WD, WW), period used is 19850101-20141231

See [indices.md](https://github.com/AusClimateService/model-evaluation/blob/master/indices.md) for a full table and documentation

### Observations & Reanalysis
| Model | Realisation | Processed | QC | Location | Person responsible | Notes |
| - | - | - | - | - | - | - |
| AGCDv1 | - | :heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/AUS-r005/none/BOM-AGCD/historical/none/none/v1/climdex` | @ngben | Missing tas |
| ERA5 | - | :heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/AUS-25/none/ECMWF-ERA5/historical/none/none/v1/climdex` | @ngben | - |

### GCMs
| Model | Realisation | Processed | QC | Location | Person responsible | Notes |
| - | - | - | - | - | - | - |
| ACCESS-CM2 | r4i1p1f1 | :heavy_check_mark: | :x: | - | @ngben | - |
| ACCESS-ESM1-5 | r6i1p1f1 | :heavy_check_mark: | :x: | - | @ngben | - |
| CESM2 | r11i1p1f1 | :x: | :x: | - | @ngben | Missing daily tasmax and tasmin |
| CMCC-ESM2 | r1i1p1f1 | :x: | :x: | - | @ngben | Error in icclim, issue raised |
| CNRM-ESM2-1 | r1i1p1f2 | :heavy_check_mark: | :x: | - | @ngben | - |
| EC-Earth3 | r1i1p1f1 | :heavy_check_mark: | :x: | - | @ngben | - |
| NorESM2-MM | r1i1p1f1 | :x: | :x: | - | @ngben | Error in icclim, issue raised |

### CCAM
| Model | Realisation | Processed | QC | Location | Person responsible | Notes |
| - | - | - | - | - | - | - |
| CCAM-ERA5 | - | :heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/AUS-10/CSIRO/ECMWF-ERA5/evaluation/none/CSIRO-CCAM-2203/v1/climdex` | @ngben | - |
| CCAM-NorESM2-MM | r1i1p1f1 | :heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/AUS-10/CSIRO/NCC-NorESM2-MM/historical/r1i1p1f1/CSIRO-CCAM-2203/v1/climdex/` | @ngben | - |
