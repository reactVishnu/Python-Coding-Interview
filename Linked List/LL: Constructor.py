class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1




# We created the Linked List
try:
    linked_list = LinkedList(4)
    print(linked_list.head.next)

except Exception as e:
    print(f'The exception is {e}')
