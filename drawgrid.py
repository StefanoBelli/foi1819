def drawHorizontalLine(pict, y, size=3, color=black):
  trackY = y
  pictWidth = getWidth(pict)
  
  for i in range(size):
    addLine(pict, 0, trackY, pictWidth, trackY, color)
    trackY += 1
    
def drawVerticalLine(pict, x, size=3, color=black):
  trackX = x
  pictHeight = getHeight(pict)
  
  for i in range(size):
    addLine(pict, trackX, 0, trackX, pictHeight, color)
    trackX += 1

def drawGrid(pict, qsize=10, linesize=2, color=black):
  for y in range(0, getHeight(pict), qsize):
    drawHorizontalLine(pict, y, linesize, color)
    
  for x in range(0, getWidth(pict), qsize):
    drawVerticalLine(pict, x, linesize, color)