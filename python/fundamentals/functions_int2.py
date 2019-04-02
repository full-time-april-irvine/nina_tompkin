#1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

x = [ [5,2,3], [10,8,9] ] 

def change_value_in_x():
    x[1][0] = 15
    return x
y = change_value_in_x()
print(y)

#2 Change the last_name of the first student from 'Jordan' to 'Bryant'

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]['last_name'] = "Bryant"

print(students)

#3 In the sports_directory, change 'Messi' to 'Andres'

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = "Andres"

print(sports_directory)

#4 Change the value 20 in z to 30

z = [ {'x': 10, 'y': 20} ]

z[0]['y'] = 30

print(z)

#5 Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(a_list):
    #Looping through each of the dictionaries in students (i.e. things between curly brackets)
    for dic in a_list:
        #create an empty list (to be used with join later)
        s = []
        #Looping through each of the key/value pairs in each dictionary's items (i.e. the items separated by commas)
        for k,v in dic.items():
            #add the following into a list: the string version of the key and the string version of the value, separated by a dash
            s.append(str(k)+" - "+str(v))
            #create a lil string that will be used for the join
            my_string = ", "
            #update the string so that the items in the list are concatenated with ", " in between
            my_string = my_string.join(s)
        print(my_string)

iterateDictionary(students)
#3 Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. 
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name,some_list):
    for dic in some_list:
        for k,v in dic.items():
            if k == key_name:
                print(v)

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

#4 Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. 

dojo = {'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']}

def printInfo(some_dict):
    #for each key within the dictionary provided...
    for k in some_dict:
        #print a string made up of the length of the value corresponding with the dictionary's key, k (which happened to be an array) along with a space and the key in all caps
        print(f"{len(some_dict[k])} {k.upper()}")
        #create a string variable for the purpose of using "join" - in this case, the string indicates a new line
        new_line = "\n"
        #then print the joined result of new lines between each interation of the value of the dictionary's key k
        print(new_line.join(some_dict[k]),new_line)

printInfo(dojo)