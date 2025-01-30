def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lowered_text = lower_string(text)
    initial_dictionary = create_dictionary(lowered_text)
    num_words = get_num_words(text)
    print(f'--- Begin report of {book_path} ---')
    print(f'{num_words} words found in the document\n')
    create_report(initial_dictionary)
    print(f'--- End report ---')


def sort_on(dict):
        return dict["num"]


def create_report(initial_dictionary):

    letters_list = []
    for char in initial_dictionary:
        if char.isalpha():
            letters_list.append({'letter' : char, 'num': initial_dictionary[char]})
            letters_list.sort(reverse=True, key=sort_on)
    for char in letters_list:
        print(f"The '{char['letter']}' character was found {char['num']} times")


def create_dictionary(lowered_text):
    dictionary = {

    }
    lowered_list = list(lowered_text)
    char_count = 0
    for char in lowered_list:
        if char in dictionary:
            char_count = dictionary[char] + 1
            dictionary[char] = char_count
        else:
            dictionary[char] = 1

    return dictionary


def lower_string(text):
    lowered_string = text.lower()
    return lowered_string


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
