

from .Question import * 

from .exceptions import * 

class MultiChoiceQuestion(Question):
    
    question_type = "multi_choice" 

    def __init__(self, msg):
        self.msg = msg
        self.choices = []

    def ask(self):
        s = self.msg + " (Enter number between 1 and %d)" % len(self.choices)

    def getPoints(self):
        ans = int(self.getAnswer()) - 1
        if ans < 0 or ans >= len(self.choices):
            raise WrongAnswerException()
        else:
            return self.choices[ans][1]

    def addChoice(self, choice, points):
        self.choices.append((choice, points))

    def getChoices(self):
        return self.choices

    def getMessage(self):
        return self.msg 
