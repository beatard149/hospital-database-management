import mysql.connector

passwd = str(input("Enter the Password Please!!:"))

mysql = mysql.connector.connect(
    host="localhost", user="root", passwd=passwd)
mycursor = mysql.cursor()
def mysql_connect():

    mycursor.execute("create database if not exists city_hospital")
    mycursor.execute("use city_hospital")
    # creating the tables we need
    mycursor.execute(
        "create table if not exists patient_detail(pid varchar(10) primary key,pname varchar(30) not null unique key,sex varchar(15),age int(3))")
    mycursor.execute(
        "create table if not exists patient_detail1(pname varchar(30) not null ,phone_no integer(12),email varchar(20),foreign key (pname) references patient_detail(pname))")
    mycursor.execute(
        "create table if not exists patient_addr(pincode integer(6) primary key,street varchar(10),city varchar(10),state varchar(6))")
    mycursor.execute(
        "create table if not exists patient_addrs(pid varchar(10),pincode integer(6),foreign key(pid) references patient_detail(pid), foreign key(pincode) references patient_addr(pincode))")
    mycursor.execute(
        "create table if not exists patient_rec(pid varchar(10) ,records varchar(10),allergies varchar(10),insuarance boolean,foreign key (pid) references patient_detail(pid))")
    mycursor.execute(
        "create table if not exists patient(pid varchar(10) primary key,pname varchar(30),sex varchar(15) ,age int(3),phone_no int(12),email varchar(20),street varchar(10),city varchar(10),state varchar(6),pincode int(6))"
    )
    mycursor.execute(
        "create table if not exists doctor_details(doctor_id varchar(10) primary key,dname varchar(20) unique key,specialization varchar(20)  )")
    mycursor.execute(
        "create table if not exists doctor_details1(dname varchar(30) ,phone_no integer(12),foreign key(dname) references doctor_details(dname))")
    mycursor.execute(
        "create table if not exists doctor(doctor_id varchar(10) primary key,dname varchar(20),specialization varchar(20),phone_no integer(12) )")
    mycursor.execute(
        "create table if not exists hospital_details(hid varchar(20) primary key,hname varchar(20)  unique key)")
    mycursor.execute(
        "create table if not exists hospital_detail(hname varchar(30) not null,contact varchar(15),email varchar(20),foreign key(hname) references hospital_details(hname))")
    mycursor.execute(
        "create table if not exists hospital_addr(hpincode integer(6) primary key,hstreet varchar(10),hcity varchar(10),hstate varchar(6))")
    mycursor.execute(
        "create table if not exists hospital_addrs(hid varchar(10),hpincode integer(6),foreign key(hid) references hospital_details(hid), foreign key(hpincode) references hospital_addr(hpincode))")
    mycursor.execute(
        "create table if not exists hospital(hname varchar(30), hid varchar(10) primary key, contact varchar(15), email varchar(20), hpincode integer(6), hstreet varchar(10), hcity varchar(10), hstate varchar(6))")
    mycursor.execute(
        "create table if not exists appointments(doctor_id varchar(10) not null,pid varchar(10) not null,appointment_date date,appointment_time time , foreign key(doctor_id) references doctor_details(doctor_id), foreign key(pid) references patient_detail(pid))")
    # creating table for storing the username and password of the user
    mycursor.execute(
        "create table if not exists user_data(username varchar(30) primary key,password varchar(30) default'000')")

mysql_connect()
