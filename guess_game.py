from random import randint


def play():
    random_int = randint(0, 100)

    while True:
        user_guess = int(input("what number did you guess (0, 100)?"))

        if user_guess == random_int:
            print("you found the number({random_int}). congrats")
            break

        if user_guess < random_int:
            print("you found is less than the number we guessed")
            continue

        if user_guess > random_int:
            print("you found is more than the number we guessed")
            continue


if __name__ == '__main__':
    play()
