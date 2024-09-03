from flask import Flask, render_template, request
import requests

app = Flask(__name__,static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    Partner1 = request.form.get('Partner1')
    Partner2 = request.form.get('Partner2')
    print(f"Received Partner1: {Partner1}, Partner2: {Partner2}")
    
    if Partner1 and Partner2:
        try:
            url = "https://love-calculator.p.rapidapi.com/getPercentage"
            querystring = {"sname": Partner2, "fname": Partner1}
            headers = {
                "X-RapidAPI-Key": "609ff95119msh90ecea48090e436p134872jsnc241186878dd",
                "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
            }
            
            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()  
            
            percentage = data.get('percentage')
            result = data.get('result')
            
            return render_template('result.html', percentage=percentage, result=result)
        except ValueError:
            return "Invalid Input"
    return "Error: Missing Partner1 or Partner2 Name"

if __name__=='__main__':
    app.run(debug=True)       
