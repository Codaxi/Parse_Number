#!/bin/bash

file = input("Enter logged file to parse\n> ")

f = open(file, 'r')

test_list = []
line_number = 1

for line in f:
    print(f"{line_number}: {line}")
    for word in line.split():
        if word.isdigit():
            print(f"\t{line_number}: {word}")
            test_list.append(word)
    line_number += 1


test_list = set(test_list)
print(f"Test List: {test_list}")


#f.close()
