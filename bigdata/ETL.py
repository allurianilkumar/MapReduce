#!/usr/bin/python
import os
import sys
import re
import simplejson as json
from collections import Counter

def  writeJson(file,data):
	json = open(file+".json","w")
	json.write(data)
	json.close()
	json.close
	return
def  createJsonFile(filename):
	myIdCount=1;
	file = open(filename, 'r')
	totalInfo="";
	for line in file:
		if(line[0] != "*"):
			totalInfo+=line.strip()
	jObject="{\"reviews\":[\n";
	row=list();
	positiveBlock=list();
	negativeBlock=list();
	row= totalInfo.split("[t]");
	for i in range(1,len(row)):
		if( i == 1):
			jObject += "{\"id\""+":"+str(int(myIdCount))+",";
		else:
			jObject += "{\"id\""+":"+str(int(myIdCount))+",";
		titleName="";
		myIdCount = myIdCount+1
		for k in range(0, len(row[i])):
			if( (row[i][k] != "[")):
				titleName+=row[i][k]
			else:
				break;
		titleName = re.sub("[^a-zA-Z]", " ",titleName)
		jObject += "\"titleName\""+":"+'"'+titleName+'"'+",\n"
		blocks=list();
		blocks = row[i].split("[");
		for j in range(0,len(blocks)):
			if( blocks[j][0] == "+"):
				positiveBlock.append(re.sub("[^a-zA-Z]", " ",blocks[j][3:]))
			if( blocks[j][0] == "-"):
				negativeBlock.append(re.sub("[^a-zA-Z]", " ",blocks[j][3:]))
		jObject+="\"positive\": ["
		for p in range(0,len(positiveBlock)):
			if p == len(positiveBlock)-1:
				jObject+='"'+positiveBlock[p]+'"'
			else:
				jObject+='"'+positiveBlock[p]+'"'+","
		jObject+="]\n,\"negative\": ["
		for n in range(0,len(negativeBlock)):
			if n == len(negativeBlock)-1:
				jObject+='"'+negativeBlock[n]+'"'
			else:
				jObject+='"'+negativeBlock[n]+'"'+","
		if i != len(row)-1:
			jObject+="]},\n"	
		else:
			jObject+="]}\n"
	jObject+="\n]}"
	writeJson(filename[:-4],jObject);
	return
for arg in range(1,len(sys.argv)):
	print "\nLoading the file ", sys.argv[arg]
	createJsonFile(sys.argv[arg]);
