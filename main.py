import wordcloud
from matplotlib import pyplot as plt
import numpy as np
import sys

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words to be use to process the text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # replace all punctuations with empty string
    for punctuation in punctuations:
        file_contents = file_contents.replace(punctuation, '')

    # replace all uninteresting word with empty string, check for other cases
    for word in uninteresting_words:
        file_contents = file_contents.replace(f" {word} ", "")
        file_contents = file_contents.replace(f" {word.upper()} ", "")
        file_contents = file_contents.replace(f" {word.title()} ", "")

    # counts the frequency of words in the formatted file_content
    frequency = {}
    for word in file_contents.split():
        if word.lower() in frequency.keys():
            frequency[word.lower()] += 1
        else:
            frequency[word.lower()] = 1
    
    #word cloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequency)
    return cloud.to_array()

if __name__ == "__main__":
    file_name = input("Enter File Path: ")
    file = open(file_name, encoding='utf-8')
    file_contents = file.read()

    # Display the wordcloud image
    myimage = calculate_frequencies(file_contents)
    plt.imshow(myimage, interpolation = 'nearest')
    plt.axis('off')
    plt.show()

    file_contents.close()
