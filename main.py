from stats import get_num_words, character_count, generate_report
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    characters_dict = generate_report(filepath)
    print("----------- Word Count ----------")
    get_num_words(filepath)
    print("--------- Character Count -------")
    for key in characters_dict:
        char_count_value = characters_dict[key]
        print(f"{key}: {char_count_value}")
    print("============= END ===============")
    

main()