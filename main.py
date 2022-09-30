import time
import colorama
from colorama import Fore, Back, Style

def main():

    def kilepes():
        print("\nA rendszer 3 másotperc múlva bezárja magát")
        time.sleep(3)
        exit()

    def converting_input_1():

        try:
            global input_1
            input_1 = int(input_1)

        except:
            print(Fore.RED +"\nEzzel az adattal nem lehez számolni!!")
            repait()

    def converting_input_2():

        try:
            global input_2
            input_2 = int(input_2)

        except:
            print(Fore.RED +"\nEzzel az adattal nem lehez számolni!!")
            repait()

    def addition():
        global input_1
        input_1 = input("\nMennyit szeretnél összeadni: ")
        converting_input_1()
        global input_2
        input_2 = input("\nMenyit szertnél hozzáadni: ")
        converting_input_2()
        eredmeny = input_1 + input_2  
        print(f"\n Az szamolás eredménye: {eredmeny}") 

    def subtraction():
        global input_1
        input_1 = input("\nMennnyiből szeretnél kivonni: ")
        converting_input_1()
        global input_2
        input_2 = input("\nMennyit?: ")
        converting_input_2()
        eredmeny = input_1 - input_2  
        print(f"\n Az szamolás eredménye: {eredmeny}")

    def multiplication():
        global input_1
        input_1 = input("\nMennyit szeretnél összeszorozni: ")
        converting_input_1()
        global input_2
        input_2 = input("\nMenyivel: ")
        converting_input_2()
        eredmeny = input_1 * input_2  
        print(f"\n Az szamolás eredménye: {eredmeny}")

    def division():
        global input_1
        input_1 = input("\nMennyit szeretnél osztani: ")
        converting_input_1()
        global input_2
        input_2 = input("\nMenyivel: ")
        converting_input_2()
        eredmeny = input_1 / input_2  
        print(f"\n Az szamolás eredménye: {eredmeny}")
    
    def exponentiation():
        global input_1
        input_1 = input("\nMennyit szeretnél négyzetre emelni: ")
        converting_input_1()
        eredmeny = input_1 ** input_1  
        print(f"\n Az szamolás eredménye: {eredmeny}")

    def root_subtraction():
        global input_1
        input_1 = int(input("\nMennyit szeretnél a négyzetgyökét: "))
        eredmeny = input_1 ** 0,5  
        print(f"\n Az szamolás eredménye: {eredmeny}")

    def district():       
        input_1 = int(input("\nMilyen alakzatnak szeretnéd a kerületét: (kör, négyzet, téglalap, háromszög) "))

        if input_1 == "kör":
            kor_input = int(input(""))

        elif input_1 == "négyzet" or "Négyzet":
            negyzet_input = int(input(""))

        elif input_1 == "téglalap" or "Téglalap":
            teglalap_input = int(input(""))

        elif input_1 == "haromszög" or "Háromszög":
            haromszög_input = int(input(""))

        else:
            print(f"\n Ilyen érték nincs megadva")
            district()

    def root_subtraction():
        input_1 = int(input("\nMilyen alakzatnak szeretnéd a területét: (kör, négyzet, téglalap, háromszög)"))

    def repait():
        user_continue = input(Fore.WHITE +"\nSzeretnéd továbbra is számolni? ( igen / nem ) ")

        if user_continue == "igen":
            choice()

        elif user_continue == "nem":            
            kilepes()

        else:
            print("\nIlyen érték nincs megadva.")
            repait()
 
    def big_text():
        print("""
   ____        _  _               _         _                  _                ____                    _  
  / ___| __ _ | || |  ___  _   _ | |  __ _ | |_  ___   _ __   | |__   _   _  _ | __ )   __ _  ____ ___ (_) 
 | |    / _` || || | / __|| | | || | / _` || __|/ _ \ | '__|  | '_ \ | | | |(_)|  _ \  / _` ||_  // __|| | 
 | |___| (_| || || || (__ | |_| || || (_| || |_| (_) || |     | |_) || |_| | _ | |_) || (_| | / / \__ \| | 
  \____|\__,_||_||_| \___| \__,_||_| \__,_| \__|\___/ |_|     |_.__/  \__, |(_)|____/  \__,_|/___||___/|_| 
                                                                      |___/                                                                                                     
    Ez egy számológép alkalmazás:""")

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

        global user_choise
        user_choise = input("Választásod? ")  

        if user_choise == "0":
            kilepes()
            repait()

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

        else:
            print("\nIlyer érték nincs felsorolva")  
            choice()

    big_text()
    choice()
    repait()

main()