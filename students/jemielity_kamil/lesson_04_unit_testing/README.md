### Lesson 4 - Unit testing
- [Testing basics](http://docs.python-guide.org/en/latest/writing/tests/) (focus on *general rules of testing*)
- [Introduction to unittest](http://www.voidspace.org.uk/python/articles/introduction-to-unittest.shtml) (sections: *Introduction, Testing, The unittest Module, The assert methods*, skip the rest)
- [py.test unit tests](https://docs.pytest.org/en/latest/getting-started.html#getstarted) better way to test (it's easier than you think)

### practice projects

1. Using `unittest.TestCase` write 4 unit tests for `collatz()` function 
(not the whole script, just the function):
    1. Test that the function raises TypeError, if called on `'aoeu'` 
       (use `self.assertRaises`),
    1. Test that it returns 4, if called on 8,
    1. Test that it returns 16, if called on 5.
    1. Test that it raises ValueError on negative numbers.
    1. Run the tests and fix the bugs, if any of the tests are failing. 
        
2. Write test module with 3 unit tests for `distance()` function from previous
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

3. Test your code from "Adding factorials"(snakify lesson 4) against function from `math` library.
(optional) try to find case, where your function fails
