s = input("Please enter a string: ")

def most_frequent(s1):
    a = {}
    for i in s1:
        if i in a:
            a[i] = a[i] + 1
        else:
            a[i] = 1
    arr = []
    for j in a:
        arr.append((a[j], j))
    arr.sort(reverse=True)
    for i, j in arr:
        print (j, i)

most_frequent(s.lower())
        