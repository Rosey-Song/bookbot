def main():
    book_name = input("What is the title? ")
    if book_name == "":
        book_name = "frankenstein"
    path_to_file = f"books/{book_name.lower()}.txt"
    try:
        text = get_book_text(path_to_file)
    except FileNotFoundError:
        print(f"Title {book_name} does not exist.")
    word_count = get_num_words(text)
    letter_occurrences = get_letter_occurrences(text)
    print(f"{book_name} contains {word_count} words.")
    print()
    for letter in letter_occurrences:
        print(f"The letter {letter} was used {letter_occurrences[letter]} times.")

def get_num_words(text):
    return len(text.split())

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_letter_occurrences(text, sort=True):
    def sort_letters_by_occurence(letters_dict={}):
        sorted_letters = {}
        order = sorted(letters_dict, key=letters_dict.get, reverse=True)
        for letter in order:
            sorted_letters[letter] = letters_dict[letter]
        return sorted_letters

    output_letters = {}
    letters = 'a A b B c C d D e E f F g G h H i I j J k K l L m M n N o O p P q Q r R s S t T u U v V w W x X y Y z Z'.split()
    for x in range(0, len(letters), 2):
        print(letters[x])
        output_letters[letters[x]] = text.count(letters[x]) + text.count(letters[x + 1])
    
    return output_letters if not sort else sort_letters_by_occurence(output_letters)

main()