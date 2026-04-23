from DatabaseFunc import ADDuser, StartDatabase, DBtable, Update
import sqlite3
db_name = "BilGoVrum.db"
Menu = False
login = True

#disse funktioner starter databasen og laver tables kig i filen databaseFunc
StartDatabase(db_name)
DBtable(db_name)

#starter med at være true
while login:
    print("\n--- Login/Signup ---")
    print("1. Login")
    print("2. Sign up")
    print("3. Quit")

    valg = input("Choose (1-3): ")

    if valg == "1":
        userN = input("Indtast dit usernavn: ")
        cx = sqlite3.connect(db_name)
        cur = cx.cursor()
        res = cur.execute("SELECT name FROM users").fetchall()
        outputN = []
        #https://www.youtube.com/watch?v=hwR9ex9QKxQ denne video forklare koden under hvor en tuble bliver konverteret til en liste
        for name in res:
            outputN.append(name[0])

        if userN in outputN:
            res = cur.execute("SELECT password FROM users").fetchall()
            outputP = []
            for password in res:
                outputP.append(password[0])

            if  input("Indsæt dit password: ") in outputP:
                login = False
                Menu = True

            else:
                print("Forkert password")

        else:
            print("Forkert username")
        cx.close()




    elif valg == "2":
        ADDuser(db_name, input("Indsæt user navn: "), input("Indsæt email: "), input("Indsæt password: "))
    
    elif valg == "3":
        print("Bye, bye")
        break
    
    else:
        print("Bevar dit svar inde for rangen vi har angivet tak")


#false indtil man login 
while Menu:
    print("\n--- MENU ---")
    print("Når man skal ind på et link skal man huske ikke at få Newline med")
    print("1. Sorter biler ud fra pris/km")
    print("2. Sorter biler ud fra modelår til pris")
    print("3. Sorter biler ud fra drivemiddel til pris")
    print("4. Sorter biler ud fra mærke til pris")
    print("5. Sorter biler ud fra hestekrafter til pris")
    print("6. Update database(Kræver en okay pc)")
    print("7. Quit")

    valg = input("Vælg (1-7): ")
    #denne video giver en god forklaring på sortering https://www.youtube.com/watch?v=51RLlmj89nQ
    if valg == "1":
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        selection = cur.execute("SELECT prisPrKM, Url FROM biler ORDER BY prisPrKM ASC").fetchall()
        print("Her er bilerne sorteret efter pris til km:")
        n = 0
        while len(selection) != n:
            print(selection[n])
            n += 1


    elif valg == "2":
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        selection = cur.execute("SELECT prisPrKM, modelÅr, Url FROM biler ORDER BY modelÅr DESC").fetchall()
        print("Her er bilerne sorteret efter pris til modelår:")
        n = 0
        while len(selection) != n:
            print(selection[n])
            n += 1

    elif valg == "3":
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        selection = cur.execute("SELECT prisPrKM, drivemidel, Url FROM biler ORDER BY prisPrKM ASC").fetchall()
        print("Her er bilerne sorteret efter pris til drivemidel:")
        n = 0
        while len(selection) != n:
            print(selection[n])
            n += 1


    elif valg == "4":
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        selection = cur.execute("SELECT prisPrKM, BilNavn, Url FROM biler ORDER BY BilNavn ASC").fetchall()
        print("Her er bilerne sorteret efter pris til mærke:")
        n = 0
        while len(selection) != n:
            print(selection[n])
            n += 1


    elif valg == "5":
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        selection = cur.execute("SELECT prisPrKM, hestekrafter, Url FROM biler ORDER BY hestekrafter ASC").fetchall()
        print("Her er bilerne sorteret efter pris til hestekrafter:")
        n = 0
        while len(selection) != n:
            print(selection[n])
            n += 1

    elif valg == "6":
        Update(db_name)
        print("Databasen er blevet updateret")

    elif valg == "7":
        print("Bye, bye")
        break
    
    else:
        print("Bevar dit svar inde for rangen vi har angivet tak")

    