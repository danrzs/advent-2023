import re

import data
from typing import List
import pandas


Part = List[List[int]]

class Matrix:
    def __init__(self, data):
        self._data: pandas.DataFrame = self.string_to_matrix(data)

    def string_to_matrix(self, data: str) -> pandas.DataFrame:
        return pandas.DataFrame([line.split('') for line in data.splitlines() if line])

    def create_partmap(self, idx_l, idx_c):
        return self._data





def parse_schematic(matrix: DataMatrix) -> List[Part]:
    def _chk_char(c):
        if re.findall('#')

    return [
        [create_partmap(idx_line, idx_char) for idx_char, _ in enumerate(line)]
        for idx_line, line in enumerate(matrix)
    ]

def part1(partmap: list[Part]) -> None:
    pass

print("day 3, part 1 example data:")
part1(parse_schematic(data_to_matrix(data.part1known)))
