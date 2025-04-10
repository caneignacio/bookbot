def main():
    filepath = "books/frankenstein.txt"
    print(get_text (filepath))

def main2 ():
    filepath = "books/frankenstein.txt"
    text = get_text (filepath)   
    print (f"--- Begin record of {filepath} ---")
    print (f"{word_count(text)} found in the document")
    print_alpha_letters(text.lower())
    print ("--- End report ---")

def get_text (file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count (text):
    words = text.split()
    return len(words)

def char_count (text):
    count = {}
    for char in text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def char_dict_to_sorted_list (char_list):
    sorted_list = []
    for char in char_list:
        sorted_list.append({"ch": char, "num": char_list[char]})
    sorted_list.sort(reverse = True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]

def print_alpha_letters (text):
    characters = char_count(text)
    sorted_characters = char_dict_to_sorted_list (characters)
    for char in sorted_characters:
        if char["ch"].isalpha():
            print (f"The '{char['ch']}' character was found {char['num']} times")


main()
