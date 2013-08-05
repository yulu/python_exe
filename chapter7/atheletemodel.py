import pickle
from athletelist import AthleteList

def get_coach_data(filename):
	try:
		with open(file_name, 'r') as file_data:
			line_data = file_data.readline()
		temp1 = line_data.strip().split(',')

		Sarah = AthleteList(temp1.pop(0), temp1.pop(0), temp1)
		return Sarah

	except IOError as ioerr:
		print('File error:' + str(ioerr))
		return(None)

def put_to_store(files_list):
	all_althletes = {}
	for each_file in files_list:
		ath = get_coach_data(each_file)
		all_athletes[ath.name] = ath
	try:
		with open('athletes.pickle', 'wb') as athf:
			pickle.dump(all_althletes, athf)
	except IOError as ioerr:
		print('File error (put_and_sotre):'+str(ioerr))

	return(all_althletes)

def get_from_store():
	all_althletes = {}
	try:
		with open('athletes.pickle', 'rb') as athf:
			all_althletes = pickle.load(athf)
	except IOError as ioerr:
		print('File error (get_from_store:'+str(ioerr))

	return(all_althletes)