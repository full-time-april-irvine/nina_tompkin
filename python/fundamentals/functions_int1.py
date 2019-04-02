import random
def randInt(min=0, max=100):
    if max > min:
        num = round(random.random()* (max - min) + min)
        return num
    else:
        print("Your min value is larger than your max value! Assuming you want a random number between " +str(max) + " and " + str(min) +"...")
        num = round(random.random()* (min - max) + max)
        return num

print(randInt())
print(randInt(min=-30, max=0))
print(randInt(min=0, max=-50))

