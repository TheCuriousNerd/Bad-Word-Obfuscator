import BadWordObfuscator.badWords as badWords

slurList = []
obfuscatedSlurList = []
slurList_toObfuscate = badWords.slurList
rot13 = str.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz1234567890",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm0987654321")

def transformWord(word:str):
    """transformWord():
        This transforms a word via string.translate() and returns it.

    Args:
        word (str): A string to transform.

    Returns:
        (str): The transformed word.
    """
    returnString = word.translate(rot13)
    return returnString

def transformWordList(words:list):
    """transformWordList():
        This will obfuscate a list of words via string.translate() and return it.

    Args:
        words (list): A list of strings to transform.

    Returns:
        (list): The transformed list of words.
    """
    newList = []
    for word in words:
        newWord = transformWord(word)
        newList.append(newWord)
    return newList

def append_SlurList(words:list):
    """load_SlurList():
        This will append the slurList and the obfuscatedSlurList by using a untransformed list.

    Args:
        words (list): A list of strings to load.
    """
    global slurList
    global obfuscatedSlurList
    for word in words:
        slurList.append(word)
        newWord = transformWord(word)
        obfuscatedSlurList.append(newWord)
    return None

def append_obfuscatedSlurList(words:list):
    """load_obfuscatedSlurList():
        This will append the obfuscatedSlurList and the slurList by using a transformed list.

    Args:
        words (list): A list of obfuscated strings to load.
    """
    global slurList
    global obfuscatedSlurList
    for word in words:
        obfuscatedSlurList.append(word)
        newWord = transformWord(word)
        slurList.append(newWord)
    return None


def load_SlurList(words:list):
    """load_SlurList():
        This will replace the slurList and the obfuscatedSlurList by using a untransformed list.

    Args:
        words (list): A list of strings to load.
    """
    clear_SlurLists()
    global slurList
    global obfuscatedSlurList
    slurList = words
    for word in words:
        newWord = transformWord(word)
        obfuscatedSlurList.append(newWord)
    return None

def load_obfuscatedSlurList(words:list):
    """load_obfuscatedSlurList():
        This will replace the obfuscatedSlurList and the slurList by using a transformed list.

    Args:
        words (list): A list of obfuscated strings to load.
    """
    clear_SlurLists()
    global slurList
    global obfuscatedSlurList
    obfuscatedSlurList = words
    for word in words:
        newWord = transformWord(word)
        slurList.append(newWord)
    return None

def load_slurListDefault():
    """load_slurListDefault():
        This loads the default slurLists into slurList and obfuscatedSlurList.
    """
    load_SlurList(badWords.slurList)
    return None

def clear_SlurLists():
    """clear_SlurLists():
        This replaces the obfuscatedSlurList and slurList with and empty list.
    """
    global obfuscatedSlurList
    global slurList
    obfuscatedSlurList = []
    slurList = []
    return None

def isSlurWord(wordToCheck:str):
    """isSlurWord():
        This checks wordToCheck against the slurList and returns true if it finds any matches.

    Args:
        wordToCheck (str): The word to be checked.

    Returns:
        (bool): Was a slur detected?
    """
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
