from PIL import Image
from encrypt import creating
from show_decoded import showing
import os



"""
    Dzień dobry, witam w moim programie do steganografii. Na tą chwilę, program oferuje dwie możliwości : zapis wiadomości
    i jej odczyt. Jak to działa? W klasycznych przykładach tego typu szyfrowania modyfikuje się ostatnie bity kolorów
    pikseli, ja jednak chciałem pójść trochę innym tropem. Zamiast tego tutaj operuje się kolorem poszczególnych pikseli
    w formacie RGB np. (255,187,61). Można wybrać, który kanał ma kodować jaką wiadomość, więc równolegle można zapisać
    do trzech wiadomości na pojedyńczym obrazku bez widocznych dla oka różnic. Algorytm jest prosty. Tekst podany przez 
    użytkownika jest przekonwertowywany na format binarny ASCII. Następnie program przechodzi po 0 i 1. Jeżeli natrafi
    na 1 to na nowym obrazku obcina wartość koloru o 1 np. z oryginalnego (255,255,255) zostaje (254,255,255) na kanale r.
    Jeżeli natomiast chcemy zaszyfrować 0 to nie robimy żadnej zmiany. Żeby zasygnalizowac koniec wiadomości, zamiast odejmować jeden,
    odejmujemy 2 od koloru. 


    Uwagi do działania:

    - może być problem z otwarciem pliku z innego folderu niż tego, w którym jest main.py, poprawne sprawdzanie ścieżek
      systemowych podanych pzez użytkownika to dla mnie zawiła sprawa w Pythonie
    
    - obecnie można prawidłowo zakodować tylko małe litery, bez polskich znaków i spację (a,b,c,d,e,f,g,h,i,j,k,l .... i spacja )
      Żeby to poprawić muszę kiedyś się przysiąść i napisać lepszy konwerter binarny w show_decoded.py :) 

    - wybierając opcję 2, nie musimy wiedzieć, które zdjęcie jest oryginałem, kolejność podawania nie ma tam znaczenia

    - wybierając opcję 1 można podać więcej niż jeden kanał na raz. Trzeba wtedy napisać np. r,g . Program zapyta się 
      o tekst dla jedengo i drugiego kanału

    - nie mam pojęcia co się stanie przy spotkaniu obrazka z kanałem Alfa, mogę tylko zgadywać :)

    - podczas pisania natrafiłem na możliwy błąd, który może uniemożliwić zapis wiadomości. Stanie się tak, gdy podamy tekst
      który będzie miał długość po przekonwertowaniu binarnym większą niż liczbę piskeli w zdjęciu. Nie naprawiłem tego, bo 
      operując na obrazku 2628x1774 pikseli taka sytuacja zdażyłaby się przy tekście długości 582 757 znaków, co jest tak 
      abstrakcyjną wartością, że taki teoretyczny błąd potraktowałem tylko jako ciekawostkę. Można też to czytać jako 
      maksymalny limit kodowanych znaków na danym kanale. Używajmy po prostu wysokiej rozdzielczości zdjęć :)
       dokładny wzór błędu : długość_wiadomości * 8 - 2 > szerokość * wysokość (zdjęcia w piskelach) 

"""





cont1 = True
while cont1:
    os.system('cls')
    print('----------------------------------------------------------------------------------------------------')
    print("Witaj podróżniku w narzędziu szyfrującym wiadomości metodą steganografii, co chcesz zrobić?")
    print()
    print("1. Zakoduj nową informację na obrazie")
    print("2. Odczytaj zakodowaną informację z obrazu")
    print()
    decision = input("")

    if decision == '1':
        os.system('cls')
        image = input("Podaj ścieżkę do obrazu na którym chcesz coś zaszyfrować : ")
        try:
            newImage = Image.open(image)
        except IOError:
            print("Nie udało się otworzyć pliku o podanej ścieżce")
            break
        
        kanal = input("Na którym kanale chcesz zaszyfrowac twoją wiadomość? <r,g,b>: ")    
        
        creating(newImage, kanal) #kanal na listę i wtedy po drobnych zmianach można zapisywac więcej niż jeden kanał na raz

        print('\n')
        d = input(" Kontynuować? <Y/N> : ")
        if d != "Y":
            cont1 = False

    elif decision == '2':
        os.system('cls')
        image1 = input("Podaj ścieżkę do pierwszego obrazka : ")
        image2 = input("Podaj ścieżkę do zmdodyfikowanego obrazka : ")
        kanal = input("Z jakiego kanału koloru pixela chcesz odczytać wiadomość ? <r,g,b> : ")
        showing(image1, image2, kanal)

        print('\n')
        d = input(" Kontynuować? <Y/N> : ")
        if d != "Y":
            cont1 = False

    else:
        print("podano niewłaściwą opcję")
        print('\n')
        d = input(" Kontynuować? <Y/N> : ")
        if d != "Y":
            cont1 = False



#showing('test.png', 'modified.png', 'r')


#print(abs(96-96)%2) #sposób liczenia


#creating(newImage, kanal, bin_message)





