#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    if "AM" in s and "12" not in s:
        return s[:-2]
    elif "AM" in s:
        time = s[:-2].split(":")
        new_time = ["00"]
        print(":".join(new_time + time[1::]))
        return ":".join(new_time + time[1::])
    elif "PM" in s and "12" in s:
        return s[:-2]       
    else:
        time = s[:-2].split(":")
        new_time = [str(int(time[0]) + 12)]
        return ":".join(new_time + time[1::])

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
