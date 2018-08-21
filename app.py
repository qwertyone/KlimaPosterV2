# -*- coding: UTF-8 -*-
from datetime import datetime
from flask import Flask,render_template
import time
from twitter import tweetAQI, tweetHeat
from multiprocessing import Process, Value
from query import queryLoop, queryAQI, queryUV
from helper import IndexAirQuality, noMediaHeat, noMediaAQI, noMediaUV, queryAQI, tipsAQI, arrowAQ, tipsHI, calcC, dirArrow, dirHI, queryUV, colorIndexHeat,colorIndexAir, IndexUV, tipsUVI,indexHeatStateColor, colorUV

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	currentStateAQI = IndexAirQuality()
	resultAQI = queryAQI()
	tipAQI = tipsAQI()
	arrowAQI = arrowAQ()
	tweetAQI(currentStateAQI,resultAQI,tipAQI)
	tipHI = tipsHI()
	tempCurrentC = str(calcC())
	tempCurrentC = tempCurrentC[:2]
	arrowHI = dirArrow()
	direction = dirHI()
	resultUVI = queryUV()
	colorHI=colorIndexHeat()
	colorAQI=colorIndexAir()
	colorUVI=colorUV()
	currentStateUVI=IndexUV()
	tipUVI=tipsUVI()
	noMedia = noMediaHeat()
	indexHeatState = indexHeatStateColor()
	tweetHeat(indexHeatState, direction, tipHI)
	return render_template('index.html', noMedia=noMedia, colorUVI=colorUVI, colorHI=colorHI, colorAQI=colorAQI, resultUVI=resultUVI, currentStateUVI=currentStateUVI, direction=direction,resultAQI=resultAQI, indexHeatState=indexHeatState, tempCurrentC=tempCurrentC, currentStateAQI=currentStateAQI, tipAQI=tipAQI, tipHI=tipHI, arrowHI=arrowHI, arrowAQI=arrowAQI)

@app.route('/heat', methods=['GET'])
def heat():
	currentStateAQI = IndexAirQuality()
	resultAQI = queryAQI()
	arrowAQI = arrowAQ()
	tempCurrentC = str(calcC())
	tempCurrentC = tempCurrentC[:2]
	arrowHI = dirArrow()
	direction = dirHI()
	resultUVI = queryUV()
	colorHI=colorIndexHeat()
	colorAQI=colorIndexAir()
	colorUVI=colorUV()
	tipHI = tipsHI()
	currentStateUVI=IndexUV()
	noMedia = noMediaHeat()
	indexHeatState = indexHeatStateColor()
	tweetHeat(indexHeatState, direction, tipHI)
	return render_template('heat.html', noMedia=noMedia, colorUVI=colorUVI, colorHI=colorHI, colorAQI=colorAQI, resultUVI=resultUVI, currentStateUVI=currentStateUVI, direction=direction,resultAQI=resultAQI, indexHeatState=indexHeatState, tempCurrentC=tempCurrentC, currentStateAQI=currentStateAQI, tipHI=tipHI, arrowHI=arrowHI, arrowAQI=arrowAQI)

@app.route('/UV', methods=['GET'])

def UV():
	currentStateAQI = IndexAirQuality()
	resultAQI = queryAQI()
	arrowAQI = arrowAQ()
	tempCurrentC = str(calcC())
	tempCurrentC = tempCurrentC[:2]
	arrowHI = dirArrow()
	direction = dirHI()
	resultUVI = queryUV()
	colorHI=colorIndexHeat()
	colorAQI=colorIndexAir()
	colorUVI=colorUV()
	currentStateUVI=IndexUV()
	tipUVI=tipsUVI()
	noMedia = noMediaUV()
	indexHeatState = indexHeatStateColor()
	return render_template('UV.html', noMedia=noMedia, colorUVI=colorUVI, colorHI=colorHI, colorAQI=colorAQI, resultUVI=resultUVI, currentStateUVI=currentStateUVI, direction=direction,resultAQI=resultAQI, indexHeatState=indexHeatState, tempCurrentC=tempCurrentC, currentStateAQI=currentStateAQI, tipUVI=tipUVI, arrowHI=arrowHI, arrowAQI=arrowAQI)
@app.route('/AQI', methods=['GET'])
def AQI():
	currentStateAQI = IndexAirQuality()
	resultAQI = queryAQI()
	tipAQI = tipsAQI()
	arrowAQI = arrowAQ()
	tweetAQI(currentStateAQI,resultAQI,tipAQI)
	tempCurrentC = str(calcC())
	tempCurrentC = tempCurrentC[:2]
	arrowHI = dirArrow()
	direction = dirHI()
	resultUVI = queryUV()
	colorHI=colorIndexHeat()
	colorAQI=colorIndexAir()
	colorUVI=colorUV()
	currentStateUVI=IndexUV()
	noMedia = noMediaAQI()
	indexHeatState = indexHeatStateColor()
	return render_template('AQI.html', noMedia=noMedia, colorUVI=colorUVI, colorHI=colorHI, colorAQI=colorAQI, resultUVI=resultUVI, currentStateUVI=currentStateUVI, direction=direction,resultAQI=resultAQI, indexHeatState=indexHeatState, tempCurrentC=tempCurrentC, currentStateAQI=currentStateAQI, tipAQI=tipAQI, arrowHI=arrowHI, arrowAQI=arrowAQI)

@app.route('/posterClimate.html')
def poster():
	return render_template('posterClimate.html')

@app.route('/styles.css')
def css():
	return render_template('styles.css')

if __name__ == '__main__':
	recording_on = Value('b', True)
	p = Process(target = queryLoop, args = (recording_on,))
	p.start()
	app.run(host='0.0.0.0', port="5000", use_reloader = False)
	p.join()
