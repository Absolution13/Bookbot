def main():
   book_path = "books/frankenstein.txt"                         #  ASSIGNING VARIABLES FOR FILE PATH / REPORT / FUNCTIONS
   text = get_book_text(book_path)
   num_words = get_num_words(text)
   report(book_path,text)


def get_num_words(text):                                        # FUNCTION FOR COUNTING THE NUMBER OF WORDS IN A STRING 
    words = text.split()
    return len(words)

def get_book_text(path):                                        # FUNCTION TO READ A FILE PATH
    with open(path) as f:
        return f.read()

def count_characters(text):                                     # FUNCTION FOR COUNTING THE NUMBER OF A LOWERCASE CHARACTER WAS USED INSIDE THE TEXT
    character_count = {}
    for character in text:
        lowered_character = character.lower()
        if lowered_character.isalpha():
            if lowered_character in character_count:
                character_count[lowered_character] += 1
            else:
                character_count[lowered_character] = 1
    return(character_count)

def sort_on(dict):                                              # SORTING FUNCTION
    return dict["num"]

def report(bookpath,text):                                      # FUNCTION FOR PUBLISHING A REPORT, CONTAINING THE TOTAL NUMBER OF WORDS AND THE NUMBER OF EACH CHARACTER USED, SORTED IN REVERSE
    print(f"--- Begin report of {bookpath} ---")

    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    character_count = count_characters(text)
    sorted_characters = sorted(character_count.items(), key=lambda item: item[1], reverse=True)
    print("Character frequency (sorted):")
    for character,count in sorted_characters:
        print(f"{character}: {count}")
    
    print("--- End of report ---")


main()
