def print_welcome():
    pass

def read_template(file_path):
    try:
        with open(file_path) as file:
            content = file.read().strip()
    except FileNotFoundError:
        return 'File not found'
    return content

def parse_template(template_string):
    content_without_words = ''
    list_of_words = []
    # Use String methods, better to use regex to parse the words out of the content (findall in regex)
    # For each word:
        # append it to the list_of_words (list_of_words.append())
        # Remove it from content (in regex, sub with '')
    return content_without_words, list_of_words


# def temp():
#     return (1,2)

    

# No testing for get_words
def get_words(words):
    answers_from_player = []
    # Iterate over words
    # Ask the player for answers
    # Append them to answers_from_player list
    # return answers_from_player


def merge(bare_text, answers):
    merged_text = ''
    # Merging process 
        # String.format(*answers) to find {} and replace with words
    return merged_text


if __name__ == "__main__":
    print(read_template('dark_and_stormy_night_template.txt'))
    # print(temp())
    
    print_welcome()
    content = read_template('file_name')
    content_without_words, list_of_words = parse_template(content)
    answers = get_words(list_of_words)
    merged_text = merge(content_without_words, answers)
    print(merged_text)
