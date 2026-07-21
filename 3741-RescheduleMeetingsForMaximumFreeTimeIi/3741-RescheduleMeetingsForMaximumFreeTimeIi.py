# Last updated: 7/21/2026, 7:07:04 PM
# class Solution:
#     def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        size = len(startTime)
        gaparr= [[0,0] for i in range(size)]
        gaps = [0]
        left = 0
        right = eventTime
        for i in range(size):
            gaparr[i][0] = startTime[i] - left
            heappush(gaps,-(startTime[i] - left))
            left = endTime[i]
        heappush(gaps,-(eventTime - endTime[-1]))
        for i in range(size-1,-1,-1):
            gaparr[i][1] = right - endTime[i]
            right = startTime[i]
        ans = 0
        for i in range(size):
            curr = gaparr[i][0]+gaparr[i][1]
            barSize = endTime[i] - startTime[i]
            if(-1*gaps[0] >= barSize):
                val = max(gaparr[i][0],gaparr[i][1])
                g1 = heappop(gaps)
                gap1 = -1*g1
                g2 = heappop(gaps)
                gap2 = -1*g2
                if(gap1 > val):
                    curr += barSize
                elif(gap1 == val):
                    if(val == gaparr[i][0]):
                        if(gap2 > gaparr[i][1]):
                            if(gap2 >= barSize):
                                curr += barSize
                        if(gap2 == gaparr[i][1]):
                            if(-1*gaps[0] >= barSize):
                                curr += barSize
                    else:
                        if(gap2 > gaparr[i][0]):
                            if(gap2 >= barSize):
                                curr += barSize
                        if(gap2 == gaparr[i][0]):
                            if(-1*gaps[0] >= barSize):
                                curr += barSize
                heappush(gaps,g1)
                heappush(gaps,g2)
            ans = max(ans, curr)
        return ans
            
        