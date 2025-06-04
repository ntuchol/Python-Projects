import PyPDF2

pdfFile = open('reverse.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))
wrd = input('Please enter one word as a password: ')
pdfWriter.encrypt(wrd)
resultPdf = open('encryptedreverse.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
print(pdfReader.isEncrypted)

helloDict = open('dictionary.txt')
helloDictCont = helloDict.read().splitlines()

liDict = []
for word in helloDictCont:
    liDict.extend(word.split())

PdfFile2 = open('encryptedreverse.pdf', 'rb')
pdfReader2 = PyPDF2.PdfFileReader(PdfFile2)
print(pdfReader2.isEncrypted)

for word in liDict:
    if pdfReader2.decrypt(word) == 1:
        break
        print(word)
    elif pdfReader2.decrypt(word.lower()) == 1:
        break
        print(word)