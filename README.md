# TOPSIS Implementation

## Program 1: Command Line Implementation
Command to run:
```bash
python <Program>.py <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

Example:
```bash
python main.py data.csv "1,1,2,1,1" "+,+,-,+,+" result.csv
```

### Sample Input Data (data.csv)
```
Fund Name,P1,P2,P3,P4,P5
M1,0.84,0.71,6.7,42.1,12.59
M2,0.91,0.83,7.0,31.7,10.11
M3,0.79,0.62,4.8,46.7,13.23
M4,0.78,0.61,6.4,42.4,12.55
M5,0.94,0.88,3.6,62.2,16.91
M6,0.88,0.77,6.5,51.5,14.91
M7,0.66,0.44,5.3,48.9,13.83
M8,0.93,0.86,3.4,37.0,10.55
```

### Sample Output (result.csv)
```
Fund Name,P1,P2,P3,P4,P5,Topsis Score,Rank
M1,0.84,0.71,6.7,42.1,12.59,0.286,6
M2,0.91,0.83,7.0,31.7,10.11,0.2852,7
M3,0.79,0.62,4.8,46.7,13.23,0.5453,3
M4,0.78,0.61,6.4,42.4,12.55,0.2646,8
M5,0.94,0.88,3.6,62.2,16.91,0.958,1
M6,0.88,0.77,6.5,51.5,14.91,0.4065,5
M7,0.66,0.44,5.3,48.9,13.83,0.425,4
M8,0.93,0.86,3.4,37.0,10.55,0.6651,2

```

### Input Requirements
- Input CSV file must have 3+ columns
- First column: Object names (M1, M2, etc.)
- 2nd column onwards: Numeric values only
- Weights: Comma-separated (e.g., "0.2,0.2,0.2,0.2,0.2")
- Impacts: Comma-separated +/- (e.g., "+,+,+,+,+")

### Error Handling
- Checks for correct parameter count
- File existence verification
- Numeric values validation
- Weights and impacts count validation
- Impact symbols must be + or -

## Program 2: PyPI Package
This implementation is available as a Python package on [`https://pypi.org/project/Topsis-vaibhav-tandon-102203877/`](https://pypi.org/project/Topsis-vaibhav-tandon-102203877/). You can easily install it via `pip`:

```bash
pip install Topsis-vaibhav-tandon-102203877
```
---

## Program 3: Web Application
Access the web interface at: https://topsis-web-app-example.vercel.app/
- Upload CSV file
- Enter weights and impacts
- Provide email
- Receive results via email

## Requirements
- Python
- pandas
- numpy

## Author
Name: Vaibhav Tandon

