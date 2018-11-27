# Please do not modify this part of the code!
result = ""

# Your code goes here
user1input = input('User 1: Choose between Rock, Paper, and Scissors: ')
user2input = input('User 2: Chopse between Rock, Paper, and Scissors: ')

if user1input == user2input:
    result = "Tie"
elif user1input == "Rock" and user2input == "Paper":
    result = "User 2 wins"
elif user1input == "Rock" and user2input == "Scissors":
    result = "User 1 wins"
elif user1input == "Paper" and user2input == "Scissors":
    result = "User 2 wins"
elif user1input == "Paper" and user2input == "Rock":
    result = "User 1 wins"
elif user1input == "Scissors" and user2input == "Rock":
    result = "User 2 wins"
elif user1input == "Scissors" and user2input == "Paper":
    result = "User 1 wins"
else:
    result = "Wrong input"

print(result)
