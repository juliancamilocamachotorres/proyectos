def numeroDinero(numero)->float:
	return f"${numero:,.2f}"

def rendimientos(interesea:float,valorinicial:float,dias:int)->int:
	interesdiario=(1+interesea)**(1/365)-1
	total=valorinicial
	dia=1
	while dia <= dias:
		total+=total*interesdiario
		print("Dia: "+str(dia)+" total: "+ numeroDinero(total))
		dia+=1
		
	return total
	

if __name__ == "__main__":
	porcentaje = float(input("Dime el interes efectivo anual: "))
	dinero = float(input("Dime la cantidad de dinero: "))
	dias = int(input("Dime dime el tiempo en dias que va estar: "))
	rendimientos(porcentaje,dinero,dias)