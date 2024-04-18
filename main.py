import string

def remove_spaces_and_special_characters(text: str) -> str:
  special_characters: str = set(string.punctuation + " " + "—,\'-’\"")
  return "".join(c for c in text if c not in special_characters)

input_text: str = input("Введіть текст: ")
print(remove_spaces_and_special_characters(text))
