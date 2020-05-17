from PIL import Image




def reading(original_image, modified_image, kanal):
    image_original = Image.open(original_image)
    pixels_original = image_original.load()

    image_modified = Image.open(modified_image)
    pixels_modified = image_modified.load()

    cont = True
    i = 1
    row = 0
    r,g,b = pixels_original[0,0]
    r1,g1,b1 = pixels_modified[0,0]
    binary_message = ''

    if kanal == 'r':
        if abs(r-r1) == 1:   #sprawdzenie czy rzeczywiście na podanym kanale jest jakaś wiadomość

            while cont:

                try:
                    r_original, g_original, b_original = pixels_original[i,row]
                    r_modified, g_modified, b_modified = pixels_modified[i,row]
                except IndexError:
                    i=0
                    row+=1
                    continue

                if abs(r_original - r_modified) == 1:
                    binary_message+='1'
                elif abs(r_original - r_modified) == 0:
                    binary_message+='0'
                elif abs(r_original - r_modified) == 2:
                    cont = False
                i+=1

            return binary_message
        else:
            print("hm, wygląda na to, że na podanym kanale nie ma zakodowanej żadnej wiadomości")
        
    elif kanal == 'g':
        if abs(g-g1) == 1:
            while cont:

                try:
                    r_original, g_original, b_original = pixels_original[i,row]
                    r_modified, g_modified, b_modified = pixels_modified[i,row]
                except IndexError:
                    i=0
                    row+=1
                    continue

                if abs(g_original - g_modified) == 1:
                    binary_message+='1'
                elif abs(g_original - g_modified) == 0:
                    binary_message+='0'
                elif abs(g_original - g_modified) == 2:
                    cont = False
                i+=1
            return binary_message            
        else:
            print("hm, wygląda na to, że na podanym kanale nie ma zakodowanej żadnej wiadomości")        

    elif kanal == 'b':
        if abs(b-b1) == 1:
            while cont:
                
                try:
                    r_original, g_original, b_original = pixels_original[i,row]
                    r_modified, g_modified, b_modified = pixels_modified[i,row]
                except IndexError:
                    i=0
                    row+=1
                    continue

                if abs(b_original - b_modified) == 1:
                    binary_message+='1'
                elif abs(b_original - b_modified) == 0:
                    binary_message+='0'
                elif abs(b_original - b_modified) == 2:
                    cont = False
                i+=1
            return binary_message            
        else:
            print("hm, wygląda na to, że na podanym kanale nie ma zakodowanej żadnej wiadomości")     