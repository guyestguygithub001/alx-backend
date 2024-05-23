#!/usr/bin/env python3

"""
This module provides a helper function for pagination.
"""

from typing import Tuple

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
