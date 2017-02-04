
import sys
import json
import os
from lib import * 
def print_help():
    s = """
This is Marina. Marina is decision making tool for you. Marina will help you create questionaries, criteria and then score 
things by that criteria by asking you questions you defined. 
Options:
marina create <id> - Create or overwrite questionarie
marina list - List all questionaries 
marina score <id> - Score one thing by criteria you specified in questionarie by given id 
marina score_answered <path> - Score candidate for criteria specified by given answers in file specified by its path
    """
    print(s)


def load_config():
    cfg = {}
    try:
        f = open("~/.marina/config.json")
        cfg = json.loads(f.read())
        return cfg
    except FileNotFoundError:
        return {}
    except json.decoder.JSONDecodeError:
        print("Error while reading config file, skipping and using default config...")
        return {}

if __name__ == "__main__":
    config = load_config()
    db_path = config.get("db_path", "%s/.marina/db/" % os.environ["HOME"])
    if len(sys.argv) == 1:
        print_help()
    if sys.argv[1] in ["help", "-h", "--help"]:
        print_help()
    if sys.argv[1] == "create":
        if len(sys.argv) != 3:
            print("Specify id.")
            exit(1)
        name = input("enter full name for this scoring system: ")
        s = ScoringSystem(name)
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
        try:
            s.saveQuestionsToJSON(db_path + "/" + sys.argv[2] + ".json")
        except FileNotFoundError:
            print("Cannot access database %s" % db_path)
            exit(1)
        ll = []
        try:
            f = open(db_path + "/list.json")
            ll = json.loads(f.read())
            ll.append({"id": sys.argv[2], "name": name})
            f.close()
        except FileNotFoundError:
            ll.append({"id": sys.argv[2], "name": name})
        f = open(db_path + "/list.json", "w")
        f.write(json.dumps(ll, indent=4, sort_keys=True))
        f.close()

    if sys.argv[1] == "list":
        try:
            f = open(db_path + "/list.json")
            ll = json.loads(f.read())
            f.close()
            for l in ll:
                print(l["id"] + " - " + l["name"])
        except FileNotFoundError:
            print("Cannot access database %s" % db_path)
            exit(1)
    if sys.argv[1] == "score":
        if len(sys.argv) != 3:
            print("Specify id!")
            exit(1)
        try:
            s = ScoringSystem.loadQuestionsFromJSON(db_path + "/" + sys.argv[2] + ".json")
            ranking = StandardInputSingleCandidateRankingSystem(s)
            ranking.scoreCandidates()
            ans = input("Do you want to save answers? ")
            if ans in ["yes", "y"]:
                path = input("Enter path to file where you want to save answers: ")
                ranking.getScoringSystem().saveAnswersToJSON(path)
        except FileNotFoundError:
            pass
    if sys.argv[1] == "score_answered":
        if len(sys.argv) != 3:
            print("Wrong parameters!")
            exit(1)
        try:
            s = ScoringSystem.loadAnswersFromJSON(sys.argv[2])
            print("Score: %f" % s.getScore())
        except FileNotFoundError:
            print("Cannot access specified file")
