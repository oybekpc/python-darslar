import re 

word1 = "temir"
word2 = "tomir"
word3 = "tulpor"

andoza  = "^t...r"

print(re.match(andoza, word1))
print(re.match(andoza, word2))
print(re.match(andoza, word3))











