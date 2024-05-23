#!/usr/bin/env python3

"""
This module implements a simple pagination system for a dataset of popular baby names.
"""

import csv
import math
from typing import List, Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end indices for a given page and page size.

    Args:
        page (int): The page number to retrieve the index range for.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices for the given page.
            The start index is inclusive, and the end index is exclusive.
    """
    return ((page - 1) * page_size, (page - 1) * page_size + page_size)

class Server:
    """
    Server class to handle pagination of a dataset of popular baby names.

    Attributes:
        DATA_FILE (str): The path to the CSV file containing the dataset.
        __dataset (List[List]): A cached copy of the dataset.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Loads and caches the dataset from the CSV file.

        Returns:
            List[List]: The dataset as a list of lists, where each inner list represents a row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                self.__dataset = dataset[1:]  # Skip the header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a page of data from the dataset.

        Args:
            page (int): The page number to retrieve (default: 1).
            page_size (int): The number of items per page (default: 10).

        Returns:
            List[List]: The requested page of data as a list of lists, where each inner list represents a row.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []

        return data[start:end]
