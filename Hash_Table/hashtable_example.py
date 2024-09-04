from hashtable import HashTable

my_table = HashTable()

my_table.print_table()
my_table.set_item('Running', 1000)
my_table.set_item('Walking', 200)
my_table.set_item('Bike', 800)
my_table.print_table()
print(my_table.get_item('Running'))
print(my_table.keys())