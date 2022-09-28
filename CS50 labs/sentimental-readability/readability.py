def calculate_grade(text):
    """Calculate readability grade"""
    # Calculate number of letters, words and sentences
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Calculate average of letters per 100 words
    L = letters / words * 100.00

    # Calculate average of sentences per 100 words
    S = sentences / words * 100

    # Put everything together using Coleman-Liau's formula
    return round((0.0588 * L) - (0.296 * S) - 15.8)


def count_letters(text):
    """Count the total number of letters in the text"""
    return len([char for char in text if char.isalpha()])


def count_words(text):
    """Count the total number of words in the text"""
    return text.count(" ") + 1


def count_sentences(text):
    """Count the total number of sentences in the text,
    Without having into account the contractions like Mr. or Mrs."""
    return text.count("!") + text.count("?") + text.count(".")


def print_grade(g):
    """Print grade accordingly"""
    if g > 16:
        print("Grade 16+")
    elif g < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {g}")


if __name__ == '__main__':
    # Get text
    text = input("Enter some text: ").rstrip()

    # Calculate grade
    grade = calculate_grade(text)

    # Print grade - max 16, min 1
    print_grade(grade)