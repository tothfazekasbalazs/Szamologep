import time

def main():
    
    def choice():
        print("""
              
    Ez egy számológép alkalmazás:

    Válaszd ki a neked kellő művelet számat.
        
        (0) Kilépés
        (1) Összeadás
        (2) Kivonás
        (3) Szorzás
        (4) Osztás     
              
              """)

        global user_choise
        user_choise = input("Választásod? ")  

        if user_choise == "0":
            print("\nA rendszer 3 másotperc múlva bezárja magát")
            time.sleep(3)
            quit()

        elif user_choise == "1":
            input_1 = int(input("\nMennyit szeretnél összeadni: "))
            input_2 = int(input("\nMenyit szertnél hozzáadni: "))
            eredmeny = input_1 + input_2  
            print(f"\n Az szamolás eredménye: {eredmeny}") 

        elif user_choise == "2":
            input_1 = int(input("\nMennnyiből szeretnél kivonni: "))
            input_2 = int(input("\nMennyit?: "))
            eredmeny = input_1 - input_2  
            print(f"\n Az szamolás eredménye: {eredmeny}") 

        elif user_choise == "3":
            input_1 = int(input("\nMennyit szeretnél összeszorozni: "))
            input_2 = int(input("\nMenyivel: "))
            eredmeny = input_1 * input_2  
            print(f"\n Az szamolás eredménye: {eredmeny}") 

        elif user_choise == "4":
            input_1 = int(input("\nMennyit szeretnél osztani: "))
            input_2 = int(input("\nMenyivel: "))
            eredmeny = input_1 / input_2  
            print(f"\n Az szamolás eredménye: {eredmeny}")                              

        else:
            print("\nIlyer érték nincs felsorolva")  
            choice()

    def repait():
        user_continue = input("\nSzeretnéd folytatni? ( igen / nem ) ")

        if user_continue == "igen":
            main()

        elif user_continue == "nem":            
            print("\nA rendszer 3 másotperc múlva bezárja magát.")
            time.sleep(3)
            quit()

        else:
            print("\nIlyen érték nincs megadva.")
            repait()

    choice()
    repait()

main()