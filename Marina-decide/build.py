
from lib import * 

s = ScoringSystem()

ans = ""
while ans != "q":
    print("Select option: ")
    print("a: Add question")
    print("q: Quit")
    ans = input(">> ")
    if ans == "a":
        while not ans in [1, 2, 3]:
            print("Select type of question")
            print("1: yes/no")
            print("2: Score")
            print("3: Multi choice")
            ans = int(input("Choice: "))
        if ans == 1:
            msg = input("Message: ")
            yes_points = int(input("Points when 'yes' answered: "))
            no_points = int(input("Points when 'no' answered: "))
            s.addQuestion(YesNoQuestion(msg, yes_points, no_points))
        elif ans == 2:
            msg = input("Message: ")
            max_score = int(input("Maximal score: "))
            min_score = int(input("Minimal score: "))
            points_per_score = float(input("Points per score point: "))
            s.addQuestion(ScoreQuestion(msg, min_score, max_score, points_per_score))
        else:
            mq = MultiChoiceQuestion(input("Message: "))
            n = int(input("Number of possible choices: "))
            for i in range(n):
                c = input("Choice description: ")
                p =  int(input("Points when choice is selected: "))
                mq.addChoice(c,p)
            s.addQuestion(mq)

path = input("Enter path to file where you want your scoring system to be saved: ")
s.saveQuestionsToJSON(path)
