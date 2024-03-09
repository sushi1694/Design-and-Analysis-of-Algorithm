def insert_at_first(lst, number):
    lst.insert(0, number)

def insert_at_last(lst, number):
    lst.append(number)

def insert_at_middle(lst, number):
    middle_index = len(lst) // 2
    lst.insert(middle_index, number)

def insert_at_position(lst, position, number):
    lst.insert(position, number)

# Example usage
my_list = [1, 2, 4, 5]

insert_at_first(my_list, 0)
print("After inserting at the first position:", my_list)

insert_at_last(my_list, 6)
print("After inserting at the last position:", my_list)

insert_at_middle(my_list, 3)
print("After inserting at the middle position:", my_list)

insert_at_position(my_list, 2, 9)
print("After inserting at a specified position:", my_list)
