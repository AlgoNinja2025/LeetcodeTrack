# Last updated: 7/21/2026, 7:08:12 PM
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        ang=0
        ans=[]
        tem = (len(encodedText) // rows)
        cnt = 0
        for h in range(len(encodedText)):
            if cnt + ang + (ang*(tem))<len(encodedText):
                ans.append(encodedText[cnt+ang+(ang*(tem))])
            ang +=1
            if ang >= rows:
                ang = 0
                cnt += 1
        while ans and ans[-1]==" ":
            ans.pop()
        return ("".join(ans))