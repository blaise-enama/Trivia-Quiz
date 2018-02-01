#Trivia Quiz

print("This is a quiz that tests your knowledge on Soccer")

'''
'''

name = input("Enter your name: ")
print("Hi there,", name, "Are you ready to begin your quiz?") 
print("I will as you six questions, and give you three choices")
print("Select which choice is the correct answer")
print("----------------------------------------------")

#Set the score of the qiuz to 0
score = 0
score = int(score)

#Question 1:
print("Question 1: Who is the most decorated player in the world as of 2017?")

print("A. L.Messi")
print("B. C. Ronaldo")
print("C. Pele")
print("D. D. Alves")
print("")

Q1answer = "D" #the right answer
Q1response = input("Your answer:")

if Q1response=="D" or Q1response== "d":
    print("Correct Answer:",Q1response)
    score = score+1
elif Q1response != "D" or Q1response != "d":
    print("Answer is incorrect") 
print("Your current score is", score, "/6")

#percentage score

final_score = (score*100)/6
print("You ended with the score of" +str(final_score)+ "percent")

