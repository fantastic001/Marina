
from .Question import * 

from .exceptions import * 

class ScoreQuestion(Question):
    
    question_type = "score" 

    def __init__(self, msg, min_score, max_score, points_per_score):
        self.msg = msg
        self.min_score = min_score 
        self.max_score = max_score
        self.points_per_score = points_per_score

    def ask(self):
        return self.msg + (" (%d-%d)" % (self.min_score, self.max_score))

    def getPoints(self):
        ans = int(self.getAnswer())
        if ans < self.min_score or ans > self.max_score:
            raise WrongAnswerException()
        else:
            return (self.max_score - self.min_score + 1) * self.points_per_score

    def getMessage(self):
        return self.msg

    def getScoreRange(self):
        return (self.min_score, self.max_score)

    def getPointsPerScore(self):
        return self.points_per_score
