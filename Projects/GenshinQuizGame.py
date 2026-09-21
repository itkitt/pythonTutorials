# Genshin Quiz Game
# Utilizing the use of Collection!

# Questions
# Created in tuples; comma used to separate each elements
questions = ("Who is the last surviving Yaksha: ",
            "What are the names of the Magician Twins in Fontaine: ",
            "Who is known as the Archon of Love: ",
            "What was the first given name for the child of the Raiden Shogun: ",
            "Who was the first playable character with a cutscene of them obtaining their vision: ")

# Options
# Created in tuples; 2D collections used to implement multiple elements within a single element
options = (("A. Indarias", "B. Ganyu", "C. Alatus", "D. Zibai"),
            ("A. Barbara & Jean", "B. Lyney & Lynette", "C. Kusanali & Rukkhadevata", "D. Odette & Odile"),
            ("A. Anastasya", "B. Raiden Makoto", "C. Guizhong", "D. Nabu Malikata"),
            ("A. Kunikuzushi", "B. Kabukimono", "C. Scaramouche", "D. Wanderer"),
            ("A. Ineffa", "B. Kazuha", "C. Rana", "D. Wanderer"))

# Answers
answers = ("C", "B", "A", "B", "D")
# Guesses to be appended later
guesses = []
# Score to be added
score = 0
# Question number for reference in loops and calculations
question_num = 0

# For loop to output questions
for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]: # For loop to output questions, referencing question number "0" to see which to output
        print(option)
    guess = input("Enter (A,B,C,D): ").upper() # Capitalize guesses
    guesses.append(guess) # Appends guesses into empty guess list to be referenced later
    if guess == answers[question_num]: # Adds score if answer are the same in the answers list
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer!")
    question_num += 1 # Increments question_num by 1

# Results
print("--------------------")
print("       RESULTS      ")
print("--------------------")

# Prints answers list
print("Answers: ", end = "")
for answer in answers:
    print(answer, end=" ")
print()

# Prints guesses list
print("Guesses: ", end = "")
for guess in guesses:
    print(guess, end=" ")
print()

# Calculates the score by having accumulated score divided by the amount of questions found, multiplied by 100 for percentage
score = int(score / len(questions) * 100)
# Prints score
print(f"Your score is {score}%")
