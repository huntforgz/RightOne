def getgender(ch):
	GENDER = { 'F' : 'Female' , 'M': "Male"}
	try:
		return GENDER[ch]
	except:
		return "Not Sure"

def geteducation(n):
	EDUCATION = {0:'currently  primary school pupil',1:'primary school',2: 'secondary school',3: 'college/bachelor degree',4:'masters degree',5:'doctorate degree'}
	try:
		return EDUCATION[n]
	except:
		return "Not Sure"


def getlocation(ch):
	LOCATION = {"AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California","CO":"Colorado","CT":"Connecticut","DE":"Delaware","FL":"Florida","GA":"Georgia","HI":"Hawaii","ID":"Idaho","IL":"Illinois","IN":"Indiana","IA":"Iowa","KS":"Kansas","KY":"Kentucky","LA":"Louisiana","ME":"Maine","MD":"Maryland","MA":"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New hampshire","NJ":"New jersey","NM":"New mexico","NY":"New York","NC":"North Carolina","ND":"North Dakota","OH":"Ohio","OK":"Oklahoma","OR":"Oregon","PA":"Pennsylvania","RI":"Rhode island","SC":"South carolina","SD":"South dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia","WA":"Washington","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming"	}
	try:
		return LOCATION[ch]
	except:
		return "Not Sure"

def getonlychild(ch):
	if ch==0:
		return "No"
	elif ch==1:
		return "Yes"
	else:
		return "Not Sure"




