# переименовывает в нужном виде и раскладывает по папкам, получаемые от фотографов фото, для публикации на сайте
#из "/<имя ЖК>/<номер корпуса>/<произвольное имя>.jpg"
#делаем "/<имя ЖК> готовые/Корпус <номер корпуса> (<номер фото в папке>).jpg"

import os

#Инициализация переменных
#путь к папке
dirPath = 'C:\\Users\\Артем\\Desktop\\tmp\\'

#Директория со списком ЖК
rootDir = os.listdir(dirPath)

#Работа со списком ЖК
for nameDir in rootDir:
    print (nameDir)
    objDir = os.listdir(dirPath + nameDir)
    dirResult = dirPath + '\\' + nameDir + ' готовые'

    if os.path.exists(dirResult):
        pass
    else:
        os.mkdir(dirResult)

    #Работа с директорией корпусов
    for nameObj in objDir:
        print (nameObj)
        objFile = os.listdir(dirPath + nameDir + '\\' + nameObj)
        j = 0

        #Работа с фото корпуса
        for namePhoto in objFile:
            j += 1
            oldName = dirPath + nameDir + '\\' + nameObj + '\\' + namePhoto
            print (oldName)
            newName = dirResult + '\\Корпус ' + nameObj + ' (' + str(j) + ').jpg'
            print (newName)
            os.rename(oldName, newName)
            
    print ('\n')

input ('Press any key')


