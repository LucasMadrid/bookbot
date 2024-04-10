import os


def count_letter(content):
    letter_dict = {}
    count = 0

    for word in content:
        for letter in word.lower():
            if letter.isalpha():
                count += 1
                letter_dict[letter] = letter_dict.get(letter, 0) + 1

    return letter_dict

def main():
    # Path to the books folder
    folder_path = "/workspace/github.com/bookbot/books"
    count_word = 0
    count_letters = 0

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a regular file
        if os.path.isfile(os.path.join(folder_path, filename)):
            # Open the file and read its content
            with open(os.path.join(folder_path, filename), "r") as file:
                content = file.read()
                # Print the content
                content = content.split()
                count_word += len(content)

                # Count the number of letters in the content
                count_letters = count_letter(content)
    
    print(f"--- Begin report of books/{filename} ---")
    print(f"{count_word} words found in the document")
    
    for letter, count in count_letters.items():
        print(f"The '{letter}' character was found {count} times")


if __name__ == "__main__":
    main()