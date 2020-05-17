from decrypt import reading

def showing(image1, image2, kanal):
    decoded_list = ''
    message_received = reading(image1, image2, kanal)


    for i in range(0, len(message_received), 8):
        decoded_list+=chr(int(message_received[i:i+8],2))
    print("Oto zaszyfrowana wiadomość na kanale koloru "+kanal+' pixeli : '+decoded_list)