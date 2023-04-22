#
def main():
    # getting user input
    file_path, first_word, second_word = get_user_input()

    create_file_with_replaced_word(file_path, first_word, second_word)


def create_file_with_replaced_word(file_path: str, first_word: str, second_word: str):
    """replace first_word with second_word and creates 'file_path.new' """
    with open(file_path, "r") as file_read:
        text_data = file_read.read()

    reworked_data = text_data.replace(first_word, second_word)

    with open(f"{file_path}.new", "w") as file_write:
        file_write.write(reworked_data)


def get_user_input():
    """Getting user input for file_name_path, first_word, second_word
     and returns it as a tuple """
    file_name_path = input("File path:")
    first_word = input("Word to replace:")
    second_word = input("Replace word:")

    return file_name_path, first_word, second_word


if __name__ == '__main__':
    main()
