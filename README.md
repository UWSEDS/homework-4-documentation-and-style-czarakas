# HW4: Documentation and Style
Claire Zarakas
<br> Due on Wednesday, November 6, 2019

Need to add function-level documentation that includes descriptions of arguments and return values.

This project directory contains 3 modules and 2 additional files, as described below:

# MODULES

## read_in_data.py
This python module is a copy of the module submitted as part of previous homeworks. It contains the following 1 function:

1. create_dataframe: creates a dataframe from a URL that points to a CSV file.
  - ***Input:*** *url*
  - ***Output:*** *pandas dataframe*

## test_parameters.py
This python module uses ReadInData to define the data frame, column names, and column types to use in testing the dataframe.

## test_dataframe.py
The module test_dataframe.py uses the parameters defined in test_parameters.

It contains the following functions:
1. **test_create_dataframe**, following HW2, checks that the following conditions hold:

  - The DataFrame contains only the columns in the list of column names.
  - The values in each column have the same python type
  - There are at least 10 rows in the DataFrame
  - ***Input:*** *none*
  - ***Output:*** *boolean*
  

1. **test_column_types** checks that all columns have values of the corect type.
  - ***Input:*** *none*
  - ***Output:*** *boolean*
  
1. **test_no_nans** checks for nan values.
  - ***Input:*** *none*
  - ***Output:*** *boolean*
  
1. **test_more_than_one_row** verifies that the dataframe has at least one row.
  - ***Input:*** *none*
  - ***Output:*** *boolean*


# ADDITIONAL FILES

## terminal_screenshot.png
A screenshot of successfully running the tests.

## pylint_output.png
A screenshot of output from pylint, documenting a pylint score >8 for all modules.
