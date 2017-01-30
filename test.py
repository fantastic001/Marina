
from lib import * 

s = ScoringSystem()

s.addQuestion(YesNoQuestion("Are you sure?", 1, 0))
s.addQuestion(ScoreQuestion("Score it!", 1, 10, 20))

mq = MultiChoiceQuestion("Choose one")
mq.addChoice("Choice 1", 1)
mq.addChoice("Choice 2", 2)
mq.addChoice("Choice 3", 3)
mq.addChoice("Choice 4", 4)

s.addQuestion(mq)

s.saveQuestionsToJSON("test.json")
