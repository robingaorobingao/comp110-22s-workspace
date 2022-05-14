"""Dictionary related utility functions."""

__author__ = "730406932"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    # TODO: more work!
    file_handle = open(filename, "r", encoding="utf8")
    # read that file
    csv_reader = DictReader(file_handle)
    # read each row of the csv line by line
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    # close the file when we're done to free its resources
    return result


def adding_counts(col_counts: dict[str, int]) -> int:
    """Add up counts for favorable responses."""
    result: int = 0
    # TODO
    for item in col_counts:
        if int(item) > 4:
            result += col_counts[item]
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    # TODO
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row oriented table to a column oriented table."""
    result: dict[str, list[str]] = {}
    # TODO: more work!
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(data_cols_head: dict[str, list[str]], row_number: int) -> dict[str, list[str]]:
    """Produce a table with the only first N rows for each column."""
    new_dict: dict[str, list[str]] = {}

    for key in data_cols_head:
        count: int = 0
        col_list: list[str] = []
        for item in data_cols_head[key]:
            if count < row_number:
                col_list.append(item)
            count += 1
        new_dict[key] = col_list
    return new_dict


def select(input_dict: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with as subset of the original columns."""
    result_dict: dict[str, list[str]] = {}
    for item in columns:
        result_dict[item] = input_dict[item]
    return result_dict


def count(val_list: list[str]) -> dict[str, int]:
    """Count the frequency of values."""
    result_dict: dict[str, int] = {}
    for item in val_list:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1
    return result_dict