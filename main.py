def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    (file_contents)
    
def read_file():
     with open("books/frankenstein.txt") as f:
        content = f.read()
        return content
     
print("---Begin report of books---")

def word_counting():
    word_count = 0
    word_count += len(read_file().split())
    return word_count
print(word_counting(), "words found in the text")

def letter_counting():
    counts = {}
    for char in read_file():
        if char.isalpha():
            if char.lower() in counts:
                counts[char.lower()] += 1
            else:
                counts[char.lower()] = 1
    counts_list = [{"char": key, "num": value} for key, value in counts.items()]
    return counts_list

def sort_funt(dict):
    return dict["num"]

alphabets = letter_counting()
alphabets.sort(reverse=True, key=sort_funt)
for char in alphabets:
    if char['num'] > 1:
        print(f"The '{char['char']}' character was found {char['num']} times")
    else:
        print (f"The '{char['char']}' character was found 1 time")

print("--- End Report ---")
print(  )

if __name__ =="__main__":
    main()
