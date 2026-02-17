from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/armstrong/<int:num>")
def armstrong(num):
    n = num
    power = len(str(num))
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** power
        n //= 10

    if total == num:
        print("Armstrong Number")
        result ={
            "Number":num,
            "Armstrong":True,
            "Server IP":"172.168.0.1",
            "Numbers":[123,21,334,24]
        } 
    else:
        print("Not an Armstrong Number")
        result ={
            "Number":num,
            "Armstrong":False,
            "Server IP":"172.168.0.1",
            "Numbers":[123,21,334,24]
        } 
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
