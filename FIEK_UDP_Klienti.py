import socket

serverAddress = 'localhost'
serverPort = 12000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:

    print("  ------------------------------------------------------------------------------" +
                   "\n | Zgjedhni njeren prej metodave:                                               |" +
                   "\n | IPADRESA                                                                     |"+
                   "\n | NUMRIIPORTIT                                                                 |" +
                   "\n | BASHKETINGELLORE {Hapsire} teksti                                            |" +
                   "\n | PRINTIMI {Hapsire} teksti                                                    |" +
                   "\n | EMRIIKOMPJUTERIT                                                             |" +
                   "\n | KOHA                                                                         |" +
                   "\n | LOJA                                                                         |" +
                   "\n | FIBONACCI {Hapsire} numer                                                    |" +
                   "\n | ROCKPAPERSCISSORS {Hapsire} aksioni                                          |" +
                   "\n | PRIM {Hapsire} numer                                                         |" +
                   "\n | KONVERTIMI {Hapsire} OPSIONI {Hapsire} numer                                 |" +
                   "\n |    *OPSIONI: HorsepowerToKilowatt, KilowattToHorsepower, DegreesToRadians,   |" +
                   "\n |               RadiansToDegrees, GallonsToLiters, LitersToGallons             |" +
                   "\n  ------------------------------------------------------------------------------" +
                   "\n | KUJDES! Komanden jepeni sipas udhezimit, pa gabime dhe me shkronja te medha! |" +
                   "\n  ------------------------------------------------------------------------------ \n")
    procesi = True
    while procesi:
        method = input()
        if method.upper() == 'E':
            print("Keni vendosur te shkeputni lidhjen me server. Kaloni nje dite te kendshme!")
            procesi = False
        elif method == '':
            print("Komande jo valide. Vazhdo me kerkese tjeter.")
        else:
            clientSocket.sendto(str.encode(method), (serverAddress, serverPort))
            serverAnswerByte = clientSocket.recvfrom(128)
            serverAnswer = serverAnswerByte[0].decode("utf-8")
            print(serverAnswer)
            print("Vazhdoni me kerkese tjeter ose shtyp E per dalje.")

except TimeoutError:
    print("Serveri morri shume kohe per tu pergjigjur andaj lidhja u mbyll!")
