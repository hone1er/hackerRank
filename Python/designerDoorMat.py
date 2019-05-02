# Enter your code here. Read input from STDIN. Print output to STDOUT

"""The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters."""
n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))