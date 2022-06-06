# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    file1 = open(filename,'r')
    text = file1.read()
    file1.close()
    
    return text


def count_words():
    text = read_file_content("./story.txt")
    word_count = {}
    print(text)
    for word in text.replace('\n','').replace(',','').split(' '):
        if word not in word_count:
            word_count[str(word)] = 1
        else:
            word_count[word] += 1
        # print(word)
    # [assignment] Add your code here

    return word_count
# text = read_file_content("./story.txt")
text =  count_words()
print(text)