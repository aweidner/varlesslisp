from vll import _eval, tokenize


def test_we_can_tokenize_a_string_of_whitespace_numbers_and_parenthesis():
    assert tokenize("(1 2 36  42)") == ["(", "1", "2", "36", "42", ")"]


def test_tokenize_will_work_on_multi_level_lists():
    assert tokenize("(1 2 3 4 (5 6 7 8) 9 10)") == ["(", "1", "2", "3", "4", "(", "5", "6", "7", "8", ")", "9", "10", ")"]


def test_tokenize_will_work_with_strings():
    assert tokenize('(1 2 3 "hello world" 4 5 "this is a test")') == ["(", "1", "2", "3", "hello world", "4", "5", "this is a test", ")"]


def test_concatination_is_recognized():
    assert tokenize('(+ "hello world" 1)') == ["(", "+", "hello world", "1", ")"]


def test_functions_can_be_tokenized():
    assert tokenize('($returnFive () (5))') == ["(", "$returnFive", "(", ")", "(", "5", ")", ")"]


def test_sub_functions_will_be_tokenized_correctly():
    assert tokenize(
        """
        (($fib ($n) (
            @cond ((= @n 0) 0)
                  ((= @n 1) 1)
                  (+ (@fib (- @n 1)) (@fib (- @n 2)))))
          (@fib ($ () 5))
        )
        """) == ["(", "(", "$fib", "(", "$n", ")", "(", "@cond", "(",
                 "(", "=", "@n", "0", ")", "0", ")", "(", "(", "=", "@n", "1", ")",
                 "1", ")", "(", "+", "(", "@fib", "(", "-", "@n", "1", ")",
                 ")", "(", "@fib", "(", "-", "@n", "2", ")", ")", ")", ")",
                 ")", "(", "@fib", "(", "$", "(", ")", "5", ")", ")", ")"]
