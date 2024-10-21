import random

print("-----------------------")
print("Welcome to Hangman game")
print("-----------------------")

print("Easy Or Hard")
x= input("Enter your choice: ")

if x == "Easy":
    words = ('apple', 'phone', 'python','car','lamp'"banana", "grape", "cherry")
    chosen = random.choice(words)
    display = ["_" for _ in chosen]
    attempts = 8
else:
    words = ("elephant", "chocolate", "butterfly", "adventure", "mountain","television", "excellent", "sunflower")
    chosen = random.choice(words)
    display = ["_" for _ in chosen]
    attempts = 16

while attempts > 0 and "_" in display:
    print("\n" + ' '.join(display))  
    guess = input("Enter a letter: ").lower()  

    if guess in chosen:
        for index, letter in enumerate(chosen):
            if letter == guess:
                display[index] = guess  
    else: 
        attempts -= 1  
        print("Wrong, Try again")

if "_" not in display:
    print("You won!!")
    print(' '.join(display))
else: 
    print("You ran out of attempts and you lost, the word was: " + chosen)
    



