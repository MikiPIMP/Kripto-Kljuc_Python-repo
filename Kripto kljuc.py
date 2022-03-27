#------------ ADMIN SERVER STRANA ------------#
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostname()
PORT = 34437

s.bind((HOST, PORT))
s.listen(1)

#----------------------------------------------------- def
def Convert(str1):
    lista0 = list(str1.split(" "))
    return lista0

def Enkripter(simbol):
    if (simbol == "a"):
        simbol = "o"
    elif (simbol == "o"):
        simbol = "c"
    elif (simbol == "c"):
        simbol = "m"
    elif (simbol == "m"):
        simbol = "f"
    elif (simbol == "f"):
        simbol = "r"
    elif (simbol == "r"):
        simbol = "p"
    elif (simbol == "p"):
        simbol = "k"
    elif (simbol == "k"):
        simbol = "h"
    elif (simbol == "h"):
        simbol = "d"
    elif (simbol == "d"):
        simbol = "u"
    elif (simbol == "u"):
        simbol = "v"
    elif (simbol == "v"):
        simbol = "b"
    elif (simbol == "b"):
        simbol = "y"
    elif (simbol == "y"):
        simbol = "g"
    elif (simbol == "g"):
        simbol = "x"
    elif (simbol == "x"):
        simbol = "w"
    elif (simbol == "w"):
        simbol = "l"
    elif (simbol == "l"):
        simbol = "z"
    elif (simbol == "z"):
        simbol = "n"
    elif (simbol == "n"):
        simbol = "j"
    elif (simbol == "j"):
        simbol = "s"
    elif (simbol == "s"):
        simbol = "i"
    elif (simbol == "i"):
        simbol = "t"
    elif (simbol == "t"):
        simbol = "q"
    elif (simbol == "q"):
        simbol = "e"
    elif (simbol == "e"):
        simbol = "a"

    if (simbol == "O"):
        simbol = "A"
    elif (simbol == "C"):
        simbol = "O"
    elif (simbol == "M"):
        simbol = "C"
    elif (simbol == "F"):
        simbol = "M"
    elif (simbol == "R"):
        simbol = "F"
    elif (simbol == "P"):
        simbol = "R"
    elif (simbol == "K"):
        simbol = "P"
    elif (simbol == "H"):
        simbol = "K"
    elif (simbol == "D"):
        simbol = "H"
    elif (simbol == "U"):
        simbol = "D"
    elif (simbol == "V"):
        simbol = "U"
    elif (simbol == "B"):
        simbol = "V"
    elif (simbol == "Y"):
        simbol = "B"
    elif (simbol == "G"):
        simbol = "Y"
    elif (simbol == "X"):
        simbol = "G"
    elif (simbol == "W"):
        simbol = "X"
    elif (simbol == "L"):
        simbol = "W"
    elif (simbol == "Z"):
        simbol = "L"
    elif (simbol == "N"):
        simbol = "Z"
    elif (simbol == "J"):
        simbol = "N"
    elif (simbol == "S"):
        simbol = "J"
    elif (simbol == "I"):
        simbol = "S"
    elif (simbol == "T"):
        simbol = "I"
    elif (simbol == "Q"):
        simbol = "T"
    elif (simbol == "E"):
        simbol = "Q"
    elif (simbol == "A"):
        simbol = "E"

    if (simbol == "1"):
        simbol = "~"
    elif (simbol == "~"):
        simbol = "2"
    elif (simbol == "2"):
        simbol = "9"
    elif (simbol == "9"):
        simbol = "#"
    elif (simbol == "#"):
        simbol = "3"
    elif (simbol == "3"):
        simbol = "."
    elif (simbol == "."):
        simbol = "+"
    elif (simbol == "+"):
        simbol = "("
    elif (simbol == "("):
        simbol = "-"
    elif (simbol == "-"):
        simbol = ")"
    elif (simbol == ")"):
        simbol = "\"
    elif (simbol == "\"):
        simbol = "<"
    elif (simbol == "<"):
        simbol = "/"
    elif (simbol == "/"):
        simbol = "@" 
    elif (simbol == "@"):
        simbol = ">"
    elif (simbol == ">"):
        simbol = ","
    elif (simbol == ","):
        simbol = "4"
    elif (simbol == "4"):
        simbol = ":"
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

def LANSER(arg_msg):
    lista_1 = Convert(arg_msg)
    lista_3 = []

    for Str in lista_1:
        for char in Str:
            index = char
            a = Enkripter(index)
            lista_3 += a
        lista_3 += [" "]

    lista_3.pop()
    lista_3.reverse()

    k = " "
    for c in lista_3:
        if c == k:
            lista_3[lista_3.index(c)] = "|"

    LISTA_GOTOVA = ''.join(lista_3)
    
    conn.sendall((LISTA_GOTOVA).encode())


#------------------------------------------------------ def

while True:
    print("Server - aktivan: ")
    conn, addr = s.accept()
    print("Konekcija ostvarena sa: ", addr)
    
    try:
        while True:
            poruka = str(input("> Unesi poruku: "))
            LANSER(poruka)
            print(">> Poruka - Poslata!")
    except:
        print("<|> Doslo je do greske! <|>")
        
    
    

 
