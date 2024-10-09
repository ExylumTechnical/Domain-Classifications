import os
import subprocess

# domainlist=["thisdomaindoesnotresolvetoanyaddress.com","yahoo.com"];

def checkResolution(ip):
# checks to see if a domain resolves or not before running further lookups
# subprocess is used instead of os.system because os.system will hang when it errors
# subrpocess does not error out but returns an exception
        try:
                out=subprocess.check_output("nslookup "+i, shell=True);
                return True;
        except:
                return False;

def getListPosition(list,value):
# iterate through a list and return the position where the value exists if it does not exist
# then the return value is incremented by one.
        position=-1;
        for i in range(len(list)):
                if(list[i]==value):
                        position=i;
        if(position==-1):
                position=len(list)+1

        return position

def report(fileName):
# this function outputs a list in the following format [[classification, occuranceCount],[classification, occuranceCount]]
# Formatting per line: class,domain

# create two lists that are corrolated
        dataClass=[]
        dataPoint=[]
# create the list that will be returned
        returnList=[]
# open the file that the desired data resides
        with open(fileName) as my_file:
                lineBuffer=my_file.readline()
                lineList=lineBuffer.split(",")
        # get the first chunk of data and set the value to 0 so that it can be counted in the first
        # iteration of the loop to follow
                dataClass.append(lineList[0])
                dataPoint.append(0)
        # start reading lines and putting them into the databuffer to be returned
                while(lineBuffer):
                # get the pointer from the function defined above
                        pointer=getListPosition(dataClass,lineList[0])
                # if the current value is in the data class then add one to the dataPoint location
                        if(lineList[0] in dataClass):
                                dataPoint[pointer]=dataPoint[pointer]+1
                # Append new data to the end of the list if it does not exist
                        else:
                                dataClass.append(lineList[0])
                                dataPoint.append(1)
                # get the next line and split the data from the csv
                        lineBuffer=my_file.readline()
                        lineList=lineBuffer.split(",")
        # put all of our nicely arranged data into the return list
                for i in range(len(dataClass)):
                        returnList.append([dataClass[i],dataPoint[i]])
        # return the list
                return returnList

print(report("./buffer.csv"))

def main():
# do a little bit of cleanup
        os.system("rm buffer.csv")

# Open the file and parse out the domains
        data=open("./data.csv","r")
        doesNotResolve=open("./buffer.csv","a")
        lineBuffer=data.readline();
        while(lineBuffer!=""):
                lineContents=lineBuffer.split(",")
## change this pointer to point to the domain name in the CSV
                domain=lineContents[2]
                classification=lineContents[1]
                flag=checkResolution(domain)
                if(flag==False):
                        didntResolve=classification+","+domain
                        doesNotResolve.writeLine(didntResolve)
                lineBuffer=data.readline();