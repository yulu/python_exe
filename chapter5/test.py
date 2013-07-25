
def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return time_string

	(mins, secs) = time_string.split(splitter)
	return(mins + '.' + secs)

def read_data(file_name):
	try:
		with open(file_name, 'r') as file_data:
			line_data = file_data.readline()
			data = line_data.strip().split(',')
		return data

	except IOError as ioerr:
		print('File error:' + str(ioerr))
		return(None)



sarah = read_data('sarah2.txt')