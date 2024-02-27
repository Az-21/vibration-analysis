# Converter for CWRU Bearing Vibration Dataset
## Dataset Source
https://engineering.case.edu/bearingdatacenter/download-data-file

## Requirement
The dataset is saved in `.mat` format and it has poor interoperability with FOSS tools, libraries, and languages.

## Naming Convention of Input Files
This script expects user to rename the saved files and encode the fault diameter and load.
- $0$ HP load <kbd>=></kbd> `0hp`.
- $0.007"$ fault diameter <kbd>=></kbd> `7inch`.
- $0.014"$ fault diameter <kbd>=></kbd> `14inch`.
- $0.021"$ fault diameter <kbd>=></kbd> `21inch`.

For example, if file is named `fan-ball-7inch-3hp.mat`, the script will extract relevant info ($0.007"$, $3$ HP).
