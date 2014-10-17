import re

transcript = open('composite.txt')
text = ''

for line in transcript.readlines():
  text += line

def process(text):
  output = re.findall(r"[\w']+", text)
  return output

text = process(text)
text_set = set(text)
common = []

print len(text_set)

ignored = 0
for word in text_set:
  if text.count(word) > 100:
    common.append(word)
    print word, len(common)
  else:
    ignored += 1
    if ignored % 100 == 0:
      print ignored, " ignored"

print len(common)
print common
