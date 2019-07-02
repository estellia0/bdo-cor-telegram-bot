# bdo-ocr-telegram-bot
OCR bot for Black Desert Online Workers Queue, needs pytesseract, opencv, telepot and mss installed to work (refer to each lib github on how to install them.

Since it's an ocr bot it needs an active game window to work.

Adjust the chatbox region to match your chat area ingame, being 'top' distance from left top angle and left as the distance from the left corner, width and height the area of the rectangle you want to pass.

Setup a telegram bot by talking with Bot Father and add the token.
You have to either hardcode your chatid instead of cID in the code or first send a message to the bot.

For better results turn your gamma to lowest possible and contrast to max to create a black background for the chat.
