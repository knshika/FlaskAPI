from flask import Flask , request

app = Flask(__name__)

users = [ 
    {'name':'Knshii'},{'name':'knshika'},{'name':'kk'}
]


@app.route("/")
def hello_world():
    return ''' 
    <form action="/" method="post">
    <label for="fname">First name:</label><br>
    <input type="text" id="fname" name="fname" value="John"><br>
    <label for="lname">Last name:</label><br>
    <input type="text" id="lname" name="lname" value="Doe"><br><br>
    <input type="submit" value="Submit">
    </form> 
     '''
@app.route("/user/<int:userid>" , methods=["GET","POST"])
def user_route(userid):
    if request.method=='GET':
        try:
            return users[userid]
        except:
            return "user not found"
    else:
        try:
            users.append({"name":"new user"})
            return str(len(users)-1)
        except:
            return "user can not be added"

    #return f"user route {userid}"
#int typecast

if __name__ == "__main__":
    app.run(debug=True)