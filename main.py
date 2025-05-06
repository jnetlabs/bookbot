from stats import count_words
from stats import count_characters
from stats import sort_char_counts
import sys

def main():
   
   if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
   else:
    book = sys.argv[1]

   text = get_book_text(book)
   num_words = count_words(text)
   num_chars = count_characters(text)
   sorted_char_list = sort_char_counts(num_chars)
   print_report(book, num_words, sorted_char_list)
 
def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def print_report(book, num_words, sorted_char_list):    
   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {book}...")
   print("----------- Word Count ----------")
   print(f"Found {num_words} total words.")
   print("--------- Character Count -------")
   for entry in sorted_char_list:
        if entry["character"].isalpha():
            print(f"{entry['character']}: {entry['quantity']}")
   print("============= END ===============")

main()
