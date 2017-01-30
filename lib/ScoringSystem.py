
import json 

from .YesNoQuestion import * 
from .ScoreQuestion import * 
from .MultiChoiceQuestion import * 

class ScoringSystem(object):
    
    def __init__(self):
        self.questions = [] 

    def addQuestion(self, q):
        self.questions.append(q)

    def getScore(self):
        score = 0 
        for q in questions:
            score = score + q.getPoints()
        return score

    def getQuestions(self):
        return self.questions

    def saveQuestionsToJSON(self, path):
        data = {}
        data["questions"] = [] 
        for q in self.getQuestions():
            Q = {}
            Q["type"] = q.getType()
            if Q["type"] == "yesno":
                Q["message"] = q.getMessage()
                Q["yes_points"] = q.getYesPoints()
                Q["no_points"] = q.getNoPoints()
            elif Q["type"] == "score":
                Q["message"] = q.getMessage()
                (Q["min_score"], Q["max_score"]) = q.getScoreRange()
                Q["points_per_score"] = q.getPointsPerScore()
            elif Q["type"] == "multi_choice":
                Q["message"] = q.getMessage()
                Q["choices"] = []
                for c in q.getChoices():
                    C = {}
                    C["choice"] = c[0]
                    C["points"] = c[1]
                    Q["choices"].append(C)
            data["questions"].append(Q)
            f = open(path, "w")
            f.write(json.dumps(data))
            f.close()

    def loadQuestionsFromJSON(path):
        f = open(path)
        data = json.loads(f.read())
        ss = ScoringSystem()
        for q in data["questions"]:
            if q["type"] == "yesno":
                ss.addQuestion(YesNoQuestion(q["message"], int(q["yes_points"]), int(q["no_points"])))
            elif q["type"] == "score":
                ss.addQuestion(ScoreQuestion(q["message"], int(q["min_score"]), int(q["max_score"]), float(q["points_per_score"])))
            elif q["type"] == "multi_choice":
                mq = MultiChoiceQuestion(q["message"])
                for c in q["choices"]:
                    mq.addChoice(c["choice"], int(c["points"]))
                ss.addQuestion(mq)
        f.close()
        return ss
    def saveAnswersToJSON(self, path):
        pass

    def loadAnswersFromJSON(path):
        pass
