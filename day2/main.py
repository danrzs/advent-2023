import data
from dataclasses import dataclass
from enum import Enum
import re 
from typing import List, Dict, Union
import itertools
import math

Pull = Dict[str, int]
Round = List[Pull]
Game = Dict[str, Union[List[Round], int]]

pull_maxes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def _parse_round(round: str) -> Round:
    rounddata = {}
    for pull in round.split(','):
        n, colour = pull.strip().split(' ')
        rounddata[colour] = int(n)
    return rounddata

def parse_input(line: str) -> Game:
    id, rounds = line.split(':')
    return {
        "game_id": int(id.split(' ')[1]),
        "rounds": [_parse_round(round) for round in rounds.split(';')]
    }

def part1(games: List[Game]) -> None:
    def _is_game_bad(game) -> bool:
        for round in game["rounds"]:
            if any([round.get(key, 0) > pull_maxes[key] for key in pull_maxes.keys()]):
                return True
        return False

    possible_games = [pg["game_id"] for pg in itertools.filterfalse(_is_game_bad, games)]

    print("Games {} are possible".format(', '.join(map(str, possible_games))))
    print(f"Their sum is {sum(possible_games)}")


def part2(games: List[Game]) -> None:
    def _powerup_game(game: Game) -> int:
        pull_mins = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for round in game["rounds"]:
            pull_mins.update({key: round[key] for key in pull_mins.keys() if round.get(key, 0) > pull_mins[key]})

        return math.prod(pull_mins.values())

    powers = list(map(_powerup_game, games))
    [print(f"Game {i} has a power of {p}") for i, p in enumerate(powers, start=1)]
    print(f"The sum of these powers is {sum(powers)}")


print("Part 1 known values: ")
part1([parse_input(line) for line in data.part1known.splitlines() if line])

print("Part 1 data: ")
part1([parse_input(line) for line in data.part1data.splitlines() if line])

print("Part 2 known values: ")
part2([parse_input(line) for line in data.part1known.splitlines() if line])

print("Part 2 data: ")
part2([parse_input(line) for line in data.part1data.splitlines() if line])
