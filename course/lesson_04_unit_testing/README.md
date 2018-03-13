### Lesson 4 - Unit testing
- [Testing basics](http://docs.python-guide.org/en/latest/writing/tests/) (focus on *general rules of testing*)
- [Introduction to unittest](http://www.voidspace.org.uk/python/articles/introduction-to-unittest.shtml) (sections: *Introduction, Testing, The unittest Module, The assert methods*, skip the rest)
- [py.test unit tests](https://docs.pytest.org/en/latest/getting-started.html#getstarted) better way to test (it's easier than you think)

### practice projects

1. Modify (The Collatz Sequence) so that its main function takes an argument and return list with all numbers.
Write `unittest.TestCase` tests (2-3) for it.
(Optional) Replace `input()` function for tests basing on https://gist.github.com/kuszcjan/fcb89621191e28dad6f8263f1960e5c8 

2. Write test suite with 3 tests for distance function (The length of the segment) using py.test module

3. Test your code from "Adding factorials"(snakify lesson 4) against function from `math` library.
(optional) try to find case, where your function fails
