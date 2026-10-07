
def reverse_each_word(text):
    return " ".join(word[::-1] for word in text.split(" "))


text = input("Enter a string: ")
print("String with each word reversed:", reverse_each_word(text))
