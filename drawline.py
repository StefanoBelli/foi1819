def drawLine(pict, y, size=3, color=black):
  trackY = y
  for i in range(size):
    addLine(pict, 0, trackY, getWidth(pict), trackY, color)
    trackY += 1