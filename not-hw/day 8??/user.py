class User:
	def __init__(self, fn = '', ln = '', e = '', un = '', pw = ""):
		self.fn = fn
		self.ln = ln
		self.e = e
		self.un = un
		self.pw = pw
	def __repr__(self):
		print("User {}: First Name: {} Last Name: {}".format(self.un, self.fn, self.ln))
	def save_db(self):
	    with open('users.csv', 'w+') as file:
            csv_writer = csv.writer(file, delimiter = ',')
            csv_writer.writerow([self.fn, self.ln, self.e, self.un, self.pw])