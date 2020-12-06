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
    if st == "F":
      return min(rang)
    if st == "B":
      return max(rang)
    if st == "":
      return rang
    if currentletter == "F":
      spread = int((max(rang)-min(rang)+1)/2)
      print(spread)
      newlow = min(rang)
      newhigh = max(rang) - spread
      rang = range(newlow,newhigh+1)
      st = st[1:]
      print(st)
      print(rang)
    if currentletter == "B":
      spread = int((max(rang)-min(rang)+1)/2)
      print(spread)
      newlow = min(rang) + spread
      newhigh = max(rang)
      rang = range(newlow,newhigh+1)
      st = st[1:]
      print(st)
      print(rang)
  return rang

print(rown(example))