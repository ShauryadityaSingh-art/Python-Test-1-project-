import random
secret_number=random.randint(1,50)
chances=5
print("Guess a number between 1 to 50 in 5 chances. Good Luck !! ")

while chances>0:
    print(f"Lives: {'❤ ' * chances}")
    guess=int(input("Enter your number: "))
    if guess == secret_number:
        print(f"Congratulation!! Your guess is correct ! ╰(*°▽°*)╯")
        break

    diff = abs(secret_number-guess)

    if diff<=2:
        hint="🗿 Hot! Diffrence is less than 2"
    elif diff<=5:
        hint="🧨 Warm! Diffrence is less than 5"
    elif diff<=10:
        hint="🤧 Cold! Diffrence is less than 10"
    else:
        hint="😪 Ice cold! Diffrence is more than 10" 
    chances = chances-1
    if chances>0:
            print(f"Wrong Guess! Hint: {hint}\n")
    else:
            print(f"Game Over! Chances Over. The Secret Number is {secret_number}")