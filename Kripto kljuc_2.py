#--------------- Klijent SERVER STRANA -----------------#

import socket

host = "192.168.0.16"
port = 34437

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))
print('Konekcija - ostvarena!')

def Convert(prijem_1):
    
    if "|" in prijem_1:
        prijem_2 = prijem_1.replace("|", " ")
        listaNova = []
        for x in prijem_2:
            listaNova += [x]
        listaNova.reverse()
        return listaNova

    else:
        listaNova_2 = []
        for x in prijem_1:
            listaNova_2 += [x]
        listaNova_2.reverse()
        return listaNova_2


def Dekripter(simbol):
    if (simbol == "o"):
        simbol = "a"
    elif (simbol == "c"):
        simbol = "o"
    elif (simbol == "m"):
        simbol = "c"
    elif (simbol == "f"):
        simbol = "m"
    elif (simbol == "r"):
        simbol = "f"
    elif (simbol == "p"):
        simbol = "r"
    elif (simbol == "k"):
        simbol = "p"
    elif (simbol == "h"):
        simbol = "k"
    elif (simbol == "d"):
        simbol = "h"
    elif (simbol == "u"):
        simbol = "d"
    elif (simbol == "v"):
        simbol = "u"
    elif (simbol == "b"):
        simbol = "v"
    elif (simbol == "y"):
        simbol = "b"
    elif (simbol == "g"):
        simbol = "y"
    elif (simbol == "x"):
        simbol = "g"
    elif (simbol == "w"):
        simbol = "x"
    elif (simbol == "l"):
        simbol = "w"
    elif (simbol == "z"):
        simbol = "l"
    elif (simbol == "n"):
        simbol = "z"
    elif (simbol == "j"):
        simbol = "n"
    elif (simbol == "s"):
        simbol = "j"
    elif (simbol == "i"):
        simbol = "s"
    elif (simbol == "t"):
        simbol = "i"
    elif (simbol == "q"):
        simbol = "t"
    elif (simbol == "e"):
        simbol = "q"
    elif (simbol == "a"):
        simbol = "e"

    if (simbol == "A"):
        simbol = "O"
    elif (simbol == "O"):
        simbol = "C"
    elif (simbol == "C"):
        simbol = "M"
    elif (simbol == "M"):
        simbol = "F"
    elif (simbol == "F"):
        simbol = "R"
    elif (simbol == "R"):
        simbol = "P"
    elif (simbol == "P"):
        simbol = "K"
    elif (simbol == "K"):
        simbol = "H"
    elif (simbol == "H"):
        simbol = "D"
    elif (simbol == "D"):
        simbol = "U"
    elif (simbol == "U"):
        simbol = "V"
    elif (simbol == "V"):
        simbol = "B"
    elif (simbol == "B"):
        simbol = "Y"
    elif (simbol == "Y"):
        simbol = "G"
    elif (simbol == "G"):
        simbol = "X"
    elif (simbol == "X"):
        simbol = "W"
    elif (simbol == "W"):
        simbol = "L"
    elif (simbol == "L"):
        simbol = "Z"
    elif (simbol == "Z"):
        simbol = "N"
    elif (simbol == "N"):
        simbol = "J"
    elif (simbol == "J"):
        simbol = "S"
    elif (simbol == "S"):
        simbol = "I"
    elif (simbol == "I"):
        simbol = "T"
    elif (simbol == "T"):
        simbol = "Q"
    elif (simbol == "Q"):
        simbol = "E"
    elif (simbol == "E"):
        simbol = "A"

    if (simbol == "~"):
        simbol = "1"
    elif (simbol == "2"):
        simbol = "~"
    elif (simbol == "9"):
        simbol = "2"
    elif (simbol == "#"):
        simbol = "9"
    elif (simbol == "3"):
        simbol = "#"
    elif (simbol == "."):
        simbol = "3"
    elif (simbol == "+"):
        simbol = "."
    elif (simbol == "("):
        simbol = "+"
    elif (simbol == "-"):
        simbol = "("
    elif (simbol == ")"):
        simbol = "-"
    elif (simbol == "\"):
        simbol = ")"
    elif (simbol == "<"):
        simbol = "\"
    elif (simbol == "/"):
        simbol = "<"
    elif (simbol == "@"):
        simbol = "/" 
    elif (simbol == ">"):
        simbol = "@"
    elif (simbol == ","):
        simbol = ">"
    elif (simbol == "4"):
        simbol = ","
    elif (simbol == ":"):
        simbol = "4"
    elif (simbol == ":"):
        simbol = "7"
    elif (simbol == "7"):
        simbol = "5"
    elif (simbol == "5"):
        simbol = "*"
    elif (simbol == "*"):
        simbol = "!"
    elif (simbol == "!"):
        simbol = "="
    elif (simbol == "="):
        simbol = "8"
    elif (simbol == "8"):
        simbol = "{"
    elif (simbol == "{"):
        simbol = "}"
    elif (simbol == "}"):
        simbol = "?"
    elif (simbol == "?"):
        simbol = "6"
    elif (simbol == "6"):
        simbol = ";"
    elif (simbol == ";"):
        simbol = "["
    elif (simbol == "["):
        simbol = "\""
    elif (simbol == "\""):
        simbol = "0"
    elif (simbol == "0"):
        simbol = "]"
    elif (simbol == "]"):
        simbol = "1"
    
    lista_2 = [simbol]
    simbol = None
    return lista_2


while True:
    data = s.recv(2400000)
    prijem = data.decode()
    kon = Convert(prijem)
    print(kon)
    
    
    
