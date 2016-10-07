#Пакетное переименование фото для дневника стройки

import os

#Инициализация переменных
#путь к папке
dirPath = 'C:\\Users\\Артем\\Desktop\\tmp\\'

#Директория со списком ЖК
rootDir = os.listdir(dirPath)
#print (rootDir)

#Работа со списком ЖК
for nameDir in rootDir:
    print (nameDir)
    objDir = os.listdir(dirPath + nameDir)
    dirResult = dirPath + '\\' + nameDir + ' готовые'

    if os.path.exists(dirResult):
        a = 1 + 1
    else:
        os.mkdir(dirResult)

    #Работа с директорией корпусов
    for nameObj in objDir:
        print (nameObj)
        objFile = os.listdir(dirPath + nameDir + '\\' + nameObj)
        j = 0

        #Работа с фото корпуса
        for namePhoto in objFile:
            j = j + 1
            #print (namePhoto)
            oldName = dirPath + nameDir + '\\' + nameObj + '\\' + namePhoto
            print (oldName)
            newName = dirResult + '\\Корпус ' + nameObj + ' (' + str(j) + ').jpg'
            print (newName)
            os.rename(oldName, newName)
            

    print ('\n')

input ('Press any key')


