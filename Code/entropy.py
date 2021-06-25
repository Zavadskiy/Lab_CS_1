import os, sys, math, re, collections, base64
from base64own import base64encode

pathFile_1 = "C:/Users/Viacheslav Zavadskyi/Documents/GitHub/Lab_CS_1/Code/Tango/Tango.txt"
pathFile_2 = "C:/Users/Viacheslav Zavadskyi/Documents/GitHub/Lab_CS_1/Code/Quickstep/Quickstep.txt"
pathFile_3 = "C:/Users/Viacheslav Zavadskyi/Documents/GitHub/Lab_CS_1/Code/ChaChaCha/ChaChaCha.txt"

def main():
    informationForFiles(pathFile_1, 'Tango')
    informationForFiles(pathFile_2, 'Quickstep')
    informationForFiles(pathFile_3, 'ChaChaCha')

    informationForArchives(pathFile_1+'.bz2', 'Tango')
    informationForArchives(pathFile_2+'.bz2', 'Quickstep')
    informationForArchives(pathFile_3+'.bz2', 'ChaChaCha')

def ReadBinary(path):
    print('Opening file...')
    with open(path, 'rb') as f:
        byteArr = list(f.read())
    return byteArr

def ReadFile(path):
    if not os.path.exists(path):
        print("File not exist")
        return
    with open(path, "r", encoding='utf-8') as f:
        text = f.read()
    return text

def informationForFiles(path, name):
    print(f'\nEntropy for {name} file\n{ReadFile(path)}\n')
    byteArr = ReadFile(path).lower()
    freqList = countFrequency(byteArr)
    printCurrentFrequency(freqList,byteArr)
    countEntropy(freqList, byteArr)
    amountOfInformation = countEntropy(freqList, byteArr)
    CompareWithSizeOfArchive(amountOfInformation, path)

    print(f'\nEntropy for {name} file base64\n')
    byteArrArchive = ReadBinary(path)
    base64_bytes = base64encode(byteArrArchive)
    b = bytearray()
   # b.extend(map(ord, base64_bytes))
    freqList = countFrequency(b)
    countEntropy(freqList, b)

def informationForArchives(path, name):
    print(f'\nEntropy for {name} archive\n')
    byteArr = ReadBinary(path)
    freqList = countFrequency(byteArr)
    countEntropy(freqList, byteArr)

    print(f'\nEntropy for {name} archive base64\n')
    base64_bytes = base64encode(byteArr)
    b = bytearray()
    b.extend(map(ord, base64_bytes))
    freqList = countFrequency(b)
    countEntropy(freqList, b)  

def countFileSize(byteArr):
    fileSize = len(byteArr)
    return fileSize

def countFrequency(byteArr):
    listOf = collections.Counter(byteArr)

    fileSize = countFileSize(byteArr)
    #Frequency list
    freqList = []
    for item in listOf:
        freqList.append(listOf[item] / fileSize)
    
    return freqList

def printCurrentFrequency(freqList, byteArr):
    listOf = collections.Counter(byteArr)
    fileSize = countFileSize(byteArr)   
    
    k = 0
    print("\n| Letter|\t|Counts|\t|Frequency|")
    percentage = 0
    for i in range(len(freqList)):
        value = list(listOf.keys())[i]

        if value ==' ': value = '\' \''
        elif value == '\n': value = '\\n'
        elif value == '\b': value = '\\b'
        elif value == '\r': value = '\\r'
        elif value == '\t': value = '\\t'
        elif value == '\v': value = '\\v'

        print(f'\a{value}\t\t| {round(freqList[i]*fileSize)}\t\t| {round(freqList[i]*100, 3)}')
        percentage+=freqList[i]
    print(f'Percentage === {percentage}')

def countEntropy(freqList, byteArr):
    fileSize = len(byteArr)

    # Entropy
    ent = 0.0
    for freq in freqList:
        if freq > 0:
            ent = ent + freq * math.log(freq, 2)
    ent = -ent

    amountOfInformation = ent*fileSize
    print(f"Averange entropy: {round(ent, 4)} біт")
    print(f"Count of information: {round(amountOfInformation, 4)} bit")
    print(f"Count of information: {round(amountOfInformation/8, 4)} byte\n")
    print(f"File size: {fileSize} byte")

    amountOfInformation = amountOfInformation/8
    if fileSize > amountOfInformation: sign='>' 
    elif fileSize == amountOfInformation: sign='==' 
    else: sign='<'

    print(f"File size {sign} Count of information\n")

    return amountOfInformation

def CompareWithSizeOfArchive(amountOfInformation, path):
    archive = [ ".rar", ".zip", ".gz", ".bz2", ".7z" ]
    
    for extention in archive:
        file_size = os.path.getsize(path+extention)
        print(f"Archive size {extention}: {file_size}")
        
        if file_size > amountOfInformation: sign='>'
        elif file_size == amountOfInformation: sign='=='
        else: sign='<'
        
        print(f"Archive size {extention} {sign} Count of information")

if __name__ == "__main__":
    main()