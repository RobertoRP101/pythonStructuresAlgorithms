list1 = [1,2,3,4,5,10]
list2 = [10,9,8,7,6,5,4]


# def item_in_common(list1, list2):
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 return True
#     return False

def item_in_common(list1, list2):
    dict1 = {}
    for i in list1:
        dict1[i] = True
    
    for j in list2:
        if j in dict1:
            return True
    return False

