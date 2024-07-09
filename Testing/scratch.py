import os


def replace_word_in_file(file_path, old_word, new_word):
    with open(file_path, 'r') as file:
        content = file.read()

    content = content.replace(old_word, new_word)

    with open(file_path, 'w') as file:
        file.write(content)


def replace_word_in_directory(directory_path, old_word, new_word):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        if os.path.isfile(file_path):
            replace_word_in_file(file_path, old_word, new_word)


if __name__ == "__main__":
    directory_path = "/home/twarit/PycharmProjects/Testing"
    old_word = "login"
    new_word = "login"

    replace_word_in_directory(directory_path, old_word, new_word)
