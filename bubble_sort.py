import random #needed only for testing

def bubblesort(elements):
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]

#Creating random list
random_list =[]
for i in range(random.randint(5,20)):
    random_list.append(random.randint(-100,100))

#Testing functions
print("Unsorted list is,")
print(random_list)
bubblesort(random_list)
print("Sorted Array is, ")
print(random_list)