import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(111)

def standardize(x):
	return x / 1000.

def destandardize(x):
	return x * 1000.

def estimatePrice(theta0, theta1, mileage) :
	return theta0 + (theta1 * mileage)

def gradientDescent (data, km, price, iter) :
	theta0 = 0.
	theta1 = 0.
	learning_rate0 = 0.01
	learning_rate1 = 0.00015

	m = len(km)

	for i in range(0, iter) :
		sum_t0 = 0.
		sum_t1 = 0.
		for j in range(0, m) :
			sum_t0 += estimatePrice(theta0, theta1, km[j]) - price[j]
			sum_t1 += (estimatePrice(theta0, theta1, km[j]) - price[j]) * km[j]
		tmp_theta0 = sum_t0 / float(m)
		tmp_theta1 = sum_t1 / float(m)
		theta0 -= learning_rate0 * tmp_theta0
		theta1 -= learning_rate1 * tmp_theta1
		if (i % 100 == 0) :
			dataVis(data, theta0 * 1000, theta1, False)
		if abs(tmp_theta0) < float(0.00001) and abs(tmp_theta1) < float(0.00001):
			return (theta0 * 1000, theta1)
	return(theta0 * 1000, theta1)

def dataVis(data, theta0, theta1, isDone) :
	min_km = min(data.km)
	max_km = max(data.km)
	ax.clear()
	ax.plot(data.km, data.price, 'o', color='black')
	ax.plot([min_km, max_km], [estimatePrice(theta0, theta1, min_km), estimatePrice(theta0, theta1, max_km)], 'k-', color='green' if isDone else 'black')
	plt.pause(0.001)

def exportTheta(theta0, theta1) :
	exportData = {'theta0' : [theta0], 'theta1' : [theta1]}
	df = pd.DataFrame (exportData, columns = ['theta0','theta1'])
	df.to_csv('theta.csv')

def main() :
	data = pd.read_csv('data.csv')
	std_km = standardize(data.km)
	std_price = standardize(data.price)
	dataVis(data, 0, 0, False)
	theta0, theta1 = gradientDescent(data, std_km, std_price, 100000)
	exportTheta(theta0, theta1)
	dataVis(data, theta0, theta1, True)
	plt.show()

if __name__ == "__main__":
	main()
