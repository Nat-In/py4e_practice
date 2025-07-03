# результат-одно из двух логических значений True/False
# <class 'bool'>
#

stored_password = "1234"
secret_answer = "yes"
attempts = 0  # счетчик попыток

while True:
    password = input("Enter password: ")
    if not password:  # nустая строка "" → False
        print("Empty input. Try again.")
        continue
    if password == stored_password:
        print("Welcome!")
        break
    attempts += 1  # увелич.счетчик
    if attempts == 3:  # attemps == 3 ->True; not equal -> False
        print("Too many attempts")
        print('Please answer your security guestion to proceed: "Is it you?"')
        answer = input("Answer: ").lower()  # нижний регистр
        if answer == secret_answer:  # True/False
            print("Verified. You have 3 attempts again.")
            attempts = 0  # сбрасываем счетчик
            continue
        else:
            print("Identity not verified. Access denied.")
            break
    else:
        # форматируемая строка с кол-вом оставшихся попыток
        print(f"Wrong password. Please try again. Attempts left: {3 - attempts}")
