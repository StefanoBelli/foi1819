# verifica 
# colonna 0, riga 0, riga 1
# colonna 0, riga 0, riga 2
# ...
# colonna 0, riga 1, riga 2
# colonna 0, riga 1, riga 3
# ...
# colonna 1, riga 0, riga 1
# colonna 1, riga 0, riga 2

def hasRedSameAsBlueGreenForEvery(p):
# @param p : Picture
  picHeight = getHeight(p)
  for w in range(getWidth(p)):
    for h in range(picHeight):
      redComp = getRed(getPixelAt(p, w, h))
      for sh in range(h+1, picHeight):
        greenComp = getGreen(getPixelAt(p, w, sh))
        blueComp = getBlue(getPixelAt(p, w, sh))
        
        if not redComp == greenComp + blueComp:
          return False
          
  return True
        
      