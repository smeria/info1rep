# Please do not modify this part of the code!
grade = '-'

# Your code goes here
score = int(input('Enter the score between 0 and 100:'))

if score >= 90 and score <= 100:
    grade="A"
elif score <= 89 and score >= 80:
    grade="B"
elif score <= 79 and score >= 70:
    grade="C"
elif score <= 69 and score >= 60:
    grade ="D"
elif score <= 59 and score >= 0:
    grade="F"
else:
    print("Error: Invalid Score")



