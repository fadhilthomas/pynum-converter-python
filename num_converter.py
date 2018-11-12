#!/usr/bin/python

def convert(input, iin, out):
	if iin == '4':
		temp = int(input)
	else:
		if iin == '1':
			iin = 2
		elif iin == '2':
			iin = 8
		elif iin == '3':
			iin = 16
		temp = int(input,iin)
	
	if out == '1':
		temp = bin(temp)
		temp = temp[2:]
	elif out == '2':
		temp = oct(temp)
	elif out == '3':
		temp = hex(temp)
		temp = temp[2:]
		
	return str(temp)

def banner(i):
	if i == '1':
		out = "Biner"
	elif i == '2':
		out = "Octal"
	elif i == '3':
		out = "Hexadesimal"
	elif i == '4':
		out = "Desimal"	
	return out	

def main():
	try:
		print """
 _   _                  _____                          _            
| \ | |                / ____|                        | |           
|  \| |_   _ _ __ ___ | |     ___  _ ____   _____ _ __| |_ ___ _ __ 
| . ` | | | | '_ ` _ \| |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
| |\  | |_| | | | | | | |___| (_) | | | \ V /  __/ |  | ||  __/ |   
|_| \_|\__,_|_| |_| |_|\_____\___/|_| |_|\_/ \___|_|   \__\___|_|   
																 
Oleh: Muhammad Thomas Fadhila Yahya

::::::::::::::::::::::::Input::::::::::::::::::::::::::
"""
		print "1. Bilangan Biner (Contoh: 1100100)"
		print "2. Bilangan Octal (Contoh: 144)"
		print "3. Bilangan Hexadesimal (Contoh: 3e8)"
		print "4. Bilangan Desimal (Contoh: 10000)"
		pilihan_input = raw_input("Masukkan pilihan input: ")
		
		print ""
		
		bilangan_input = raw_input("Masukkan bilangan input: ")
		print ""
		print "1. Bilangan Biner"
		print "2. Bilangan Octal"
		print "3. Bilangan Hexadesimal"
		print "4. Bilangan Desimal"
		
		pilihan_konversi = raw_input("Masukkan pilihan konversi: ")
		
		hasil = bilangan_input + " (" + banner(pilihan_input)+ ") => "
		
		if pilihan_input == pilihan_konversi:
			hasil += bilangan_input
		else:
			hasil += convert(bilangan_input, pilihan_input, pilihan_konversi)

		hasil += " (" + banner(pilihan_konversi) + ")"
		print ""
		print "::::::::::::::::::::::::Result::::::::::::::::::::::::::"
		print ""
		print banner(pilihan_input) + " => " + banner(pilihan_konversi)
		print hasil
		
	except:
		print ""
		print "::::::::::::::::::::::::Result::::::::::::::::::::::::::"
		print ""
		print "Input salah, periksa kembali inputan anda."

if __name__ == "__main__":
	main()