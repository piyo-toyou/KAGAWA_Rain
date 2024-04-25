import Scraping_24 as sc
import Rain_Management_12 as rm
import send_mail_02 as sm

#Execution sc
my_url1 = "http://www.skr.mlit.go.jp/road/mobile/M0711_39_7801_3_5_1.html"
my_url2 = "http://www.skr.mlit.go.jp/road/mobile/M0711_39_56_0_5_1.html"
my_parser = "html.parser"
text1 = sc.Scraping(my_url1, my_parser)
text2 = sc.Scraping(my_url2, my_parser)

all_text = text1 + text2

my_directiry = "C:/Users/S2212357/Documents/Z6_DataBase/Nakamura_Rain_Excel/"
file_type = ".xlsx"
file_path = sc.FilePath(my_directiry, file_type)

sc.Output(all_text, file_path)

#Execution rm
file_path = "C:/Users/S2212357/Documents/Z6_DataBase/Nakamura_Rain_Excel/nakamura_rain_*.xlsx"
list_length, df_dict = rm.InputData(file_path, 20)

df2 = rm.EditDataframe(list_length, df_dict)

output_file = "G:/マイドライブ/Nakamura_Rain/Nakamura_Rain.xlsx"
rm.OutputExcel(df2, output_file)
rm.AdjustExcel(output_file)

#Execution sm
flug, rain_max = sm.AlartCheck(df2)

if flug:
    gmail_account = "koga.wataru@kiso.co.jp"
    gmail_password = "kgwt2211"
    mail_to = "koga.wataru@kiso.co.jp"
    mail_cc = "furuyama.shoichi@kiso.co.jp"

    sm.SendMail(gmail_account, gmail_password, mail_to, mail_cc, rain_max)
else:
    pass
