answers = []

# list of tuples -список кортежей,каждый из кот.содержит строку(вопрос),словарь(фидбек)
questions = [
    (
        "What happened to Rick C-137’s family? Choose a, b, or c:\n"  # tекст вопроса со всеми вариантами
        "a) He killed his family\n"
        "b) He abandoned his family\n"
        "c) His family was killed\n"
        "Your answer: ",
        {
            "a": "This Rick didn’t kill them",  # cловарь с обратной связью для каждого варианта
            "b": "This Rick didn’t abandon them",
            "c": "That’s right",
        },
    ),
    (
        "What kind of children does Morty have? Choose a, b, or c:\n"
        "a) A test-tube baby\n"
        "b) An incest baby\n"
        "c) No children\n"
        "Your answer: ",
        {
            "a": "Yeah… no",
            "b": "“My giant incest baby’s out there somewhere…” (Morty)",
            "c": "Yeah, right...",
        },
    ),
    (
        "How does Rick feel about Jerry Smith? Choose a, b, or c:\n"
        "a) A close friend\n"
        "b) An arch-enemy\n"
        "c) Something in between\n"
        "Your answer: ",
        {
            "a": "“I don’t like Jerry. He’s an idiot” (Rick)",
            "b": "Wrong dimension, pal. He’s a pain, not a rival",
            "c": "“Jerry, you’re a pain in my ass, but I guess you’re family” (Rick)",
        },
    ),
    (
        "In season 3, what did Rick turn himself into to avoid family therapy? Choose a, b, or c:\n"
        "a) A pickle\n"
        "b) A chili pepper\n"
        "c) An eggplant\n"
        "Your answer: ",
        {
            "a": "A super cool pickle!",
            "b": "That would be interesting, but no",
            "c": "“Nope. Not today, Morty.” (Rick)",
        },
    ),
    (
        "Who’s famous for saying “Wubba Lubba Dub Dub”? Choose a, b, or c:\n"
        "a) Morty\n"
        "b) Squanchy\n"
        "c) Rick\n"
        "Your answer: ",
        {
            "a": "Morty only has exclamations.\n"
            "“Aw, jeez...”\n"
            "“Oh man...”\n"
            "“Oh, geez Rick, I don’t know about this...”",
            "b": "Nice try, but Squanchy’s got his own “Squanch!” vibes",
            "c": "“Classic Rick.” His signature catchphrase",
        },
    ),
]
print()  # для гибкости print()
print(
    "Answer 5 questions about the animated series “Rick and Morty”\n"
    "to test your knowledge and find out how well you know the story!"
)
print()
print("-" * 90)

# две переменные со значением списка и словаря для каждого элемента списка answers
for (
    q_text,  # список
    feedback,  # словарь
) in questions:  # список
    while True:
        answer = input(q_text).lower()
        if answer in ["a", "b", "c"]:
            print()
            print(
                feedback.get(answer)
            )  # вывод фидбека методом .get для словаря по ключу
            print()
            print("-" * 90)
            answers.append(answer)
            break

        else:
            print(
                "\n" + "Invalid input. Please enter a, b, or c.", "\n"
            )  # для компактности \n

correct_answers = ["c", "b", "c", "a", "c"]
score = 0

for user_ans, correct_ans in zip(answers, correct_answers):
    if user_ans == correct_ans:  # сравнение пары ответов
        score += 1

# print(f"Your score: {score} out of {len(correct_answers)}")
print()
if score <= 0:
    print("“What the hell is going on?!”")
elif score <= 3:
    print("Wanna hit rewind on this crazy ride?")
elif score == 4:
    print("“Ready to get schwifty again, dude?”")
elif score == 5:
    print("Looks like you’re schwifty enough to get this nonsense")
print()
print("-" * 90)
