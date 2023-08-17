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

    def print_list(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next


# We created the Linked List
try:
    linked_list = LinkedList()
    print(linked_list.head.value)

except Exception as e:
    print(f'The exception is {e}')
