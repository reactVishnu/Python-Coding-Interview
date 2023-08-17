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

    def print_items(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head

        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            new_node.next = temp
            self.head = new_node
        self.length += 1
        return True


linked_list = LinkedList(4)
linked_list.append(5)
linked_list.append(6)
linked_list.append(7)
linked_list.append(8)
print(f'Append List')
linked_list.print_items()
print(f'Prepend List')
linked_list.prepend(1)
linked_list.prepend(9)
linked_list.print_items()
