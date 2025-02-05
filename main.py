def main():
    word_count = 0
    with open("books/frankenstein.txt") as f:
            for line in f:
                 words = line.split()
                 word_count += len(words)
            file_contents = f.read()
    print(file_contents)
    return word_count


if __name__ =="__main__":
    main()