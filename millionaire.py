def millionairegame():

    start = input("Start game? yes/no ")
    if start == "Yes" or start == "yes":
        print("What is 1 + 1?")
        answer1 = input("a)1\nb)2\nc)3\nd)4\nAnswer: ")
        if answer1.lower() == "b" or answer1.lower() == "2":
            print("Congratulations! You got $100")
        else:
            print("Game Over")
        print("In what year did Word War II end?")
        answer2 = input("a)1942\nb)1943\nc)1945\nd)1946\nAnswer: ")
        if answer2.lower() == "c" or answer2.lower() == "1945":
            print("Congratulations! You got $500")
        else:
            print("Game Over")
        print("In Greek mythology, who is the Goddess of beauty?")
        answer3 = input("a)Aphrodite\nb)Hera\nc)Athena\nd)Persephone\nAnswer: ")
        if answer3.lower() == "a" or answer3.lower() == Aphrodite:
            print("Congratulations! You won $1000! You won!")
        else:
            print("Game Over")

millionairegame()


