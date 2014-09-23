import os
import json
import re
from pprint import pprint
from dirtools import Dir
from github import Github
from sh import git,sudo


_DIR = "/Users/hassaanali/Desktop/hassaanaliw.github.io/_posts/"
_REPO = "/Users/hassaanali/Desktop/hassaanaliw.github.io/"


def listallfiles():
    list_files = os.listdir(_DIR)
    return list_files




def do_json():
    f = open(_DIR + "data.json", "wb")
    f.write('{\n')
    f.close()
    i = 0

    filecount = 0
    for file in listallfiles():

        if file[-3:] == ".md":
            filecount += 1

    for file in listallfiles():

        if file[-3:] == ".md":

            i += 1

            contents = open(_DIR + "/" + file, 'r+')
            cont = contents.read()

            reg = r'---\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n---'
            matches = re.match(reg, cont)
            title = matches.group(2)

            description = matches.group(3)
            category = matches.group(4)
            tags = matches.group(5)

            contents.close()

            f = open(_DIR + "data.json", 'a')
            # json.dumps(data,f)

            title = title.split(':')[1]
            description = description.split(':')[1]
            print 'i is %d' % i

            if i != filecount:
                f.write('"%d" : {  \n'
                        ' "title" :  %s, \n\n'
                        '"description" : %s \n\n'
                        "},\n"
                        % (i, title, description))
            elif i == filecount:
                print i
                f.write('"%d" : {  \n'
                        ' "title" :  %s, \n\n'
                        '"description" : %s \n\n'
                        "}\n"
                        % (i, title, description))

            f.write('\n\n\n')
            f.close()
            #test()

    f = open(_DIR + "data.json", 'a')
    f.write("}")
    f.close()
    test()


def test():
    f = open(_DIR + "data.json", 'r')
    dat = json.load(f)
    print(dat)


def github():


    git1 = git.bake(_cwd=_REPO)

    print sudo.git("add", "*")
    print sudo.git("commit","-m","Hrl")
    print sudo.git("push origin master")








github()