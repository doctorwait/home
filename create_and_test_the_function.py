"""
The task of this test task was to delve into someone else's (already written) code, 
write the function get_score and also test suite for it.
"""



from pprint import pprint
import random
import math
import unittest
import random

TIMESTAMPS_COUNT = 500000

PROBABILITY_SCORE_CHANGED = 0.0001 

PROBABILITY_HOME_SCORE = 0.45 

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0 
    }
}


def generate_stamp(previous_value: dict):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
                             PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()


pprint(game_stamps)


def get_score(game_stamps: list, offset: int) -> tuple | str:
    if type(game_stamps) != list or type(offset) != int:
        return 'Incorrect arguments were passed to the function.'
    # range_of_offset_change is an internal function constant that depends on the offset_change in the "generate_stamp"
    # function. Ideally, it should be passed as an argument, but in order to follow the condition of the task more,
    # I will not change the function arguments.
    range_of_offset_change = 3
    range_in_list = int(sum(i for i in range(1, range_of_offset_change + 1)) / range_of_offset_change)
    # The current value may not be in the offset dictionary. Note that all values are sorted in ascending order.
    # In order not to go through the entire list, let's take an approximate slice:
    start = offset // range_in_list - range_in_list * range_of_offset_change * 100
    end = offset // range_in_list + range_in_list * range_of_offset_change * 100
    if start < 0:
        start = 0
    approximate_slice = slice(start, end)
    approximate_game_stamps = game_stamps[approximate_slice]
    # The list has become significantly smaller. Now, finding the right value is not difficult.
    home = away = None
    for offset_ in approximate_game_stamps:
        if offset_['offset'] == offset:
            home, away = offset_['score']['home'], offset_['score']['away']
    return (home, away) if home is not None else f'The current offset ({offset}) was not found.'


class TestGetScore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.keys = [offset_num['offset'] for offset_num in game_stamps]

    def get_random_existing_number(self):
        end = game_stamps[-1]['offset']
        num = random.randint(1, end)
        while num not in self.keys:
            num = random.randint(1, end)
        return num

    def test_random_offset_number(self):
        num = self.get_random_existing_number()
        res = get_score(game_stamps, num)
        self.assertEqual(type(res), tuple,
                         'The function did not find a number that is present in the list.')

    def test_for_all_existing_numbers(self):
        for key in self.keys:
            res = get_score(game_stamps, key)
            self.assertEqual(type(res), tuple,
                             "The function did not find a number while iterating over all existing numbers.")

    def test_number_that_not_exist(self):
        end = game_stamps[-1]['offset']
        res = get_score(game_stamps, end + 1)
        self.assertEqual(type(res), str, 'The function found a non-existent number offset.')

    def test_negative_numbers(self):
        res = get_score(game_stamps, -1)
        self.assertEqual(type(res), str, 'The function found a nonexistent negative number.')

    def test_type_of_return_values(self):
        num = self.get_random_existing_number()
        for_tuple_res = get_score(game_stamps, num)
        self.assertEqual(type(for_tuple_res), tuple, 'The return type for an existing number is invalid.')

        beyond_end = game_stamps[-1]['offset'] + 100
        for_string_res = get_score(game_stamps, beyond_end)
        self.assertEqual(type(for_string_res), str, 'The return type for a non-existent number is invalid.')

    def test_running_with_wrong_arguments_types(self):
        arguments = ({'one': 'two'}, [1, 2], 'one', 3, 2.32, (1, 2), False, {2, 1}, -1)
        for i in arguments:
            for j in arguments:
                if type(i) == list and type(j) == int:
                    continue
                res = get_score(i, j)
                error_msg = 'Incorrect arguments were passed to the function.'
                self.assertEqual(res, error_msg, 'The function must not work with invalid arguments.')

