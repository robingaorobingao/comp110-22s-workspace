"""Some helpful utility functions for working with csv files."""

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