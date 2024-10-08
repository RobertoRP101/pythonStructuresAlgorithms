from doubly_linked_list import DoublyLinkedList 

my_doubly_linked_list = DoublyLinkedList(3)
my_doubly_linked_list.print_list()
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(10)
my_doubly_linked_list.print_list()
my_doubly_linked_list.pop()
my_doubly_linked_list.print_list()
my_doubly_linked_list.pop()
my_doubly_linked_list.print_list()
my_doubly_linked_list.pop()
my_doubly_linked_list.print_list()
print('prepend function:\n')
my_doubly_linked_list.prepend(-10)
my_doubly_linked_list.print_list()
my_doubly_linked_list.prepend(-20)
my_doubly_linked_list.print_list()
print('pop_first function:\n')
my_doubly_linked_list.pop_first()
my_doubly_linked_list.print_list()
my_doubly_linked_list.pop_first()
my_doubly_linked_list.print_list()
print('get function:\n')
my_doubly_linked_list.prepend(200)
my_doubly_linked_list.prepend(59)
my_doubly_linked_list.prepend(23)

for position in range(0, 3):
    print(f'Get element in position {position}: {my_doubly_linked_list.get(position).value}')
    
print('set function:\n')
my_doubly_linked_list.set(1, -20000)
my_doubly_linked_list.print_list()

print('insert function:\n')
my_doubly_linked_list.insert(0, 999)
my_doubly_linked_list.insert(1, 555)
my_doubly_linked_list.insert(my_doubly_linked_list.length, 9999)
my_doubly_linked_list.print_list()
my_doubly_linked_list.remove(0)
my_doubly_linked_list.print_list()
my_doubly_linked_list.remove(my_doubly_linked_list.length-1)
my_doubly_linked_list.print_list()
