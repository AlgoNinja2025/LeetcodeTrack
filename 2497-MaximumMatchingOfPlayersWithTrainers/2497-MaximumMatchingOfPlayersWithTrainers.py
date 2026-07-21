# Last updated: 7/21/2026, 7:08:01 PM
class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        i=0
        j=0
        match = 0
        while i<len(players) and j<len(trainers):
            if players[i] <= trainers[j]:
                i+=1
                j+=1
                match += 1
            else:
                j+=1
        return match