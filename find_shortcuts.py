# Dictioanries of key costs, each one representing the use of a different
# Finger
a = { 'z': 1 }
s = { 'w': 1, 'x': 1, 'q': 1 }
d = { 'e': 1, 'r': 1, 't': 2 }
f = { 'c': 1, 'v': 1, 'g': 1, 'b': 2 }
n = { 'b': 1 }
k = { 'j': 1, 'i': 1, 'm': 1, 'u': 2, 'h': 2, 'y':3, ',':1 }
l = { 'o': 1, 'p': 0, "'": 1 }

homes = [a, s, d, f, n, k, l]

# Divide a given string into a list of characters.
def split(word):
  char_list = []
  for char in word:
    char_list.append(char)
  return char_list

# Calculate the spatial cost of each character in a given word.
def cost(word):
  char_list = split(word)
  cost = 0
  fingers = []
  for char in char_list:
    for home in homes:
      if home.has_key(char):
        cost += home.get(char)
        if home not in fingers:
          fingers.append(home)
  return [cost, len(fingers)]

# Split a huge string of barewords into a list of them, Perl-style
def qw(words):
  return list(words.split(' '))
