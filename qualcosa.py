import time

def black_and_white(pic):
  beg = time.time()
  for i in getPixels(pic):
     b = ( getRed(i) + getGreen(i) + getBlue(i) ) / 3
     setColor(i, makeColor(b,b,b) )
     
  end = time.time() - beg
  return end