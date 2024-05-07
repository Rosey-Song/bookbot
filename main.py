def main():
    book_name = input("What is the title? ")
    if book_name == "":
        book_name = "frankenstein"
    path_to_file = f"books/{book_name.lower()}.txt"
    try:
        text = get_book_text(path_to_file)
    except FileNotFoundError:
        return print(f"Title \"{book_name}\" does not exist.")
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
    letters = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
    output_letters = {}
    def sort_letters_by_occurence():
        sorted_letters = {}
        order = sorted(output_letters, key=output_letters.get, reverse=True)
        for letter in order:
            sorted_letters[letter] = output_letters[letter]
        return sorted_letters
    for x in range(len(letters)):
        output_letters[letters[x]] = text.count(letters[x]) + text.count(letters[x].lwoer())
    
    return output_letters if not sort else sort_letters_by_occurence()

main()