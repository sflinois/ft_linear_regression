import sys
import pandas as pd

def estimatePrice(theta0, theta1, mileage) :
	return theta0 + (theta1 * mileage)

def getMileage():
	while (1):
		try:
			mileage = int(input("Please enter a mileage: "))
			if (mileage >= 0) :
				return mileage
			print('That is not a valid mileage. Try again...')
		except ValueError:
			print('That is not a valid mileage. Try again...')
		except:
			exit('Wrong user input. exiting the program...')

def main() :
	mileage = getMileage()
	theta = pd.read_csv('theta.csv')
	estimatedPrice = estimatePrice(theta.theta0[0], theta.theta1[0], mileage)
	if (estimatedPrice > 0 and mileage < 1000000) :
		print("The estimated price for a car that has a mileage of {}km is {}$".format(mileage, round(estimatedPrice)))
	else :
		print("The car mileage is too high, it is not worth anything anymore !")


if __name__ == "__main__":
	main()
