class Difference:
    def __init__(self, a):
        self.__elements = a
    def __init__(self,elements):
        self.__elements = elements
        self.maximumDifference = 0
	# Add your code here
    def computeDifference(self):
        posElements = [abs(e) for e in self.__elements]
        self.maximumDifference = max(posElements) - min(posElements)            
                
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)