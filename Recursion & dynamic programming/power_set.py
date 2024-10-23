'''
8.4
Power Set

Write a method to return all subsets of a set
'''

def power_set(list_set):
    return_list = []



    return return_list

if __name__ == '__main__':
    list_set = set(1, 2, 3, 4, 5)
    l = power_set(list_set)
    print(l)


# (1, 2, 3, 4, 5)

# (1), (2), (3), (4), (5), (1, 2), (1, 3), (1, 4), (1, 5), (1, 2, 3)...

# (1, 2, 5), (5, 1, 2)