from flask import Flask,request,render_template, jsonify
app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template('index.html')

@app.route('/math', methods = ['POST'])
def check_input():
    ops = request.form.get('operation')
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')

    if ops == 'add':
        r= int(num1)+int(num2)
        return f"addition of {num1} and {num2} is {r}"
    elif ops == 'subtract':
        r = int(num1)-int(num2)
        return f"subtraction of {num1} and {num2} is {r}"
    elif ops == 'multiply':
        r = int(num1)*int(num2)
        return f"multiplication of {num1} and {num2} is {r}" 
    elif ops == 'divide':
        r = int(num1)/int(num2)
        return f"division of {num1} and {num2} is {r}"

 # launch the app :
if __name__ == '__main__':
    app.run(host ='0.0.0.0')             
#we are hosting a computer at a global leve where every one can access

