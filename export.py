import cv2 as cv
import math
import sys

args = sys.argv[::1]

DST_DIR = 'output'

## output
try:
  indexOutput = args.index('-o')
  
  if (indexOutput + 1) < len(args):
    DST_DIR = args[indexOutput + 1]
except ValueError:
  print('Output path is not in list')

# input
try:
  indexInput = args.index('-i')

  if (indexInput + 1) < len(args):
    SRC_FILE = args[indexInput + 1]
except ValueError:
  print('Input path is not in list')

GRAY = False
# gray
try:
  indexGray = args.index('-gray')
  GRAY = True
except ValueError:
  GRAY = False


video = cv.VideoCapture(SRC_FILE)
index = 0

fps = video.get(cv.CAP_PROP_FPS)

while(video.isOpened()):
  frameIndex = video.get(cv.CAP_PROP_POS_FRAMES)
  ret, frame = video.read()

  if ret != True:
    break

  if frameIndex % math.floor(fps) == 0:
    filePath = DST_DIR + '/frame_' + str(index) + '.jpg'

    if GRAY:
      frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imwrite(filePath, frame)

    index += 1

video.release()
cv.destroyAllWindows()