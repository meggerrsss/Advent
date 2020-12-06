f = open('2020/inputs/2020d5input.txt', 'r')
inp = f.read()
f.close() 
linp = inp.split('\n')


example = "FBFBBFFRLR"

def rown(st,deb = False):   #st is FBFBBFFRLR
  st = st[0:6]
  rang = range(0,128)
  while len(st) > 0:
    currentletter = st[0]
    if st == "F":
      return min(rang)
    if st == "B":
      return max(rang)-1
    if st == "":
      return rang
    if currentletter == "F":
      spread = int((max(rang)-min(rang)+1)/2)
      newlow = min(rang)
      newhigh = max(rang) - spread
      rang = range(newlow,newhigh+1)
      if deb: print("spread: ",spread,", range: ", rang, ", letter: ",currentletter, " remaining: ", st[1:])
      st = st[1:]
    if currentletter == "B":
      spread = int((max(rang)-min(rang)+1)/2)
      newlow = min(rang) + spread
      newhigh = max(rang)
      rang = range(newlow,newhigh+1)
      if deb: print("spread: ",spread,", range: ", rang, ", letter: ",currentletter, " remaining: ", st[1:])
      st = st[1:]
  return rang

def seatn(st):   #st is FBFBBFFRLR
  st = st[7:]
  rang = range(0,8)
  while len(st) > 0:
    currentletter = st[0]
    if st == "L":
      return min(rang)
    if st == "R":
      return max(rang)
    if st == "":
      return rang
    if currentletter == "L":
      spread = int((max(rang)-min(rang)+1)/2)
      newlow = min(rang)
      newhigh = max(rang) - spread
      rang = range(newlow,newhigh+1)
      st = st[1:]
    if currentletter == "R":
      spread = int((max(rang)-min(rang)+1)/2)
      newlow = min(rang) + spread
      newhigh = max(rang)
      rang = range(newlow,newhigh+1)
      st = st[1:]
  return rang

def seatid(st):
  row = rown(st)
  seat = seatn(st)
  print(row,seat)
  return row * 8 + seat 

print(seatid("BFFFBBFRRR"))

#saved = 0 
#for person in linp:
#  s = seatid(person)
#  if s > saved: saved = s
#print(saved)