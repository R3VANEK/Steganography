from PIL import Image


def creating(image_current, kanal):
    width, height = image_current.size
    pixels = image_current.load()
    lista_kanal = []
    lista_message = []

    if kanal.find(',') != -1:   #funkcja dzięki której możliwe jest zapisywanie od razu wiadomości na paru kanałach
        lista_kanal = kanal.split(',')
    else:
        lista_kanal.append(kanal)

    for i in range(len(lista_kanal)):
        message = input('Podaj ukrytą wiadomość dla kanału '+lista_kanal[i]+' : ')
        bin_message = ''
        for letter in message:
            help1 = bin(ord(letter))
            if letter != ' ':
                help2 = help1.replace('b','')
            else:
                help2 = help1.replace('b','0')
            bin_message+=help2
        lista_message.append(bin_message)


    for i in range(len(lista_message)):
        

            if lista_kanal[i] == 'r':
                r,g,b = image_current.getpixel((0,0)) #pierwszy pixel sygnalizuje na których kanałach sa wiadomości
                pixels[0,0] = (r-1,g,b)

                row = 0
                signed_letters = 0    #właściwy, niezerujący się iterator
                j = 0
                while signed_letters < len(lista_message[i]):   #pętla zapisu
                    
                    if j == 0 and signed_letters == 0:   #jednokrotne pominęcie specjalnego pixela pierwszego
                        j+=1                          
                        continue
                    else:

                        try:
                            r, g, b = image_current.getpixel((j,row)) 
                        except IndexError:
                            j=0
                            row+=1
                            continue

                        if lista_message[i][signed_letters] == '1':      #jeżeli mamy zapisać zero, to nie musimy robić żadnej różnicy bo x-x to zawsze 0
                            pixels[j,row] = (r-1, g, b)
                            signed_letters+=1
                            j+=1
                        else:
                            j+=1
                            signed_letters+=1
                            continue
                r, g, b = image_current.getpixel((j+1,row)) 
                pixels[j+1,row] = (r-2,g,b)

            elif lista_kanal[i] == 'g':
                r,g,b = image_current.getpixel((0,0)) 
                pixels[0,0] = (r,g-1,b)
                row = 0
                signed_letters = 0   
                j = 0

                while signed_letters < len(lista_message[i]): 
                    if j == 0 and signed_letters == 0:   
                        j+=1                          
                        continue
                    else:

                        try:
                            r, g, b = image_current.getpixel((j,row)) 
                        except IndexError:
                            j=0
                            row+=1
                            continue

                        if lista_message[i][signed_letters] == '1':      #jeżeli mamy zapisać zero, to nie musimy robić żadnej różnicy bo x-x to zawsze 0
                            pixels[j,row] = (r, g-1, b)
                            signed_letters+=1
                            j+=1
                        else:
                            j+=1
                            signed_letters+=1
                            continue
                r, g, b = image_current.getpixel((j+1,row)) 
                pixels[j+1,row] = (r,g-2,b)

            elif lista_kanal[i] == 'b':
                r,g,b = image_current.getpixel((0,0)) 
                pixels[0,0] = (r,g,b-1)

                row = 0
                signed_letters = 0 
                j = 0
                while signed_letters < len(lista_message[i]):
                    
                    if j == 0 and signed_letters == 0:  
                        j+=1                          
                        continue
                    else:

                        try:
                            r, g, b = image_current.getpixel((j,row)) 
                        except IndexError:
                            j=0
                            row+=1
                            continue

                        if lista_message[i][signed_letters] == '1':      #jeżeli mamy zapisać zero, to nie musimy robić żadnej różnicy bo x-x to zawsze 0
                            pixels[j,row] = (r, g, b-1)
                            signed_letters+=1
                            j+=1
                        else:
                            j+=1
                            signed_letters+=1
                            continue
                r, g, b = image_current.getpixel((j+1,row)) 
                pixels[j+1,row] = (r,g,b-2)


    image_current.save('modified.png')