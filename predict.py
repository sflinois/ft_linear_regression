import sys

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

if __name__ == "__main__":
	main()
