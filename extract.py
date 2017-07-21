#PROGRAM TO EXTRACT DATA FOR A PARTICULAR COMMAND WORD INTO A FILE 
#IT CREATES A TEXT FILE FOR THE COMMANDWORD AND PUTS THE DATA THERE
#MAKE SURE DATA FOLDER IS CREATED
import os
def extract(commandword,repfile):
	commandwordfile=str(commandword)+".txt"
	f=open(str(repfile),"r")
	print(os.getcwd()+"\\data")
	n=open("data//"+commandwordfile,"w+")
	s=f.readlines()
	x=0
	for line in s:
		if x>0:
			if "words" in line:
				x=0
				pass
			elif 'a' in line or 'b' in line or 'c' in line or 'd' in line or 'f' in line or 'A' in line or 'B' in line or 'C' in line or 'D' in line or 'F' in line:	#for case 111 111 111
				n.write(line)
				#print line
				x=x-1
			elif '0' in line or '1' in line or '2' in line or '3' in line or '4' in line or '5' in line or '6' in line or '7' in line or '8' in line or '9' in line:	#for case 000 000 000
				n.write(line)
				#print line
				x=x-1
		if str(commandword) in line:
			x=2
			n.write(str(commandword)+"\n")
			#print line
