import sys 
import datetime
from tarif import t1, t2, t3

print('Enter your amount energy (KBt): ')
totalEnergy = int(input())
payment = 0.0

#Текущая дата
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	
def until100():
	sum = totalEnergy * t1
	return round(sum)

def from100to500():
	sumPay100 = totalEnergy - 100 
	sum = (sumPay100 * t2) + (100 * t1)
	return round(sum)

def extra500():
	sumPast500 = totalEnergy - 600 
	sum = (100 * t1) + (500 * t2) + (sumPast500 * t3)
	return round(sum)
	
#Сохраняем результат в файл
def saveResult():
	print('Payment: ' + str(payment) + ' UAH')
	f = open('save.txt', 'a')
	f.write('Date: ' + str(date) + '\n')
	f.write('Payment: ' + str(payment) + ' UAH' + '\n')
	f.write('KBt: ' + str(totalEnergy) + '\n' + '\n')

if totalEnergy <= 100:	
	payment = until100()
	saveResult()
elif totalEnergy >= 100 and totalEnergy < 500:
	payment = from100to500()
	saveResult()
else:
	payment = extra500()
	saveResult()

	

	
