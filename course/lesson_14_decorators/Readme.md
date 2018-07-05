### Lesson 14 - Decorators
#### introduction

- [A guide to Python's function decorators](https://www.thecodeship.com/patterns/guide-to-python-function-decorators/)
- [Easy introduction into decorators](https://www.python-course.eu/python3_decorators.php)

#### practice projects

1. Write `@sort` decorator that when applied to a function that returns a list, sorts this list, so we can do this:
```
@sort
def data_feeder():
  return [4,2,1,3]

data_feeder() == [1,2,3,4] # <- this is True
```

2. Write `@access_required` decorator that when applied to a function executes subjected function only if `has_access` function from `authorization.py` returns `True`. So we can do this:
```
@access_required
def restricted_print(*args, **kwargs):
  print(*args, **kwargs)

restricted_print('1 - visible')
restricted_print('2 - invisible')
restricted_print('3 - invisible')
restricted_print('4 - visible')
```

3. Write `@logged` decorator using `logger_wrapper` from lesson 6. Apply it to several functions to demonstrate that it works.
