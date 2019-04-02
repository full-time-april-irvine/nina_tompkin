#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(my_list):
    for i in range(len(my_list)):
        if my_list[i] > 0:
            my_list[i] = "big"
    return my_list
y = biggie_size([-1, 3, 5, -5])
print(y)


#Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
#Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(my_list):
    count = 0
    lastInList = len(my_list)
    for i in range(lastInList):
        if my_list[i] > 0:
            count+=1
    my_list[lastInList-1] = count
    return my_list
y = count_positives([-1,1,1,1])
print(y)
x = count_positives([1,6,-4,-2,-7,-2])
print(x)

#Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 7

def sum_total(my_list):
    sum = 0
    for i in range(len(my_list)):
        sum+=my_list[i]
    return sum
y = sum_total([1,2,3,4])
print(y)
x = sum_total([6,3,-2])
print(x)


#Average - Create a function that takes a list and returns the average of all the values.
#Example: average([1,2,3,4]) should return 2.5

def average(my_list):
    sum = 0
    for i in range(len(my_list)):
        sum+=my_list[i]
    return sum/float((len(my_list)))

y = average([1,2,3,4])
print(y)

def average2(my_list):
    sum = 0
    for i in my_list:
        sum+=i
    return sum/len(my_list)

y = average2([1,2,3,4])
print(y)

#Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0

def length(my_list):
    return len(my_list)

y = length([37,2,1,-9])
print(y)
x = length([])
print(x)

#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False

def minimum(my_list):
    if len(my_list) == 0:
        return False
    else:
        min = my_list[0]
        for i in range(1,len(my_list),1):
            if my_list[i] < min:
                min = my_list[i]
    return min
y = minimum([37,2,1,-9])
print(y)
x = minimum([])
print(x)

#Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False

def maximum(my_list):
    if len(my_list) == 0:
        return False
    else:
        max = my_list[0]
        for i in range(1,len(my_list),1):
            if my_list[i] > max:
                max = my_list[i]
    return max
y = maximum([37,2,1,-9])
print(y)
x = maximum([])
print(x)

#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(my_list):
    result = {}
    avg = 0
    sum = my_list[0]
    max = my_list[0]
    min = my_list[0]
    for i in range(1,len(my_list),1):
        if my_list[i] > max:
            max = my_list[i]
        elif my_list[i] < min:
            min = my_list[i]
        sum+=my_list[i]
        avg = sum / float(len(my_list))
    result.update({"sumTotal":sum})
    result.update({"average": avg})
    result.update({"minimum":min})
    result.update({"maximum":max})
    result.update({"length":len(my_list)})
    print(result)

ultimate_analysis([37,2,1,-9])

#Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(my_list):
    temp = 0
    for i in range(len(my_list)/2):
        temp = my_list[len(my_list)-i-1]
        my_list[len(my_list)-i-1] = my_list[i]
        my_list[i] = temp
    return my_list
y = reverse_list([37,2,1,-9])
print(y)