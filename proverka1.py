from os import walk

def rec(dir):
    for (dirpath, dirnames, files) in walk(dir):
        for file in files:
            print(file)
        if len(dirnames) != 0:
            for i in range(len(dirnames)):
                rec(dir+'\\'+dirnames[i])
        return 0

rec('C:/Users/Сергей/PycharmProjects/pythonProject1/proverka1.py')