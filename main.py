from stats import word_count, character_count, sorted_dictionary

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    num_words = word_count(book_text)
    num_chars = character_count(book_text)
    sorted_chars = sorted_dictionary(num_chars)
    print(f"{num_words} words found in the document")
    
    report = "============ BOOKBOT ============\n"
    report += "Analyzing book found at books/frankenstein.txt...\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {num_words} total words\n"
    report += "--------- Character Count -------\n"

    for num_chars in sorted_chars:
        char = num_chars["char"]
        count = num_chars["num"]

        if char.isalpha():
            report += f"{char}: {count}\n"

    report += "============= END ==============="

    print(report)

    

main()