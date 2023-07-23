import os           
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.image import MIMEImage
import telegram
import asyncio

# email
email_id='youremailid'
# verification
email_txt ="yourtxt"
# bot token
token = "your token"
# chat id
chatid="chatidhere"
def report_send_mail(label, image_path):
    with open(image_path, 'rb') as f:
        img_data = f.read()
    fromaddr = email_id
    toaddr = email_id            
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    msg['Subject'] = "Alert"
    body = label
    msg.attach(MIMEText(body, 'plain'))  
    image = MIMEImage(img_data, name=os.path.basename(image_path))
    msg.attach(image) 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(fromaddr, email_txt) 
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit()
    bot_token=token
    chat_id= chatid
    asyncio.run(send_telegram_alert(bot_token, chat_id, image_path,label))
async def send_telegram_alert(bot_token, chat_id, image_path,text):
    bot = telegram.Bot(token=bot_token)
    await bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'))
    await bot.send_message(chat_id=chat_id,text=text)
  



