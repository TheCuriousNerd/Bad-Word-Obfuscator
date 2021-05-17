import BadWordObfuscator.badWords as badWords

slurList = []
obfuscatedSlurList = ["snt", "snttbg", "avtn", "avttn", "avttre", "ergneq", "gneq", "egneq", "pbba", "qtuqgeuefl56rh556"]
slurList_toObfuscate = badWords.slurList
rot13 = str.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz1234567890",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm0987654321")

def load_obfuscatedSlurList(targetList):
    for word in targetList:
        word:str = word
        newWord = word.translate(rot13)
        slurList.append(newWord)

def load_slurListDefault():
    for word in obfuscatedSlurList:
        word:str = word
        newWord = word.translate(rot13)
        slurList.append(newWord)

def isSlurWord(wordToCheck):
    isSlur = False
    for word in slurList:
        if wordToCheck == word:
            #print("Found Slur")
            isSlur = True
    if isSlur == True:
        return True
    else:
        return False


if __name__ == "__main__":
    #load_slurList(obfuscatedSlurList)
    load_slurListDefault()
