import string
def count_word_occurences(filename):
    word_counts={}
    try:
        with open (filename,'r')as file:
            for line in file:
                words=line.split()
                for word in words:
                    word=word.strip(string.punctuation)
                    word_counts[word]=word_counts.get(word,0)+1
    except fileNotFoundError:
        print("file not found. Please make sure the file exists")
        return None
    return word_counts
def display_word_count(word_counts):
    sorted_word_counts=sorted(word_counts.items(),key=lambda x:x[0].lower())
    for word,count in sorted_word_counts:
        print(f"{word}:{count}")
while True:
    filename=input("Enter the filename:")
    try:
        word_count=count_word_occurences(filename)
        display_word_count(word_count)
        break
    except FileNotFoundError:
        print("File not found")
        choice=input("do you want to enter another filename?(y/n)").lower()
        if choice!='y':
            break