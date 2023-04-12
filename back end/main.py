from flask import Flask, json,redirect,render_template,flash,request
from flask.globals import request,session
from flask_sqlalchemy import SQLAlchemy
from flask.helpers import url_for
from flask_login import login_manager,LoginManager,UserMixin,login_required,logout_user,login_user,current_user
from werkzeug.security import generate_password_hash,check_password_hash
import json

# my database connection
local_server=True
app=Flask(__name__)
app.secret_key='jayasria'

# this is fro getting the unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://username:password@localhost/databsename"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/college"
db=SQLAlchemy(app)

# with open('Config.json', 'r') as c:
#     par = json.load(c)["par"]
    
    
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    srfid=db.Column(db.String(20),unique=True)
    email=db.Column(db.String(50))
    dob=db.Column(db.String(10))
    
class studentuser(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    ccode=db.Column(db.String(20))
    email=db.Column(db.String(50))
    password=db.Column(db.String(1000))
    
class student(UserMixin,db.Model):
    ccode=db.Column(db.String(20))
    id=db.Column(db.Integer,primary_key=True)
    fname=db.Column(db.String(100))
    lname=db.Column(db.String(100))
    sem=db.Column(db.String(10))
    email=db.Column(db.String(50))
    phno=db.Column(db.String(12))
    gender=db.Column(db.String(10))
    branch=db.Column(db.String(100))
    aadharno=db.Column(db.String(12))
    
class Trig(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    HRid=db.Column(db.Integer,unique=True)
    ccode=db.Column(db.String(20))
    email=db.Column(db.String(50))
    phno=db.Column(db.String(12))
    gender=db.Column(db.String(10))
    branch=db.Column(db.String(100))
    aadharno=db.Column(db.String(12))
    querys=db.Column(db.String(50))
    date=db.Column(db.String(50))   
    
# class staff(UserMixin,db.Model):
#     ccode=db.Column(db.String(20))
#     id=db.Column(db.Integer,primary_key=True)
#     fname=db.Column(db.String(100))
#     lname=db.Column(db.String(100))
#     email=db.Column(db.String(50))
#     phno=db.Column(db.String(12))
#     gender=db.Column(db.String(10))
#     branch=db.Column(db.String(100))
#     aadharno=db.Column(db.String(12))
    
class healthrecords(db.Model):
    id=db.Column(db.Integer,unique=True)
    HRid=db.Column(db.Integer,primary_key=True)
    Covidvac=db.Column(db.String(50))
    Doses=db.Column(db.String(10))
    Medications=db.Column(db.String(100))
    Reg_Checkup=db.Column(db.String(100))
    
    
@app.route('/')
def home():
    return  render_template("index.html")

@app.route('/usersignup')
def usersignup():
    return  render_template("usersignup.html")

@app.route('/userlogin')
def userlogin():
    return  render_template("userlogin.html")

@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method=="POST":
        srfid=request.form.get('srf')
        email=request.form.get('email')
        dob=request.form.get('dob')
        # print(srfid,email,dob)
        encpassword=generate_password_hash(dob)
        user=User.query.filter_by(srfid=srfid).first()
        emailUser=User.query.filter_by(email=email).first()
        if user or emailUser:
            flash("Email or srif is already taken","warning")
            return render_template("usersignup.html")
        new_user=db.engine.execute(f"INSERT INTO `user` (`srfid`,`email`,`dob`) VALUES ('{srfid}','{email}','{encpassword}') ")
                
        flash("SignUp Success Please Login","success")
        return render_template("userlogin.html")

    return render_template("usersignup.html")

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=="POST":
        srfid=request.form.get('srf')
        dob=request.form.get('dob')
        user=User.query.filter_by(srfid=srfid).first()
        if user and check_password_hash(user.dob,dob):
            login_user(user)
            flash("Login Success","info")
            return render_template("index.html")
        else:
            flash("Invalid Credentials","danger")
            return render_template("userlogin.html")


    return render_template("userlogin.html")

@app.route('/addStuUser',methods=['POST','GET'])
def studentUser():
   if('user' in session and session['user']=="admin"):
        if request.method=="POST":
            ccode=request.form.get('ccode')
            email=request.form.get('email')
            password=request.form.get('password')        
            encpassword=generate_password_hash(password)  
            ccode=ccode.upper()      
            emailUser=studentuser.query.filter_by(email=email).first()
            if  emailUser:
                flash("Email or srif is already taken","warning")
         
            db.engine.execute(f"INSERT INTO `studentuser` (`ccode`,`email`,`password`) VALUES ('{ccode}','{email}','{encpassword}') ")

            # my mail starts from here if you not need to send mail comment the below line
           
            # mail.send_message('COVID CARE CENTER',sender=params['gmail-user'],recipients=[email],body=f"Welcome thanks for choosing us\nYour Login Credentials Are:\n Email Address: {email}\nPassword: {password}\n\nHospital Code {hcode}\n\n Do not share your password\n\n\nThank You..." )

            flash("Data Sent and Inserted Successfully","warning")
            return render_template("addStuUser.html")
        else:
            flash("Login and try Again","warning")
            return render_template("addStuUser.html")

@app.route('/addstudentinfo',methods=['POST','GET'])
def addstudentinfo():
    if request.method=="POST":
            ccode=request.form.get('ccode')
            id=request.form.get('id')
            fname=request.form.get('fname')
            lname=request.form.get('sname')
            sem=request.form.get('sem')
            email=request.form.get('email')
            phno=request.form.get('phno')
            gender=request.form.get('gender')
            branch=request.form.get('branch')
            email=request.form.get('email')
            aadharno=request.form.get('aadharno')
            # suser=studentuser.query.filter_by(ccode=ccode).first()
            # sduser=student.query.filter_by(ccode=ccode).first()
            # # print(ccode,id,fname,lname,sem,email,phno,gender,branch,aadharno)
            # if sduser:
            #     flash("Data is already present you can update it...","primary")
            #     return render_template("student.html")
            # if suser:
            db.engine.execute(f"INSERT INTO `student` (`ccode`,`id`,`fname`,`lname`,`sem`,`email`,`phno`,`gender`,`branch`,`aadharno`) VALUES ('{ccode}',{id},{fname}','{lname}','{sem}','{email}','{phno}','{gender}','{branch}','{aadharno}')")
            flash("Data is Added","info")
            return redirect('/addstudentinfo')
            # else:
            #     flash("Student data does not exist","warning")
            #     return redirect('/addstudentinfo')
    return render_template("student.html")

@app.route("/sdetails")
def studentdetails():
    query=db.engine.execute(f"SELECT * FROM `student`") 
    return render_template('sdetails.html',query=query)
    
  
# @app.route("/hedit/<string:id>",methods=['POST','GET'])
# @login_required
# def hedit(id):
#     posts=addstudentinfo.query.filter_by(id=id).first()
  
#     if request.method=="POST":
#             ccode=request.form.get('ccode')
#             id=request.form.get('id')
#             fname=request.form.get('fname')
#             lname=request.form.get('sname')
#             sem=request.form.get('sem')
#             email=request.form.get('email')
#             phno=request.form.get('phno')
#             gender=request.form.get('gender')
#             branch=request.form.get('branch')
#             email=request.form.get('email')
#             aadharno=request.form.get('aadharno')
#             db.engine.execute(f"UPDATE `student` SET `ccode` ='{ccode}',`fname`='{fname}',`lname`='{lname}',`sem`='{sem}',`email`='{email}',`phno`='{phno}',`gender`='{gender}',`branch`='{branch}',`aadharno='{aadharno}' WHERE `addstudentinfo`.`id`={id}")
#             flash("Slot Updated","info")
#             return redirect("/addstudentinfo")
#     return render_template("hedit.html",posts=posts)

# def updatess(code):
    
#     postsdata=student.query.filter_by(ccode=code).first()
#     return render_template("student.html",postsdata=postsdata)

# @app.route("/hdelete/<string:id>",methods=['POST','GET'])
# @login_required
# def hdelete(id):
#     db.engine.execute(f"DELETE FROM `student` WHERE `addstudentinfo`.`id`={id}")
#     flash("Date Deleted","danger")
#     return redirect("/addstudentinfo")


@app.route("/sdetails",methods=['GET'])
@login_required
def sdetails():
    code=current_user.id
    print(code)
    data=healthrecords.query.filter_by(HRid=code).first()
    return render_template("details.html",data=data)

@app.route('/admin',methods=['POST','GET'])
def admin():
    if request.method=="POST":
        username=request.form.get('username')
        password=request.form.get('password')
        if(username=="Jayasri" and password=="Jay4502"):
            session['user']=username
            flash("login success","info")
            return render_template("addColUser.html")
        else:
            flash("Invalid Credentials","danger")

    return render_template("admin.html")

@app.route('/studentlogin',methods=['POST','GET'])
def studentlogin():
    if request.method=="POST":
        ccode=request.form.get('ccode')
        password=request.form.get('password')
        user=studentuser.query.filter_by(ccode=ccode).first()
        if user and check_password_hash(user.password,password):
            login_user(user)
            flash("Login Success","info")
            return render_template("index.html")
        else:
            flash("Invalid Credentials","danger")
            return render_template("studentlogin.html")


    return render_template("studentlogin.html")

@app.route("/triggers")
def triggers():
    query=Trig.query.all() 
    return render_template("triggers.html",query=query)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout SuccessFul","warning")
    return redirect(url_for('login'))

# testing whether db is connected or not
@app.route('/test')
def Test():
    try:
        a=Test.query.all()
        print(a)
        return f"My database is connected {a.name}"
    except Exception as e:
        print(e)
        return f"My database is not connected {e}"

app.run(debug=True)
