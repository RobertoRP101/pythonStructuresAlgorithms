from link_list import LinkedList

list_element = LinkedList(1)
list_element.append(2)
list_element.append(3)
list_element.append(4)
print(list_element.print_list())
print(list_element.pop())
print(list_element.pop())

list_element.prepend(0)
list_element.prepend(-1)
list_element.prepend(-2)
list_element.prepend(-3)
print(list_element.print_list())
print(f'Element poped: {list_element.pop_first()}')
print(list_element.print_list())
print(f'Element got: {list_element.get(2)}')

