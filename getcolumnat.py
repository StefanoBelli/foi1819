def getColumnAt(pic, w, pos):
  height = getHeight(pic)
  canvas = makeEmptyPicture(w, height)
  
  for j in range(0, w - 1):
    for i in range(0, height - 1):
      pixelCoord = getPixelAt(pic, j + pos * w, i)
      origColor = makeColor(getRed(pixelCoord), 
                            getGreen(pixelCoord), 
                            getBlue(pixelCoord))
      setColor(getPixelAt(canvas, j, i), origColor)
      
  return canvas
                                    