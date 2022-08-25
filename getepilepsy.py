import time

def replaceColor(pic, toReplace, replaceWith):
  for pix in getPixels(pic):
    currentColor = getColor(pix)
    if currentColor == toReplace:
      setColor(pix, replaceWith)
      
def timedRepaintWithColorReplacement(pic, col0, col1, ts=0.001):
    replaceColor(pic, col0, col1)
    repaint(pic)
    time.sleep(ts)
    
def getEpilepsy(pic):
  colorPair = [ (white, green), (green, blue), (blue, red), (red, white) ]
  
  i = 0
  while i < 4:
    timedRepaintWithColorReplacement(pic, colorPair[i][0], colorPair[i][1])
    i += 1
    if i == 4:
      i = 0
      
    
