#def addition (x,y):
    #return x+y

#print(addition(2,3)) # you have print inside the console

# we will try to call this function from a URL/browser or form.
# we want  to execute this function from the different system using flask framework.

from flask import Flask, request

# by using app = Flask(__name__) we are wrapping our function that we want to calll from another system
app = Flask(__name__)
## to expose our function
@app.route('/add')
# calling this decorator we creating a set of rules that will make our addition function independent of language
def addition ():
    return f"This is my test function"

@app.route('/name')
def print_name():
    return f"sudh"

@app.route('/user')
def print_user():
    data = request.args.get('name') # passing the data as a quesry argument.
    return f'{data}'
#giving/passing a data to the function present in  the  server computer.
if __name__ == '__main__':
    app.run(host = "0.0.0.0")

# use this url - https://gray-engineer-wsyky.pwskills.app:5000/add
#https://gray-engineer-wsyky.pwskills.app:5000/user?name=Neha
#:5000/user?name=Sudh
#server is a computer/system we are tryingto hit. that is sudhanshu sir's server
# I am the client

#create form - UX people designs it

