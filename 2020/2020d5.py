f = open('2020/inputs/2020d5input.txt', 'r')
inp = f.read()
f.close() 
linp = inp.split('\n')


example = "FBFBBFFRLR"

def rown(st,deb = False):   #st is FBFBBFFRLR
  st = st[0:7]
  rang = range(0,128)
  if deb: print("starting sequence: ",st , ", range: ", rang)
  while len(st) > 0:
    currentletter = st[0]
    if st == "F":
      if deb: print("letter: ",st,", final: ", min(rang))
      return min(rang)
    if st == "B":
      if deb: print("letter: ",st,", final: ", max(rang))
      return max(rang)
    if st == "":
      return rang
    if currentletter == "F":
      spread = int((max(rang)-min(rang)+1)/2)
      newlow = min(rang)
      newhigh = max(rang) - spread
      rang = range(newlow,newhigh+1)
      if deb: print("letter: ",currentletter,", range: ", rang, ", spread: ",spread, " remaining: ", st[1:])
      st = st[1:]
    if currentletter == "B":
      spread = int((max(rang)-min(rang)+1)/2)
      newlow = min(rang) + spread
      newhigh = max(rang)
      rang = range(newlow,newhigh+1)
      if deb: print("letter: ",currentletter,", range: ", rang, ", spread: ",spread, " remaining: ", st[1:])
      st = st[1:]
  return rang

def seatn(st, deb = False):   #st is FBFBBFFRLR
  st = st[7:]
  rang = range(0,8)
  if deb: print("starting sequence: ",st , ", range: ", rang)
  while len(st) > 0:
    currentletter = st[0]
    if st == "L":
      if deb: print("letter: ",st,", final: ", min(rang))
      return min(rang)
    if st == "R":
      if deb: print("letter: ",st,", final: ", max(rang))
      return max(rang)
    if st == "":
      return rang
    if currentletter == "L":
      spread = int((max(rang)-min(rang)+1)/2)
      newlow = min(rang)
      newhigh = max(rang) - spread
      rang = range(newlow,newhigh+1)
      if deb: print("letter: ",currentletter,", range: ", rang, ", spread: ",spread, " remaining: ", st[1:])
      st = st[1:]
    if currentletter == "R":
      spread = int((max(rang)-min(rang)+1)/2)
      newlow = min(rang) + spread
      newhigh = max(rang)
      rang = range(newlow,newhigh+1)
      if deb: print("letter: ",currentletter,", range: ", rang, ", spread: ",spread, " remaining: ", st[1:])
      st = st[1:]
  return rang

def seatid(st, deb = False):
  row = rown(st, deb)
  seat = seatn(st,deb)
  if deb: print(row,seat)
  return row * 8 + seat 

print(seatid("BBBBFFBRRL",True)) #974

saved = 0 
for person in linp:
  s = seatid(person)
  if s > saved: saved = s
print(saved)