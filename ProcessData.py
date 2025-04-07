#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
 # line= inFile.readline()
  for line in inFile:
    data = line.split( )
    #print(data)
    

    student_id=makeID(data[0], data[1], data[3])
    major= data[6]
  

  
    year="none"
    #print(data[5])
   
    for text in list(data[5]):
      if text[0]== "F":
        year="FR"
      if text[0]== "J":
        year="JR"
      if text[0]=="S":
          year="SO"
      if text[0]=="S" and len(text)==6:
          year="SR"

    print(student_id, major[0:3]+"-"+year)

    output = data[1] + "," + data[0] +"," + data[3] + "," + major[0:3]+"-" + year +"\n"
    outFile.write(output)
    
  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum,):
  #print(first, last, idNum)
  idLen= len(idNum)

  while len(last) <5:
    last= last + "X"

  id= first[0] + last +idNum[idLen-3: ]
  #print(id)
  return id


if __name__ == '__main__':
  main()
