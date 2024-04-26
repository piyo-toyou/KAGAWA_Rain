# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created on April 26 2024.
@author: W.OGURAHATA
SLACKに雨量警報を通知する。
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# モジュールのインポート
import pandas as pd
import numpy as np
import slackweb as sw

# メッセージを送るかどうかのチェック
def AlertCheck(df):
  last1_array = np.squeeze(df.iloc[0:1].values)
  last2_array = np.squeeze(df.iloc[1:2].values)

  last1_array_slice = last1_array[1::2]
  last2_array_slice = last2_array[1::2]

  last1_max = last1_array_slice.max()
  last1_max_index = last1_array_slice.argmax()
  last2_max = last2_array_slice[last1_max_index]

  if last1_max < 170: #最終計測雨量 < 170mm---->>何もしない
      return False, None
  elif 170 <= last1_max < 200 and last2_max < 170: #最終前計測雨量 < 170mm　かつ　最終計測雨量 < 200mm---->>170mm警報
      return True, 170
  elif 200 <= last1_max < 250 and last2_max < 200: #最終前計測雨量 < 200mm　かつ　最終計測雨量 < 250mm---->>200mm警報
      return True, 200
  elif 250 <= last1_max and last2_max < 250:
      return True, 250
  else:
      return False, None

# メッセージの作成 --- (*3)
def SendMessage(n):
  alert_message = "香川管内地区のどこかで連続雨量が{}mmを超えました。引き続き雨量情報に警戒してください。作成者：小倉畑\n\
    <参考雨量集計表>https://docs.google.com/spreadsheets/d/1-1W2_CG4r0xnTXq-EjOKqV0A8ZV88XI9/edit?usp=drive_link&ouid=101597215013316794281&rtpof=true&sd=true\n\
    <参考雨量サイト>https://www.skr.mlit.go.jp/road/mobile/M0712_37.html"

  # メッセージの送信
  ### 小倉畑DM slack = sw.Slack(url="https://hooks.slack.com/services/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")
  ### 新宮DM slack = sw.Slack(url="https://hooks.slack.com/services/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")
  #令和6年度香川管内防災点検PJ
  slack = sw.Slack(url="https://hooks.slack.com/services/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")
  slack.notify(text=alert_message.format(n))

