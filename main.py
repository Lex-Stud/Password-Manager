def addPass():
    acc = input("Nume Site/App\n")
    if acc.find("=") >=0:
        print ("Numele nu are voie sa contina '='")
        quit()
    auto_pass = input ("Doresti sa generezi o parola? Da/Nu\n")
    
    if auto_pass == "Da":
        import random
        import string
        pwd = ''.join(random.choices(string.ascii_letters + string.digits, k=8))    
    else:
        pwd = input ("Introdu Parola:\n")
    
    with open("passwords.txt", 'a') as file:
        file.write(acc + " = " + pwd + "\n") 
    
def viewPass():
    acc = input ("Nume Site/App\n")
    
    with open ("passwords.txt", 'r') as file:
        for line in file:
            get_name = line[: line.find("=")]
            
            if get_name.find(acc) >= 0:
                print(line)
                break
    print("Contul nu există")

def deletePass():
    acc = input ("Nume Site/App\n")
    
    with open("passwords.txt", 'r') as file:
        lines = file.readlines()
    
    with open("passwords.txt", 'w') as file:
        for line in lines:
            get_name = line[: line.find("=")]
            
            if get_name.find(acc) < 0:
                file.write(line)
                break
            
    print("Contul a fost gasit")
            

option = input("Adaugă parola: add\nVezi parola existentă: view\nSterge parola: delete\n")

if option == "add":
    addPass()
elif option == "view":
    viewPass()
elif option == "delete":
    deletePass()
else:
    print("Opțiune incorectă")
