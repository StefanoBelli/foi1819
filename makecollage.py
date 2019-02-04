def makeCollage(pict1, pict2):
# @param pict1 : Picture
# @param pict2 : Picture
  pict1Width = getWidth(pict1)
  pict1Height = getHeight(pict1)
  pict2Height = getHeight(pict2)
  
  if pict1Height < pict2Height:
    targetHeight = pict2Height
  else:
    targetHeight = pict1Height
  
  newPict = makeEmptyPicture(pict1Width + getWidth(pict2), targetHeight)
  copyInto(pict1, newPict, 0, 0)
  copyInto(pict2, newPict, pict1Width, 0)
  
  return newPict