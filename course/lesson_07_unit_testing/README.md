### Lesson 7 - Unit testing
- [Testing basics](http://docs.python-guide.org/en/latest/writing/tests/) (focus on *general rules of testing*)
- [Introduction to unittest](http://www.voidspace.org.uk/python/articles/introduction-to-unittest.shtml) (sections: *Introduction, Testing, The unittest Module, The assert methods*, skip the rest)
- [py.test unit tests](https://docs.pytest.org/en/latest/getting-started.html#getstarted) better way to test (it's easier than you think)

### practice projects

1. Modify **The Collatz Sequence** from lesson 3 so that its main function takes an argument and returns list with all numbers.
Write `unittest.TestCase` tests 3 for it: 
 - **TO BE DEFINED** test 1
 - **TO BE DEFINED** test 2
 - **TO BE DEFINED** test 3

 - (Optional) **TO BE PRECISED** Replace `input()` and `print()` function for tests basing on https://gist.github.com/jedzej/c9129558e87ec5d0b37405afd0ce6f46 

2. Write test suite with 3 tests for distance function **The length of the segment** using py.test module

3. Test your code from "Adding factorials" (snakify lesson 4) against function from `math` library.
(optional) try to find case, where your function fails