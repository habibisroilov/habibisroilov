from datetime import datetime


with open ('text.txt' , 'a') as text:
    while True:
        login = input('Enter login ') 
        password = input ('Enter password ') 
        time = datetime.now()
        print(time)
        text.write(f"login: {login}\n")
        text.write(f"password: {password}\n")
        a = input("davom etasizmi  ('xa / yoq )") 
        print("Salom " , login )
        if a == 'yoq':
            break
            
 
   
   

        
        
        