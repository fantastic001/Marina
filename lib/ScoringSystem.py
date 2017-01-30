
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
        for q in self.questions:
            score = score + q.getPoints()
        return score

    def getQuestions(self):
        return self.questions

    def makeQuestionsDict(self):
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
        return data

    def dictToQuestion(q):
        if q["type"] == "yesno":
            return YesNoQuestion(q["message"], int(q["yes_points"]), int(q["no_points"]))
        elif q["type"] == "score":
            return ScoreQuestion(q["message"], int(q["min_score"]), int(q["max_score"]), float(q["points_per_score"]))
        elif q["type"] == "multi_choice":
            mq = MultiChoiceQuestion(q["message"])
            for c in q["choices"]:
                mq.addChoice(c["choice"], int(c["points"]))
            return mq
        

    def saveQuestionsToJSON(self, path):
            f = open(path, "w")
            f.write(json.dumps(self.makeQuestionsDict(), indent=4, sort_keys=True))
            f.close()

    def loadQuestionsFromJSON(path):
        f = open(path)
        data = json.loads(f.read())
        ss = ScoringSystem()
        for q in data["questions"]:
            ss.addQuestion(ScoringSystem.dictToQuestion(q))
        f.close()
        return ss

    def saveAnswersToJSON(self, path):
        data = self.makeQuestionsDict()
        for i in range(len(data["questions"])):
            for question in self.getQuestions():
                if question.ask() == data["questions"][i].ask():
                    data["questions"][i]["answer"] = question.getAnswer()
        f = open(path, "w")
        f.write(json.dumps(data, indent=4, sort_keys=True))
        f.close()

    def loadAnswersFromJSON(path):
        ss = ScoringSystem.loadQuestionsFromJSON(path)
        f = open(path)
        data = json.loads(f.read())
        s = ScoringSystem()
        for q in ss.getQuestions():
            for question in data["questions"]:
                if ScoringSystem.dictToQuestion(question).ask() == q.ask():
                    q.answer(question["answer"])
                    s.addQuestion(q)
        return s
