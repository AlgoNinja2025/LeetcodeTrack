// Last updated: 7/21/2026, 7:07:57 PM
class Solution {
public:
    bool isCircularSentence(string sentence) {
         stringstream s(sentence);
        string firstword, prevword, word;
        s >> firstword;
        prevword = firstword;

        while (s >> word) {
            if (prevword.back() != word.front()) {
                return false;
            }
            prevword = word;
        }

        return prevword.back() == firstword.front();
    }
};