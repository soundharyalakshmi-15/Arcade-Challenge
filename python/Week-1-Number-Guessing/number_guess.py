import random


def check_guess(secret: int, guess: int) -> str:
    """
    Compare secret and guess.

    :param secret: the actual number to guess
    :param guess: the user's guess
    """
    if secret == guess:
        return "CORRECT"
    elif secret < guess:
        return "HIGH"
    else:
        return "LOW"


def calculate_score(attempts: int) -> int:
    """
    Score calculation based on attempts.

    :param attempts: Number of attempts made by the user
    """
    if attempts <= 2:
        return 100
    elif attempts <= 5:
        return 70
    elif attempts <= 8:
        return 40
    else:
        return 10


def give_hint(secret: int, guess_history: list) -> str:
    """
    Provide a hint based on the secret number and the history of guesses.

    :param secret: the actual number to guess
    :param guess_history: list of previous guesses
    """
    last = guess_history[-1]
    diff = abs(secret - last)
    if diff <= 5:
        return "Very Close!"
    if diff <= 10:
        return "Close!"
    lower = 1
    upper = 100

    for i in guess_history:
        if i < secret and i >= lower:
            lower = i + 1
        if i > secret and i <= upper:
            upper = i - 1
    return f"Try between {lower} and {upper}"

    # -------- CLI PART (DO NOT MODIFY) ---------


def play():
    secret = random.randint(1, 100)
    attempts = 0
    history = []

    print("Welcome to Smart Number Guessing Game!")

    while True:
        guess = int(input("Enter guess: "))
        attempts += 1
        history.append(guess)

        result = check_guess(secret, guess)

        if result == "CORRECT":
            print("Correct!")
            print("Score:", calculate_score(attempts))
            break

        print(result)
        print("Hint:", give_hint(secret, history))


if __name__ == "__main__":
    play()
