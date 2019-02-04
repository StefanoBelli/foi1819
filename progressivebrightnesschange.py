from time import sleep

def opDoneHook():
  showWarning("requested operation was completed.")

def changeBrightness(pict, x):
# @param pict : Picture
# @param x : float
  for pix in getPixels(pict):
    origColor = makeColor( getRed(pix) + x, getGreen(pix) + x, getBlue(pix) + x)
    setColor(pix, origColor)

def checkIfEntirely(pict, rgbcomp):
# @param pict : Picture
# @param color : Color
  for pix in getPixels(pict):
    if getRed(pix) != rgbcomp[0] or getGreen(pix) != rgbcomp[1] or getBlue(pix) != rgbcomp[2]:
      return False
      
  return True
    
def __viewProgressiveBrightnessChange(pict, rgbenc, threadSleepS, brightnessChange, finishHook=None):
# @param pict : Picture
# @param rgbenc : tuple
# @param threadSleepS : float
# @param brightnessChange : int
  repaint(pict)
  while not checkIfEntirely(pict, rgbenc):
    changeBrightness(pict, brightnessChange)
    repaint(pict)
    sleep(threadSleepS)
  
  if finishHook:
    finishHook()
    
def viewProgressiveLessBrightness(pict, sleepms=0.25, change=-20):
# @param pict : Picture
# @param sleepms : float
# @param change : int
  if change >= 0:
    showError("change value must be strictly negative")
    return
    
  __viewProgressiveBrightnessChange(pict, (0,0,0), sleepms, change, finishHook=opDoneHook)
  

def viewProgressiveMoreBrightness(pict, sleepms=0.25, change=20):
# @param pict : Picture
# @param sleepms : float
# @param change : int
  if change <= 0:
    showError("change value must be strictly positive")
    return
  
  __viewProgressiveBrightnessChange(pict, (255,255,255), sleepms, change, finishHook=opDoneHook)
  