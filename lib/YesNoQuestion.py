
from .Question import * 

from .exceptions import * 

class YesNoQuestion(Question):
    
    question_type = "yesno" 

    def __init__(self, msg, yes_points, no_points):
        self.msg = msg
        self.y = yes_points 
        self.n = no_points

    def ask(self):
        return self.msg + " (yes/no)"

    def getPoints(self):
        if self.getAnswer() in ["yes", "y", "Y", "Yes"]:
            return self.y
        elif self.getAnswer() in ["no", "n", "N", "No"]:
            return self.n
        else:
            raise WrongAnswerException()

    def getMessage(self):
        return self.msg

    def getYesPoints(self):
        return self.y

    def getNoPoints(self):
        return self.n
