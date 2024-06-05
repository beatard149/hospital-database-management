import mysqlconnector
def show_hosp():
    mysqlconnector.mycursor.execute(
        "select * from hospital")
    row = mysqlconnector.mycursor.fetchall()
    for i in row:
        v = list(i)
        k = ["hname", "hid", "contact",
             "email", "hpincode", "hstreet", "hcity", "hstate"]
        d = dict(zip(k, v))
        print(d)
def insert_hosp():
    hname = input("Enter hospital name:")
    hid = input("Enter hospital id")
    contact = input("Enter hospital contact no.")
    email = input("Enter hospital email address")
    hpincode = input("Enter hospital pincode")
    hstreet = input("Enter hospital street")
    hcity = input("Enter hospital city")
    hstate = input("Enter hospital state")

    # INSERTING VALUES ENTERED TO THE TABLE
    mysqlconnector.mycursor.execute(
        "insert into hospital values('" + hname + "','" + hid + "','" + contact + "','" + email + "','" + hpincode
        + "','" + hstreet + "','" + hcity + "','" + hstate + "')")
    mysqlconnector.mysql.commit()
    print("SUCCESSFULLY ADDED")
def del_hosp():
    hname = input("Enter hospital Name:")
    mysqlconnector.mycursor.execute(
        "select * from hospital where hname='" + hname + "'")
    row = mysqlconnector.mycursor.fetchall()
    print(row)
    p = input(
        "you really wanna delete this data? (y/n):")
    if p == "y":
        mysqlconnector.mycursor.execute(
            "delete from hospital where hname='" + hname + "'")
        mysqlconnector.mysql.commit()
        print("SUCCESSFULLY DELETED!!")
    else:
        print("NOT DELETED")
