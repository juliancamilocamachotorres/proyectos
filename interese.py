def rendimientos(interesea:float,valorinicial:float,dias:int)->int:
	interesdiario=(1+interesea)(1/365)-1
	total=valorinicial
	dia=0
	while dia < dias:
		total+=total*interesdiario
		print(total)
		dia+=1
		
	return total
	
print(rendimientos(0.095,8000000,150))