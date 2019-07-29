from typing import Union
import urllib
from math import ceil


class TaskSolver:
    '''
    http://www.pythonchallenge.com/pc/def/linkedlist.php
    '''
    def __init__(self):
        self.url_base: str = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
        self.nothing_param: str = 'nothing'
        self.request_count = 399
        self.initial_id = 12345
        self.result = None
    
    def get_id_from_response(self, response: str) -> Union[int, None]:
        response_split = response.split()
        try:
            result = int(response_split[-1])
        except ValueError:
            result = None 
        return result
    
    def url_from_id(self, url_id: int) -> str:
        if not isinstance(url_id, (int, float)):
            raise ValueError('You should pass integer value as url param')
        url = f'{self.url_base}?{self.nothing_param}={url_id}'
        return url

    def make_request(self, url: str) -> str:
        with urllib.request.urlopen(url) as resp:
            result = resp.read().decode()
        return result

    def solve(self):
        current_id = self.initial_id
        for i in range(self.request_count):
            if i >= 85:
                current_id /= 2
                current_id = ceil(current_id)
            try:
                self.result = self.make_request(
                    self.url_from_id(current_id)
                )
            except ValueError as exc:
                print(i, self.result, exc)
            print(f'{i} [{current_id}] -> {self.result}')
            current_id = self.get_id_from_response(self.result)
    