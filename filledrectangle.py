def filledRectangle(pict_c, x, y, w, h, color):
  pict = pict_c
  pictHeight = getHeight(pict)
  pictWidth = getWidth(pict)
  
  for wi in range(w):
    for hi in range(h):
      setColor(getPixelAt(pict, x + wi, y + hi), color)
      
  return pict  