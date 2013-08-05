def santize():
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return time_string
	(mins, secs) = time_string.split(splitter)
	return(mins + '.' + secs)

#self-defined class
class Athlete:
	def __init__(self, a_name, a_dob=None, a_times=[]):
		self.name = a_name
		self.dob = a_dob
		self.times = a_times

	def top3(self):
		return sorted(set([sanitize(t) for t in self.times]))[0:3]

	def add_time(self, new_time):
		self.times.append(new_time)

	def add_times(self, new_times=[]):
		self.times.extend(new_times)

#inherate class
class AthleteList(list):
	def __init__(self, a_name, a_dob=None, a_times=[]):
		list.__init__([])
		self.name = a_name
		self.dob = a_dob
		self.extend(a_times)
	def top3(self):
		return(sorted(set([sanitize(t) for t in self]))[0:3])

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
		temp1 = line_data.strip().split(',')
		"""return ({'Name' : temp1.pop(0),
				 'DOB' 	: temp1.pop(0),
				 'Times'	: str(sorted(set([sanitize(t) for t in temp1]))[0:3])})"""
		Sarah = AthleteList(temp1.pop(0), temp1.pop(0), temp1)
		return Sarah

	except IOError as ioerr:
		print('File error:' + str(ioerr))
		return(None)


sarah = read_data('sarah2.txt')

print(sarah.name + "'s times are: " + str(sarah))

sarah.append('3:33')
sarah.extend(['4:44','5:55'])
print(sarah.name + "'s new times are: " + str(sarah))
