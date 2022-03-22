def max_min(data):
    l = data[0]
    s = data[0]
    for num in data:
        if num > l:
            l = num
        elif num < s:
            s = num
    return l, s
print("Maximum", max_min([1, 4, 6, 7, 9, 3, 5]))
