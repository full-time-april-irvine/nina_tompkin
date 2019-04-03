class SLNode:
    def __init__(self,val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self,val):  # added this line, takes a value
        new_node = SLNode(val)  # create a new instance of our Node class using the given value
        current_head = self.head    # save the current head in a variable
        new_node.next = current_head    # SET the new node's next TO the list's current head
        self.head = new_node    # return self to allow for chaining
        return self

    def print_values(self):
        runner = self.head  # a pointer to the list's first node
        while (runner != None): # iterating while runner is a node and not None
            print(runner.value) # print the current node's value
            runner = runner.next    #set the runner to its neighbor
        return self # once the loop is done, return self to allow for chaining

    def add_to_back(self,val): 
        new_node = SLNode(val)  # if the list is empty
        runner = self.head  # run the add_to_front method
        while (runner.next != None):    #let's make sure the rest of this function doesn't happen if we add to the front
            runner = runner.next
        runner.next = new_node  # increment the runner to the next node in the list
        return self # return self to allow for chaining
    

my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()   # chaining, yeah!
# output should be:
# Linked lists
# are
# fun!
