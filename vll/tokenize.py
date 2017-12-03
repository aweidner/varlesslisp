import string
from vll.util import make_generator

O_PAREN = "("
C_PAREN = ")"
FUNC_DEF = "$"
FUNC_CALL = "@"

WHITESPACE = [" ", "\n", "\t"]
NUMBER = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
QUOTE = ['"', "'"]
OPS = ["+", "=", "-"]
ALPHANUMERIC = [char for char in string.ascii_lowercase] + [char for char in string.ascii_uppercase] + NUMBER


def tokenize(string):
    return list(_tokenize(make_generator(string)))


def _tokenize(generator):
    for character in generator:
        if character == O_PAREN or character == C_PAREN or character in OPS:
            yield character
        elif character in NUMBER:
            numbers, remaining = _tokenize_number(generator)
            yield "".join([character] + numbers)

            if remaining and remaining not in WHITESPACE:
                yield remaining
        elif character in QUOTE:
            string = _tokenize_string(generator, sentinel=character)
            yield "".join(string)
        elif character in WHITESPACE:
            pass
        elif character == FUNC_DEF or character == FUNC_CALL:
            characters, remaining = _tokenize_funcname(generator)
            yield "".join([character] + characters)

            if remaining and remaining not in WHITESPACE:
                yield remaining
        else:
            raise Exception("Symbol {} is unrecognized".format(character))


def _tokenize_number(generator):
    tokens = []

    for character in generator:
        if character not in NUMBER:
            return tokens, character
        tokens.append(character)
    raise Exception("End of number never found")


def _tokenize_string(generator, sentinel):
    tokens = []

    for character in generator:
        if character == sentinel:
            return tokens
        tokens.append(character)
    raise Exception("No matching quote found for {}".format(sentinel))


def _tokenize_funcname(generator):
    tokens = []
    for character in generator:
        if character not in ALPHANUMERIC:
            return tokens, character
        tokens.append(character)
    raise Exception("Function names must end with a whitespace character")
