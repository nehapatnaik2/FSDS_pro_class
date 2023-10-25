from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
# you have to create html file using css/front end people will do that for creating form like structure
# our finction will take the input from the form validate and return
# write a code so that the user/client can see the form.
# render template in Flask is used to showcase your html file.
@app.route('/') #show in the homepage
def show_form():
    return render_template('index.html')

#we are trying to get the information from client after they submit the form
# This is post or after they have made the query. Hence post query method.
@app.route('/check_password',methods = ['POST']) 
def check_password():
    name = request.form.get('username')
    password = request.form.get('password')
    print({name},{password})
    return "username and password received"

    

if __name__ == '__main__':
    app.run(host = '0.0.0.0')    