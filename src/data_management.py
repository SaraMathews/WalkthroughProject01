import numpy as np
import pandas as pd
import os
import base64
from datetime import datetime
import joblib


def download_dataframe_as_csv(df):

    datetime_now = datetime.now().strftime("%d%b%Y_%Hh%Mmin%Ss")
    csv = df.to_csv().encode()
    b64 = base64.b64encode(csv).decode()
    href = (
        f'<a href="data:file/csv;base64,{b64}" download="Report {datetime_now}.csv" '
        f'target="_blank">Download Report</a>'
    )
    return href


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)


"""
The `data_management.py` module provides utility functions related to data
handling and file management.

1. `download_dataframe_as_csv(df)`: 
This function takes a pandas DataFrame `df` as input and returns an HTML string
that creates a download link for the DataFrame in CSV format. It encodes the
DataFrame as a CSV, then base64-encodes the CSV data to create a data URI.
The data URI is embedded in an anchor (`<a>`) element, which allows users to
click the link to download the CSV file with a timestamp in its name.

2. `load_pkl_file(file_path)`: This function is used to load data stored in a
Pickle file (`.pkl`). It takes the file path as input and uses the
`joblib.load()` function from the `joblib` library to read the data stored in
the file and return it.

Both of these functions are designed to assist in data handling and file
management tasks within the application. The first function facilitates the
download of data, while the second function helps to load data from saved
Pickle files, which can be useful for various purposes such as loading trained
models or other serialized objects.
"""
