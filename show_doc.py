
import mysqlconnector

def show_doctor():
    mysqlconnector.mycursor.execute(
        "select * from doctor")
    row = mysqlconnector.mycursor.fetchall()
    for i in row:
        b = 0
        v = list(i)
        k = ["doctor_id", "dname", "specialization", "phone_no"]
        d = dict(zip(k, v))
        print(d)
def insert_doc():
    doctor_id = input("Enter the doctor id")
    dname = input("Enter the doctor's name")
    specialization = input("Enter the specilization:")
    phone_no = input("Enter Contact Details:")

    # Inserting values in doctors details
    mysqlconnector.mycursor.execute("insert into doctor values('" + doctor_id + "','" + dname +
                                    "','" + specialization + "','" + phone_no + "')")
    mysqlconnector.mysql.commit()
    print("SUCCESSFULLY ADDED")
def del_doc():
    dname = input("Enter Doctor's Name:")
    mysqlconnector.mycursor.execute(
        "select * from doctor where dname='" + dname + "'")
    row = mysqlconnector.mycursor.fetchall()
    print(row)
    p = input(
        "you really wanna delete this data? (y/n):")
    if p == "y":
        mysqlconnector.mycursor.execute(
            "delete from doctor where name='" + dname + "'")
        mysqlconnector.mysql.commit()
        print("SUCCESSFULLY DELETED!!")
    else:
        print("NOT DELETED")

