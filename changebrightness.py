def changeBrightness(pict, x):
# @param pict : Picture
# @param x : float
  for pix in getPixels(pict):
    origColor = makeColor( getRed(pix) + x, getGreen(pix) + x, getBlue(pix) + x)
    setColor(pix, origColor)