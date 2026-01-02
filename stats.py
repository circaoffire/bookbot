def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    word_list = (file_contents).split()
    print(f"Found {len(word_list)} total words")


def character_count(filepath):
    characters = {}

    with open(filepath) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
    
    for character in file_contents:
        if character not in characters:

            characters[character] = 1

        else:
            characters[character] += 1
    
    return characters


def generate_report(filepath):
    characters_dict = character_count(filepath)
    counts = []
    for i in characters_dict:
        if i.isalpha():
            new_dict = {"char": i, "num": characters_dict[i]}
            counts.append(new_dict)

    counts.sort(reverse=True, key=sort_on)
    sorted_dict = {}
    for i in counts:
        sorted_dict[i["char"]] = i["num"]
    return sorted_dict


def sort_on(items):
    return items["num"]

#generate_report("books/frankenstein.txt")