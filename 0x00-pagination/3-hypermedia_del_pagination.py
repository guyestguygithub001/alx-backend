#!/usr/bin/env python3

"""
This module implements a deletion-resilient hypermedia pagination system for a dataset of popular baby names.
"""

import csv
import math
from typing import Dict, List, Tuple

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
    Server class to handle deletion-resilient hypermedia pagination for a dataset of popular baby names.

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

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves hypermedia information for a page of the dataset based on a given index and page size.

        Args:
            index (int): The starting index for the page (default: None, starts from the beginning).
            page_size (int): The number of items per page (default: 10).

        Returns:
            Dict: A dictionary containing hypermedia information for the requested page, including:
                - 'index': The starting index for the current page.
                - 'next_index': The starting index for the next page, or None if it's the last page.
                - 'page_size': The number of items on the current page.
                - 'data': The data for the current page.
        """
        data = self.dataset()
        assert index is None or (index >= 0 and index <= len(data) - 1)

        page_data = []
        data_count = 0
        next_index = None

        start = index if index is not None else 0

        for i, item in enumerate(data[start:], start=start):
            if data_count < page_size:
                page_data.append(item)
                data_count += 1
            else:
                next_index = i
                break

        page_info = {
            'index': index if index is not None else 0,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data,
        }

        return page_info
