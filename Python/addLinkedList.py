class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        res = []
        temp = None
        prev = None
        carry = 0
        while l1 is not None or l2 is not None:
            fdata = 0 if l1 is None else l1.val
            sdata = 0 if l2 is None else l2.val
            Sum = carry + fdata + sdata

            carry = 0 if Sum < 10 else 1

            Sum = Sum if Sum < 10 else Sum % 10

            temp = ListNode(Sum)

            if prev is None:
                prev = temp
            else:
                prev.next = temp
            
            prev = temp
            res.append(prev)
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
                
        if carry > 0:
            temp.next = ListNode(carry)
            res.append(temp)
        return res[0]



l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)

while result:
  print(result.val)
  result = result.next
  
