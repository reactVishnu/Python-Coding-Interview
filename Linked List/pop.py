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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_items(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=', ')
            temp = temp.next
        print()

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

linked_list = LinkedList(4)
linked_list.append(1)
linked_list.append(7)
linked_list.append(3)
linked_list.append(2)
print('Before PoPing')
linked_list.print_items()
print(linked_list.pop())
print(linked_list.pop())
print(linked_list.pop())