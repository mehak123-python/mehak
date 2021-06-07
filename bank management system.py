#Source Code:
"""***************************
                            MODULES USED IN PROJECT
***************************"""
import pickle
import os
import MySQLdb
"""***************************
                            CLASS USED FOR CONNECTIVITY
***************************"""
class connect():
    conn=MySQLdb.connect("localhost","root","mahakal","bank")
    cur=conn.cursor()
    #here you have to pass the accno, name, type, deposit
    def create(self, acno, name, type, deposit):
        query=(self.acno,self.name,self.type,self.deposit)
        Insert="INSERT INTO acc_det VALUES()"
        cur.execute("insert into acc_det ('accno','holder_name','acctype','balance') values(%s,%s,%s,%s)",query)
        conn.commit()
        cur.close()
        conn.close()
        return "Success"
    def deposit(self, acno, amount):
        query=(self.amount, self.acno)
        update="update acc_det set balance = balance + %s where accno= %s;"
        cur.execute(update,query)
        conn.commit()
        cur.close()
        conn.close()
        return "Success"
    def withdraw(self, acno, amount):
        query=(self.amount, self.acno)
        update="update acc_det set balance = balance - %s where accno= %s;"
        cur.execute(update,query)
        conn.commit()
        cur.close()
        conn.close()
        return "Success"
    def show_balance(self, acno):
        query=(self.acno)
        show="select balance from acc_det where accno=%s;"
        cur.execute(show,query)
        res=cur.fetchall()
        print("Your current balance is: ",res)
        cur.close()
        conn.close()
    def show_holder(self):
        show="select holder_name from acc_det;"
        cur.execute(show)
        res=cur.fetchall()
        for rec in res:
            print(rec)
        cur.close()
        conn.close()
    def closethe(self, acno):
        query=(self.acno)
        show="delete from acc_det where accno=%s;"
        cur.execute(show,query)
        res=cur.fetchall()
        conn.commit()
        print("Your account deleted successfull")
        cur.close()
        conn.close()
"""***************************
                            CLASS USED IN PROJECT
***************************"""
class account(object):
    con=connect()
    def _init_(self):
        self.acno=0
        self.name=""
        self.deposit=0
        self.type=""
    def create_account(self):  #function to get data from user
        self.acno=input("enter the acount no")
        name=input("\n\nEnter the name of the account holder: ")
        self.name=name.capitalize()
        type=input("\nEnter type of the account (C/S): ")
        self.type=type.upper()
        self.deposit=int(input("\nEnter initial amount\n(>=500 for Saving and >=1000 for Current): "))
        con.create(acno,name,type,deposit)
    def show_account(self):    #function to show data on screen
        print ("\nAccount No. :", self.acno)
        print ("\nAccount holder name: ", self.name)
        print ("\nType of account", self.type)
        print ("\nBalance amount: ", self.deposit)
    def modify(self):          #function to get new data from user
        print ("\nAccount No. : ", self.acno)
        self.name=input("\n\nEnter the name of account holder: ")
        type=input("\n\nEnter type of account (C/S): ")
        self.type=type.upper()
        self.deposit=int(input("\nEnter the amount: "))
    def dep(self,n,x):           #function to accept amount and add to balance
        self.deposit+=x
        con.deposit(n,x)
    def draw(self,n,x):          #function to accept amount and subtract from balance amount
        self.deposit-=x
        con.withdraw(n,x)
    def report(self):          #function to show data in tabular format
        print ("%-10s"%self.acno,"%-20s"%self.name,"%-10s"%self.type,"%-6s"%self.deposit)
    def retacno(self):         #function to return account number
        return self.acno
    def retdeposit(self):      #function to return balance amount 
        return self.deposit
    def rettype(self):         #function to return type of account
        return self.type
"""***************************
                    FUNCTION TO GENERATE ACCOUNT NUMBER
***************************
def gen_acno():
    try:
        inFile=open("account2.dat","rb")
        outFile=open("text2.dat","wb")
        n=inFile.read()
        n=int(n)
        while True:
            n+=1
            outFile.write(str(n))
            inFile.close()
            outFile.close()
            os.remove("account2.dat")
            os.rename("text2.dat","account2.dat")
            yield n
            
    except IOError:
        print ("I/O error occured")"""

"""***************************
                    FUNCTION TO WRITE RECORD IN BINARY FILE
***************************"""
def write_account():
    try:
        ac=account()
        outFile=open("account.dat","ab")
       # ch=gen_acno()
        ac.create_account()
        pickle.dump(ac,outFile)
        outFile.close()
        print ("\n\n Account Created Successfully")
        print ("\n\n YOUR ACCOUNT NUMBER IS: ",ac.retacno())
    except:
        pass

"""***************************
                FUNCTION TO DISPLAY ACCOUNT DETAILS GIVEN BY USER
***************************"""
def display_sp(n):
    flag=0
    try:
        inFile=open("account.dat","rb")
        print ("\nBALANCE DETAILS\n")
        while True:
            ac=pickle.load(inFile)

            if ac.retacno()==n:
                ac.show_account()
                flag=1
                
    except EOFError:
        inFile.close
        if flag==0:
            print ("\n\nAccount number not exist")

    except IOError:
        print ("File could not be open !! Press any Key...")

"""***************************
                        FUNCTION TO MODIFY RECORD OF FILE
***************************"""
def modify_account(n):
    found=0
    try:
        inFile=open("account.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            ac=pickle.load(inFile)
            if ac.retacno()==n:
                print (30*"-")
                ac.show_account()
                print (30*"-")
                print ("\n\nEnter The New Details of Account")
                ac.modify()
                pickle.dump(ac,outFile)
                print ("\n\n\tRecord Updated")
                found=1
            else:
                pickle.dump(ac,outFile)
             
    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print ("\n\nRecord Not Found ")

    except IOError:
        print ("File could not be open !! Press any Key...")
        
    os.remove("account.dat")
    os.rename("temp.dat","account.dat")

"""***************************
                    FUNCTION TO DELETE RECORD OF FILE
***************************"""
def delete_account(n):
    found=0

    try:
        inFile=open("account.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            ac=pickle.load(inFile)
            if ac.retacno()==n:
                found=1
                print ("\n\n\tRecord Deleted ..")
            else:
                pickle.dump(ac,outFile)

    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print ("\n\nRecord Not Found")

    except IOError:
        print ("File could not be open !! Press any Key...")

    os.remove("account.dat")
    os.rename("temp.dat","account.dat")

"""***************************
                    FUNCTION TO DISPLAY ALL ACCOUNT DETAILS
***************************"""
def display_all():
    print ("\n\n\tACCOUNT HOLDER LIST\n\n")
    print (60*"=")
    print ("%-10s"%"A/C No.","%-20s"%"Name","%-10s"%"Type","%-6s"%"Balance")
    print (60*"=","\n")
    try:
        inFile=open("account.dat","rb")
        while True:
            ac=pickle.load(inFile)
            ac.report()
            
    except EOFError:
        inFile.close()
        
    except IOError:
        print ("File could not be open !! Press any Key...")

"""***************************
            FUNCTION TO DEPOSIT/WITHDRAW AMOUNT FOR GIVEN ACCOUNT
***************************"""
def deposit_withdraw(n,option):
    found=0

    try:
        inFile=open("account.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            ac=pickle.load(inFile)
            if ac.retacno()==n:
                ac.show_account()
                if option==1:
                    print ("\n\n\tTO DEPOSIT AMOUNT")
                    amt=int(input("Enter the amount to be deposited: "))
                    ac.dep(n, amt)
                elif option==2:
                    print ("\n\n\tTO WITHDRAW AMOUNT")
                    amt=int(input("Enter amount to be withdraw: "))
                    bal=ac.retdeposit()-amt
                    if((bal<500 and ac.rettype()=="S")or(bal<1000 and ac.rettype()=="C")):
                        print ("Insufficient balance")
                    else:
                        ac.draw(n, amt)
                pickle.dump(ac,outFile)
                found=1
                print ("\n\n\tRecord Updated")
            else:
                pickle.dump(ac,outFile)
                
    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print ("\n\nRecord Not Found")
    
    except IOError:
        print ("File could not be open !! Press any Key...")

    os.remove("account.dat")
    os.rename("temp.dat","account.dat")

"""***************************
                        INTRODUCTORY FUNCTION
***************************"""
def intro():
    print ("\n\n\tBanking Management System")
    print ("Created and Compiled by : mehaak sharma")
    print ("    r.c institute of technology")
"""***************************
                        THE MAIN FUNCTIONING  OF PROGRAM
***************************"""
intro()
while True:
    print (2*"\n",60*"=")
    print ("""           MAIN MENU

    1. New Account
    2. Deposit Amount
    3. Withdraw Amount
    4. Balance Enquiry
    5. All Account Holder List
    6. Close An Account
    7. Modify An Account
    8. Exit
    """)
    try:
        ch=int(input("Enter Your Choice(1~8): "))
        if ch==1:
            write_account()
        elif ch==2:
            num=int(input("\n\nEnter Account Number: "))
            deposit_withdraw(num,1)
        elif ch==3:
            num=int(input("\n\nEnter Account Number: "))
            deposit_withdraw(num,2)
        elif ch==4:
            num=int(input("\n\nEnter Account Number: "))
            display_sp(num)
        elif ch==5:
            display_all()
        elif ch==6:
            num=int(input("\n\nEnter Account Number: "))
            delete_account(num)
        elif ch==7:
            num=int(input("\n\nEnter Account Number: "))
            modify_account(num)
        elif ch==8:
            break
        else:
            print ("Input correct choice...(1-8)")
    except NameError:
        print ("Input correct choice...(1-8)")

x=input("\n\n\n\n\nTHANK YOU\n\nPress any key to exit...")





