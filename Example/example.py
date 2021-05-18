import BadWordObfuscator.Obfuscator as BadWordObfuscator_

test1 = BadWordObfuscator_.isSlurWord("dghdtrhrsy65eu665")
test2 = BadWordObfuscator_.isSlurWord("This is not a bad Word")
print(test1)
print(test2)

print(BadWordObfuscator_.transformWord("dghdtrhrsy65eu665"))

print(BadWordObfuscator_.transformWordList(["dghdtrhrsy65eu665"]))

BadWordObfuscator_.clear_SlurLists()
BadWordObfuscator_.append_obfuscatedSlurList(BadWordObfuscator_.transformWordList(["dghdtrhrsy65eu665", "123"]))
print(BadWordObfuscator_.obfuscatedSlurList)
print(BadWordObfuscator_.slurList)

BadWordObfuscator_.load_SlurList(["testing123"])

print(BadWordObfuscator_.obfuscatedSlurList)
print(BadWordObfuscator_.slurList)

#BadWordObfuscator_.load_slurListDefault()
#print(BadWordObfuscator_.obfuscatedSlurList)
#print(BadWordObfuscator_.slurList)