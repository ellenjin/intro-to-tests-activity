from main import count_a_letter
import pytest

def test_letter_is_int(): # Pass in an integer for letter
    # Arrange
    letter = 1
    sentence = "Hello World!"

    with pytest.raises(AttributeError): # expected AttributeError
        count_a_letter(sentence, letter)

def test_empty_sentence(): # Check that empty sentence returns None
    # Arrange
    letter = 'A'
    sentence = ""
    # Act
    result = count_a_letter(sentence, letter)
    # assert
    assert result == None

def test_sentence_letter_same():
    letter = "A"
    sentence = "A"
    result = count_a_letter(sentence, letter)
    assert result == 1