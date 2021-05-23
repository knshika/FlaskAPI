from flask import Flask , request

app = Flask(__name__)
users = [ 
    {'name':'Knshii'},{'name':'knshika'},{'name':'kk'}
]


@app.route("/",methods=["POST"])
def hello_world():
    return "Hello, World!"


@app.route("/users",methods=["POST",])
def add_user():
    name=request.args.get('key', '')
    users.append({"name":name})    
    return f' user added at {str(len(users)-1)}'   

@app.route('/users/<int:user_id>',methods=["GET","POST","DELETE","PATCH"])
def user_data(user_id):
        try:
            if request.method=="GET":
                return f'user id {users[user_id]}'

            elif request.method=="PATCH":
                name=request.args.get('name', '')
                users[user_id]={"name":name}
                return "user updated"

            elif request.method=="DELETE":
                users.pop(user_id)
                return "user data deleted"
        except:
            return 'user not found'




if __name__=="__main__":
    app.run(debug=True)