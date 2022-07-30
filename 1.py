import os , sys
import time

from FileInfo import FileInfo
from XmlExporter import XmlExporter

arguments = sys.argv
print("Passed arguments ", arguments)

if (len(arguments)!=3):
    print("The program requires 2 argyments: Root folder, folder template: ")
    exit()

rootFolder = arguments[1]
templateFolder = arguments[2]
fileCounter = 0
foundFiles = []

for (root, dirs, files) in os.walk(rootFolder, topdown = True):
    if(templateFolder in root):
        print(files)
        print(dirs)
        for f in files:
            fileCounter += 1
            modfiTime = os.path.getmtime(os.path.join(root, f))
            modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modfiTime))
            fileInfo = FileInfo(f, fileCounter, root , modificationTime)
            foundFiles.append(fileInfo)


xmlExporter = XmlExporter()
xmlExporter.exportToXml(rootFolder, templateFolder, foundFiles)
