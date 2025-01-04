def main():

    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    # print(file_contents)

    words = file_contents.split()
    # print(len(words))

    # get list of all ascii lowercase characters
    ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"

    char_counter = {}
    for char in file_contents:
        char_lower = char.lower()
        if char_lower in ascii_lowercase:
            if char_lower in char_counter:
                char_counter[char_lower] += 1
            else:
                char_counter[char_lower] = 1

    # print(char_counter)

    # Report
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{len(words)} words found in the document\n")

    for key, value in char_counter.items():
        print(f"The '{key}' character was found {value} times")

    print("--- End report ---")


if __name__ == "__main__":
    main()
