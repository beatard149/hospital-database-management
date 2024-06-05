import signin
import show_doc
import show_patient
import show_hospital
import mysqlconnector
def work():
    for i in signin.row:
        a = list(i)
        if a[0] == str(signin.ps):
            while (True):
                print("""
                                   1.Administration
                                   2.Patient(Details)
                                   3.Sign Out

                                                               """)

                a = int(input("ENTER YOUR CHOICE:"))
                if a == 1:
                    print("""
                                       1. Display the details
                                       2. Add a new member
                                       3. Delete a member
                                       4. Make an exit
                                                                """)
                    b = int(input("Enter your Choice:"))
                    # details
                    if b == 1:
                        print("""
                                           1. Doctors Details
                                           2. Hospital details
                                           3. Others
                                                            """)

                        c = int(input("Enter your Choice:"))
                        if c == 1:

                            show_doc.show_doctor()
                        # displays hospital details
                        elif c == 2:
                            show_hospital.show_hosp()
                        # displays worker details
                        elif c == 3:
                            show_patient.show_patient_details()
                    # IF USER WANTS TO ENTER DETAILS
                    elif b == 2:
                        print("""

                                           1. Doctor Details
                                           2. Hospital Details
                                           3. Others
                                                                                       """)
                        c = int(input("ENTER YOUR CHOICE:"))
                        # enter doctor details
                        if c == 1:
                            # ASKING THE DETAILS
                            show_doc.insert_doc()
                        # for nurse details
                        elif c == 2:
                            # ASKING THE DETAILS
                            show_hospital.insert_hosp()
                        # for entering workers details
                        elif c == 3:
                           show_patient.add_patient()
                    # to delete data
                    elif b == 3:
                        print("""
                                           1. Doctor Details
                                           2. Hospital Details
                                           3. Others
                                                                                       """)
                        c = int(input("Enter your Choice:"))
                        # deleting doctor's details
                        if c == 1:
                            show_doc.del_doc()
                        # deleting nurse details
                        elif c == 2:
                            show_hospital.del_hosp()
                        # deleting other_workers details
                        elif c == 3:
                            name = input("Enter the worker Name")
                            mysqlconnector.mycursor.execute(
                                "select * from workers_details where name='" + name + "'")
                            row = mysqlconnector.mycursor.fetchall()
                            print(row)
                            p = input(
                                "you really wanna delete this data? (y/n):")
                            if p == "y":
                                mysqlconnector.mycursor.execute(
                                    "delete from other_workers_details where name='" + name + "'")
                                mysqlconnector.mysql.commit()
                                print("SUCCESSFULLY DELETED!!")
                            else:
                                print("NOT DELETED")
                    elif b == 4:
                        break

                # entering the patient details table
                elif a == 2:

                    print("""
                                           1. Show Patients Info
                                           2. Add New Patient
                                           3. records
                                           4. Exit
                                                                  """)
                    b = int(input("Enter your Choice:"))
                    # showing the existing details
                    # if user wants to see the details of PATIENT
                    if b == 1:
                        show_patient.show_patient_details()


                    # adding new patient
                    elif b == 2:
                        show_patient.add_patient()
                    # dischare process
                    elif b == 3:
                        show_patient.show_records()
                    # if user wants to exit
                    elif b == 4:
                        break
                # SIGN OUT

                elif a == 3:
                    break

        # IF THE USERNAME AND PASSWORD IS NOT IN THE DATABASE
        else:
            break
