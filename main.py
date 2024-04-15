# main.py

def main():
     book_path = "books/frankenstein.txt"
     text = get_text(book_path)
     count = word_count(text)
     #print(text.lower())
     letters = letter_count(text)
     char_sorted =get_char_report(letters)
     print(f"--- Begin report of {book_path} ---")
     print(f"{count} words found in the document\n\n")
     for char in char_sorted:
          if char["name"].isalpha():
               print(f"The {char["name"]} character was found {char["num"]} times")
     print("--- End report ---")
     
def get_text(book_path):
     with open(book_path) as f:
         return f.read()

def word_count(text):
     words = text.split()
     return len(words)
     
def letter_count(text):
     letter_dict = {}
     text = text.lower()
     for letter in text:
          if letter in letter_dict:
               letter_dict[letter] += 1
          else:
               letter_dict[letter] = 1
     return letter_dict

def sort_on(d):
     return d["num"]

def get_char_report(letters):
     sorted_list =[]
     for key in letters:
          new_dict = { "name": key, "num": letters[key]}
          sorted_list.append(new_dict)
     sorted_list.sort(reverse=True, key=sort_on)
     return sorted_list


main()