def cut(pict, x, y, w, h):
  canvas = makeEmptyPicture(w,h)
  
  i = 0
  j = 0
  
  for xc in range(x, w):
    for yc in range(y, h):
      setColor(getPixelAt(canvas,i,j), getColor(getPixelAt(pict, xc, yc)))
      j += 1
    i += 1
    
  return canvas