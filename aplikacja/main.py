import csv
import statistics

import scipy
from scipy.stats import skew, pearsonr, stats
from Tank import Tank
from turtle import *
tracer(0, 0)
bgpic("pantera_tygrys2.png")
hideturtle()
wn = Screen()
wn.addshape('chiny.gif')
wn.addshape('brazil.gif')
wn.addshape('croatia.gif')
wn.addshape('india.gif')
wn.addshape('france.gif')
wn.addshape('rfn.gif')
wn.addshape('zsrr.gif')
screensize(canvwidth=1800, canvheight=1000)
setup(1280, 720)

def flag(flaga, x, y):
    myflag = Turtle()
    myflag.speed(0)
    if(flaga=="Brazil"):
        myflag.shape('brazil.gif')
    elif(flaga=="West Germany"):
        myflag.shape('rfn.gif')
    elif (flaga == "China"):
        myflag.shape('chiny.gif')
    elif (flaga == "Croatia"):
        myflag.shape('croatia.gif')
    elif (flaga == "Soviet Union"):
        myflag.shape('zsrr.gif')
    elif (flaga == "France"):
        myflag.shape('france.gif')
    elif (flaga == "India"):
        myflag.shape('india.gif')
    myflag.penup()
    myflag.goto(x-20, y)
    update()

def leg(wypelnienie):
    fillcolor(wypelnienie)
    pensize(2)
    pencolor("black")
    begin_fill()
    pensize(1)
    for i in range(4):
        forward(15)
        right(90)
    end_fill()


def gasiennice(r):
    begin_fill()
    for loop in range(2):
        forward(r)
        circle(-10,180)
    end_fill()

def lufa(kaliber):
    kaliber = kaliber - 60
    pensize(3)

    for i in range(2):
        begin_fill()
        forward(kaliber*1.6)
        right(90)
        forward((kaliber+5)/4.5)
        right(90)
        end_fill()
    pensize(6)


def rysowanieBaku(kolorbaku):

    x = xcor()
    y = ycor()
    penup()
    right(90)
    forward(48)
    right(90)
    forward(28)
    right(180)
    pendown()
    pencolor("#6f6f6f")
    pensize(3)
    fillcolor(kolorbaku)
    begin_fill()
    for i in range(2):
        forward(25)
        left(90)
        forward(30)
        left(90)
    end_fill()
    pensize(6)

    penup()
    setx(x)
    sety(y)
    pendown()





def czolg(dlugosc, szerokosc, nazwa, tankcolor, kaliber, kolorgasiennic, tankfill, country, zasieg, kolorbaku):
    pencolor("black")
    write(nazwa, font=('Arial', 10, 'normal'))
    pencolor(tankcolor)
    #showturtle()
    #rysowanie wieży
    for i in range(2):
        begin_fill()
        forward(dlugosc/1.6)
        right(90)
        forward(szerokosc/1.8)
        right(90)
        end_fill()
    #rysowanie lufy
    penup()
    forward(dlugosc/1.6)
    right(90)
    forward(szerokosc/1.8/3)
    left(90)
    pendown()

    lufa(kaliber)
    penup()
    left(90)
    forward(szerokosc / 1.8 / 4)
    left(90)
    forward(dlugosc/1.6)
    left(180)

    penup()
    forward(-dlugosc/1.6/4)
    right(90)
    forward(szerokosc / 1.8)
    left(90)
    pendown()
    #rysowanie podwozia
    for i in range(2):
        begin_fill()
        forward(dlugosc)
        right(90)
        forward(szerokosc)
        right(90)
        end_fill()
    #rysowanie gasiennic
    penup()
    right(90)
    forward(szerokosc-12)
    left(90)
    pendown()
    fillcolor(kolorgasiennic)
    gasiennice(dlugosc)
    fillcolor(tankFill)
    penup()
    left(90)
    forward(szerokosc-12)
    right(90)



    penup()
    left(90)
    forward(szerokosc/1.8)
    right(90)
    pendown()

    #rysowanie baku

    rysowanieBaku(kolorbaku)



    # rysowanie flagi
    penup()

    pendown()
    flag(country, xcor(), ycor()+5)



with open('tanks.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    tanks = []
    for row in csv_reader:
        if(line_count>0):
            tanks.append(Tank(row[0], row[3], row[4], row[23], row[11], row[22], row[1]))
        line_count+=1
    #print(f'Processed {line_count} lines.')
    #tanks[17].print_info()
    bgcolor("#ebebeb")
    pensize(6)
    speed(0)
    penup()
    goto(-230, 280)
    pendown()


    tanks.sort(key=lambda x:x.country)



#legenda
    penup()
    right(180)
    forward(200)
    pendown()
    right(180)
    pencolor("black")
    write("Legenda", font=('Arial', 14, 'normal'))
    right(90)
    penup()
    forward(20)
    right(90)
    forward(160)
    left(180)
    pendown()
    write("Kolor gąsiennic - max prędkość 80km/h, 55km/h", font=('Arial', 11, 'normal'))
    pozycjax = xcor()
    pozycjay = ycor()
    penup()
    forward(220)
    right(90)
    forward(5)
    left(90)
    pendown()
    wypelnienie = (1.0, 0.0, 0.0)
    leg(wypelnienie)
    penup()
    forward(60)
    pendown()
    wypelnienie = (1.0,1.0,1.0)
    leg(wypelnienie)
    penup()
    pozycjay -= 45
    goto(pozycjax, pozycjay)
    pendown()
    pencolor("black")
    write("Kolor wypełnienia - rok produkcji 2014,   1956", font=('Arial', 11, 'normal'))
    penup()
    forward(220)
    right(90)
    forward(5)
    left(90)
    pendown()
    wypelnienie = (0.0, 0.0, 1.0)
    leg(wypelnienie)
    penup()
    forward(50)
    pendown()
    wypelnienie = (0.0, 1.0, 0.0)
    leg(wypelnienie)
    penup()
    pozycjay -= 40
    goto(pozycjax, pozycjay)
    pendown()

    pencolor("black")
    write("Kolor krawędzi - masa pojazdu  30ton,   70ton", font=('Arial', 11, 'normal'))
    penup()
    forward(220)
    right(90)
    forward(5)
    left(90)
    pendown()
    wypelnienie = (0.0, 1.0, 0.0)
    leg(wypelnienie)
    penup()
    forward(50)
    pendown()
    wypelnienie = (1.0, 0.0, 0.0)
    leg(wypelnienie)
    penup()
    pozycjay -= 40
    goto(pozycjax, pozycjay)
    pendown()

    pencolor("black")
    write("Kolor baku - zasięg pojazdu  400km,   700km", font=('Arial', 11, 'normal'))
    penup()
    forward(200)
    right(90)
    forward(5)
    left(90)
    pendown()
    wypelnienie = (1.0, 1.0, 1.0)
    leg(wypelnienie)
    penup()
    forward(60)
    pendown()
    wypelnienie = (1.0, 0.0, 0.0)
    leg(wypelnienie)
    penup()
    pozycjay -= 40
    goto(pozycjax, pozycjay)
    pendown()




    pencolor("black")
    write("Długość lufy - kaliber armaty(90mm - 125mm)", font=('Arial', 11, 'normal'))






#Rysowanie czolgow
    penup()
    goto(-200, 280)
    pendown()
    pensize(6)
    rzad = 0
   # print(tanks[0])
    for tank in tanks:
        #30 ton - zielony, 70 ton - czerwony
        waga = float(tank.weight)-28
        waga = waga/40
        #print("kolor czołgu " + tank.name + " " + str(waga))
        tankColor = (0.0+waga, 1.0-waga, 0.0)
        pencolor(tankColor)

        #2014 - niebieski, 1956 - zielony
        rok = float(tank.year)-1955
        rok = rok/59
        tankFill = (0.0, 1.0-rok, 0.0 + rok)
        fillcolor(tankFill)

        #szybkosc. 80 czerwony, 57,25 bialy
        szybkosc = float(tank.speed)-55
        szybkosc = szybkosc/25
        kolorGasiennic = (1.0, 1.0-szybkosc, 1.0-szybkosc)
        dlugosc = 80
        szerokosc = 40

        # zasieg. 400 - minimalny zasieg, 700 - maksymalny
        bak = (float(tank.range) - 400) / (700 - 400)

        kolorbaku = (1.0, 1.0-bak, 1.0-bak)

        czolg(80, 40, tank.name, tankColor, float(tank.caliber), kolorGasiennic, tankFill, tank.country, int(tank.range), kolorbaku)



        if(rzad!=2):
            penup()
            forward(240)
            pendown()
        else:
            penup()
            right(90)
            forward(100)
            right(90)
            forward(440)
            left(180)
            pendown()
        rzad = (rzad+1)%3

    exitonclick()

    #liczenie

    lista_mas = []
    lista_kalibru = []
    lista_zasiegu = []
    lista_roku = []
    lista_predkosci = []
    i = 0
    for tank in tanks:
        i+=1
        lista_mas.append(float(tank.weight))
        lista_roku.append(float(tank.year))
        lista_kalibru.append(float(tank.caliber))
        lista_zasiegu.append(float(tank.range))
        lista_predkosci.append(float(tank.speed))


    #for j in range (i):
        #print("masa: "  + lista_mas[j])
    odch_masy = statistics.stdev(lista_mas)
    odch_roku = statistics.stdev(lista_roku)
    odch_kalibru = statistics.stdev(lista_kalibru)
    odch_zasiegu = statistics.stdev(lista_zasiegu)
    odch_predkosci = statistics.stdev(lista_predkosci)

    sr_masy = (sum(lista_mas)/len(lista_mas))
    sr_roku = (sum(lista_roku)/len(lista_roku))
    sr_kalibru = (sum(lista_kalibru)/len(lista_kalibru))
    sr_zasiegu = (sum(lista_zasiegu)/len(lista_zasiegu))
    sr_predkosci = (sum(lista_predkosci)/len(lista_predkosci))

    skosnosc_mas = skew(lista_mas)
    skosnosc_kalibru = skew(lista_kalibru)
    skosnosc_zasiegu = skew(lista_zasiegu)
    skosnosc_roku = skew(lista_roku)
    skosnosc_predkosci = skew(lista_predkosci)

    kurtoza_mas = scipy.stats.kurtosis(lista_mas)
    kurtoza_kalibru = scipy.stats.kurtosis(lista_kalibru)
    kurtoza_zasiegu = scipy.stats.kurtosis(lista_zasiegu)
    kurtoza_roku = scipy.stats.kurtosis(lista_roku)
    kurtoza_predkosci = scipy.stats.kurtosis(lista_predkosci)



    korelacja_masa_kaliber, p_value = stats.pearsonr(lista_mas,lista_kalibru)
    korelacja_masa_zasieg, p_value = stats.pearsonr(lista_mas,lista_zasiegu)
    korelacja_masa_rok, p_value = stats.pearsonr(lista_mas,lista_roku)
    korelacja_masa_predkosc, p_value = stats.pearsonr(lista_mas,lista_predkosci)
    korelacja_kaliber_zasieg, p_value = stats.pearsonr(lista_kalibru,lista_zasiegu)
    korelacja_kaliber_rok, p_value = stats.pearsonr(lista_kalibru,lista_roku)
    korelacja_kaliber_predkosc, p_value = stats.pearsonr(lista_kalibru,lista_predkosci)
    korelacja_zasieg_rok, p_value = stats.pearsonr(lista_zasiegu,lista_roku)
    korelacja_zasieg_predkosc, p_value = stats.pearsonr(lista_zasiegu,lista_predkosci)
    korelacja_rok_predkosc, p_value = stats.pearsonr(lista_roku,lista_predkosci)

    print("Dane mas pojazdów:")
    print("odchylenie standardowe: " + str(odch_masy) + " ton")
    print("średnia: " + str(sr_masy) + " ton")
    print("skośność: " + str(skosnosc_mas))
    print("kurtoza: " + str(kurtoza_mas))
    print(" ")


    print("Dane kalibrów pojazdów:")
    print("odchylenie standardowe: " + str(odch_kalibru) + " mm")
    print("średnia: " + str(sr_kalibru) + " mm")
    print("skośność: " + str(skosnosc_kalibru))
    print("kurtoza: " + str(kurtoza_kalibru))
    print(" ")

    print("Dane zasięgu pojazdów:")
    print("odchylenie standardowe: " + str(odch_zasiegu) + " km")
    print("średnia: " + str(sr_zasiegu) + " km")
    print("skośność: " + str(skosnosc_zasiegu))
    print("kurtoza: " + str(kurtoza_zasiegu))
    print(" ")

    print("Dane prędkości pojazdów:")
    print("odchylenie standardowe: " + str(odch_predkosci) + "km/h")
    print("średnia: " + str(sr_predkosci) + "km/h")
    print("skośność: " + str(skosnosc_predkosci))
    print("kurtoza: " + str(kurtoza_predkosci))
    print(" ")

    print("Dane roku produkcji pojazdów:")
    print("odchylenie standardowe: " + str(odch_roku) + "")
    print("średnia: " + str(sr_roku) + "")
    print("skośność: " + str(skosnosc_roku))
    print("kurtoza: " + str(kurtoza_roku))
    print(" ")

    print("Korelacje:")
    print("Korelacja masy do kalibru: " + str(korelacja_masa_kaliber))
    print("Korelacja masy do roku produkcji: " + str(korelacja_masa_rok))
    print("Korelacja masy do zasięgu: " + str(korelacja_masa_zasieg))
    print("Korelacja masy do prędkości: " + str(korelacja_masa_predkosc))

    print("Korelacja kalibru do roku produkcji: " + str(korelacja_kaliber_rok))
    print("Korelacja kalibru do prędkości: " + str(korelacja_kaliber_predkosc))
    print("Korelacja kalibru do zasięgu: " + str(korelacja_kaliber_zasieg))

    print("Korelacja zasięgu do roku produkcji: " + str(korelacja_zasieg_rok))
    print("Korelacja zasięgu do prędkości: " + str(korelacja_zasieg_predkosc))

    print("Korelacja roku produkcji do prędkości: "  + str(korelacja_rok_predkosc))