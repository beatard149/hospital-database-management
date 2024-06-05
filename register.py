import mysqlconnector

def registeration():

    print("""

                   =======================================
                   !!!!!!!!!!Register Yourself!!!!!!!!
                   =======================================
                                                       """)
    u = input("Input your username!!:")
    p = input("Input the password (Password must be strong!!!:")
    mysqlconnector.mycursor.execute(
        "insert into user_data values('" + u + "','" + p + "')")
    mysqlconnector.mysql.commit()

    print("""
                   ============================================
                   !!Well Done!!Registration Done Successfully!!
                   ============================================
                                                       """)
    x = input("enter any key to continue:")

