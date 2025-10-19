def num_of_words(text):
    print(f"Found {len(text.split())} total words")

def num_of_characters(text):
   characters = {}
   words =  text.split()
   for word in words:
      character =list(word.lower())
      for c in character: 
        if c in characters:
           characters[c] += 1
        else:
            characters[c] = 1 
   for character in characters:
      print(f"{character}: {characters[character]}")   
   return characters
