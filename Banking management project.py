import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="banking")
if mydb.is_connected():
    print("Connection success")
else:
    print("Connection failure!")
mycursor=mydb.cursor(buffered=True)
def menu():
    print("*"*167)
    print("MAIN MENU".center(167))
    print("1.insert record/records".center(167))
    print("2.display records details sorted by account number".center(167))
    print("3.search record details as per the account number".center(167))
    print("4.update record".center(167))
    print("5.delete record".center(167))
    print("6.transaction menu".center(167))
    print("7.Exit".center(167))
    print("*"*167)
def insert():
        acc=input("Enter an account no:")
        if acc.isalpha():
              print("Invalid input")
              print("Please enter again")
              insert()
        query = "select * from balance"
        mycursor.execute(query)
        mydb.commit()
        records = mycursor.fetchall()
        c=""
        for record in records:
           c=record[0]
           if acc==c:
               print("Account number already exists please enter another account number")
               insert()
        a=True
        while a==True:    
           name=input("Enter name:")
           if name.isdigit():
              print("Invalid input")
              print("Please enter again")
              continue
           name=name.capitalize()
           a=False
        a=True
        while a==True:       
            mob=int(input("Enter mobile number:"))
            if str(mob).isalpha():
              print("Invalid input")
              print("Please enter again")
              continue
            a=False
        address=input("Enter address:")
        a=True
        while a==True:    
           city=input("Enter city:")
           if city.isdigit():
              print("Invalid input")
              print("Please enter again")
              continue 
           city=city.capitalize()
           a=False
        rec=[acc,name,mob,address,city]
        cmd=("insert into bank values(%s,%s,%s,%s,%s)")
        mycursor.execute(cmd,rec)
        mydb.commit()
        print("Record created")
        print()
        print("Please pay RS.5000 as opening balance in the front desk")
        print()
        cde="insert into balance values('{}',{})".format(acc,5000)
        mycursor.execute(cde)
        mydb.commit()
        ch=input("Do you want to insert more records(y/n):")
        if ch=="Y" or ch=="y":
            insert()

def sortbyacc():
        print("Printing customer details ordered by accno")
        cmd="select * from bank order by accno"
        mycursor.execute(cmd)
        print("           accno","name","mobile","address","city",sep='\t\t    ')
        print("="*167)
        for i in mycursor:
           for j in i:
                print("%17s" % j,end='\t') 
           print()
        print()   
        print("Do you also want to print their previous transaction details ordered by accno")
        c=input("Enter your choice(y/n):")
        if c.lower()=='y':
            cmd="select * from transaction order by accno"
            mycursor.execute(cmd)
            print("           accno","date of trans","medium of trans","   trans type","         trans amount",sep='\t\t    ')
            print("="*167)
            for i in mycursor:
                for j in i:
                   print("%17s" % j,end='\t\t') 
                print()
        print()   
        print("Do you also want to print their balance ordered by accno")
        c=input("Enter your choice(y/n):")
        if c.lower()=='y':
            cmd="select * from balance order by accno"
            mycursor.execute(cmd)
            print("            accno","Balance",sep='\t\t   ')
            print("="*167)
            for i in mycursor:
               for j in i:
                 print("%17s" % j,end='\t') 
               print()
def searchbyacc():
        cmd="select * from bank"
        cde="select * from transaction"
        cme="select * from balance"
        mycursor.execute(cmd)
        s=mycursor.fetchall()
        mydb.commit()
        mycursor.execute(cde)
        x=mycursor.fetchall()
        mydb.commit()
        mycursor.execute(cme)
        n=mycursor.fetchall()
        mydb.commit()
        d=0
        ch=input("Enter the accno to be searched:")
        for i in s:
            if i[0]==ch:
                print()
                print()
                print("Displaying customer details:")
                print("="*116)
                print("           accno","name","mobile","address","city",sep='\t\t    ')
                print("="*116)
                for j in i:
                     print("%17s" % j,end='\t')
                     mydb.commit()
                d=1     
                break
        if d==1:        
          for i in x:
              if i[0]==ch:
                print()
                print()
                print()
                print()
                print()
                print("Displaying transation details:")
                print("="*167)
                print("           accno","date of trans","medium of trans","   trans type","         trans amount",sep='\t\t    ')
                print("="*167)
                for j in i:
                      print("%17s" % j,end='\t\t')
                      mydb.commit()
                print()
                break
        if d==1:
            for i in n:
             if i[0]==ch:
                print()
                print()
                print()
                print()
                print()
                print("Displaying balance:")
                print("="*45)
                print("            accno","Balance",sep='\t\t   ')
                print("="*45)
                for j in i:
                     print("%17s" % j,end='\t')
                     mydb.commit()
                print()
                print()
                print()
                break
        if d==0:
              print("Wrong account number")
              p=input("Do you want to try again?(y/n):")
              if p.lower()=='y':
                   searchbyacc()
                
            
      
def update():
        cmd="select * from bank"
        mycursor.execute(cmd)
        s=mycursor.fetchall()
        mydb.commit()
        d=0
        c=0
        A=input("Enter the accno whose details to be updated:")
        for i in s:
            i=list(i)
            if i[0]==A:
                ch=input("Do you want to change mobile number(yes/no):")
                if ch=='yes' or ch=='YES':
                    a=True
                    while a==True:
                        i[2]=int(input("Enter the new mobile number:"))
                        if str(i[2]).isalpha():
                            print("Invalid input")
                            print("Please enter again")
                            continue
                        c+=1
                        a=False
                ch=input("Do you want to change address(yes/no):")
                if ch=='yes' or ch=='YES':
                    i[3]=input("Enter the new address:")
                    c+=1
                ch=input("Do you want to change city(yes/no):")
                if ch=='yes' or ch=='YES':
                    a=True
                    while a==True:
                        i[4]=input("Enter the new city:")
                        if i[4].isdigit():
                            print("Invalid input")
                            print("Please enter again")
                            continue
                        c+=1
                        a=False
                        i[4]=i[4].capitalize()
                cmd="update bank set mobile={},address='{}',city='{}' where accno='{}'".format(i[2],i[3],i[4],i[0])
                mycursor.execute(cmd)
                mydb.commit()
                if c!=0:
                   print("Account Updated")   
                c=input("Do you want to display the updated record?(y/n):")
                if c.lower()=='y':
                    print()
                    print()
                    cmd="select * from bank where accno='{}'".format(A)
                    mycursor.execute(cmd)
                    mydb.commit
                    print("           accno","name","mobile","address","city",sep='\t\t    ')
                    print("="*167)
                    for i in mycursor:
                         for j in i:
                             print("%17s" % j,end='\t') 
                         print()
                    print("="*167)
                    print()    
                d=1
                break
        if d==0:
            print("Wrong account number")
            print("Please try again")
            update()
                           
def delete():
        cmd="select * from bank"
        cde="select * from transaction"
        cme="select * from balance"
        mycursor.execute(cmd)
        s=mycursor.fetchall()
        mydb.commit()
        mycursor.execute(cde)
        x=mycursor.fetchall()
        mydb.commit()
        mycursor.execute(cme)
        j=mycursor.fetchall()
        mydb.commit()
        c=0
        A=input("Enter the accno that has to be deleted:")
        for i in j:
            i=list(i)
            if i[0]==A:
                cmd="delete from balance where accno='{}'".format(A)
                mycursor.execute(cmd)
                mydb.commit()
                print("Balance details deleted")
                c=1
                break
        if c==1:
          for i in x:
            i=list(i)
            if i[0]==A:
                cmd="delete from transaction where accno='{}'".format(A)
                mycursor.execute(cmd)
                mydb.commit()
                print("Transaction details deleted")
                break
        if c==1:    
          for i in s:
            i=list(i)
            if i[0]==A:
                cmd="delete from bank where accno='{}'".format(A)
                mycursor.execute(cmd)
                mydb.commit()
                print("Customer details deleted")
                break
            
        if c==0:
            print("Wrong account number")
            print("Please try again")
            delete()
               
def transaction():
        accno=input("Enter account no:")
        query = "select * from balance"
        mycursor.execute(query)
        mydb.commit()
        records = mycursor.fetchall()
        c=""
        r=0
        for record in records:
           c=record[0]
           if accno==c:
               r=1
               break
        if r==1:
          a=True
          b=True
          c=True
          dot=input("Please enter today's date(YYYY-MM-DD):")
          print("Do you wish to withdraw or deposit")
          while a==True:
              transtype=input("Enter your choice (withdraw/deposit):")
              if transtype.isdigit():
                 print("Invalid input")
                 print("Please enter again")
                 continue
              if transtype.lower() not in ['withdraw','deposit']:
                 print("Invalid input")
                 print("Please enter again")
                 continue
              a=False
          print("Do you want to",transtype,"through cash or cheque")    
          while b==True:    
               transmedium=input("Enter your choice(Cash/Cheque):")
               if transmedium.isdigit():
                  print("Invalid input")
                  print("Please enter again")
                  continue
               if transmedium.lower() not in ['cash','cheque']:
                   print("Invalid input")
                   print("Please enter again")
                   continue
               b=False
               transmedium=transmedium.capitalize()
          while c==True:
               transamount=(int(input("Enter the amount to "+transtype+" :")))
               if str(transamount).isalpha():
                    print("Invalid input")
                    print("Please enter again")
                    continue
               c=False 
          if transtype.lower()=='withdraw':
            cme="select balance from balance where accno='{}'".format(accno)
            mycursor.execute(cme)
            mydb.commit()             
            s=mycursor.fetchone()
            m=s[0]
            if transamount>m:
               print("Your balance is insufficient")
               x=print("Do you wish to try again?(y/n):")          
               if x.lower()=='y':
                  transaction()
               else:
                  print("Returning to main menu...")
                  menu()                       
          rec=[accno,dot,transmedium,transtype,transamount]
          cmd=("insert into transaction values(%s,%s,%s,%s,%s)")
          mycursor.execute(cmd,rec)
          mydb.commit()                
          if transtype.lower()=='deposit':
            cde="update  balance set balance=balance+{} where accno='{}'".format(transamount,accno)
            mycursor.execute(cde)
            mydb.commit()
          elif transtype.lower()=='withdraw':
            ade="update  balance set balance=balance-{} where accno='{}'".format(transamount,accno)
            mycursor.execute(ade)
            mydb.commit()
          print("Transaction complete")
          m=input("Do you want to see your balance?(y/n):")
          if m.lower()=='y':
            cxe="select balance from balance where accno='{}'".format(accno)
            mycursor.execute(cxe)
            mydb.commit()
            s=mycursor.fetchone()
            print("Your balance is :",s[0])
        else:
            print("Account number does not exist")
            print("Please try again")
            transaction()
x=int(input("Enter password to continue :"))
if x==1234:               
 while True:    
    menu()
    ch=input("Enter your choice:")
    if ch=="1":
        insert()
    elif ch=="2":
        sortbyacc()
    elif ch=="3":
        searchbyacc()
    elif ch=="4":
        update()
    elif ch=="5":
        delete()
    elif ch=="6":
        print("*"*167)
        print("Welcome to transaction menu".center(167))
        print("*"*167)
        transaction()
    elif ch=="7":
        print("Thank you for choosing us")
        print("Exiting!...")
        break
    else:
        print("Wrong choice entered")
else:
     print("Wrong password")
     print("Access denied")        

