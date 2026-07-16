# Space Adventure Quiz
# A beginner-friendly Python project

print("Welcome to the Space Adventure Quiz! 🚀")
print("Answer the questions and test your space knowledge.\n")

score = 0

name = input("What is your name? ")
print(f"Good luck, {name}!\n")

answer = input("1. Which planet is known as the Red Planet? ").strip().lower()
if answer == "mars":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The answer is Mars.\n")

answer = input("2. What is the name of Earth's natural satellite? ").strip().lower()
if answer == "moon" or answer == "the moon":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The answer is the Moon.\n")

answer = input("3. Which planet is the largest in our solar system? ").strip().lower()
if answer == "jupiter":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The answer is Jupiter.\n")

answer = input("4. What star is closest to Earth? ").strip().lower()
if answer == "sun" or answer == "the sun":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The answer is the Sun.\n")

answer = input("5. How many planets are in our solar system? ").strip()
if answer == "8" or answer.lower() == "eight":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The answer is 8.\n")

print(f"{name}, your final score is {score}/5.")

if score == 5:
    print("Amazing! You are a space expert! 🌟")
elif score >= 3:
    print("Great job! You know a lot about space! 🪐")
else:
    print("Nice try! Keep exploring the universe! 🌌")

input("\nPress Enter to close the program.")
