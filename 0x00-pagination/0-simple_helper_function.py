#!/usr/bin/env python3
"""
Pagination helper function
"""


def index_range(page=1, page_size=2):
    """
    a function named index_range that takes two integer
                        arguments page and page_size
    The function should return a tuple of size two containing
                        a start index and an end
       index corresponding to the range of indexes to return in list for those
                        particular pagination parameters.
    Page numbers are 1-indexed
    """
    if page < 1 or page_size < 1:
        raise ValueError("Not an Integer")
    start_index = (page-1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
