import os
import datetime

def rec(dir):
    for (dirpath, dirnames, files) in os.walk(dir):
        for file in files:
            if file.endswith('.py'):
                print(file)
                print(datetime.datetime.fromtimestamp(os.path.getatime(dir+'/'+file)))
        if len(dirnames) != 0:
            for i in range(len(dirnames)):
                rec(dir+'\\'+dirnames[i])
        return 0

rec('C:/Users/Сергей/PycharmProjects/pythonProject1')