
class longestCommonSubsequence(object):
    def __init__(self, text1, text2):
        if not isinstance(text1, None) and not isinstance(text2, None):
            self.text1 = text1
            self.text2 = text2
        else:
            print(f"Одна из строк пустая!")
    def lcs(text1, text2):
        print(text1, text2)
        L = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    L[i][j] = L[i-1][j-1] + 1
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])
        return L[len(text1)][len(text2)]
        
textX = "AGGTAB"
textY = "GXTXAYB"
c = longestCommonSubsequence
print("LCS длина: ", c.lcs(textX, textY))
#print("LCS длина: ", len(c.lcs(textX, textY)))