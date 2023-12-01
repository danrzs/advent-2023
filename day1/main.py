import data
import re

mapping = {
    "one": "o1ne",
    "two": "t2wo",
    "three": "thr3ee",
    "four": "fo4ur",
    "five": "fi5ve",
    "six": "s6ix",
    "seven": "sev7en",
    "eight": "eig8ht",
    "nine": "ni9ne",
}

def part1(line):
    digits = re.findall('\d', line)
    return int(digits[0] + digits[-1])


def part2(line):
    for k,v in mapping.items():
        line = line.replace(k, v)
    digits = re.findall('\d', line)
    return int(digits[0] + digits[-1])

print("Total value for part1 knowns is: {}".format(sum([part1(v) for v in data.known_part1.splitlines() if v])))
print("Total value for part1 data is: {}".format(sum([part1(v) for v in data.data.splitlines() if v])))
print("Total value for part2 knowns is: {}".format(sum([part2(v) for v in data.known_part2.splitlines() if v])))
print("Total value for part2 data is: {}".format(sum([part2(v) for v in data.data.splitlines() if v])))

