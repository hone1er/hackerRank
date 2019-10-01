#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    all_grades = []
    for grade in grades:
        # find the number needed to add for rounded
        if grade >= 50:
            mod = 100 % grade
            add = mod % 5
        elif grade >= 38:
            mod = 50 % grade
            add = mod % 5
        else:
            add = 0

        # add the number and append it to the grades list
        if add <= 2:
            grade += add
            all_grades.append(grade)
        else:
            all_grades.append(grade)
    return all_grades
        

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
