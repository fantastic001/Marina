
class RankingSystem():
    
    def __init__(self, scoring_system, **kwargs):
        self.scoring_system = scoring_system
        self.setup(**kwargs)

    def setup(self, **kwargs):
        """
        This has to be implemented to setup specific ranking system
        """
        pass

    def scoreCandidates(self):
        """
        This has to be implemented for every specific ranking system. 

        This method is aimed to provide answers to questions for scoring system
        """
        pass

    def getScoringSystem(self):
        return self.scoring_system
