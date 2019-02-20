def is_palindrome(text):
    """Return True or False if the text is a palindrome."""
    text = remove_non_letters(text.lower())
#  // 2 helps us look at just half of the list
    for idx in range(len(text) // 2):
        print(text, text[idx], text[-(idx + 1)])
        return text == text[::-1]

def remove_non_letters(text):
    """Strip out every character that is not a letter."""
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    all_letters += all_letters.upper()

    new_text = ""
    for char in text:
        if char in all_letters:
            new_text += char
    return new_text

text = input("Enter a possible palindrome: ")
if is_palindrome(text):
    print("is a palindrome.")
else: 
    print("is not a palindrome.")



    