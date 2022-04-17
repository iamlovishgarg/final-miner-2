from flask import Flask, render_template, request, redirect
import os
import re

app = Flask(__name__)

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  

def email_checker(email):

    if(re.search(regex, email)):
        with open("data.csv", "a") as f:
            f.write(f"{email},\n")
        return "valid"

@app.route("/", methods=['GET', 'POST'])
def landing_page():
    if request.method=='POST':
        mail_status = email_checker(str(request.form.get("email")))
    
        if mail_status=="valid":
            return render_template("index.html", text = "Mail added!", status = "success")
        else:
            return render_template("index.html", text="Invalid email.", status = "danger")
    
    return render_template("index.html", text="", status = "")


app.run(debug=True)