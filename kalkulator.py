import  time, math, os

clear = lambda: os.system('cls')

def kalkulator():
	clear()
	wybor = input("Co chcesz zrobić? Wpisz odpowiadającą liczbę i potwierdź klawiszek Enter.\n1. Dodać\n2. Odjąć\n3. Pomnożyć.\n4. Podzielić\n5. Spotęgować.\n6. Spierwiastkować.\n7. Obliczyć pola i obwody.\n0. Wyjść.\n")
	if "1" in wybor:
		clear()
		dodawanie()
	elif "2" in wybor:
		clear()
		odejmowanie()
	elif "3" in wybor:
		clear()
		mnozenie()
	elif "4" in wybor:
		clear()
		dzielenie()
	elif "5" in wybor:
		clear()
		potega()
	elif "6" in wybor:
		clear()
		pierwiastek()
	elif "7" in wybor:
		clear()
		wybor = input("Co chcesz zrobić? Wpisz odpowiadającą liczbę i potwierdź klawiszek Enter.\n1. Obliczyć pole i obwód prostokąta.\n2. Obliczyć pole i obwód koła.\n3. Obliczyć pole i obwód trójkąta.\n")
		if "1" in wybor:
			clear()
			pole1()
		elif "2" in wybor:
			clear()
			pole2()
		elif "3" in wybor:
			clear()
			pole3()
	elif "0" in wybor:
		clear()
		print("Dziękujemy za skorzystanie z naszego kalkulatora.")
		time.sleep(5)
		quit()

def powtorka():
	wybor = input("Czy chcesz dokonać kolejnej operacji? T/n:\n")
	if "n" in wybor:
		clear()
		print("Dziękujemy za skorzystanie z naszego kalkulatora.")
		time.sleep(5)
		quit()
	else: kalkulator()

def dodawanie():
	pierwsza=input("Podaj pierwszą liczbę: ")
	druga=input("Podaj drugą liczbę: ")

	wynik = float(pierwsza) + float(druga)
	print("Wynik dodawania %s oraz %s równa się %s." %(pierwsza,druga,wynik))
	powtorka()

def odejmowanie():
	pierwsza=input("Podaj pierwszą liczbę: ")
	druga=input("Podaj drugą liczbę: ")

	wynik = float(pierwsza) - float(druga)
	print("Wynik odejmowania %s oraz %s równa się %s." %(pierwsza,druga,wynik))
	powtorka()

def mnozenie():
	pierwsza=input("Podaj pierwszą liczbę: ")
	druga=input("Podaj drugą liczbę: ")

	wynik = float(pierwsza) * float(druga)
	print("Wynik mnożenia %s razy %s równa się %s." %(pierwsza,druga,wynik))
	powtorka()

def dzielenie():
	pierwsza=input("Podaj pierwszą liczbę: ")
	druga=input("Podaj drugą liczbę(różną od zera): ")
	while float(druga) == 0:
		druga=input("Nie można dzielić przez 0. Podaj inną liczbę: ")
	wynik = float(pierwsza) / float(druga)
	print("Wynik dzielenia %s przez %s równa się %s." %(pierwsza,druga,wynik))
	powtorka()

def potega():
	pierwsza=input("Podaj podstawę potęgi: ")
	druga=input("Podaj wykładnik potęgi: ")
	
	wynik = float(pierwsza) ** float(druga)
	print("%s do potęgi %s to %s." %(pierwsza,druga,wynik))
	powtorka()

def pierwiastek():
	pierwsza=input("Podaj pierwiastkowaną liczbę(nieujemną): ")
	while float(pierwsza)<0:
		pierwsza=input("Nie można pierwiastkować liczb ujemnych. Podaj inną liczbę: ")
	druga=input("Podaj stopień pierwiastka: ")
	
	wynik = float(pierwsza) ** (1/float(druga))
	print("Pierwiastek z %s stopnia %s równa się %s." %(pierwsza,druga,wynik))
	powtorka()

def pole1():

	for i in range(6):
		if i == 0:
			print("	a")
		elif i == 3:
			print("*"*20,"b")
		else:print("*"*20)
	pierwsza=input("Podaj pierwszy bok prostokąta (a): ")
	while float(pierwsza)<=0:
		pierwsza=input("Długość boku musi być większa od 0. Podaj inną liczbę: ")
	druga=input("Podaj drugi bok prostokąta (b): ")
	while float(druga)<=0:
		druga=input("Długość boku musi być większa od 0. Podaj inną liczbę: ")

	wynik = float(pierwsza) * float(druga)
	print("Pole prostokąta o bokach równych %s oraz %s wynosi %s." %(pierwsza,druga,wynik))
	wynik = 2*float(pierwsza)+ 2* float(druga)
	print("Obwód prostokąta o bokach równych %s oraz %s wynosi %s." %(pierwsza,druga,wynik))
	powtorka()
	
def pole2():
	pi= 3.14159
	spacje=3
	for i in range(1,5):
		print("   "*spacje,"**"*3*i)
		spacje-=1
	print(13*"**")
	print(6*"**","------r------")
	print(13*"**")

	spacje=0
	for i in range(1,5):
		print("   "*spacje,"**"*(15-i*3))
		spacje+=1

	pierwsza=input("Podaj promień koła (r): ")
	while float(pierwsza)<=0:
		pierwsza=input("Długość promienia musi być większa od 0. Podaj inną liczbę: ")
	

	wynik = pi*float(pierwsza)**2
	print("Pole koła o promieniu %s wynosi %s." %(pierwsza,wynik))
	wynik = 2*pi*float(pierwsza)
	print("Obwód koła o promieniu %s wynosi %s." %(pierwsza,wynik))
	powtorka()

def pole3():
	trojkat=input("Jakie wymiary znasz? Wpisz odpowiadającą liczbę i potwierdź klawiszek Enter\n1. Podstawę i wysokość.\n2. Trzy boki.\n3. Dwa boki i kąt pomiędzy nimi.\n")
	if "1" in trojkat:
		print(" "*9+"h")
		spacje=6
		for i in range(1,7):
			print(" "*spacje,"*"*i,"h","*"*i)
			spacje-=1
		print(" "+"*"*18)
		print(" "*6,"a")

		pierwsza=input("Podaj wysokość trójkąta (h): ")
		while float(pierwsza)<=0:
			pierwsza=input("Długość musi być większa od 0. Podaj inną liczbę: ")
		druga=input("Podaj podstawę trójkąta (a): ")
		while float(druga)<=0:
			druga=input("Długość musi być większa od 0. Podaj inną liczbę: ")
		wynik = float(pierwsza)*float(druga)/2
		print("Pole trójkąta o wysokości %s i podstawie %s wynosi %s." %(pierwsza,druga,wynik))
		powtorka()

	elif "2" in trojkat:
		spacje=6
		print(" "*spacje," *")
		for i in range(1,7):
			if i == 3:
				print(" ","a  "+"*"*9+"  b")
				spacje-=1
			else:
				print(" "*spacje,"***"*i)
				spacje-=1
		print(" "*7,"c")

		pierwsza=input("Podaj pierwszy bok trójkąta (a): ")
		while float(pierwsza)<=0 :
			pierwsza=input("Długość musi być większa od 0. Podaj inną liczbę: ")
		druga=input("Podaj drugi bok trójkąta (b): ")
		while float(druga)<=0:
			druga=input("Długość musi być większa od 0. Podaj inną liczbę: ")
		trzecia=input("Podaj trzeci bok trójkąta (c): ")
		while float(trzecia)<=0:
			trzecia=input("Długość musi być większa od 0. Podaj inną liczbę: ")
		p=(float(pierwsza)+float(druga)+float(trzecia))/2
		wynik = (p*(p-float(pierwsza))*(p-float(druga))*(p-float(trzecia)))**(1/2)
		print("Pole trójkąta o bokach %s, %s, oraz %s wynosi %s." %(pierwsza,druga,trzecia,wynik))
		wynik = float(pierwsza)+float(druga)+float(trzecia)
		print("Obwód trójkąta o bokach %s, %s, oraz %s wynosi %s." %(pierwsza,druga,trzecia,wynik))
		powtorka()

	elif "3" in trojkat:
		spacje=6
		print(" "*spacje," *")
		for i in range(1,7):
			if i == 3:
				print(" ","a  "+"*"*9)
				spacje-=1
			elif i == 5:
				print(" "*spacje,"***alfa","***"*2)
				spacje-=1
			else:
				print(" "*spacje,"***"*i)
				spacje-=1
		print(" "*7,"b")

		pierwsza=input("Podaj pierwszy bok trójkąta (a): ")
		while float(pierwsza)<=0:
			pierwsza=input("Długość musi być większa od 0. Podaj inną liczbę: ")
		druga=input("Podaj drugi bok trójkąta (b): ")
		while float(druga)<=0:
			druga=input("Długość musi być większa od 0. Podaj inną liczbę: ")
		trzecia=input("Podaj kąt pomiędzy bokami (alfa): ")
		while float(trzecia)<=0:
			trzecia=input("Kąt musi być większy od 0. Podaj inną liczbę: ")
		
		wynik = float(pierwsza)*float(druga)*math.sin(float(trzecia))/2
		print("Pole trójkąta o bokach %s, %s, oraz %s wynosi %s." %(pierwsza,druga,trzecia,wynik))
		powtorka()

	else: pole3()


while True:
	kalkulator()