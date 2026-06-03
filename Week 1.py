import string

#clean text

def clean_text(text):
    
    text=text.lower()
    text=text.translate(str.maketrans("", "", string.punctuation))
    return text

"""
samples = [
    "Hey, what's up, I am Manas",
    "What a great view! I want to come here again.",
    "Wait... are you serious?! That's unbelievable.",
]
for s in samples:
    print(f"  Original : {s}")
    print(f"  Cleaned  : {clean_text(s)}")
    print()
"""

#count words

def count_words(text):
    words= clean_text(text).split()

    freq={}

    for word in words:
        freq[word]= freq.get(word,0)+1

    return freq


#mood words

MOOD_WORDS = [
    "happy", "sad", "stressed", "hyped",
    "angry", "calm", "excited", "hopeful",
    "frustrated", "peaceful"
]

def find_mood_words(text):
    words = set(clean_text(text).split())

    found= [ m for word in words if word in MOOD_WORDS]
    if found:
        print(f"Mood words found : {found}")
    else:
        print("No mood words found")



#top 5 words
def top_5_words(text):
    freq= count_words(text)

    sorted_words = sorted(freq.items(), key= lambda x: x[1], Reverse=True)
    top_5= sorted_words[:5] 
    
    print(f"Top 5 Words: {top_5}")



#Q6

with open("sentences.txt", "r") as f:
    sentences = [line.strip() for line in f if line.strip()]

for i,sentence in enumerate(sentences,1):
    print(f"Stentence{i}")
    print(f"Original: {sentence}")
    print(f"Cleaned: {clean_text(sentence)}")
    print()

    find_mood_words(sentence)

    top_5_words(clean_text(sentence))





