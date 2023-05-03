# ICCLIM processing

This file maintains a list of Obs (AGCDv1), reanalysis (ERA5), GCMs and downscaled runs which have been or are being processed using [icclim](https://github.com/AusClimateService/indices)

### Issues (2023-02-20), currently waiting for icclim to fix
- R75pTOT/R95pTOT/R99pTOT in RCMs/GCMs (data with `kg m-2 s-1` units) have no/missing data
- DTR/vDTR/ETR are converted to `degC` after calculation, causing RCMs/GCMs (data with `degK` units) to be offset by -273.15
---
### Periods analysed
Follows periods outlined in [evaluation_standards.md](https://github.com/AusClimateService/ccam-evaluation/blob/main/evaluation_standards.md)

- Observations, reanalysis and evaluation runs
  - AGCD, ERA5, and CCAM-ERA5: `19790101-20211231`
  - BARPA-R-ERA5: `19790101-20201231`
  - Percentile indices (#16: TX10p, TX90p, TN10p, TN90p, TG10p, TG90p, R75p, R75pTOT, R95p, R95pTOT, R99p, R99pTOT, CD, CW, WD, WW): `19850101-20141231`

- Historical
  - GCM/RCM data: `19790101-20141231`
  - Percentile indices: `19850101-20141231`

- Future
  - GCM/RCM data: `20150101-21001231`
  - Percentile indices: 
    - Near: `20150101-20441231`
    - Mid: `20350101-20641231`
    - Far: `20700101-20991231`
---
### Additional information

See [indices.md](https://github.com/AusClimateService/model-evaluation/blob/master/indices.md) for a full table and documentation. Scripts used for calculation can be found [here](https://github.com/AusClimateService/ccam-evaluation/tree/main/bxn599/icclim_indices)

---
### Observations & Reanalysis
| Model | Processed | QC | Location | Person responsible | Notes |
| - | - | - | - | - | - |
| AGCDv1 | :heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/AUS-r005/none/BOM-AGCD/historical/none/none/none/climdex/` | @ngben | Missing `tas` |
| ERA5 | :heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/AUS-25/none/ECMWF-ERA5/historical/none/none/none/climdex/` | @ngben | - |

### GCMs
| Model | Processed | QC | Location | Person responsible | Notes |
| - | - | - | - | - | - |
| ACCESS-CM2 | Historical::heavy_check_mark:<br>SSP126::heavy_check_mark:<br>SSP370::heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/GLOBAL-gn/none/CSIRO-ARCCSS-ACCESS-CM2/` | @ngben | - |
| ACCESS-ESM1-5 | Historical::heavy_check_mark:<br>SSP126::heavy_check_mark:<br>SSP370::heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/GLOBAL-gn/none/CSIRO-ACCESS-ESM1-5/` | @ngben | - |
| CESM2  | Historical::heavy_check_mark:<br>SSP126::heavy_check_mark:<br>SSP370::heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/GLOBAL-gn/none/NCAR-CESM2/` | @ngben | `pr` and `tas` indices calculated, missing historical daily `tasmax` and `tasmin` |
| CMCC-ESM2 | Historical::heavy_check_mark:<br>SSP126::heavy_check_mark:<br>SSP370::heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/GLOBAL-gn/none/CMCC-CMCC-ESM2/` | @ngben | - |
| CNRM-ESM2-1 | Historical::heavy_check_mark:<br>SSP126::heavy_check_mark:<br>SSP370::heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/GLOBAL-gn/none/CNRM-CERFACS-CNRM-ESM2-1/` | @ngben | - |
| EC-Earth3 | Historical::heavy_check_mark:<br>SSP126::heavy_check_mark:<br>SSP370::heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/GLOBAL-gn/none/EC-Earth-Consortium-EC-Earth3/` | @ngben | - |
| NorESM2-MM | Historical::heavy_check_mark:<br>SSP126::heavy_check_mark:<br>SSP370::heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/GLOBAL-gn/none/NCC-NorESM2-MM/` | @ngben | - |

### CCAM
| Model | Processed | QC | Location | Person responsible | Notes |
| - | - | - | - | - | - |
| CCAM-ERA5 | :heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/AUS-10/CSIRO/ECMWF-ERA5/evaluation/none/CSIRO-CCAM-2203/v1/climdex/` | @ngben | - |
| CCAM-ACCESS-CM2 | Historical::x:<br>SSP126::x:<br>SSP370::x: | :x: | :x: | @ngben | - |
| CCAM-ACCESS-ESM1-5 | Historical::x:<br>SSP126::x:<br>SSP370::x: | :x: | :x: | @ngben | - |
| CCAM-CESM2 | Historical:running<br>SSP126::x:<br>SSP370::x: | :x: | :x: | @ngben | - |
| CCAM-CMCC-ESM2 | Historical:running<br>SSP126::x:<br>SSP370::x: | :x: | :x: | @ngben | - |
| CCAM-CNRM-ESM2-1 | Historical::x:<br>SSP126::x:<br>SSP370::x: | :x: | :x: | @ngben | - |
| CCAM-EC-Earth3 | Historical:running<br>SSP126::x:<br>SSP370::x: | :x: | :x: | @ngben | - |
| CCAM-NorESM2-MM | Historical::heavy_check_mark:<br>SSP126::heavy_check_mark:<br>SSP370::heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/AUS-10/CSIRO/NCC-NorESM2-MM/` | @ngben | - |

### BARPA
| Model | Processed | QC | Location | Person responsible | Notes |
| - | - | - | - | - | - |
| BARPA-ERA5 | :heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/AUS-10/CSIRO/ECMWF-ERA5/evaluation/none/CSIRO-CCAM-2203/v1/climdex/` | @chunhsusu | - |
| BARPA-ACCESS-CM2 | Historical::heavy_check_mark:<br>SSP126::heavy_check_mark:<br>SSP370::heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/AUS-15/BOM/CSIRO-BOM-ACCESS-CM2/` | @ngben, @EmmaHoward | - |
| BARPA-ACCESS-ESM1-5 | Historical::heavy_check_mark:<br>SSP126::heavy_check_mark:<br>SSP370::heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/AUS-15/BOM/CSIRO-BOM-ACCESS-ESM1-5/` | @ngben, @EmmaHoward | - |
| BARPA-CESM2 | Historical:running<br>SSP126::x:<br>SSP370::x: | :x: | :x: | @ngben | - |
| BARPA-CMCC-ESM2 | Historical:running<br>SSP126::x:<br>SSP370::x: | :x: | :x: | @ngben | - |
| BARPA-CNRM-ESM2-1 | Historical::x:<br>SSP126::x:<br>SSP370::x: | :x: | :x: | - | - |
| BARPA-EC-Earth3 | Historical::heavy_check_mark:<br>SSP126::heavy_check_mark:<br>SSP370::heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/AUS-15/BOM/EC-Earth-Consortium-EC-Earth3/` | @ngben, @EmmaHoward | - |
| BARPA-NorESM2-MM | Historical::heavy_check_mark:<br>SSP126::heavy_check_mark:<br>SSP370::heavy_check_mark: | :x: | `/g/data/ia39/australian-climate-service/test-data/CORDEX-CMIP6/indices/AUS-15/BOM/NCC-NorESM2-MM` | @ngben | - |
