"""
Hello!

I debugged and tested this program numerous times,
but due to the command-line nature of the code, I found it
difficult to show you the instances of me debugging and testing.
Regardless, I encourage you to play around with the program and
try out different csv files and command line arguments. I had a
lot of fun coding this out, and I hope to hear back soon!

"""

import csv

def main():
  print("Welcome to the program! type 'done' to exit\n")

  while True:
    tmpInput = input("$ ")
    if tmpInput.lower() == "done":
      break

    brokenUpInput = tmpInput.split()

    if len(brokenUpInput) == 4 and checkInput(brokenUpInput):
      returnCookies(brokenUpInput[1],brokenUpInput[3][-10:])
    else:
      print("CMD not recognized. Try again or type 'done' to exit")

def checkInput(brokenUpInput):
  if brokenUpInput[0] == "./most_active_cookie" and brokenUpInput[2] == "-d":
    return True
  else:
    return False

def parseLines(file):
  with open(file, newline='') as file:
    data = list(csv.reader(file))
    return data[1:]


def returnCookies(inputCookies,day):
  lines = parseLines(inputCookies)
  datesDict = {}

  for line in lines:
    tmp = line
    if tmp[1][:10] not in datesDict:
      datesDict[tmp[1][:10]] = dict()
      

    if tmp[0] not in datesDict[tmp[1][:10]]:
      datesDict[tmp[1][:10]][tmp[0]] = 1
    else:
      datesDict[tmp[1][:10]][tmp[0]] += 1
    
  if day in datesDict:
    maxKey = max(datesDict[day].values())
    print("")
    for value in datesDict[day]:
      if datesDict[day][value] == maxKey:
        print(value)
  else:
    print("Date not found\n")

main()
