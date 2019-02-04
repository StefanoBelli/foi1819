def makeBlackAndWhite(pict):
# @param pict : Picture
  for pix in getPixels(pict):
    r = g = b = (getRed(pix) + getGreen(pix) + getBlue(pix)) / 3
    setColor(pix, makeColor(r,g,b))