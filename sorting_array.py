
# sorting method used
arr = [3, 56, 46, 34, 12, 64]
k = 2

sort_list = []

arr.sort(reverse=False)
def largenumber(arr, k):

    for i in range(k):
        print(arr[i], end=',')
        sort_list.append(arr[i])
        print(sort_list)

largenumber(arr, k)






