import os

#membuat direktori jika belum ada
def CreateDirectory(namaFolder):
    if not os.path.exists(namaFolder):
        os.makedirs(namaFolder)

#membuat file baru
def CreateNewFile(path):
    f = open(path, "w")
    f.write("")
    f.close()

#menambahkan data ke file
def WriteToFile(path, data):
    with open(path,"a", encoding="utf-8") as file:
        file.write(data+"\n")

#menambahkan data ke file 
def WriteToFile2(path, data, response):
    fullPath = os.path.join(path, data)
    with open(fullPath, 'wb') as f:
        f.write(response.content)

#memeriksa apakah file sudah ada
def DoesFileExist(path):
    return os.path.isfile(path)

#membaca data pada file
def ReadData(path):
    with open(path, "rt") as file:
        for line in file:
            print(line.replace("\n", ""))

#membaca data per page
def ReadLines(path, lines):
    with open(path, "rt") as file:
        currLine = 0
        for line in file:
            if currLine == lines:
                break
            currLine += 1
            print(line.replace("\n", ""))
