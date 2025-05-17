def common_elements(a, b):
    list1 = []
    for i in a:
        if i in b:
            list1.append(i)
    print(list1)

a = [1, 2, 5]
b = [3, 5, 7]
common_elements(a, b)