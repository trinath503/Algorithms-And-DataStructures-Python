class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev =prev
        self.data =data
        self.next = next



class Stack:
    head = None
    tail = None

    def Push(self,data):
        node = Node(data)
        if self.head is not None:
            self.tail.next = node
            node.prev = self.tail
        else:
            self.head = node
        self.tail = node

    def Pop(self):
        s= ' '
        if self.tail is not None:
            if self.tail == self.head:
                s = self.tail.data
                self.head = self.tail =None
            else:
                current_node = self.head
                s = current_node.next.data
                while current_node.next.next is not None:
                    s = current_node.next.data
                    current_node = current_node.next

                current_node.next = None
                self.tail = current_node
        return s

    def show(self):
        current_data = self.head
        while current_data is not None:
            print(current_data.data)
            current_data = current_data.next




# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])
stack = Stack()

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            stack.Push(next)
            # print(type(next))
        if next in ")]}":
            # Process closing bracket, write your code here
            data = stack.Pop()
            if data not in "([{":
                s = Bracket(next, i)
                print("Yes",s)


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()


