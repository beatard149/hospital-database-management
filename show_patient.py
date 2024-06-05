import mysqlconnector
def show_patient_details():
    import mysqlconnector

    mysqlconnector.mycursor.execute(
        "select * from patient")

    row = mysqlconnector.mycursor.fetchall()
    for i in row:
        b = 0
        v = list(i)
        k = ["pid", "pname", "sex",
             "age", "phone_no", "email", "street", "city", "state", "pincode"]
        d = dict(zip(k, v))
        print(d)
def add_patient():
    pid = input("Enter the patient id ")
    pname = input("Enter the patient name ")
    sex = input("Enter gender ")
    age = input("Enter age ")
    phone_no = input("Enter the phone_no of patient ")
    email = input("Enter email of patient ")
    street = input("Enter the street")
    city = input("Enter the city")
    state = input("Enter the state")
    pincode = input("Enter the pincode")

    mysqlconnector.mycursor.execute("insert into patient values('" + pid + "','" + pname + "','" +
                                    sex + "','" + age + "','" + phone_no + "','" + email + "','" + street + "','" + city + "','" + state + "','" + pincode + "')")
    mysqlconnector.mysql.commit()
    mysqlconnector.mycursor.execute(
        "select * from patient")
    for i in mysqlconnector.mycursor:
        v = list(i)
        k = ["pid", "pname", "sex",
             "age", "phone_no", "email", "street", "city", "state", "pincode"]
        print(dict(zip(k, v)))
        print("""
                                               ====================================
                                               !!!!!!!Registered Successfully!!!!!!
                                               ====================================

                                                     """)


def show_records():
    pname = input("Enter the Patient Name:")
    mysqlconnector.mycursor.execute(
        "select * from patient where pname='" + pname + "'")
    row = mysqlconnector.mycursor.fetchall()
    print(row)
    bill = input(
        "Has he paid all the bills? (y/n):")
    if bill == "y":
        mysqlconnector.mycursor.execute(
            "delete from patient where pname='" + pname + "'")
        mysqlconnector.mysql.commit()
