from identifier import Identifier

def test_valid_identifiers():
    id = Identifier()
    assert id.validate_identifier("abc") == True
    assert id.validate_identifier("a1b2") == True
    assert id.validate_identifier("A12345") == True
    assert id.validate_identifier("abc123") == True

def test_invalid_identifiers():
    id = Identifier()
    assert id.validate_identifier("") == False
    assert id.validate_identifier("1abc") == False
    assert id.validate_identifier("a_123") == False
    assert id.validate_identifier("abcdefg") == False
    assert id.validate_identifier("abc1234") == False

def test_identifier_starts_with_number():
    id = Identifier()
    assert id.validate_identifier("1abc") == False
    assert id.validate_identifier("2foo") == False
    assert id.validate_identifier("9x9x9x") == False

def test_identifier_only_digits():
    id = Identifier()
    assert id.validate_identifier("123456") == False
    assert id.validate_identifier("987654") == False
    assert id.validate_identifier("0") == False

def test_identifier_mixed_letters_digits():
    id = Identifier()
    assert id.validate_identifier("a1b2c3") == True
