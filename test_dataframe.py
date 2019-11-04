"""
Homework 3, CSE 583
Claire Zarakas
Due on Wednesday, October 30, 2019
"""
import numpy as np

import test_parameters
DF = test_parameters.DF
COLUMN_NAMES = test_parameters.COLUMN_NAMES
COLUMN_TYPES = test_parameters.COLUMN_TYPES

def test_dataframe():
    """ Replicates test that was done in item 2 for HW2 """

    # Checks if the DataFrame contains only the columns that you specified as the second argument
    column_names_actual = DF.columns.tolist()
    correct_columns = (set(column_names_actual) == set(COLUMN_NAMES))

    # Checks if there are at least 10 rows in the DataFrame.
    min_rows = 10
    count_row, _ = DF.shape
    enough_rows = count_row >= min_rows

    # Checks if the values in each column have the same python type
    consistent_data_types = True
    for column in DF:
        consistent_data_types_this_column = True
        column_values = DF[column].tolist()
        column_types = [type(item) for item in column_values]
        num_types = len(set(column_types))
        if num_types > 1:
            consistent_data_types_this_column = False
        consistent_data_types = (consistent_data_types and consistent_data_types_this_column)

    # Return as True if all conditions are met
    assert (correct_columns and enough_rows and consistent_data_types)

def test_column_types():
    """ Check that all columns have values of the corect type. """
    i = 0
    correct_type_all_columns = True
    for column in DF:
        column_values = DF[column].tolist()
        column_types = [type(item) for item in column_values]
        expected_column_type = COLUMN_TYPES[i]
        if len(set(column_types)) == 1:
            if column_types[0] == expected_column_type:
                correct_type_this_column = True
            else:
                correct_type_this_column = False
        else:
            correct_type_this_column = False
        correct_type_all_columns = correct_type_all_columns and correct_type_this_column
        i = i+1
    assert correct_type_all_columns

def test_no_nans():
    """ Check for nan values if expecting int or float column. """
    i = 0
    contains_nans_all_columns = False
    for column in DF:
        column_values = np.array(DF[column].values)
        expected_column_type = COLUMN_TYPES[i]
        if expected_column_type in (int, float):
            # Check for nans
            column_values = np.array(DF[column].values)
            contains_nans_this_column = np.isnan(column_values).any()
        else:
            contains_nans_this_column = False
        contains_nans_all_columns = contains_nans_all_columns and contains_nans_this_column
        i = i+1
    assert not contains_nans_all_columns

def test_more_than_one_row():
    """ Verify that the dataframe has at least one row. """
    min_rows = 1
    count_row, _ = DF.shape
    enough_rows = (count_row >= min_rows)
    assert enough_rows
