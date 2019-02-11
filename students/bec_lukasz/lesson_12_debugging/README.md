### Lesson 12 - Debugging
#### introduction
- [Automate the Boring Stuff with Python / Chapter 10](https://automatetheboringstuff.com/chapter10/)
#### practice projects
1. [Automate the Boring Stuff with Python / Chapter 10 / Debugging Coin Toss](https://automatetheboringstuff.com/chapter10/)
1. Verbose output - add configurable logger and 'verbose output' command line argument to project 1 from lesson 11 to allow the user to follow intermediate steps of program execution. The program must allow to configure verbosity on at least 3 levels - disabled, warning (warns and errors only) and info (most detailed)
1. Validated user base - write script that takes email, password, phone number and postal code, validates these fields and if validation passes, saves it to a file as CSV with email considered as unique field. If a record with the same email is already in the file, the old record should be altered by new one. Use validators implemented in lesson 8, exercises 2, 3, 4 and 5. As part of this exercise write combined_validator function that takes email, password, phone number and postal code and throws exceptions if any of arguments doesn't pass validation. Add 'verbose output'.
