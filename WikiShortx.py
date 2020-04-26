#WikiShortx.py

import urllib.request
import time
import re

#def--------00000000000000000

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False

def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext

def cleanxml(raw_xml):
	cleanxr = re.compile('{.*?}')
	cleantxt = re.sub(cleanxr, '', raw_xml)
	return cleantxt

def strip_tags(value):
	return re.sub(r'<[^>]*?>', '', force_unicode(value))

#-----------00000000000000000

print("\n")
print(" `VA            .AIIIA `YA    A7 ")
print("  `VA           II'  IV `YA  A7  ")
print("   `VA    A    A`VIo.    `YA7'   ") 
print("    `YA  AXA  A7  `YIA.  .A7YA.  ")
print("     `VAA7'YAA7 AA   XD .A7  YA. ")
print("       V7  `V7  `VIII7'.A7    YA.") 

#Introduction
print ("\n= WikiShortx","="*46," \n")
z=1
print("  This program gets information from Wikipedia.\n")
print("  Loading ... \n")
time.sleep(6)		
print ("  Checking Internet Connection ...Wait!")

#Checking connection
if (connect()):
    print("  Device is connected to Internet ...")
    contx=1
else:
    print("  Device isn't connected to Internet ... ")
    print("  WARNING: Program requires Internet Connection to function. ")
    contx=7

#Getting the input
term= input("\n  Input the valid term you want to search= ")
domain= 'https://en.wikipedia.com/wiki/'
xite=domain+term

#Validating url
print("  Validating url ...")
try:
	fx = urllib.request.urlopen(xite)
	mybytes = fx.read()
except:
	print("\n  Enter a valid term to search \n  and/or \n  Check your Internet connection.")
	contx=0

if (contx==1):
	
	#Getting HTML file for the url
	print("  Connecting Wikipedia ...")
	fp = urllib.request.urlopen(xite)
	mybytes = fp.read()
	mystr = mybytes.decode("utf8")
	fp.close()
	print("  Organizing data ... ")
	
	#Removing scripts from data using regex 
	mystr= cleanhtml(mystr)
	mystr= cleanxml(mystr)
	
	#Stripping off empty lines
	mystr = mystr.split('\n',20)[-1]
	lines = mystr.split("\n")
	non_empty_lines = [line for line in lines if line.strip() != ""]
	string_without_empty_lines = ""
	for line in non_empty_lines:
		string_without_empty_lines += line + "\n"
	mystr=string_without_empty_lines 
	mystr = mystr.split('\n',5)[-1]
	rx=''
	new= "\n"
	
	#Removing lines with specific substrings
	spixted= mystr.splitlines()
	for i in range (len(spixted)):
		if('parser' in spixted[i] or 'For other uses' in spixted[i] or 'directs here' in spixted[i] or 'This article' in spixted[i] or '&amp' in spixted[i] or 'appropriate' in spixted[i] or '•' in spixted[i] or 'Disambiguation' in spixted[i] or '^' in spixted[i]):
			rx= rx
		else:
			rx= rx+new+spixted[i]			
	mystr= rx
	rx=''
	spixted= mystr.splitlines()
	for i in range (len(spixted)):
		lex= len(spixted[i])
		if(lex<=60):
			rx= rx
		else:
			rx= rx+new+spixted[i]
	mystr= rx
	rx=''
	
	#Removing CSS traces
	mystr = re.sub(r'\([^)]*\)', '', mystr)	
	mystr = mystr.replace('&#160;',' ')
	for i in range (500):
		z='&#'+str(i)+';'
		mystr = mystr.replace(z,' ')
	for i in range (9):
		z=' '+str(i)+' '
		mystr = mystr.replace(z,' ')
	for i in range (99):
		z=' '+str(i)+' '
		mystr = mystr.replace(z,' ')
		
	#Optimizing text readability
	mystr = mystr.replace('; ','')
	mystr = mystr.replace(' , ',', ')
	mystr = mystr.replace(' . ','. ')
	mystr = mystr.replace('  ',' ')
	mystr = mystr.replace('   ',' ')
	mystr = mystr.replace('&#xfeff;',' ')
	pax=2
	
	#Removing Glitched lines	
	small='abcdefghijklmnopqrstuvwxyz'
	large='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	spixted= mystr.splitlines()
	for i in range (len(spixted)):	
		for u in range (26):
			#small
			first=small[u]
			for z in range (26):
				secnd=large[z]
				viewr=first+secnd
				if (viewr in spixted[i]):
					pax=0
		if(pax==0):
			rx=rx
			pax=1 		
		else:
			rx=rx+new+spixted[i]		
	mystr=rx	
	rx=''	
	
	#Giving final touches
	print("  Giving final touches ...")													
	mystr = mystr.split('\n',0)[-1]
	spixted= mystr.splitlines()	
	try:
		for i in range (10):
			rx= rx+new+spixted[i]			
	except:
		for i in range (len(spixted)):
			rx= rx+new+spixted[i]	
	mystr= rx
	rx=''
	terx=56-len(term)
	print("\n=",term.upper(),"="*terx,"\n")		
	mystr = mystr.replace(')','')
	mystr = mystr.replace('; ','')
	mystr = mystr.replace(' , ',', ')
	mystr = mystr.replace(' . ','. ')
	mystr = mystr.replace('  ',' ')
	mystr = mystr.replace('   ',' ')		
	spixted= mystr.splitlines()
	for i in range (len(spixted)):		
		if('xfeff' in spixted[i]):
			rx= rx			
		else:
			rx= rx+new+spixted[i]
	mystr= rx
	rx=''
	
	#Stripping off empty lines							
	lines = mystr.split("\n")
	non_empty_lines = [line for line in lines if line.strip() != ""]
	string_without_empty_lines = ""	
	for line in non_empty_lines:
		string_without_empty_lines += line + "\n"
	mystr=string_without_empty_lines 
		
	#Removing useless information	
	if('This page was last edited on' in mystr):
		spixted= mystr.splitlines()
		for i in range (len(spixted)):			
			if('This page was last edited on' in spixted[i]):
				linx=i
		mystr= rx
		rx=''		
		try:				
			spixted= mystr.splitlines()
			for i in range (2):
				rx= rx+new+spixted[i]
			mystr= rx
			rx=''			
		except:
			print("  Error, try other term.")
	print(mystr)
	
else:
	print("  Program ended.\n")
	mystr='null'
	
print("="*59)
print("  WikiShortx")
print("="*59)
x=input("\n  Do you want to save this as a txt file? (y/n)")
x=x.lower()
termu=term.upper()

if (x=='y'):
	fix=term+'.txt'
	f= open(fix,"w+")
	fdt= termu+'\n\n'+mystr
	f.write(fdt)
	f.close()
	print("  File saved successfully ... ")
	print("\n  Press enter to end program ...\n")
	print("= XXXXXXXXXXX","="*46)
	ix= input()

else:
	print("\n  Press enter to end program ...\n")
	print("= XXXXXXXXXXX","="*46)
	ix= input()
#WikiShortx - A python based program for downloading information from Wikipedia. 
