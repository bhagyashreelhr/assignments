# Python program for implementation of linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get_node(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current
 
    # Function to insert elememt at different places
    def insert_after(self, ref_node, new_node):
        new_node.next = ref_node.next
        ref_node.next = new_node

    def insert_before(self, ref_node, new_node):
        prev_node = self.get_prev_node(ref_node)
        self.insert_after(prev_node, new_node)

    def insert_at_beg(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    # Function to remove element from linked list
    def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next

    # Function to display linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next

new_list = LinkedList()
print('Menu')
print('insert <data> after <index>')
print('insert <data> before <index>')
print('insert <data> at beg')
print('insert <data> at end')
print('remove <index>')
print('quit')

while True:
    print('The list: ', end = ' ')
    new_list.display()
    print()
    do = input('Select any operation: ').split()

    operation = do[0].strip().lower()

    if operation == 'insert':
        data = int(do[1])
        position = do[3].strip().lower()
        new_node = Node(data)
        suboperation = do[2].strip().lower()
        if suboperation == 'at':
            if position == 'beg':
                new_list.insert_at_beg(new_node)
            elif position == 'end':
                new_list.insert_at_end(new_node)
        else:
            index = int(position)
            ref_node = new_list.get_node(index)
            if ref_node is None:
                print('No such index.')
                continue
            if suboperation == 'after':
                new_list.insert_after(ref_node, new_node)
            elif suboperation == 'before':
                new_list.insert_before(ref_node, new_node)

    elif operation == 'remove':
        index = int(do[1])
        node = new_list.get_node(index)
        if node is None:
            print('No such index.')
            continue
        new_list.remove(node)

    elif operation == 'quit':
        break

