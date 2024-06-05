from flask import Flask,render_template,request,flash
import mysqlconnector
app=Flask(__name__)

@app.route('/')
def miniproj():
    return render_template('miniproject.html')


@app.route('/login',methods=['GET','POST'])
def login():
    un =str(request.form.get('uname'))
    ps = str(request.form.get('password'))
    try:
        mysqlconnector.mycursor.execute(
            "select password from user_data where username='" + un + "'")
    except:
        pass

    return render_template('login.html')




@app.route('/register',methods=['GET','POST'])
def sign_up():
    u=str(request.form.get('email'))
    p=str(request.form.get('psw'))
    password_r=request.form.get('psw-repeat')

    try:
        if (u == 'None' and p == 'None'):
            pass
        else:
                mysqlconnector.mycursor.execute(
                    "insert into user_data values('" + u + "','" + p + "')")
                mysqlconnector.mysql.commit()
    except:
        pass

    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/administration')
def admin():
    return render_template('administration.html')

@app.route('/display')
def disp():
    return render_template('display.html')

@app.route('/displayhos')
def disp_hos():
    return render_template('displayhos.html')

@app.route('/displaypat')
def disp_pat():
    return render_template('displaypat.html')

@app.route('/displaydoct')
def disp_doc():
    return render_template('displaydoct.html')

@app.route('/register1')
def regist():
    return render_template('register1.html')

@app.route('/registerd')
def regisdoc():
    return render_template('registerd.html')

@app.route('/registerh')
def regishos():
    return render_template('registerh.html')

@app.route('/registerp')
def regispat():
    return render_template('registerp.html')
@app.route('/delete')
def dele():
    return render_template('delete.html'
    )

@app.route('/patient')
def patient():
    return render_template('patient.html')

@app.route('/appointment')
def appoint():
    return render_template('appointment.html')

@app.route('/signout')
def signout():
    return render_template('signout.html')
