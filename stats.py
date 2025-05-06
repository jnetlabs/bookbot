def count_words(text):
    return len(text.split())

def count_characters(input):
    character_counts = {}
    lowerinput = input.lower()
    for character in lowerinput:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    return character_counts

def sort_on(dict):
    return dict["quantity"]

def sort_char_counts(num_chars):
    character_count_list = []
    for char in num_chars:
            list_entry = {
                "character": char,
                "quantity": num_chars[char]
            }
            character_count_list.append(list_entry)
    character_count_list.sort(reverse=True, key=sort_on)
    return character_count_list
