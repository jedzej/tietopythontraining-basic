'''
Regex Version of strip()
Write a function that takes a string and does
the same thing as the strip() string method.
If no other arguments are passed other than
the string to strip, then whitespace characters
will be removed from the beginning and end of the string.
Otherwise, the characters specified in the second argument
to the function will be removed from the string.
'''
import re


def regex_strip(original, char_to_remove=""):
    if char_to_remove == "":
        regex_strip = re.compile(r'^\s*(.*?)\s*$')
        mo = regex_strip.findall(original)
        if mo != []:
            return(mo[0])
    else:
        reStri = r'^[' + char_to_remove + r']' + \
            r'*(.*?)[' + char_to_remove + r']*$'
        regex_strip = re.compile(reStri)
        mo = regex_strip.findall(original)
        if mo != []:
            return(mo[0])


if __name__ == "__main__":
    print(regex_strip("  ala ma kota    "))
    print(regex_strip("  ala     "))
    print(regex_strip("  \t ola \t "))
    print(regex_strip("abaceOla nie ma kotaabace", "abce"))
    print(regex_strip("abaceOlaniemakotaabace", "abce"))
