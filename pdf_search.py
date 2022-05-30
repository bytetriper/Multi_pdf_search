from posixpath import basename
import pdfplumber
import os
import re
#pdf=pdfplumber.open("./python/pdfplumber/test.pdf")
#lt=pdf.pages[1].extract_text()
#print(lt)
#print(len(pdf.pages))
#
#os.chdir("./python/pdfplumber")
cur_dir=os.getcwd()
files=os.listdir(cur_dir)
pdffiles=[]
for file in files:
    if file.split('.')[1]=="pdf":
        pdffiles.append(file)
#print(pdffiles)
print("Finding Files......")
for file in pdffiles:
    print("Find "+file+" Loading....")
    pdf=pdfplumber.open(file)
    with open("tmp.txt","w",encoding="utf8") as f:
       for page in pdf.pages:
           content=page.extract_text()
           f.write(content)
print("Loading complete!")
tar=open("tmp.txt","r",encoding="utf8")
cts=tar.readlines()
while 1:
    input_words=input("Input Search Text:")
    if input_words=="exit":
        break
    words=input_words.split(' ')
    pat=[]
    matched=[]
    for key in words:
        pat.append('.*'+key+'.*')
        print(key,' ')
    print('')
    fg=0
    output_check=0
    for txt in cts:
        fg=0
        for keypat in pat:
            match=re.match(keypat,txt)
            if match:
                fg+=1
            else:
                break
        if fg==len(pat):
            print(txt)
            output_check=1
    if output_check==0:
        print("No Matching content:(")
tar.close()
os.remove("tmp.txt")
