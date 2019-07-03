#!/usr/bin/python
import collections

Item = collections.namedthttps://classroom.udacity.com/nanodegrees/nd256/parts/94ec3f1b-f3ae-4de4-acbc-ec4b27548116/modules/7de98578-b282-48ef-bc47-3167f88582f8/lessons/266c368c-92dd-46c3-bd74-dab505a547bc/concepts/2c3fdfba-c032-4da5-8f61-cb391ad9ea0b#uple('Item', ['weight', 'value'])


def max_value(knapsack_max_weight, items):
    lookup_table = [0] * (knapsack_max_weight + 1)

    for item in items:
        for capacity in reversed(range(knapsack_max_weight + 1)):
            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity - item.weight] + item.value)

    return lookup_table[-1]


tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
for test in tests:
    assert test['correct_output'] == max_value(**test['input'])
