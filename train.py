import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def standardize(x):
	return x / 1000.

def destandardize(x):
	return x * 1000.

def estimatePrice(theta0, theta1, mileage) :
	return theta0 + (theta1 * mileage)

def gradientDescent (km, price, iter) :
	theta0 = 0.
	theta1 = 0.
	learning_rate = 0.00015

	m = len(km)

	for i in range(0, iter) :
		sum_t0 = 0.
		sum_t1 = 0.
		for j in range(0, m) :
			sum_t0 += estimatePrice(theta0, theta1, km[j]) - price[j]
			sum_t1 += (estimatePrice(theta0, theta1, km[j]) - price[j]) * km[j]
		tmp_theta0 = sum_t0 / float(m)
		tmp_theta1 = sum_t1 / float(m)
		theta0 -= learning_rate * tmp_theta0
		theta1 -= learning_rate * tmp_theta1
	return(theta0 * 1000, theta1)

def dataVis(data, theta0, theta1) :
	min_km = min(data.km)
	max_km = max(data.km)
	plt.plot(data.km, data.price, 'o', color='black')
	plt.ylabel("Price")
	plt.xlabel("Km")
	plt.plot([min_km, max_km], [estimatePrice(theta0, theta1, min_km), estimatePrice(theta0, theta1, max_km)], 'k-')
	plt.show()

def main() :
	data = pd.read_csv('data.csv')
	std_km = standardize(data.km)
	std_price = standardize(data.price)
	print(std_km)
	print(std_price)
	theta0, theta1 = gradientDescent(std_km, std_price, 100000)
	print(theta0, theta1)
	dataVis(data, theta0, theta1)

if __name__ == "__main__":
	main()
