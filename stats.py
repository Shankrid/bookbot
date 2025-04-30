def word_count(book_text):
    num_words = len(book_text.split())
    return num_words

def character_count(book_text):
    book_text_lower= book_text.lower()
    num_chars = {}
    for char in book_text_lower:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars

def sorted_dictionary(num_chars):

    def sort_on(dict):
        return dict["num"]

    chars_list = []
    for char, count in num_chars.items():
        chars_list.append({"char": char, "num": count})
    
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list