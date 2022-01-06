'''
Byron De Loor
'''

import requests
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

'''
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///weather.db'

db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
'''
def get_weather_data(ciudad):
    url=f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&units=metric&appid=8874533926928e550b8fef2e274a83f3"
    r = requests.get(url.format(ciudad)).json()
    return r

@app.route('/' , methods=['GET','POST'])
def index():
    weather={
            'ciudad':'',
            'temperatura':'',
            'descripcion': '',
            'icon': '',
            'humedad':'',
            'viento':'',
            'icono':''
        }
    err_msg=''
    if request.method=='POST':
        print("yes")
        consulta=request.form.to_dict()
        print(consulta['ciudad'])

        r=get_weather_data(consulta['ciudad'])
        print(r['cod'])

        if r['cod'] == 200:
            weather={
                'ciudad':r['name'],
                'temperatura': r['main']['temp'],
                'descripcion': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
                'humedad':r['main']['humidity'],
                'viento':r['wind']['speed'],
                'icono':r['weather'][0]['icon']
            }
            err_msg="si"
        else:
            err_msg='La ciudad no existe'


    return render_template('weather.html',weather=weather,err_msg=err_msg)

