class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:

    def __init__(self):
        self.program = 'Return reverse linked list'
        self.author  = 'Trinath Reddy'
        self.external_refernece = None
        self.head = None
        self.tail = None

    def insert_node(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def show_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def reverse_list(self):
        previous_node = None
        current_node = self.head

        self.tail = current_node

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node



tri = SingleLinkedList()
tri.insert_node(1)
# tri.show_list()
tri.insert_node(3)
# tri.show_list()
tri.insert_node(2)
# tri.show_list()
tri.insert_node(4)
tri.show_list()
tri.reverse_list()
tri.show_list()