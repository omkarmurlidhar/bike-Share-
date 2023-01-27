from flask import Flask,request,render_template
import pickle
app=Flask(__name__,template_folder='Template')
filename="model4.pkl"
fileobj=open(filename,'rb')
b= pickle.load(fileobj)
@app.route('/')
def main():
    return render_template('pico.html')

@app.route('/end')
def alankar():
    return render_template('form_bike.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        day=int(request.form['day'])
        mnth=int(request.form['mnth'])
        year=int(request.form['year'])
        season=int(request.form['season'])
        holiday=int(request.form['holiday'])
        weekday=int(request.form['weekday'])
        workingday=int(request.form['workingday'])
        weathersit=int(request.form['weathersit'])
        temp=float(request.form['temp'])
        hum=float(request.form['hum'])
        windspeed=float(request.form['windspeed'])  

        prediction=b.predict([[day,mnth,year,season,holiday,weekday,workingday,weathersit,temp,hum,windspeed]])
        
        return render_template("form_bike.html",prediction_text="Total Rent on that day is {} ".format(int(prediction)))

    else:
        return render_template('form_bike.html')

if __name__=='__main__':
    app.run(debug=True)