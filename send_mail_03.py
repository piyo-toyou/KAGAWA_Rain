import smtplib, ssl
from email.mime.text import MIMEText
import numpy as np

# メールを送るかどうかのチェック
def AlartCheck(df):
  last1_array = np.squeeze(df.iloc[0:1].values)
  last2_array = np.squeeze(df.iloc[1:2].values)

  last1_array_slice = last1_array[1::2]
  last2_array_slice = last2_array[1::2]

  last1_max = last1_array_slice.max()
  last1_max_index = last1_array_slice.argmax()
  last2_max = last2_array_slice[last1_max_index]

  if last1_max < 180:
      return False, None
  elif 180 <= last1_max < 230 and last2_max < 180:
      return True, 180
  elif 230 <= last1_max < 250 and last2_max < 230:
      return True, 230
  elif 250 <= last1_max and last2_max < 250:
      return True, 250
  else:
      return False, None

# メールデータ(MIME)の作成 --- (*3)
def SendMail(me, pw, to, cc, n):
  subject = "中村雨量警報【自動配信】"
  my_html = f"""\
  <html>
    <head></head>
    <body>
      <p>中村地区のどこかで連続雨量が{n}mmを超えました</p>
      <p>引き続き雨量情報に警戒してください</p>
      <br>
      <p>------以下参考サイト-------</p>
      <p>小倉畑サイト：https://sites.google.com/kiso.co.jp/nakamura-rain-kiroku/%E3%83%9B%E3%83%BC%E3%83%A0</p>
      <p>中村宿毛道路2地点：http://www.skr.mlit.go.jp/road/mobile/M0711_39_7801_3_5_1.html</p>
      <p>国道56号6地点：http://www.skr.mlit.go.jp/road/mobile/M0711_39_56_0_5_1.html</p>
    </body>
  </html>
  """
  msg = MIMEText(my_html, "html")
  msg["Subject"] = subject
  msg["From"] = me
  msg["To"] = to
  if cc:
    msg["Cc"] = cc

  # Gmailに接続 --- (*4)
  server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
      context=ssl.create_default_context())
  server.login(me, pw)
  server.send_message(msg) # メールの送信
