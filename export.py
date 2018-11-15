import cv2 as cv
import math
import sys
import argparse
import os

parser = argparse.ArgumentParser(description='Convert all frames of a video in jpeg images')
parser.add_argument('--gray', '-g', help='Convert image in gray scale color', action='store_true')
parser.add_argument('--output', '-o', help='Output directory', default='output')
parser.add_argument('--input', '-i', help='Input video file', required=True)

args = parser.parse_args()

DST_DIR = args.output
SRC_FILE = args.input
GRAY = args.gray

if not os.path.exists(DST_DIR):
  os.makedirs(DST_DIR)

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