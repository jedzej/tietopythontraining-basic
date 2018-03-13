### Lesson 4 - Unit testing
- [Testing basics](http://docs.python-guide.org/en/latest/writing/tests/) (focus on *general rules of testing*)
- [Introduction to unittest](http://www.voidspace.org.uk/python/articles/introduction-to-unittest.shtml) (sections: *Introduction, Testing, The unittest Module, The assert methods*, skip the rest)
- [py.test unit tests](https://docs.pytest.org/en/latest/getting-started.html#getstarted) better way to test (it's easier than you think)

### practice projects

1. Using `unittest.TestCase` write tests for **The Collatz Sequence** exercise from lesson 3:
- Write 2-3 tests for isolated `collatz()` function to test whether calculations are performed correctly. Aim to pick representative testing sets to verify algorithm reliability in typical, corner and out-of-range conditions.
- Write 2-3 full-scope tests of overall application data flow. Mock `input()` and `print()` functions to perform  end-to-end application testing basing on [this sample code](https://gist.github.com/jedzej/c9129558e87ec5d0b37405afd0ce6f46). Aim to pick representative testing sets to verify algorithm reliability in typical, corner and out-of-range conditions.
 
2. Write test suite with 3 tests for distance function (The length of the segment) using py.test module

3. Test your code from "Adding factorials"(snakify lesson 4) against function from `math` library.
(optional) try to find case, where your function fails
