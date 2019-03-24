
def ebob(a,b):
	while b:
		a,b=b,a%b
		#tmp_a=a		
		#a=b
		#b=tmp_a%b
	return a

def ekok(a,b):
	return a*b/ebob(a,b)

print("Ebob :",ebob(30,40))
print("Ekok :",ekok(30,40))
