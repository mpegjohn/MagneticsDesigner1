import os
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
			'winder.settings')

import django
django.setup()
from reactor.models import Wire

def populate():

	with open("/home/john/python/tests/metric_wire.csv") as csvfile:
	        reader = csv.reader(csvfile)
		first_row = 1
		for row in reader:

			if first_row == 1:
				first_row = 0
				continue

			standard_csv = 'n'
			if (row[0] =='NS'):
				standard_csv = 'y'

			w = Wire(area=getFoat(row[3]),
				standard=standard_csv,
				diameter=getFoat(row[1]),
				tolerance=getFoat(row[2]),
				ohms_per_m_min=getFoat(row[5]),
				ohms_per_m_rated=getFoat(row[6]),
				ohms_per_m_max=getFoat(row[7]),
				mass=getFoat(row[4]),
				grade_1_dia_min=getFoat(row[8]),
				grade_1_dia_max=getFoat(row[9]),
				grade_2_dia_min=getFoat(row[10]),
				grade_2_dia_max=float(row[11]))
			w.save(force_insert=True)	

def getFoat(float_num):
	
	num = 0.0	

	try:
		num = float(float_num)
	except ValueError:
		num = 0.0
	return num


if __name__ == '__main__':
	populate()
