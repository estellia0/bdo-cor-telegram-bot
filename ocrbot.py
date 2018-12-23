import time
import mss
import mss.tools
import pytesseract
import cv2
import telepot
from telepot.loop import MessageLoop
import numpy as np

bot = telepot.Bot('')#add telegram bot token here
cID = 0
previousMatch = ''
# The screen part to capture
chatbox = {"top": 990, "left": 61, "width": 450, "height": 50}
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

def handle(msg):
    global cID
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(chat_id)
    cID = chat_id

def process(im):
    im = np.flip(im[:, :, :3], 2) #turn bgra to rgb
    height, width, channel = im.shape
    img = cv2.resize(im, (3*width, 3*height), interpolation = cv2.INTER_LINEAR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #grayscale
    return gray

def postprocess(im):
    gray = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray = cv2.medianBlur(gray, 3)
    return gray

MessageLoop(bot, handle).run_as_thread()
while 1:
    with mss.mss() as sct:
        # Grab the data
        im = np.array(sct.grab(chatbox), dtype=np.uint8)
        gray = process(im)
        #cv2.imshow("Output", gray)
        text = pytesseract.image_to_string(gray)
        #cv2.waitKey(0)
        if text == previousMatch:
            time.sleep(0.5)
        else:
            if cID == 0:
                print("no chat yet")
                time.sleep(1)
            else:
                if 'Worker' in text:
                    bot.sendMessage(cID, text)
                    previousMatch = text
