def greenColSum(p, col):
# @param p : Picture
# @param col : int
  sum = 0
  for row in range(getHeight(p)):
    sum += getGreen(getPixelAt(p, col, row))
    
  return sum