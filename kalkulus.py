try:

	# usr/bin/python2
	import os,sys,time

	# pungsi
	def tambah(x,y):
		return x + y

	def kurang(x,y):
		return x - y

	def kali(x,y):
        	return x * y

	def bagi(x,y):
        	return x / y

	def sisa_bagi(x,y):
        	return x % y


	def pangkat(x,y):
        	return x ** y



	# membuat logo 
	logo = """
\033[1;32m
____________________________________________
_  _ _  _ ___  ____ ____     ___  ____ _  _
|_/  |  | |__] |__| |__/     |  \ |___ |  |
| \_ |__| |__] |  | |  \ ___ |__/ |___  \/
-------------------------------------------
\033[1;31m             Autor: M.Luqman.Arief\033[1;32m
\033[1;31m             Team : X-Garuda_Red\033[1;32m
___________________________________________
"""
	os.system("clear")
	print logo
	print "\n"

	# mulai hitung
	while True:
		try:
			angka1 = int(input("masukkan angka >> "))
			angka2 = int(input("masukkan angka >> "))
			# hasil
			print
			print angka1,"+",angka2,"=",tambah(angka1,angka2)
			print angka1,"-",angka2,"=",kurang(angka1,angka2)
			print angka1,"x",angka2,"=",kali(angka1,angka2)
			print angka1,":",angka2,"=",bagi(angka1,angka2)
			print angka1,"sisa_bagi",angka2,"=",sisa_bagi(angka1,angka2)
			print angka1,"pangkat",angka2,"=",pangkat(angka1,angka2)
			print


		except TypeError,e:
			print "[%s]" % (time.srtftime("%X")),"Error:",e
		except SyntaxError,e:
			print "[%s]" % (time.strftime("%X")),"Error:",e

		except ZeroDivisionError,e:
			print "[%s]" % (time.strftime("%X")),"Error:",e


		except NameError,e:
			print "[%s]" % (time.strftime("%X")),"Error:",e

		except ValueError,e:
			print "[%s]" % (time.strftime("%X")),"Error:",e



except KeyboardInterrupt:
	print "exit..."
	sys.exit()




























