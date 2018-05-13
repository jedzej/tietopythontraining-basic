import re


def my_strip(text, characters=" "):
    r_text = re.compile("^([" + characters + "]*)|([" + characters + "]*)$")
    print(r_text.sub("", text))


def main():
    my_strip("  No to wywalamy spacje...  ")
    my_strip("chyba Python jest ok!    ", " chyba")
    my_strip("Hmmm  Kurcze! To działa  Hmmm", "Hm ")


if __name__ == "__main__":
    main()
