from flask import Flask, redirect, render_template, request
from ctypes import *
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/compete", methods=["GET", "POST"])
def compete(msg=None):
    prob="Alice and Bob are discussing a secret project on messenger. Unfortunately, their classmate Eve is using his hacking skills to read the messages. Alice and Bob are aware of the same and they want to exchange encrypted messages. They both agree to a simple protocol of turning each character into its ASCII equivalent. Given a message S, help Alice and Bob encrypt it."
    inp="The first line contains an integer T denoting the number of test cases. Following T lines contains a string S denoting the unencrypted message."
    constraint = ["1 <= T <= 100", "1 <= |S| <= 10^6"]
    op = "For each test case, print a single line containing the encrypted message."
    example = {}
    if request.method == 'POST':
        try:
            f = request.files['file']  
            f.save(f.filename) 
            ans = solve(f.filename) 
            msg = "Successfully Uploaded"+str(f.filename) if ans != -1 else "Incompatible File Uploaded."
            os.remove(f.filename)
        except:
            msg = "File Not Found"
    return render_template("compete.html", msg=msg, prob=prob, inp=inp, constraint=constraint, op=op)

def py_solve():
    pass

def c_solve(file_name):

    os.system('cmd /c "cc -fPIC -shared -o'+file_name[:-2]+".so"+file_name+"\"")
    so_file = os.getcwd() + '\\'+file_name
    print(so_file)
    test = CDLL(so_file)

    print(type(test))
    print(test.main())


 

def cpp_solve():
    pass

def java_solve():
    pass

def solve(f_name, result=None):
    ext = f_name.split(".")[-1]
    if ext == "py":
        result = py_solve(f_name)
    elif ext == "c":
        result = c_solve(f_name)
    elif ext == "cpp":
        result = cpp_solve(f_name)
    elif ext == "java":
        result = java_solve(f_name)
    else:
        return -1
    
    return result

@app.route("/indi")
def one_v_one():
    return "Comming Soon..."

@app.route("/prac_l")
def practice():
    return "Comming Soon..."



app.run(debug=True)