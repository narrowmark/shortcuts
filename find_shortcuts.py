import pickle, os.path

# Dictioanries of key costs, each one representing the use of a different
# Finger
a = { 'a': 1, 'z': 1 }
s = { 's': 1, 'w': 1, 'x': 1, 'q': 1 }
d = { 'd': 1, 'e': 1, 'r': 1, 't': 2 }
f = { 'f': 1, 'c': 1, 'v': 1, 'g': 1, 'b': 2 }
n = { 'n': 1, 'b': 1 }
k = { 'k': 1, 'j': 1, 'i': 1, 'm': 1, 'u': 2, 'h': 2, 'y':3, ',':1 }
l = { 'l': 1, 'o': 1, 'p': 0, "'": 1 }

homes = [a, s, d, f, n, k, l]

# Split a huge string of barewords into a list of them, Perl-style.
def qw(words):
  return list(words.split(' '))

# Takes a dictionary and returns a list sorted according to its values.
def sorted_dict(dictionary):
  output = sorted(dictionary, key=dictionary.get)
  output.reverse()
  return output

# Divide a given string into a list of characters.
def split(word):
  char_list = []
  for char in word:
    char_list.append(char)
  return char_list

# Calculate the spatial cost of each character in a given word.
def calc_cost(word):
  char_list = split(word)
  cost = 0
  fingers = []
  for char in char_list:
    for home in homes:
      if home.has_key(char):
        cost += home.get(char)
        if home not in fingers:
          fingers.append(home)
  return [cost, fingers]

# Opened the pickled dictionary containing common words.
def open_word_dict(source='common_words'):
  if not os.path.isfile(source):
    return

  word_dict = pickle.load(open(source, 'rb'))
  return word_dict

# Return a dictionary withs words as keys and the total costs for each word
# in the corpus as values.
def common_costs(word_dict):
  cost_dict = {}

  keys_by_freq = sorted(word_dict, key=word_dict.get)
  keys_by_freq.reverse()

  for word in keys_by_freq:
    cost = calc_cost(word)[0] * word_dict[word]
    cost_dict[word] = cost

  return cost_dict

def make_shortcut(word, shortcut_dict):
  if len(word) < 3:
    return

  shortcuts = list(shortcut_dict.viewvalues())

  split_string = split(word)
  if split_string[0] not in shortcuts:
    shortcut_dict[word] = split_string[0]
  else:
    shortcut_string = split_string[0]
    split_string.remove(split_string[0])
    for i in split_string:
      temp = shortcut_string + i
      if temp not in shortcuts and calc_cost(i)[0] < 2:
        shortcut_dict[word] = temp

if __name__ == '__main__':
  word_dict = open_word_dict()
  costs = common_costs(word_dict)

  sorted_costs = sorted_dict(costs)
#  print sorted_dict(costs)

  temp = {}

  for key in word_dict:
    make_shortcut(key, temp)

  for i in temp:
    print temp[i], i
