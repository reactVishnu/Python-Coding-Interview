class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def __str__(self):
        return f'Head: {self.head}, Tail {self.tail}'

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            print('if runned')
            self.head = new_node
            self.tail = new_node
        else:
            print('Else runned')
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def print_item(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


linked_list = LinkedList(4)
print(linked_list.head.next)
linked_list.append(5)
print(linked_list.tail.next)
linked_list.print_item()
