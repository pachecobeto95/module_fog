class Module(object):
	def __init__ (self, postvars):
		self.postvars = postvars
		for line in self.postvars['load']:
        		self.tmp = line.split('\n')

	def delete_data(self):
		delete_list = []
		for i in range(len(self.tmp)):
			if (self.tmp[i][0:-1] == 0):
				delete_list.append(i)
		for i in reversed(delete_list):
			del self.tmp[i]

	def media_measure(self, measure):
		contador = 0
		print "oi mundao"
		for line in self.postvars['header']:
                	vect = line.split(",")
                	for var in vect:
				if ( var == measure):
                                	for line in tmp:
                                        	vect_tmp = line.split(",")
                                        	nr_measure = nr_measure + float(vect_tmp[contador])
                        	contador = contador + 1
        	media_nr_measure = nr_measure / len(tmp)
        	return media_nr_measure

