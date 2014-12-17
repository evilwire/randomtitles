from yaml import load
from os.path import realpath, dirname
from random import randint

def random_title():
    title_dir = dirname(realpath(__file__))

    with open("%s/title.yml" % title_dir) as title_file:
        titles = load(title_file)

    index = randint(0, len(titles) - 1)
    return titles[index]

print random_title()