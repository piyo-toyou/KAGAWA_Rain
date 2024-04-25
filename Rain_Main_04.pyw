from cmath import nan
import Scraping_25 as sc
import Rain_Management_14 as rm

#Execution sc
#道路降雨状況のサイトにアクセスし、スクレイピングを実行
KAGAWA_Rain_URL = "https://www.skr.mlit.go.jp/road/mobile/M0712_37.html"
my_parser = "html.parser"
all_rain_text = sc.Scraping(KAGAWA_Rain_URL, my_parser)

my_directory = "C:/Users/H71871/Documents/Z6_DataBase/KAGAWA_Rain_Excel/"
file_type = ".xlsx"
file_path = sc.FilePath(my_directory, file_type)

sc.Output(all_rain_text, file_path)

#Execution rm
#入手したエクセルファイルを整理
file_path = "C:/Users/H71871/Documents/Z6_DataBase/KAGAWA_Rain_Excel/KAGAWA_rain_*.xlsx"
list_length, df_dict = rm.InputData(file_path, 60)

df2 = rm.EditDataframe(list_length, df_dict)

output_file = "G:/マイドライブ/KAGAWA_Rain/KAGAWA_Rain.xlsx"
rm.OutputExcel(df2, output_file)
rm.AdjustExcel(output_file)