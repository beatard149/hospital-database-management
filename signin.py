import mysqlconnector


def sign():
    print("""
                       ==================================
                       !!!!!!!!  {{Sign In}}  !!!!!!!!!!
                       ==================================
                                                           """)
    un = input("Enter Username!!:")
    global ps
    ps= input("Enter Password!!:")

    mysqlconnector.mycursor.execute(
        "select password from user_data where username='" + un + "'")
    global row
    row= mysqlconnector.mycursor.fetchall()
