# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created on August 02 2021.
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
mpl.rcParams['font.family'] = 'MS Gothic'

# データの抽出
df1  = pd.read_excel(DataPATH + "Nakamura_Rain_230602.xlsx", header=None, index_col=0)
x    = np.array(df1.index.values[2:]) #日付の取得
# 以下で各テレメータのみの値を配列として取得
# （押ノ川：2と3、窪川：6と7、佐賀：8と9、右山：10と11、山奈：12と13、宿毛：14と15）
y1   = np.array(df1.iloc[2:, 8]) #列数を変更する
y2   = np.array(df1.iloc[2:, 9]) #列数を変更する

# 作図範囲の設定
n = 360
if len(x) > n:
    x = np.delete(x, slice(0, -n))
    y1 = np.delete(y1, slice(0, -n))
    y2 = np.delete(y2, slice(0, -n))
else:
    pass

# データの時系列反転
x    = np.flipud(x)
y1   = np.flipud(y1)
y2   = np.flipud(y2)

# 図・座標軸の設定
fig = plt.figure(figsize=(10,6))
ax1 = fig.subplots()
ax2 = ax1.twinx()
fig.subplots_adjust(bottom=0.35)

# データのプロット
ax1.bar(x, y1,
 width=0.2, color="navy", label="時間雨量（mm）")
ax2.plot(x, y2,
 linestyle = "solid", linewidth = 1.0, c="red", marker='.', label="連続雨量（mm）")

# x軸,y軸の範囲
# 全自動
# ax1.set_ylim(0, max(y1)+10)
# ax2.set_ylim(0, max(y2)+50)
# 任意
ax1.set_ylim(0, 70)
ax2.set_ylim(0, 370)

# 軸ラベル名
ax1.set_ylabel('時間雨量（mm）', fontsize=10, labelpad=5)
ax2.set_ylabel('連続雨量（mm）', fontsize=10, labelpad=5)

# 軸メモリラベル
split_num = 10 #抽出間隔を指定
ax1.set_xticks(x[::split_num])
ax1.set_xticklabels(x[::split_num], rotation=90)

# 凡例の有無・大きさ・位置
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, fontsize=10, loc="upper left", edgecolor="black")

plt.show() 
