from flask import Markup
from query import queryAQI, queryHC, queryTemp, queryUV

x = []
y = []

#UVI functions
	
def IndexUV():
	resultUVI = queryUV()
	if resultUVI < 2.9:
		currentStateUVI = 'Low'
		return currentStateUVI
	elif 2.9 > resultUVI and resultUVI <= 5.9:
		currentStateUVI = 'Moderate'
		return currentStateUVI
	elif 6 > resultUVI and resultUVI <= 7.9:
		currentStateUVI = 'High'
		return currentStateUVI
	elif 8 > resultUVI and resultUVI <= 10.9:
		currentStateUVI = 'Very-High'
		return currentStateUVI
	else:
		currentStateUVI = 'Extreme'
		return currentStateUVI
		
def noMediaUV():
	resultUVI = queryUV()
	if resultUVI < 2.9:
		noMedia = '12'
		return noMedia
	elif 2.9 > resultUVI and resultUVI <= 5.9:
		noMedia = '13'
		return noMedia
	elif 6 > resultUVI and resultUVI <= 7.9:
		noMedia = '14'
		return noMedia
	elif 8 > resultUVI and resultUVI <= 10.9:
		noMedia = '15'
		return noMedia
	else:
		noMedia = '16'
		return noMedia

def tipsUVI():
	currentStateUVI = queryUV()
	if currentStateUVI == 'Low':
		from tips import GR
		tipUVI = GR()
		return tipUVI
	elif currentStateUVI == 'Moderate':
		from tips import YE
		tipUVI = YE()
		return tipUVI
	elif currentStateUVI == 'High':
		from tips import OR
		tipUVI = OR()
		return tipUVI
	elif currentStateUVI == 'Very-High':
		from tips import RE
		tipUVI = RE()
		return tipUVI
	else:
		from tips import VI
		tipUVI = VI()
		return tipUVI
		
###AQI functions
def IndexAirQuality():
	resultAQI = queryAQI()
	if resultAQI < 50:
		currentStateAQI = 'Good'
		return currentStateAQI
	elif 51 > resultAQI and resultAQI <= 100:
		currentStateAQI = 'Moderate'
		return currentStateAQI
	elif 101 > resultAQI and resultAQI <= 150:
		currentStateAQI = 'Unhealthy-for-Sensitive-Groups'
		return currentStateAQI
	elif 151 > resultAQI and resultAQI <= 200:
		currentStateAQI = 'Unhealthy'
		return currentStateAQI
	elif 201 > resultAQI and resultAQI <= 300:
		currentStateAQI = 'Very-Unhealthy'
		return currentStateAQI
	else:
		currentStateAQI = 'Hazardous'
		return currentStateAQI

def tipsAQI():
	currentStateAQI = IndexAirQuality()
	if currentStateAQI == 'Good':
		from tips import G
		tipAQI = G()
		return tipAQI
	elif currentStateAQI == 'Moderate':
		from tips import M
		tipAQI = M()
		return tipAQI
	elif currentStateAQI == 'Unhealthy-for-Sensitive-Groups':
		from tips import U1
		tipAQI = U1()
		return tipAQI
	elif currentStateAQI == 'Unhealthy':
		from tips import U2
		tipAQI = U2()
		return tipAQI
	elif currentStateAQI == 'Very-Unhealthy':
		from tips import V
		tipAQI = V()
		return tipAQI
	else:
		from tips import H
		tipAQI = H()
		return tipAQI

#### Heat Index functions

def calcC():
	tempCurrentRaw = queryTemp()
	tempCurrentC = tempCurrentRaw - 273.15
	return tempCurrentC
	
def calcF():
	tempCurrentRaw = queryTemp()
	tempCurrentF = (tempCurrentRaw * 1.8) - 459.67
	return tempCurrentF

def humCurrent():
	humCurrent = queryHC()
	return humCurrent

def calcHeatIndex():
	tempCurrentF = calcF()
	humCurrent = queryHC()
	indexHeat = -42.379 + 2.0401523 * tempCurrentF + 10.14333127 * humCurrent - .22475541 * tempCurrentF * humCurrent - .00683783 * tempCurrentF * tempCurrentF - .05481717 * humCurrent * humCurrent + .00122874 * tempCurrentF * tempCurrentF * humCurrent + .00085282 * tempCurrentF * humCurrent * humCurrent - .00000199 * humCurrent * humCurrent * tempCurrentF * tempCurrentF
	if humCurrent < 13 and 80 < tempCurrentF < 112:
		ADJUSTMENT = - (( 13 - humCurrent ) / 4 ) * sqrt((17 - abs(tempCurrentF - 95)))
	elif humCurrent > 85 and 80 < tempCurrentF < 87:
		ADJUSTMENT = ((( humCurrent - 85)/ 10) * ((87 - tempCurrentF)/5))
	else:
		ADJUSTMENT = 0
	#convert to str to avoid iterable float error
	indexHeatCurrent = (indexHeat + ADJUSTMENT) #change numbers here to create a simulation of recommendation changes.
	return indexHeatCurrent

def indexHeatStateColor():
	indexHeatCurrent = calcHeatIndex()
	if indexHeatCurrent <= 80:
		indexHeatState = 'Safe'
		return indexHeatState
		
	elif 80 < indexHeatCurrent <= 90:
		indexHeatState = 'Yellow'
		return indexHeatState

	elif 90 < indexHeatCurrent <= 103:
		indexHeatState = 'L_Orange'
		return indexHeatState

	elif 103 < indexHeatCurrent <= 124:
		indexHeatState = 'D_Orange'
		return indexHeatState

	else:
		indexHeatState = 'Red'
		return indexHeatState
		
def noMediaHeat():
	indexHeatCurrent = calcHeatIndex()
	if indexHeatCurrent <= 80:
		noMedia = '1'
		return noMedia
		
	elif 80 < indexHeatCurrent <= 90:
		noMedia = '2'
		return noMedia

	elif 90 < indexHeatCurrent <= 103:
		noMedia = '3'
		return noMedia

	elif 103 < indexHeatCurrent <= 124:
		noMedia = '4'
		return noMedia

	else:
		noMedia = '5'
		return noMedia

def tipsHI():
	indexHeatCurrent = calcHeatIndex()
	if indexHeatCurrent <= 80:
		indexHeatState = 'Safe'
		from tips import S
		tipHI = S()
		return tipHI
		
	elif 80 < indexHeatCurrent <= 90:
		indexHeatState = 'Yellow'
		from tips import Y
		tipHI = Y()
		return tipHI

	elif 90 < indexHeatCurrent <= 103:
		indexHeatState = 'L_Orange'
		from tips import L
		tipHI = L()
		return tipHI

	elif 103 < indexHeatCurrent <= 124:
		indexHeatState = 'D_Orange'
		from tips import D
		tipHI = D()
		return tipHI

	else:
		indexHeatState = 'Red'
		from tips import R
		tipHI = R()
		return tipHI

def dirHI():
	indexHeatCurrent = calcHeatIndex()
	x.append(float(indexHeatCurrent))
	print(str(x) + '2')
	if len(x) == 2:
		heatIndexDirection = x[1] - x.pop(0)
		print(str(x) + '3')
		if heatIndexDirection < 0:
			direction = 'It is cooling.'
			return direction
		elif heatIndexDirection == 0:
			direction = ''
			return direction
		else:
			direction = 'It is warming.'
			return direction
	else:
		direction = ''
		return direction

def dirArrow():
	indexHeatCurrent = calcHeatIndex()
	x.append(float(indexHeatCurrent))
	print(str(x) + '2')
	if len(x) == 2:
		heatIndexDirection = x[1] - x.pop(0)
		print(str(x) + '3')
		if heatIndexDirection < 0:
			arrowHI = Markup("<img src='../static/arrowDOWN.svg'>")
			return arrowHI
		elif heatIndexDirection == 0:
			arrowHI = Markup("<img src='../static/arrowDOWN.svg'>")
			return arrowHI
		else:
			arrowHI = Markup("<img src='../static/arrowUP.svg'>")
			return arrowHI
	else:
		arrowHI = ''
		return arrowHI

def arrowAQ():
	resultAQI = queryAQI()
	y.append(float(resultAQI))
	if len(y) == 2:
		AQIndexDirection = y[1] - y.pop(0)
		if AQIndexDirection < 0:
			arrowAQI = Markup("<img src='../static/arrowDOWN.svg'>")
			return arrowAQI
		elif AQIndexDirection == 0:
			arrowAQI = Markup("<img src='../static/arrowDOWN.svg'>")
			return arrowAQI
		else:
			arrowAQI = Markup("<img src='../static/arrowUP.svg'>")
			return arrowAQI
	else:
		arrowAQI = ''
		return arrowAQI

def colorUV():
	resultUVI = queryUV()
	if resultUVI < 2.9:
		colorUVI = 'Green'
		return colorUVI
	elif 2.9 < resultUVI <= 5.9:
		colorUVI = 'Yellow'
		return colorUVI
	elif 6 <resultUVI <= 7.9:
		colorUVI = 'Orange'
		return colorUVI
	elif 8 < resultUVI <= 10.9:
		colorUVI = 'Red'
		return colorUVI
	else:
		colorUVI = 'Violet'
		return colorUVI
		
				
def colorIndexAir():
	resultAQI = queryAQI()
	if resultAQI < 50:
		colorAQI = 'Green'
		return colorAQI
	elif 51 < resultAQI <= 100:
		colorAQI = 'Yellow'
		return colorAQI
	elif 101 < resultAQI <= 150:
		colorAQI = 'Orange'
		return colorAQI
	elif 151 < resultAQI <= 200:
		colorAQI = 'Red'
		return colorAQI
	elif 201 < resultAQI <= 300:
		colorAQI = 'Violet'
		return colorAQI
	else:
		colorAQI = 'Black'
		return colorAQI
		
def noMediaAQI():
	resultAQI = queryAQI()
	if resultAQI < 50:
		noMedia = 6
		return noMedia
	elif 51 < resultAQI <= 100:
		noMedia = 7
		return noMedia
	elif 101 < resultAQI <= 150:
		noMedia = 8
		return noMedia
	elif 151 < resultAQI <= 200:
		noMedia = 9
		return noMedia
	elif 201 < resultAQI <= 300:
		noMedia = 10
		return noMedia
	else:
		noMedia = 11
		return noMedia
		
def colorIndexHeat():
	indexHeatCurrent = calcHeatIndex()
	if indexHeatCurrent <= 80:
		colorHI = 'Green'
		return colorHI
		
	elif 80 < indexHeatCurrent <= 90:
		colorHI = 'Yellow'
		return colorHI

	elif 90 < indexHeatCurrent <= 103:
		colorHI = 'L_Orange'
		return colorHI

	elif 103 < indexHeatCurrent <= 124:
		colorHI = 'D_Orange'
		return colorHI

	else:
		colorHI = 'Red'
		return colorHI

#print(arrowAQ())
#print(calcHeatIndex())
#print(calcC())
#print(calcF())
#print(humCurrent())
#print(tipsAQI())
#print(tipsHI())
#print(dirHI())
