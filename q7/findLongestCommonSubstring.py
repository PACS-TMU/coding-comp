def findLongestCommonSubstring(words):
    n = len(words)
    baseWord = words[0]
    baseLen = len(baseWord)
    #result = ""

    for i in range(baseLen):
        for j in range(i + 1, baseLen + 1):
            stem = baseWord[i:j]
            k = 1
            for k in range(1, n):
                #if stem not in words[k]:
                    #break

            if #k + 1 == n and len(result) < len(stem):
                #result = stem

    return result

if __name__ == "__main__":
    wordList1 = ["appleisred", "grapeisreadytoeat", "johnisright", "thisisreal"]
    test1 = findLongestCommonSubstring(wordList1)
    print(test1)
    wordList2 = ["grace", "graceful", "disgraceful", "gracefully"]
    test2 = findLongestCommonSubstring(wordList2)
    print(test2)