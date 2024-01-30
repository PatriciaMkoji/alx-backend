#!/usr/bin/env python3
""" implement get_page function """
import csv
import math
from typing import List

def index_range(page=1, page_size=2):
        """
        function named index_range that takes two integer args page & page_size
        """
        if page < 1 or page_size < 1:
            raise ValueError("Not an Integer")
        start_index = (page-1) * page_size
        end_index = start_index + page_size
        return start_index, end_index

    class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
    
    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

            return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0, "Should be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Should be a positive Integer"
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]
