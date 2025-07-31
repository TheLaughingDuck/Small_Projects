import numpy as np
import pandas as pd

def unique(series, ascending=False):
    '''
    Returns the unique values, along with the corresponding counts for a pandas series.
    The values are by default sorted by the counts in descending order.
    '''

    # If at least one element is str, then the others should be treated as str as well.
    # The others might be nan for example, which does not play nicely with str.
    if str in set(type(i) for i in series):
        series = [str(i) for i in series]
    
    # Count frequencies
    counts = np.unique(series, return_counts=True)
    df = pd.DataFrame({"Values": counts[0], "Counts":counts[1]})
    df.sort_values(inplace=True, by="Counts", ascending=ascending)
    return df


def df_summary(df):
    '''
    Returns a summary of a dataframe df, including the number of rows and columns,
    the number of missing values, and the number of unique values for each column.
    '''
    # Check if the input is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    # Get the number of rows and columns
    num_rows, num_cols = df.shape
    # Get the number of missing values for each column
    missing_values = df.isnull().sum()
    # Get the number of unique values for each column
    unique_values = df.nunique()
    # Get the data types for each column
    data_types = df.dtypes

    
    summary = pd.DataFrame({
        "Column": df.columns,
        "Missing": df.isnull().sum(),
        "Unique": [len(df[col].unique()) for col in df.columns],
        "Type": [df[col].dtype for col in df.columns]
    })

    return summary