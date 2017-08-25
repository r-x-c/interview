class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            prev_ = prev
            next_ = head.next
            prev = head
            head.next = prev_
            if next_ is None:
                return head
            head = next_


x = ListNode(3)
y = ListNode(6)
z = ListNode(9)

x.next = y
y.next = z


sol = Solution()
ans = sol.reverseList(x)
print("Hello")
print("\n\n\n")
while ans:
    print(ans.val)
    ans = ans.next