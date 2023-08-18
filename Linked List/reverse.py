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
        ll = []
        while temp is not None:
            ll.append(temp.value)
            temp = temp.next
        return ll

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = None
            self.tail = None
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

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

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None

        return temp.value

    def get(self, index):
        if index<0 or index >= self.length:
            return None
        temp = self.head
        for _ in range():
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index, value):
        if index < 0 or index < self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value

    def reverse(self):
        temp = self.head
        pre = self.tail
        self.head = pre
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

linked_list = LinkedList(4)
linked_list.append(3)
linked_list.append(2)
linked_list.append(1)
print(linked_list.print_items())
linked_list.reverse()
print(linked_list.print_items())

