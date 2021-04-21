import config

def insert(con,cursor):
    #read values to be inserted
    st = input("Titlu cartii: ")
    sa = input("Anul lansarii: ")
    sauth = input("Numele autorului: ")
    #create the Insert query
    sql = "INSERT INTO carte (titlu, anul_lansarii ,autor) VALUES (%s, %s, %s)"
    #create list of values typed from user to insert in customer table
    val = (st, sa, sauth)

    try:
        #Execute query with values
        cursor.execute(sql, val)
        #commit for permanent storage in database
        con.commit()
        #display success message
        print(cursor.rowcount, "Record inserted.")
    except:
        Exception
        print('Error: Insert')

def insert_spam(con,cursor):
    mult = 1000
    while mult != 10000:
        mult +=1
        st = f"Carte{mult}"
        sa = 2000 + mult
        sauth = f"Autor{mult}"
        sql = "INSERT INTO carte (titlu, anul_lansarii ,autor) VALUES (%s, %s, %s)"
        val = (st, sa, sauth)
        try:
            #Execute query with values
            cursor.execute(sql, val)
            #commit for permanent storage in database
            con.commit()
            #display success message
            print(cursor.rowcount, "Record inserted.")
        except:
            Exception
            print('Error: Insert')

def update(con,cursor):
    #read values to be updated
    sid=input("ID pentru care dorim sa facem modificari: ")
    st=input("Titlu: ")
    sa=input("Anul lansarii: ")
    sauth=input("Autor: ")
    #create update query
    sql = "UPDATE carte SET titlu='"+st+"', anul_lansarii='"+sa+"', autor='"+sauth+"' WHERE id='"+sid+"' "
    #Execute Update query on opened cursor
    cursor.execute(sql)
    #commit Changes to DB   
    con.commit()
    #display success message
    print(F"{cursor.rowcount} Record updated.")

def display(cursor):
    #Execute SELECT statement 
    cursor.execute("SELECT * FROM carte")
    #Fetch all records from table
    res = cursor.fetchall()
    #print
    print("--------------------------------")
    print("ID   Titlu  Anul Lansarii  Autor")
    print("--------------------------------")
          
    for x in res:
        print("--------------------------------")
        print(f"{str(x['id'])} {str(x['titlu'])} {str(x['anul_lansarii'])} {str(x['autor'])}")
    print("--------------------------------")
    print("")


def delete(con,cursor):
    sid=input("Enter  ID :")
    sql = "delete FROM carte where ID = '"+sid+"'"
    cursor.execute(sql)
    con.commit()
    print(cursor.rowcount, "Record deleted.")

def main():

    con = config.connect()
   
   
    cursor = con.cursor(dictionary=True)
    ch=0
    
    while(ch<=4):
        #menu options
        print("1. INSERT")
        print("2. UPDATE")
        print("3. DELETE")
        print("4. DISPLAY")
        print("5. EXIT")
        # ask user to enter what he wants to do
        ch=int(input("Ce doriti sa faceti? Introduceti cifra dorita: "))
        #call relevant functions defined above
        if (ch==1):
            insert(con, cursor)
        if (ch==2):
            update(con, cursor)
        if (ch==3):
            delete(con, cursor)
        if  (ch==4):
            display(cursor)

main()