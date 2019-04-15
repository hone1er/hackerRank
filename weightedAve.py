# Enter your code here. Read input from STDIN. Print output to STDOUT
# return weighted average
n = int(input()) # an integer,N, denoting the number of elements in arrays x and w. 
x = input().split() # space-separated integers describing the respective elements of array x
w = input().split() # space-separated integers describing the respective elements of array w
numerator = [int(x[i])*int(w[i]) for i in range(n)]
denominator = [int(w[i]) for i in range(n)]
print(round(sum(numerator)/sum(denominator),1))