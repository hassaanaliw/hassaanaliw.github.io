import os
import json
import re

from sh import git, sudo
import uuid


_DIR = "/Users/hassaanali/Desktop/hassaanaliw.github.io/_posts/"
_REPO = "/Users/hassaanali/Desktop/hassaanaliw.github.io/"


def listallfiles():
    list_files = os.listdir(_DIR)
    return list_files


def do_json():
    f = open(_REPO + "data.json", "wb")
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

            u = file.split('-')
            url = '"http://hassaanaliw.github.io/%s/%s/%s/%s/%s/"' % (category.split(':')[1].replace(" ","",1), u[0], u[1], u[2], title.split(':')[1].replace(" ","",1))

            contents.close()

            f = open(_REPO + "data.json", 'a')
            # json.dumps(data,f)

            title = title.split(':')[1]
            description = description.split(':')[1]
            print 'i is %d' % i

            if i != filecount:
                f.write('"%d" : {  \n'
                        ' "title" :  %s, \n\n'
                        '"description" : %s \n\n'
                        '"url" : %s \n\n'
                        "},\n"
                        % (i, title, description,str(url)))
            elif i == filecount:
                print i
                f.write('"%d" : {  \n'
                        ' "title" :  %s, \n\n'
                        '"description" : %s \n\n'
                        '"url" : %s \n\n'
                        "}\n"
                        % (i, title, description,str(url)))

            f.write('\n\n\n')
            f.close()
            # test()

    f = open(_REPO + "data.json", 'a')
    f.write("}")
    f.close()
    github()


def test():
    f = open(_REPO + "data.json", 'r')
    dat = json.load(f)
    print(dat)


def github():
    git1 = git.bake(_cwd=_REPO)
    uu = uuid.uuid4()

    print sudo.git("add", "*")
    print sudo.git("commit", "-m", "%s" % uu)
    print sudo.git("push")


do_json()

