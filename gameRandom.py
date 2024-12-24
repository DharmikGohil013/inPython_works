import  random
print("Enter any number (1 to 15) only 5 time")

x=int(input())

random_choice = random.randint(1,15)

for i in range(5):
    if (random_choice == x):
        print("You win!")
        exit()
    else:
        if(x>random_choice):
            print("Enter Low Number")
        elif(x<random_choice):
            print("Enter High Number")

        print(f"your chance is {i}")
        x=int(input())
print("Game Over")