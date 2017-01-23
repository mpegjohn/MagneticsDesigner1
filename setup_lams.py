import os
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
			'winder.settings')

import django
django.setup()
from reactor.models import Lamination

def populate():

	with open("lam.csv") as csvfile:
	        reader = csv.reader(csvfile)
		first_row = 1
		for row in reader:

			if first_row == 1:
				first_row = 0
				continue

			l = Lamination(lam_size=row[0],
				measure_A=getFoat(row[1]),
				measure_B=getFoat(row[2]),
				measure_C=getFoat(row[3]),
				measure_D=getFoat(row[4]),
				measure_E=getFoat(row[5]),
				measure_F=getFoat(row[6]),
				measure_G=getFoat(row[7]),
				path_length=getFoat(row[8]),
				window_area=getFoat(row[9]))

			l.save(force_insert=True)	

def getFoat(float_num):
	
	num = 0.0	

	try:
		num = float(float_num)
	except ValueError:
		num = 0.0
	return num


if __name__ == '__main__':
	populate()
