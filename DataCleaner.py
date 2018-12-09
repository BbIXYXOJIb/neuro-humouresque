import codecs
FileName = "h.txt"
WriteFile = "h2.txt"
Test_V = ""
f = codecs.open( FileName, "r", "utf_8_sig" )
line = "A \n"
char1,char2 = '',''
while line:
    Flag = False
    line = f.readline()
    for char in line:
        char2 = char1
        char1 = char
        if (char1=='k' and char2 == 'v'):
            Flag=True
            continue
        if (char1=='t' and char2 == 'h'):
            Flag=True
            continue
        if (ord(char)>=255):
            if ( ord(char)<1040 or ord(char)>1103):
                Flag = True
    if Flag:
        continue
    Test_V += str(line)
f.close()


f = codecs.open( WriteFile, "w", "utf_8_sig" )
f.write(Test_V)
f.close