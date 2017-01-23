import os
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
			'winder.settings')

import django
django.setup()
from reactor.models import Bobbin

def populate():

	with open("bobbins.csv") as csvfile:
	        reader = csv.reader(csvfile)
		for row in reader:

			b = Bobbin(size=row[0],
				us_name = row[1],
				section_type = row[2],
				terminals = row[3],
				measure_A=getFoat(row[4]),
				measure_B=getFoat(row[5]),
				measure_C=getFoat(row[6]),
				measure_D=getFoat(row[7]),
				measure_E=getFoat(row[8]),
				measure_F=getFoat(row[9]),
				measure_G=getFoat(row[10]),
				measure_H=getFoat(row[11]),
				measure_J=getFoat(row[12]),
				measure_K=getFoat(row[13]),
				measure_L=getFoat(row[14]),
				measure_M=getFoat(row[15]),
				measure_N=getFoat(row[16]),
				measure_P=getFoat(row[17]),
				core_material = row[18],
				frame_va = getFoat(row[19]),
				mp_part_number = row[20])

			b.save(force_insert=True)	

def getFoat(float_num):
	
	num = 0.0	

	try:
		num = float(float_num)
	except ValueError:
		num = 0.0
	return num


if __name__ == '__main__':
	populate()
