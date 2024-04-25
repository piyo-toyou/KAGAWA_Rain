import smtplib, ssl
from email.mime.text import MIMEText

# 以下にGmailの設定を書き込む★ --- (*1)
gmail_account = "koga.wataru@kiso.co.jp"
gmail_password = "kgwt2211"
# メールの送信先★ --- (*2)
mail_to = "koga.wataru@kiso.co.jp"
mail_cc = "josephy.mg.wk@gmail.com"

# メールデータ(MIME)の作成 --- (*3)
def SendMail(me, pw, to, cc, n):
  subject = "中村雨量警報【自動配信】"
  my_html = f"""\
  <html>
    <head></head>
    <body>
      <p>中村地区の連続雨量が{n}mmを超えました</p>
      <p>引き続き雨量情報に警戒してください</p>
      <br>
      <p>------以下参考サイト-------</p>
      <p>古賀サイト：https://sites.google.com/kiso.co.jp/nakamura-rain-kiroku/%E3%83%9B%E3%83%BC%E3%83%A0</p>
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