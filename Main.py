from DatabaseFunc import ADDuser, StartDatabase, DBtable
import sqlite3
db_name = "BilGoVrum.db"
Menu = False
login = True

StartDatabase(db_name)
DBtable(db_name)

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




    if valg == "2":
        ADDuser(db_name, input("Indsæt user navn: "), input("Indsæt email: "), input("Indsæt password: "))
    
    if valg == "3":
        print("Bye, bye")
        break


while Menu:
    print("\n--- MENU ---")
    print("1. Sorter biler ud fra pris/km")
    print("2. Sorter biler ud fra modelår til pris")
    print("3. Sorter biler ud fra drivemidel til pris")
    print("4. Sorter biler ud fra Mærke til pris")
    print("5. Update database(Tager mega lang tid)")
    print("6. Quit")

    valg = input("Choose (1-6): ")

    if valg == "1":
        pass

    elif valg == "2":
        pass

    elif valg == "3":
        pass

    elif valg == "4":
        pass

    elif valg == "5":
        pass

    elif valg == "6":
        print("Bye, bye")
        break
    
    else:
        print("Bevar dit svar inde for rangen vi har angivet tak")

    