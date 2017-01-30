
from .RankingSystem import * 

class StandardInputSingleCandidateRankingSystem(RankingSystem):
    
    def setup(self, **kwargs):
        pass

    def scoreCandidates(self):
        ss = self.getScoringSystem()
        for q in ss.getQuestions():
            if q.getType() == "multi_choice":
                print(q.ask())
                for i in range(len(q.getChoices())):
                    print("%d: %s" % (i+1, q.getChoices()[i][0]))
                q.answer(input("Answer: "))
            else:
                q.answer(input(q.ask() + " "))
        return ss.getScore()

                    
