import json
sentence="this is a super idea this idea will change the idea if learing"
word=sentence.split()
d={}
for a in word:
  key=a
  if key not in d:
    count=word.count(key)
    d[key]=count
print("counting frequancy", word)
print(json.dumps(d,indent=2))
