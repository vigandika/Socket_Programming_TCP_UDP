import socket
import sys
import datetime
import random
import re
import math


serverAddress = 'localhost'
port = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


try:
    serverSocket.bind((serverAddress, port))
except socket.error:
    print("Startimi i serverit deshtoi! Binding Failed.")
    sys.exit()


print('Serveri eshte i gatshem te pranoje kekresa...' +"\n")

def IPAddress(address):
    return address[0]

def PortNumber(address):
    return str(address[1])

def Consonants(text):
    consonantNr = 0
    for i in text.upper():
        if (i == 'B' or i == 'C' or i == 'D' or i == 'F' or i == 'G' or i == 'H' or i == 'J' or i == 'K'
            or i=='L' or i=='M' or i=='N' or i=='P' or i=='Q' or i=='R' or i=='S' or i=='T' or i=='V'
                or i == 'W' or i=='X' or i=='Z'):
            consonantNr += 1
    return str(consonantNr)


def Print(text):
    text = text.strip()
    return text


def PCName():
    pcName = socket.gethostname()
    if not pcName:
        return "Emri i hostit nuk mund te gjendet!"
    else:
        return pcName


def getTime():
    now = datetime.datetime.now()
    return "Data dhe koha tani: " + now.strftime("%Y-%m-%d , %H:%M:%S")


def randNumber():
    numbersArray = []
    for i in range(7):
        number = random.randint(1, 49)
        numbersArray.append(number)
    numbers = str(numbersArray)
    numbers = numbers.replace('[', '(').replace(']', ')')
    return numbers


def fibonacci(member):
    try:
        if member.isdigit():
            memberNo = int(member)
            fibSeq = []
            fibSeq.append(0)
            fibSeq.append(1)
            for i in range(2, memberNo):
                fibSeq.append(fibSeq[i-1]+fibSeq[i-2])
            return "Anetari i " + member + " i vargut Fibonacci eshte numri: " + str(fibSeq[memberNo-1])
        else:
            return "Komande jo valide!"
    except MemoryError:
        print("Numri qe ka derguar klienti ka qene shume i madh dhe i paprocesueshem")
        return "Numri qe keni derguar ka qene shume i madh dhe i paprocesueshem"

def convert(urdheri):
    vlera = re.findall(r"[-+]?\d*\.\d+|\d+", urdheri)
    vlera = str(vlera).replace("[", "").replace("]", "").replace("'", "").replace("'", "")
    vlera = float(vlera)                                            # ekstraktimi i numrit nga stringu i marre
    if urdheri[11:31].upper()=='KILOWATTTOHORSEPOWER':
        return str(vlera) + " KiloWatt = " + str(vlera*1.34102) + "HorsePower"
    elif urdheri[11:31].upper()=='HORSEPOWERTOKILOWATT':
        return str(vlera) + " HorsePower = " +str(vlera/1.341) +" KiloWatt"
    elif urdheri[11:27].upper() == 'DEGREESTORADIANS':
        return str(vlera) + " degrees = "+ str(vlera*math.pi/180) + " rad"
    elif urdheri[11:27].upper() == 'RADIANSTODEGREES':
        return str(vlera) +" rad = " + str(vlera*180/math.pi) + " degrees"
    elif urdheri[11:26].upper() == 'GALLONSTOLITERS':
        return str(vlera) + " gallons = " + str(vlera * 3.785) + " Liters"
    elif urdheri[11:26].upper() == 'LITERSTOGALLONS':
        return str(vlera) + " Liters = " + str(vlera / 3.785) + " Gallons"
    else:
        return "Keni dhene formatin gabim!"


def prim(number):
    if number.isdigit():
        number = int(number)
        nrPjest = 0
        for i in range(1, number+1):
            if number % i == 0:
                nrPjest += 1

        if nrPjest==2:
            return "Numri " + str(number) + " eshte numer prim"
        else:
            return "Numri " + str(number) + " nuk eshte numer prim"
    else:
        return "Keni dhene komande jo valide!"


def rockpapersci(human):
    aksioni = ("Rock", "paper", "scissors")
    pc = aksioni[random.randint(0, 2)]

    human = human.lower()
    pc = pc.lower()

    if human == pc:
        return "(You) " + human + " vs " + pc + " (PC)" + "\nDraw"
    elif human == 'paper':
        if pc == 'rock':
            return "(You) " + human + " vs " + pc + " (PC)" + "\nYou win"
        elif pc == 'scissors':
            return "(You) " + human + " vs " + pc + " (PC)" + "\nYou lose"

    elif human == 'scissors':
        if pc == 'rock':
            return "(You) " + human + " vs " + pc + " (PC)" + "\nYou lose"
        elif pc == 'paper':
            return "(You) " + human + " vs " + pc + " (PC)" + "\nYou win"

    elif human == 'rock':
        if pc == 'paper':
            return "(You) " + human + " vs " + pc + " (PC)" + "\nYou lose"
        if pc == 'scissors':
            return "(You) " + human + " vs " + pc + " (PC)" + "\nYou win"
    else:
        return "Keni dhene komande jo valide!"


while True:
    methodByte, client_address = serverSocket.recvfrom(128)
    method = methodByte.decode("utf-8")
    print("Serveri u lidh me klientin " + client_address[0] + " me port "+ str(client_address[1]) +"\n")
    try:
        if not method:
            break
        if method.upper() == 'IPADRESA':
            answer = "IP adresa e Klientit eshte: " + IPAddress(client_address)
        elif method.upper() == 'NUMRIIPORTIT':
            answer = "Klienti eshte duke perdorur portin " + PortNumber(client_address)
        elif method[0:16].upper() == 'BASHKETINGELLORE':
            answer = "Teksti i shkenuar ka " + Consonants(method[16:]) + " bashketingellore"
        elif method[0:8].upper() == 'PRINTIMI':
            answer = "Teksti i printuar: " + Print(method[8:])
        elif method.upper() == 'EMRIIKOMPJUTERIT':
            answer = "Emri i hostit: " + PCName()
        elif method.upper() == 'KOHA':
            answer = getTime()
        elif method.upper() == 'LOJA':
            answer = randNumber()
        elif method[0:9].upper() == 'FIBONACCI':
            answer = fibonacci(method[10:])
        elif method[0:10].upper() == 'KONVERTIMI':
            answer = convert(method)
        elif method[0:4].upper() == 'PRIM':
            answer = prim(method[5:])
        elif method[0:17].upper() == 'ROCKPAPERSCISSORS':
            answer = rockpapersci(method[18:])
        else:
            answer = "Keni dhene nje komande jo valide!"
            print("Klienti ka dhene komande jo valide!")
        serverSocket.sendto(str.encode(answer), client_address)
        print("Klientit " + client_address[0] + " iu dergua pergjigja: " + str(answer) + "\n")
    except ConnectionResetError:
        print("Serveri u shkeput me klient!")
    except ConnectionAbortedError:
        print("Serveri u shkeput me klient!")