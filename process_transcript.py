import re, pickle, os.path

# Opens a text file and returns a list of its words, in lowercase.
def get_word_list(source='composite.txt'):
  if not os.path.isfile(source):
    print "File does not exist"
    exit()

  transcript = open(source)
  text = ''

  for line in transcript.readlines():
    text += line

  transcript.close()
  text = text.lower()
  words = re.findall(r"[\w']+", text)

  return words

# Takes a list of words
# Returns a dictionary of words that appear more often than the given
# lower bound together with their count in the corpus.
def get_common_word_dict(words, low_bound=100):
  common = {}
  ignored = 0
  word_set = set(words)

  for word in word_set:
    count = words.count(word)
    if count > low_bound:
      common[word] = count
    else:
      ignored += 1
      if ignored % 100 == 0:
        print ignored, " ignored"

  return common

if __name__ == '__main__':
  words = get_word_list()
  common_words = get_common_word_dict(words)

  print common_words

  word_file = open('common_words', 'wb')
  pickle.dump(common_words, word_file)
  word_file.close()

  word_file = pickle.load(open('common_words', 'rb'))
  print word_file
