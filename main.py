"""Main fucntion for Magic 8 ball"""
from mods.ball_code import MagicBall
QUESTION = input("Ask your question : ")
print(MagicBall().ball_says())
while True:
    CHOICE = input("Want to ask another question? (Y/n) : ")
    if CHOICE == 'Y':
        QUESTION = input("Ask your question : ")
        print(MagicBall().ball_says())
    elif CHOICE == 'n':
        print("Exiting magic 8 ball...")
        break
    else:
        print("Wrong choice, try again.")
