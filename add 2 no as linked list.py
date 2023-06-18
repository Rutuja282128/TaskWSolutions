# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode()  # Dummy node to hold the result
    current = dummy  # Pointer to build the result linked list
    carry = 0  # Carry for addition

    while l1 or l2 or carry:
        # Get the values of the current nodes or 0 if they're None
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Perform the addition
        total = val1 + val2 + carry
        carry = total // 10  # Calculate the carry
        digit = total % 10  # Calculate the digit

        # Create a new node with the digit and append it to the result
        current.next = ListNode(digit)
        current = current.next

        # Move to the next nodes
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next  # Return the result linked list


# Example usage:
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)

# Print the result
while result:
    print(result.val, end=" ")
    result = result.next

