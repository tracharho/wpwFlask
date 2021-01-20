from flask import Flask, render_template, request, redirect
import smtplib

app = Flask(__name__) #turn this file into a web application

students = []

@app.route("/") #listen to get requests on slash
def index():
    #name = request.args.get("name", "Brian") #read documentation
    return render_template("index1.html") 


# @app.route("/register", methods=["POST"])
# def register():
#     name = request.form.get("name")
#     dorm = request.form.get("dorm")
#     if not name or not dorm:
#         return "failure" #returns failure if 
#     return render_template("success.html")

@app.route("/registrants")
def registrants():
    return render_template("registered.html", students=students)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")
    if not name or not dorm:
        return render_template("failure.html") #returns failure if 
    students.append("{} from {}".format(name, dorm))
    message = "You are registered!"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("trchrh@gmail.com", "") #password goes in second argument
    server.sendmail("trchrh@gmail.com", email, message)
    return redirect("/registrants")

"""Remember to go to terminal and do
$ export FLASK_APP=application
$ flask run
to start the webserver"""

#Use serverside to check for logic and prevent malicious use. 
#Javascript can be disabled from the 