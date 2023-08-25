#<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
#<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
#<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>
#<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    att = s.split(" ")
    for a in att:
        if url := re.search(r"^src=\"(https?\://(?:www.)?youtube.com/embed/)(.+)\"(?:\>.+)?$", a):
            return f"https://youtu.be/{url.group(2)}"

if __name__ == "__main__":
    main()