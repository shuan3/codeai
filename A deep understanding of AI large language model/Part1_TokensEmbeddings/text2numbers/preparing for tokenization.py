import numpy as np
import requests
import re
text=requests.get('https://www.gutenberg.org/files/11/11-0.txt').text
print(len(text))
# character strings to replace with space
strings2replace = [
                 '\r\n\r\nâ\x80\x9c', # new paragraph
                 'â\x80\x9c',         # open quote
                 'â\x80\x9d',         # close quote
                 '\r\n',              # new line
                 'â\x80\x94',         # hyphen
                 'â\x80\x99',         # single apostrophe
                 'â\x80\x98',         # single quote
                 '_',                 # underscore, used for stressing
                 ]

# e.g., 'â\x80\x9d'.encode('latin1').decode('utf8')

# use regular expression (re) to replace those strings with space
for str2match in strings2replace:
  regexp = re.compile(r'%s'%str2match)
  text = regexp.sub(' ',text)

# remove non-ASCII characters
text = re.sub(r'[^\x00-\x7F]+', ' ', text)

# remove numbers
text = re.sub(r'\d+','',text)

# and make everything lower-case
text = text.lower()

# let's have a look!
print(text[:10])

# split by punctuation
import string
print(string.punctuation)
puncts4re = fr'[{string.punctuation}\s]+'

words = re.split(puncts4re,text)
words = [item.strip() for item in words if item.strip()]

# remove single-character words
words = [item for item in words if len(item)>1]

# let's have a look!
print(words[:10])


# create the vocab! (set of unique words)
vocab = sorted(set(words))

# convenience variables for later
nWords = len(words)
nLex = len(vocab)

print(f'{nWords} words')
print(f' {nLex} unique tokens')
word2idx = {w:i for i,w in enumerate(vocab)}
idx2word = {i:w for i,w in enumerate(vocab)}

print(f'{idx2word} idx2word')
print(f' {word2idx} word2idx tokens')
# print out a few
# for i in list(word2idx.items())[0:10000:87]:
#   print(i)

# encoder function (using for-loop instead of list-comp)
def encoder(words,encode_dict):

  # initialize a vector of numerical indices
  idxs = np.zeros(len(words),dtype=int)

  # loop through the words and find their token in the vocab
  for i,w in enumerate(words):
    idxs[i] = encode_dict[w]

  # return the indices!
  return idxs


# also need a decoder function
def decoder(idxs,decode_dict):
  return ' '.join([decode_dict[i] for i in idxs])
# test the encoder
print(encoder(['the','time','machines'],word2idx))