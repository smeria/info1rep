# Please do not modify this part of the code! 
# This is just to show how you should name the variables containing your answers
task_0 = 'Python is cool!' * 3
print('Task 0:', task_0)


# Your code goes here
# Task 1
formla = ((65**17%3233)**413)%3233
if formla == 65.00:
    task_1 = True
else:
    task_1 = False

print("Task 1: ", task_1)

# Task 2
doghouse = "doghouse"
task_2_p1 = doghouse[:3]
task_2_p2 = doghouse[3:8]

print("Task 2 part 1: ",task_2_p1)
print("Task 2 part 2: ",task_2_p2)

# Task 3
word ="anna"
if word == word[::-1]:
    task_3=True
else:
    task_3=False
print("Task 3: ",task_3)


# Task 4
if "alpha" in "alphanumeric":
    task_4=True
else:
    task_4=False
print("Task 4: ",task_4)

# Task 5
expression ="Python is cool!"
task_5 = expression*3
print("Task 5: ", task_5)

# Task_6
percentage = 95.66666666666667
task_6 = '{0:4.2f}'.format(percentage)
#task_6 = round(percentage,2)
print("Task 6: ", task_6)