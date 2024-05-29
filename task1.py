class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Функція реверсування однозв'язного списку
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Функція сортування вставками для однозв'язного списку
def sorted_insert(sorted_head, new_node):
    if not sorted_head or sorted_head.data >= new_node.data:
        new_node.next = sorted_head
        sorted_head = new_node
    else:
        current = sorted_head
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
    return sorted_head

# Функція об'єднання двох відсортованих однозв'язних списків
def insertion_sort_linked_list(head):
    sorted_head = None
    current = head
    while current:
        next_node = current.next
        sorted_head = sorted_insert(sorted_head, current)
        current = next_node
    return sorted_head


def merge_sorted_linked_lists(l1, l2):
    dummy = Node(0)
    tail = dummy
    
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    
    return dummy.next


# Створення списку та додавання елементів
llist = LinkedList()
llist.append(3)
llist.append(1)
llist.append(2)
llist.append(4)

print("Original list:")
llist.print_list()

# Реверсування списку
llist.head = reverse_linked_list(llist.head)
print("Reversed list:")
llist.print_list()

# Сортування списку вставками
llist.head = reverse_linked_list(llist.head)  # Реверсування назад до оригінального списку для сортування
llist.head = insertion_sort_linked_list(llist.head)
print("Sorted list:")
llist.print_list()

# Об'єднання двох відсортованих списків
llist1 = LinkedList()
llist1.append(1)
llist1.append(3)
llist1.append(5)

llist2 = LinkedList()
llist2.append(2)
llist2.append(4)
llist2.append(6)

merged_list = LinkedList()
merged_list.head = merge_sorted_linked_lists(llist1.head, llist2.head)
print("Merged sorted lists:")
merged_list.print_list()
