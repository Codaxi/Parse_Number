#!/bin/bash


file_to_parse = input("Enter logged file to parse\n> ")

test_list = []
line_number = 1

with open(file_to_parse, 'r') as file:
    for line in file:
        for word in line.split():
            if word.isdigit():
                test_list.append(word)
        line_number += 1

def sort_list(list):
    int_list = []
    for i in list:
        int_list.append(int(i))

    int_list = sorted(int_list)
    return int_list

test_list = set(test_list)
sorted_test_list = sort_list(test_list)
print(f"Affected Services(RAW): {test_list}")
print(f"Affected Services(SORTED): {sorted_test_list}")
