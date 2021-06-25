import os, re, math, base64, sys

pathFile_1 = "C:/Users/Viacheslav Zavadskyi/Documents/GitHub/Lab_CS_1/Code/Tango/Tango.txt"
pathFile_2 = "C:/Users/Viacheslav Zavadskyi/Documents/GitHub/Lab_CS_1/Code/Quickstep/Quickstep.txt"
pathFile_3 = "C:/Users/Viacheslav Zavadskyi/Documents/GitHub/Lab_CS_1/Code/ChaChaCha/ChaChaCha.txt"

def main():
    OutputTheResultsForFile(pathFile_1)
    OutputTheResultsForFile(pathFile_2)
    OutputTheResultsForFile(pathFile_3)

def OutputTheResultsForFile(path):
    text = ReadFile(path)
    print(f'\n{text}\n\nMy realization Base64\n')
    textbyte = Read(path)
    print(base64encode(textbyte))
   
    print('Default realization')
    msgbyte = text.encode('UTF-8')
    base64_bytes = base64.b64encode(msgbyte)
    print(f'\n{base64_bytes}\n')

    print('\nMy realization FOR(Archives)\n')
    textbyte = Read(path+'.bz2')
    print(base64encode(textbyte)) 

def base64encode(s):
    i = 0
    base64 = end = ''
    base64vocabulary = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
  
    padding = len(s) % 3
    if padding != 0:
        while padding < 3:
            s.append(192)
            end += '='
            padding += 1

    while i < len(s):
        b = 0

        for j in range(0,3,1):
            n = s[i]
            b += n << 8 * (2-j)
            i += 1
        print(b)
        base64 += base64vocabulary[ (b >> 18) & 63 ]
        base64 += base64vocabulary[ (b >> 12) & 63 ]
        base64 += base64vocabulary[ (b >> 6) & 63 ]
        base64 += base64vocabulary[ b & 63 ]
 
    base64 += end

    return base64

def Read(path):
    if not os.path.exists(path):
      #  print("File not exist")
        return
    arr = []
    with open(path, "rb") as f:
        while (byte := f.read(1)):
           arr.append(int.from_bytes(byte, "little"))
    return arr

def ReadFile(path):
    if not os.path.exists(path):
        #print("File not exist")
        return

    with open(path, "r", encoding='utf-8') as f:
        text = f.read()
    return text

if __name__ == "__main__":
    main()