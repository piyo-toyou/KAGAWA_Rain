# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created on July 25 2021.
@author: W.KOGA
各雨量データのグラフを作成する。
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# モジュールのインポート
import pandas as pd
import numpy as np
import matplotlib as mpl
import math
import matplotlib.pylab as plt
import datetime

# パス設定
DataPATH = "G:/マイドライブ/Nakamura_Rain/"

# 図のフォントの設定
font_size=22
# フォント設定 'sans-serif','IPAexGothic','IPAexMincho'
mpl.rcParams['font.family'] = 'IPAexGothic'

# 図の作成
df1   = pd.read_excel(DataPATH + "Nakamura_Rain.xlsx", header=0, index_col=0)
x     = np.array(df1.columns.values)
y1   = np.array(df1.loc['窪川・時間'])
y2   = np.array(df1.loc['窪川・連続'])

#作図範囲の設定
n = 36
if len(x) > n:
    x = np.delete(x, slice(0, -n))
    y1 = np.delete(y1, slice(0, -n))
    y2 = np.delete(y2, slice(0, -n))
else:
    pass

# 図・座標軸の設定
fig1 = plt.figure(figsize=(10,6))      # 全体サイズ
ax1  = fig1.subplots()  # apect 縦横比
ax2 = ax1.twinx()
# データのプロット
d1 = ax1.bar(x, y1,
             width = 0.5, color = "blue" , label = "Jikan")
d2 = ax2.plot(x, y2,
             linestyle = "solid" , linewidth = 1.0,
             color = "red" , label = "Renzoku")
# "dashed", "dashdot", "dashdot", "dotted"    
# x軸,y軸の範囲
ax1.set_xlim(0, len(x))
ax1.set_ylim(0, max(y1)+50)
ax2.set_ylim(0, max(y1)+100)
# 軸ラベル名
ax1.set_xlabel('[Date & Time]' ,fontsize=10, fontdict=None,labelpad=5)
ax1.set_ylabel('[Fall Rain]' ,fontsize=10, fontdict=None,labelpad=5)
# 図の枠線の有無
ax1 = plt.gca().spines['right'].set_visible(True)
ax1 = plt.gca().spines['left'].set_visible(True)
ax1 = plt.gca().spines['top'].set_visible(True)
ax1 = plt.gca().spines['bottom'].set_visible(True)
# 図の枠線幅
line_width = 2
ax1 = plt.gca().spines['right'].set_linewidth(line_width)
ax1 = plt.gca().spines['left'].set_linewidth(line_width)
ax1 = plt.gca().spines['top'].set_linewidth(line_width)
ax1 = plt.gca().spines['bottom'].set_linewidth(line_width)
# 図の枠線色
line_color='black'
ax1 = plt.gca().spines['top'].set_color(line_color)
ax1 = plt.gca().spines['bottom'].set_color(line_color)
ax1 = plt.gca().spines['right'].set_color(line_color)
ax1 = plt.gca().spines['left'].set_color(line_color)
# グリッド
ax1 = plt.grid(which='both', axis='x',
               color='black',linestyle='dotted',linewidth=1,alpha= 0.5)
ax1 = plt.grid(which='both', axis='y',
               color='black',linestyle='dotted',linewidth=1,alpha= 0.5)
# which:{'major','minor','both'}
# linestyle:"solid","dashed","dashdot","dotted"
# 軸ラベルの表示設定
#ax1 = plt.xticks(np.linspace(0, 110, 12))
#plt.set_xticklabels([])
ax1 = plt.xticks(rotation=90)
# 目盛りの大きさ
ax1 = plt.tick_params(axis= 'x',  which= 'major', bottom= True, top= False,
                    labelsize= 5, direction= 'in',
                    pad= 10, length= 5, width= 1, colors= 'black'
                    )
ax1 = plt.tick_params(axis= 'y',  which= 'major', left= True, right= False,
                    labelsize= 10, direction= 'in',
                    pad= 10, length= 5, width= 1, colors= 'black'
                    )
# 凡例の有無・大きさ・位置
font_size = 10
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc='upper left',fontsize = font_size)
# ax1 = plt.legend(loc='upper left',fontsize = font_size,
#                facecolor='white',edgecolor='black',
#                title='').get_title().set_fontsize(font_size)
# 'best','upper right','upper left','lower left','lower right'.'right'
# 'center left','center right','lower center','upper center','center'
# 図の保存
now = datetime.datetime.now() # 現在日付・時刻の取得
time = now.strftime("%M%S")
fig1.savefig(fname= DataPATH + "test_" + time + '.png',
            dpi=100,facecolor='white',bbox_inches='tight')