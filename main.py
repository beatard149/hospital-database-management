import mysqlconnector
import register
import signin
import working
from flask import Flask,render_template,request,flash
app=Flask(__name__)

while (True):
    @app.route('/')
    def miniproj():
        return render_template('miniproject.html')


    mysqlconnector.mysql_connect()
    while (True):
        print("""
                        1. Sign In
                   -     2. Registration
                                                            """)

        r = int(input("enter your choice:"))
        if r == 2:
            register.registeration()


        # IF USER WANTS TO LOGIN
        elif r == 1:
            signin.sign()
            working.work()
