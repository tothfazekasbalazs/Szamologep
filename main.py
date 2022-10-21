import time
import colorama
from colorama import Fore, Back, Style
from colorama import init

init()

def main():

    #Kilepés fügvény

    def kilepes():
        print("\nA rendszer 3 másotperc múlva bezárja magát")
        time.sleep(3)
        exit()

    #Kilepés fügvény vége
    #Karakterek convertálása inté ha nem teljesül be akkor a program bezárja magát (1)

    def converting_input_1():

        try:
            global input_1
            input_1 = int(input_1)

        except:
            print(f"\n{Fore.RED}Ezzel az adattal nem lehet számolni!!{Style.RESET_ALL}")
            repait()

    def converting_input_2():

        try:
            global input_2
            input_2 = int(input_2)

        except:
            print(f"\n{Fore.RED}Ezzel az adattal nem lehet számolni!!{Style.RESET_ALL}")
            repait()

    #Karakterek convertálása inté ha nem teljesül be akkor a program bezárja magát vége
    #Összeadás

    def addition():
        global input_1
        input_1 = input("\nMennyit szeretnél összeadni: ")
        converting_input_1()
        global input_2
        input_2 = input("\nMenyit szertnél hozzáadni: ")
        converting_input_2()
        eredmeny = input_1 + input_2  
        print(f"{Fore.GREEN}\n Az szamolás eredménye: {eredmeny}{Style.RESET_ALL}") 

    #Összeadás vége
    #Kivonás

    def subtraction():
        global input_1
        input_1 = input("\nMennnyiből szeretnél kivonni: ")
        converting_input_1()
        global input_2
        input_2 = input("\nMennyit?: ")
        converting_input_2()
        eredmeny = input_1 - input_2  
        print(f"\n{Fore.GREEN} Az szamolás eredménye: {eredmeny}{Style.RESET_ALL}")

    #Kivonás vége
    #Szorzás

    def multiplication():
        global input_1
        input_1 = input("\nMennyit szeretnél összeszorozni: ")
        converting_input_1()
        global input_2
        input_2 = input("\nMenyivel: ")
        converting_input_2()
        eredmeny = input_1 * input_2  
        print(f"\n{Fore.GREEN} Az szamolás eredménye: {eredmeny}{Style.RESET_ALL}")

    #Szorzás vége
    #Osztás

    def division():
        global input_1
        input_1 = input("\nMennyit szeretnél osztani: ")
        converting_input_1()
        global input_2
        input_2 = input("\nMenyivel: ")
        converting_input_2()
        eredmeny = input_1 / input_2  
        print(f"\n{Fore.GREEN} Az szamolás eredménye: {eredmeny}{Style.RESET_ALL}")

    #Osztás vége
    #Hatványozás
    
    def exponentiation():
        global input_1
        input_1 = input("\nMennyit szeretnél négyzetre emelni: ")
        converting_input_1()
        eredmeny = input_1 ** input_1  
        print(f"\n{Fore.GREEN} Az szamolás eredménye: {eredmeny}{Style.RESET_ALL}")

    #Hatványozás vége
    #Gyökvonás

    def root_subtraction():
        global input_1
        input_1 = input("\nMennyit szeretnél a négyzetgyökét: ")
        converting_input_1()
        eredmeny = input_1 ** 0.5  
        print(f"\n{Fore.GREEN} Az szamolás eredménye: {eredmeny}{Style.RESET_ALL}")

    #Gyökvonás vége
    #Kerület

    def district():       
        input_ker_1 = input("\nMilyen alakzatnak szeretnéd a kerületét: (kör, négyzet, téglalap, háromszög) ")

        if input_ker_1 == "1":
            print("alma")

        elif input_ker_1 == "2" or input_1 == "négyzet" or input_1 == "negyzet":
            negyzet_ker()

        elif input_ker_1 == "3" or input_ker_1 == "teglalap" or input_ker_1 == "téglalap":
            teglalap_ker()

        elif input_ker_1 == "4" or input_ker_1 == "haromszog" or input_ker_1 == "háromszög":
            haromszog_ker()

        else:
            print(f"\n Ilyen érték nincs megadva")
            district()


    #Kör kerülete ke
    #Négyzet kerülete területe

    def negyzet_ker():

        def inputs_ker_negyzet():
            global in_kerulet_negyzet_1
            in_kerulet_negyzet_1 = input("\nAdd meg a négyzet oldalát: ")
            converting_input_negyzet_1()

        def converting_input_negyzet_1():

            try:
                global in_kerulet_negyzet_1
                in_kerulet_negyzet_1 = int(in_kerulet_negyzet_1)
                negyzetcallc()

            except:
                print(f"\n{Fore.RED}Ezzel az adattal nem lehet számolni!!{Style.RESET_ALL}")
                inputs_ker_negyzet()

        def negyzetcallc():
            kerülete_negyzet = 4 * in_kerulet_negyzet_1
            területe_negyzet = in_kerulet_negyzet_1 * in_kerulet_negyzet_1
            print(f"{Fore.GREEN}\nA kerület: {kerülete_negyzet}{Style.RESET_ALL}")
            print(f"\n{Fore.GREEN}A terület: {területe_negyzet}{Style.RESET_ALL}")

        inputs_ker_negyzet()

    #Négyzet kerülete területe vége
    #Téglalap kerülete területe

    def teglalap_ker():

        def inputs_ker_teglalap():
            global in_kerulet_teglalap_1
            in_kerulet_teglalap_1 = input("\nAdd meg az eggyik oldalt: ")
            converting_input_teglalap_1()
            global in_kerulet_teglalap_2
            in_kerulet_teglalap_2 = input("\nAdd meg az másis oldalt: ")
            converting_input_teglalap_2()

        def converting_input_teglalap_1():

            try:
                global in_kerulet_teglalap_1
                in_kerulet_teglalap_1 = int(in_kerulet_teglalap_1)

            except:
                print(f"\n{Fore.RED}Ezzel az adattal nem lehet számolni!!{Style.RESET_ALL}")
                inputs_ker_teglalap()

        def converting_input_teglalap_2():

            try:
                global in_kerulet_teglalap_2
                in_kerulet_teglalap_2 = int(in_kerulet_teglalap_2)
                teglalapcallc()

            except:
                print(f"\n{Fore.RED}Ezzel az adattal nem lehet számolni!!{Style.RESET_ALL}")
                inputs_ker_teglalap()

        def teglalapcallc():
            kerülete_teglalap = in_kerulet_teglalap_1 + in_kerulet_teglalap_2
            területe_teglalap = in_kerulet_teglalap_1 * in_kerulet_teglalap_2
            print(f"{Fore.GREEN}\nA kerület: {kerülete_teglalap}{Style.RESET_ALL}")
            print(f"\n{Fore.GREEN}A terület: {területe_teglalap}{Style.RESET_ALL}") 
            repait()


        inputs_ker_teglalap()

    #Téglalap kerülete területe vége
    #Haromszög kerülete területe

    def haromszog_ker():

        def inputs_ker_haromszog():  
            global in_kerulet_haromszog_1
            in_kerulet_haromszog_1 = input("Add meg az első adatot: ")
            converting_input_ker_1()
            global in_kerulet_haromszog_2
            in_kerulet_haromszog_2 = input("Add meg az másidak adatot: ")
            converting_input_ker_2()
            global in_kerulet_haromszog_3
            in_kerulet_haromszog_3 = input("Add meg az harmadik adatot: ")
            converting_input_ker_3()

        def converting_input_ker_1():

            try:
                global in_kerulet_haromszog_1
                in_kerulet_haromszog_1 = int(in_kerulet_haromszog_1)

            except:
                print(f"\n{Fore.RED}Ezzel az adattal nem lehet számolni!!{Style.RESET_ALL}")
                inputs_ker_haromszog()

        def converting_input_ker_2():

            try:
                global in_kerulet_haromszog_2
                in_kerulet_haromszog_2 = int(in_kerulet_haromszog_2)

            except:
                print(f"\n{Fore.RED}Ezzel az adattal nem lehet számolni!!{Style.RESET_ALL}")
                inputs_ker_haromszog()

        def converting_input_ker_3():

            try:
                global in_kerulet_haromszog_3
                in_kerulet_haromszog_3 = int(in_kerulet_haromszog_3)
                haromszogcallc()

            except:
                print(f"\n{Fore.RED}Ezzel az adattal nem lehet számolni!!{Style.RESET_ALL}")
                inputs_ker_haromszog()

        def derekszog():

            if (in_kerulet_haromszog_1 ** 2) + (in_kerulet_haromszog_2 ** 2) == (in_kerulet_haromszog_3 ** 2) or (in_kerulet_haromszog_2 ** 2) + (in_kerulet_haromszog_1 ** 2) == (in_kerulet_haromszog_3 ** 2) or (in_kerulet_haromszog_3 ** 2) + (in_kerulet_haromszog_2 ** 2) == (in_kerulet_haromszog_1 ** 2):
                print(f"\n{Fore.RED}Ez a háromszög derékszögű.{Style.RESET_ALL}")

            else:
                print(f"\n{Fore.RED}Ez a háromszög nem derékszögű.{Style.RESET_ALL}")

        def haromszogcallc():

            if in_kerulet_haromszog_1 + in_kerulet_haromszog_2 >= in_kerulet_haromszog_3 or in_kerulet_haromszog_2 + in_kerulet_haromszog_1 >= in_kerulet_haromszog_3 or in_kerulet_haromszog_1 + in_kerulet_haromszog_3 >= in_kerulet_haromszog_2 or in_kerulet_haromszog_3 + in_kerulet_haromszog_1 >= in_kerulet_haromszog_2 or in_kerulet_haromszog_3 + in_kerulet_haromszog_1 >= in_kerulet_haromszog_2 or in_kerulet_haromszog_1 + in_kerulet_haromszog_3 >= in_kerulet_haromszog_2:
                derekszog()
                print(Fore.GREEN +"\nEz a háromszög szerkezthető" + Style.RESET_ALL)
                kerülete_haromszog = in_kerulet_haromszog_1 + in_kerulet_haromszog_2 + in_kerulet_haromszog_3
                print(f"{Fore.GREEN}\nA kerület: {kerülete_haromszog}{Style.RESET_ALL}")
                s = kerülete_haromszog / 2
                cal_1 = s * ((s - in_kerulet_haromszog_1) * (s - in_kerulet_haromszog_2) * (s - in_kerulet_haromszog_3))
                területe_haromszog = cal_1 ** 0.5
                print(f"\n{Fore.GREEN}A terület: {területe_haromszog}{Style.RESET_ALL}")   
                repait()

            else:
                print(Fore.RED + "Nem szerkezthető")

        inputs_ker_haromszog()


    #Haromszög kerülete területe vége

    #Kerület vége
    #Terület

    def region():
        input_1 = int(input("\nMilyen alakzatnak szeretnéd a területét: (kör, négyzet, téglalap, háromszög)"))

    #Terület vége
    #Ismétlés függvény

    def repait():
        user_continue = input("\nSzeretnéd továbbra is számolni? ( igen / nem ) ")

        if user_continue == "igen" or user_continue == "i":
            choice()

        elif user_continue == "nem" or user_continue == "n":            
            kilepes()

        else:
            print("\nIlyen érték nincs megadva.")
            repait()

    #Ismétlés függvény vége
    #Ez csak egy nagy szöveg kiiratásának függvénye
 
    def big_text():
        print(f"""{Fore.YELLOW}
   ____        _  _               _         _                  _                ____                    _  
  / ___| __ _ | || |  ___  _   _ | |  __ _ | |_  ___   _ __   | |__   _   _  _ | __ )   __ _  ____ ___ (_) 
 | |    / _` || || | / __|| | | || | / _` || __|/ _ \ | '__|  | '_ \ | | | |(_)|  _ \  / _` ||_  // __|| | 
 | |___| (_| || || || (__ | |_| || || (_| || |_| (_) || |     | |_) || |_| | _ | |_) || (_| | / / \__ \| | 
  \____|\__,_||_||_| \___| \__,_||_| \__,_| \__|\___/ |_|     |_.__/  \__, |(_)|____/  \__,_|/___||___/|_| 
                                                                      |___/                                                                                                     
    {Style.RESET_ALL}Ez egy számológép alkalmazás:""")

    #Ez csak egy nagy szöveg kiiratásának függvénye vége

    def choice():

        print("""
    Válaszd ki a neked kellő művelet számat.
        
        (0) Kilépés
        (1) Összeadás
        (2) Kivonás
        (3) Szorzás
        (4) Osztás 
        (5) Négyzetre emelés
        (6) Négyzet gyökvonás
        (7) Kerület
        (8) Terület 
              
              """)

    #A felhasználótól bekér egy inputut    

        global user_choise
        user_choise = input("Választásod? ")  

        if user_choise == "0":
            kilepes()

        elif user_choise == "1":
            addition()
            repait()

        elif user_choise == "2":
            subtraction()
            repait()

        elif user_choise == "3":
            multiplication()
            repait()

        elif user_choise == "4":
            division()
            repait()
   
        elif user_choise == "5":
            exponentiation()
            repait()

        elif user_choise == "6":
            root_subtraction()
            repait() 

        elif user_choise == "7":
            district()
            repait()

        elif user_choise == "8":
            region()
            repait()                          

        else:
            print("\nIlyer érték nincs felsorolva")  
            choice()

    big_text()
    choice()

main()