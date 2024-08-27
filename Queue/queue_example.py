from queue import Queue

my_queue = Queue(1)
my_queue.print_queue()
print(f'Length: {my_queue.length}')
my_queue.enqueue(2)
my_queue.print_queue()
print(f'Length: {my_queue.length}')
my_queue.enqueue(3)
my_queue.print_queue()
print(f'Length: {my_queue.length}')
print(my_queue.dequeue().value)
# my_queue.dequeue()
print(f'Length: {my_queue.length}')
my_queue.print_queue()
