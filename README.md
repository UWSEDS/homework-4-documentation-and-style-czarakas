# HW4: Documentation and Style
Claire Zarakas
Due on Wednesday, November 6, 2019

Need to add function-level documentation that includes descriptions of arguments and return values.

This project directory contains 3 modules and X additional files, as described below:

# MODULES

## ReadInData.py
This python module is a copy of the module submitted as part of contains the following 2 functions:

1. create_dataframe: creates a dataframe from a URL that points to a CSV file.

1. test_create_dataframe: takes a pandas DataFrame and list of column names as input, and returns True if the following conditions hold:

  - The DataFrame contains only the columns that you specified as the second argument.
  - The values in each column have the same python type
  - There are at least 10 rows in the DataFrame.

## test_parameters.py
This python module uses ReadInData to define the data frame, column names, and column types to use in testing the dataframe.

## test_dataframe.py
The module test_dataframe.py uses the parameters defined in test_parameters.

It contains the following tests:
1. **test_create_dataframe**, following HW2, checks that the following conditions hold:

  - The DataFrame contains only the columns in the list of column names.
  - The values in each column have the same python type
  - There are at least 10 rows in the DataFrame

1. **test_column_types** checks that all columns have values of the corect type.
1. **test_no_nans** checks for nan values.
1. **test_more_than_one_row** verifies that the dataframe has at least one row.


# ADDITIONAL FILES

## terminal_screenshot.png
A screenshot of successfully running the tests.

## Pylint output
Include the output from pylint in your homework repository, need pylint score >8
