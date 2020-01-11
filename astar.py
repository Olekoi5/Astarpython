#tworzymy mapę, ustalamy punkty A i B między którymi szukami drogi
M = [['A', ' ', '#', '#', ' ', '#', ' ', ' '],
     [' ', ' ', ' ', ' ', '#', ' ', '#', ' '],
     ['#', ' ', '#', ' ', ' ', ' ', '#', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B'],
     [' ', ' ', '#', ' ', ' ', ' ', '#', ' '],
     [' ', '#', ' ', ' ', ' ', ' ', '#', ' '],
     ['#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
     [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ']];
#funkcja zwracająca współrzędne punktu początkowego A
def Start(mapa):
    wS = [];
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == 'A':
                wS = [i, j];
                break;
    return wS;
#funkcja zwracająca współrzędne punktu końcowego B
def Koniec(mapa):
    wK = [];
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == 'B':
                wK = [i, j];
                break;
    return wK;
#inicjalizujemy listy zamkniętą i otwartą, wyliczamy współrzędne punktów A i B
#Dodajemy współrzędne punktu A, jako pierwszy element listy zamkniętej
wK = Koniec(M);
wS = Start(M);
K = [wK[0], wK[1], 0, 0, None, None]
S = [wS[0], wS[1], 0, 0, None, None]
listaOtwarta = [];
listaZamknieta = [];
listaZamknieta.append([wS[0], wS[1], 0, 0, None, None]);
Q = listaZamknieta[0];
minimalny = 0;
maxymalny = len(M);
#funkcja sprawdzająca czy podany punkt znajduje się już w liście zamkniętej
#jeśli nie, pomijamy go w dodawaniu do listy otwartej
def sprCzyoZ(px, py):
    for i in range(len(listaZamknieta)):
        if px == listaZamknieta[i][0] and py == listaZamknieta[i][1]:
            return False;
    return True;
#Funkcja obliczająca heurerystykę dla podanego punktu
def h(xp, yp):
    return (((xp - S[0])**2 + (yp - K[1])**2)**(1/2));
#funkcja tworząca punkt jako tablicę zawierąjącą:
#-współrzędne punktu na mapie x i y,
#-koszt przybycia do tego punktu z punktu startowego(drogaP),
#-całkowity koszt dotarcia do punktu końcowego(drogaF),
#-współrzędne punktu rodzica x i y
def KreatorPkt(xp, yp, prodzic):
    drogaP = prodzic[2] + 1;
    drogaF = drogaP + h(xp, yp);
    Pkt = [xp, yp, drogaP, drogaF, prodzic[0], prodzic[1]];
    return Pkt;
#funkcja sprawdzająca czy podany punkt znajduje się już w liście otwartej
def sprCzyOL(p):
    for i in range(len(listaOtwarta)):
        if p[0] == listaOtwarta[i][0] and p[1] == listaOtwarta[i][1]:
            if p[3] < listaOtwarta[i][3]:
                listaOtwarta[i] = p;
                return False;
            return False;
    return True;
#funkcja dodająca punkt do listy otwartej
def dodajOL(p):
    if(sprCzyOL(p)):
        listaOtwarta.append(p);
#funkcja przenosząca punkt o najniższym koszcie całkowitym z listy otwartej do listy zamkniętej
def dodajoZ():
    l = len(listaOtwarta);
    if l > 1:
        najmniejszy = listaOtwarta[0];
        for i in range(l):
            if listaOtwarta[i][3] < najmniejszy[3]:
                najmniejszy = listaOtwarta[i];
        listaZamknieta.append(najmniejszy);
        listaOtwarta.remove(najmniejszy);
    if l == 1:
        listaZamknieta.append(listaOtwarta[0]);
        listaOtwarta.pop(0);
#Szukamy punktów, które dodajemy do listy otwartej,
#a z niej przenosimy do listy zamkniętej
Teraz = Q;
w = True;
while(w == True):
    #punkt z góry
    gorny = Teraz[0] - 1;
    if gorny >= minimalny:
        if M[gorny][Teraz[1]] != '#':
            if (sprCzyoZ(gorny, Teraz[1])):
                pg = KreatorPkt(gorny, Teraz[1], Teraz);
                dodajOL(pg);
    #punkt z dołu
    dolny = Teraz[0] + 1;
    if dolny < maxymalny:
        if M[dolny][Teraz[0]] != '#':
            if (sprCzyoZ(dolny, Teraz[1])):
                pd = KreatorPkt(dolny, Teraz[1], Teraz);
                dodajOL(pd);
    #punkt z prawej
    prawy = Teraz[1] + 1;
    if prawy < maxymalny:
        if M[Teraz[0]][prawy] != '#':
            if (sprCzyoZ(Teraz[0], prawy)):
                pprawy = KreatorPkt(Teraz[0], prawy, Teraz);
                dodajOL(pprawy);
    #punkt z lewej
    lewy = Teraz[1] - 1;
    if lewy >= minimalny:
        if M[Teraz[0]][lewy] != '#':
            if (sprCzyoZ(Teraz[0], lewy)):
                plewy = KreatorPkt(Teraz[0], lewy, Teraz);
                dodajOL(plewy);
    dodajoZ();
    Teraz = listaZamknieta[-1];
    if(Teraz[0] == K[0] and Teraz[1] == K[1]):
        w = False
        # inicjalizujemy tablicę, która zapisuje współrzędne punktów i ich rodziców z listy zamkniętej
        punkty = []

        for t in listaZamknieta:
            t = t[:2] + t[4:]
            punkty.append(t)

        punkty.reverse()

        Droga = []
        Droga.append(punkty[0])

        # Szukamy drogi
        i = 0
        wr = True
        while (i < len(punkty) and wr == True):
            j = i + 1
            while (j < len(punkty)):
                if Droga[i][2] == punkty[j][0] and Droga[i][3] == punkty[j][1]:
                    Droga.append(punkty[j])
                    # print(sciezka)
                    break
                j += 1
            if Droga[-1][2] == None and Droga[-1][3] == None:
                wr = False
            i += 1

        Droga.reverse()
        #Zaznaczamy punkty wchodzę w sklad ścieżki na mapie
        for i in Droga:
            M[i[0]][i[1]] = '+';
        #Zaznaczamy drogę na mapie
        for i in range(len(M)):
            for j in range(len(M[i])):
                print(M[i][j], end='')
            print()
    #Jeśli lista otwarta jest pusta, Wyświetlamy komunikat "Nie ma drogi!"
    if not listaOtwarta:
        print("Nie ma drogi!")
        break;
