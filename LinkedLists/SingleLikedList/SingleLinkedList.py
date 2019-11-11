#create a node
class Node:
    def __init__(self, data, next= None):
        self.data = data
        self.next = None

class SingleLinkedList:
    head =None
    tail = None

    def show(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def PushFront(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

    def PopFront(self):
        if self.head is not None:
            self.head = self.head.next
        if self.head == self.tail:
            self.tail = None

    def PushBack(self,data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next =node
        self.tail = node
    def PopBack(self,data):
        if self.head == self.tail:
            self.head = self.tail =None
        elif self.tail is not None:
            current_node = self.head
            while current_node.next.next is not None:
                current_node =current_node.next

            current_node.next = None
            self.tail = current_node
        else:
            print("No elemnets to pop")

    def AddAfter(self,data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                node =Node(data)
                if self.head == current_node:
                    node.next = self.head
                    self.head = node
                elif self.tail == current_node:
                    current_node.next = self.tail
                    self.tail = node
                else:
                    node.next = current_node.next
                    current_node.next = node
            current_node = current_node.next
    # def PopMiddle(self,data):
    #     if self.head is not None:
    #         current_node = self.head
    #         while current_node is not None:
    #             if current_node.data == data:
    #                 print()



tri = SingleLinkedList()
tri.PushBack(1)
tri.show()
tri.PushBack(3)
tri.show()
tri.PushBack(2)
tri.show()
tri.PopFront()
tri.show()







