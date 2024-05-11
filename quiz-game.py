print("Welcome to my computer quiz!")

playing = input("Do you want to play the game? ")

if playing.lower() != "yes":
    quit()

print("Okay, let's play the game :)")

score = 0

# Define questions and answers
questions = [
    ("What does CPU stand for? ", "central processing unit"),
    ("What does GPU stand for? ", "graphics processing unit"),
    ("What does RAM stand for? ", "random access memory"),
    ("What does ROM stand for? ", "read only memory"),
    ("What does PSU stand for? ", "power supply unit")
]

# Loop through questions
for question, correct_answer in questions:
    attempts = 0
    while attempts < 2:  # Allow maximum 2 attempts
        answer = input(question)
        if answer.lower() == correct_answer:
            print("You got it right! Answer is correct")
            score += 1
            break  # Exit the loop if correct answer is given
        else:
            print("Sorry, incorrect.")
            attempts += 1  # Increment attempts
    else:
        print("Out of chances. The correct answer is '{}'.".format(correct_answer))

# Print final score
print("You got {} questions correct out of {}.".format(score, len(questions)))
print("You got {:.2f}% of the questions correct.".format(score / len(questions) * 100))