def bubble(a):
    i = 1
    mid = 1
    while i < len(a):
        temp = i
        while i > 0:
            if a[i] < a[i-1]:
                mid = a[i]
                a[i] = a[i-1]
                a[i-1] = mid
            i -= 1
        i = temp+1
    return a


my_list = [41, 42, 32, 54 ,-520]
my_list = bubble(my_list)
print(my_list)
