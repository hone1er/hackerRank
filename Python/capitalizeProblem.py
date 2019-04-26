#!/bin/python3

# Complete the solve function below.
def solve(s):
    a_string = s.split(' ') 
    return (' '.join((word.capitalize() for word in a_string)))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()