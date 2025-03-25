from textblob import TextBlob

def check_spelling(sentence):
    blob = TextBlob(sentence)
    corrections = {}

    for word in blob.words:
        # Correct word if it's misspelled
        corrected_word = word.correct()
        if word != corrected_word:
            corrections[word] = corrected_word

    return corrections

# Get input from the user
input_sentence = input("Enter the sentence you want to check for errors: ")

# Check spelling and get corrections
corrections = check_spelling(input_sentence)

# Print the errors and suggestions
if corrections:
    print("The following errors were found and suggested corrections are provided:")
    for word, correction in corrections.items():
        print(f"{word} -> {correction}")
else:
    print("No spelling errors found in the sentence.")

