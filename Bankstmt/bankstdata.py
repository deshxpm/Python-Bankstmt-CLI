import datetime
import PyPDF2

class Bank:
	def __init__(self, name, account_number):
		self.name = name
		self.account_number = account_number
class Bankst(Bank):		
	def __init__(self, name, account_number, IFSC, MICR):
		Bank.__init__(self, name, account_number)
		self.IFSC = IFSC
		self.MICR = MICR
	def bankdetails(self):
		print('Bank Account Statement :\n'+self.name+'\n'+str(self.account_number)+'\n'+self.IFSC+'\n'+str(self.MICR))

Bs = Bankst("Deepak",11544578444,'SBIN0001111',123456789)
#print(Bs.Name) 
Bs.bankdetails()		