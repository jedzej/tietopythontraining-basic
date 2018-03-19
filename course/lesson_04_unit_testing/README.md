### Lesson 4 - Unit testing
Unit testing is very wide area of engineering. There are plenty of tools and frameworks supporing developers and testers in tests implementation and execution. In this lesson we'll go through 2 poular testing frameworks: **unittest** and **pytest**.

**Please read the introduction materials carefully - especially if you've never implemented your own unit tests. Your main goal in this lesson is to catch the idea of unit testing.**

#### Introduction materials

- [What is Unit Testing?](https://code.tutsplus.com/articles/the-beginners-guide-to-unit-testing-what-is-unit-testing--wp-25728) (section *What is Unit Testing?* only)
- [Testing basics](http://docs.python-guide.org/en/latest/writing/tests/) (focus on *general rules of testing*)
- [Introduction to unittest](http://www.voidspace.org.uk/python/articles/introduction-to-unittest.shtml) (sections: *Introduction, Testing, The unittest Module, The assert methods*, skip the rest)
- [py.test unit tests](https://docs.pytest.org/en/latest/getting-started.html#getstarted) better way to test (it's easier than you think)

### practice projects

1. Using `unittest.TestCase` write 4 unit tests for `collatz()` function (not the whole script, just the function). Base on [26.4.1. Basic example](https://docs.python.org/3.6/library/unittest.html#basic-example). Don't focus too much on `class` keyword in test definition. Treat this as a code that must be there for tests to be ran. Implement following tests:
    1. Test that the function raises TypeError, if called on `'aoeu'` 
       (use `self.assertRaises`),
    1. Test that it returns 4, if called on 8,
    1. Test that it returns 16, if called on 5.
    1. Run the tests and fix the bugs, if any of the tests are failing. 
        
2. Write test module with 3 unit tests for `distance()` from `The length of the segment` exercise from previous
   exercise [Snakify / Lesson 8 / Problems](https://snakify.org/lessons/functions/problems/):
    1. Test that it crashes with `TypeError` when called on `None` (use `pytest.raises`),
    1. Test that it crashes with `ValueError` when called on `'aoeu'`,
    1. Test it on corner cases:
        1. Zero length,
        1. Negative coordinates,
        1. Only vertical distance,
        1. Only horizontal distance,
    1. Typical conditions (difference on both coordinates),
    1. Test that the order of points does not matter.

3. Test your code from `Fibonacci numbers` from previous lesson. You can use **pytest** or **unittest**.
