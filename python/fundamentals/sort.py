arr = [8,1,5,3,2,0]

def bubbleSort(my_arr):
    for j in range(len(my_arr)-1):
        for i in range(len(my_arr)-1):
            if my_arr[i] > my_arr[i+1]:
                my_arr[i], my_arr[i+1] = my_arr[i+1], my_arr[i]
    return my_arr

y = bubbleSort([8,1,5,3,2,0])
print(y)