f = open('2020/inputs/2020d5input.txt', 'r')
inp = f.read()
f.close() 


example = "FBFBBFFRLR"

def rown(st):   #st is FBFBBFFRLR
  st = st[0:6]
  rang = range(0,128)
  print(rang)
  while len(st) > 0:
    currentletter = st[0]
    if st == "":
      return rang
    if currentletter == "F":
      spread = int(len(rang)/2)
      rang = range(rang[0],rang[spread])
      st = st[1:]
      print(rang)
    if currentletter == "B":
      spread = int(len(rang)/2)
      rang = range(rang[0]+spread, rang[len(rang)-1])
      st = st[1:]
      print(rang)
  return rang

print(rown(example))