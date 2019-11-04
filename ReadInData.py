"""
Claire Zarakas
HW 3
"""


### Set up workspace
import pandas as pd

### Function to create a dataframe from a URL that points to a CSV file
def create_dataframe(url):
    """ Creates data frame from url """
    df = pd.read_csv(url)
    return df
