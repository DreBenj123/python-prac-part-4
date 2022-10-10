def multiplyList(mylist):
    result = 1
    for x in mylist:
        result = result * x
    return result


list1 = [1, 3, 5]
list2 = [10, 20, 30]
print(multiplyList(list1))
print(multiplyList(list2))
