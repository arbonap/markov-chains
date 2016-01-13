from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    #first open file and read it
    #create variable to hold the string of text
    #return the content variable

    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}  #tuple as key, list as value

    #split file into list of words 
    #.split() returns a list of strings
    words = text_string.split()

    #loop over these words by i,
    for i in range(len(words) - 2): #we stopped before last group of words
        if (words[i], words[i + 1]) in chains: #check if key already exists, if yes, append value list
            chains[(words[i], words[i + 1])].append(words[i + 2])
        else:
            chains[(words[i], words[i + 1])] = [words[i + 2]] #if key not already exists, create empty list as value
            # chains[(words[i], words[i + 1])].append(words[i + 2])


    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    # print "CHAINS: ", chains
    #get the first link
    first_key = choice(chains.keys())
    first_word = first_key[0]
    second_word = first_key[1]
    #take random word from the list
    third_word = choice(chains[first_key])
    text = text + first_word + " " + second_word + " " + third_word
    # print text

    #get the new link
    next_word = choice(chains[(second_word, third_word)])

    #take random word from the list
    #which equals to our new key's first word

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

# print chains
