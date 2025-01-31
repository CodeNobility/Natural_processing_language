import string
from collections import Counter
import matplotlib.pyplot as plt

# with open("file.txt", "w", encoding="utf-8") as f :
#     text = f.write("Prince kuMAr @email id # is princeGupta1726@gmail.com !")

with open("file.txt", encoding="utf-8") as f:
    text1 = f.read()
    lower_case = text1.lower()
    #print(lower_case)
    cleaned_text = lower_case.translate(str.maketrans(" ", " ", string.punctuation))
    #print(cleaned_text)

tokenized_words = cleaned_text.split()
#print(tokenized_words)

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_word = []
for word in tokenized_words:
    if word not in stop_words:
        final_word.append(word)

#print(final_word)


emotion_list = []
with open("emotions.txt", "r") as file:
    for line in file:
        clear_line = line.replace("\n", "").replace("'", '').replace(",", "").strip()
        word, emotion = clear_line.split(":")

        if word in final_word:
            emotion_list.append(emotion)

print(emotion_list)
x = Counter(emotion_list)
print(x)

fig , ax1 = plt.subplots()
ax1.bar(x.keys(), x.values())
fig.autofmt_xdate()
plt.savefig("graph")
plt.show()




