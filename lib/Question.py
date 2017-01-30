
class Question(object):
    
    """
    This has to be defined differently for each question type 
    """
    question_type = "base" 

    def ask(self):
        """
        Should return message for a given question
        """
        pass

    def getPoints(self):
        """
        Returns nuber which represents number of points for a given answer to specific question
        """
        pass

    def answer(self, ans):
        self.answer = ans 

    def getAnswer(self):
        return self.answer 
    
    def getType(self):
        return self.question_type
