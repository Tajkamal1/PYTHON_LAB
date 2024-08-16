# Node class definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Linking nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Function to traverse and print the linked list


def print_linked_list(head):
    current_node = head
    while current_node is not None:
        print(current_node.data, end=" -> " if current_node.next else "")
        current_node = current_node.next
    print()  # For a new line after the linked list is printed

# Call the function to display the linked list starting from node1


print_linked_list(node1)
