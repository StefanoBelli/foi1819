def reflVert(pict):
# @param pict : Picture
  height = getHeight(pict)
  width = getWidth(pict)
  midWid = width / 2
  
  for xcoord in range(midWid):
    for ycoord in range(height):
      fromPixel = getPixelAt(pict, xcoord, ycoord)
      targetPixel = getPixelAt(pict, width - xcoord - 1, ycoord)
      setColor(targetPixel, getColor(fromPixel))