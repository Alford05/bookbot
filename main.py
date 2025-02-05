def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    
def read_file():
     with open("books/frankenstein.txt") as f:
        content = f.read()
        return content

def word_counting():
    word_count = 0
    word_count += len(read_file().split())
    return word_count
print(word_counting())

counts = {}
for char in read_file():
    if char.lower() in counts:
        counts[char] =+ 1
    else:
        counts[char.lower()] = 1
print(counts)

if __name__ =="__main__":
    main()
