import glob

import pandas as pd
from pandas import DataFrame

import json

test_data_path = glob.glob('C:/Users/user/git/SpeedWagon/data/한국어대화요약_valid/*')
train_data_path = glob.glob('C:/Users/user/git/SpeedWagon/data/한국어대화요약_train/*')

def transformType(train_data_path):
  train = pd.DataFrame()
  for train_data in train_data_path:
    with open(train_data) as data_path:
      data = json.load(data_path) # 데이터 파일 불러옴
      for i in range(len(data['data'])): # 해당 주제의 dialogue
        text = "" # 대화 속 텍스트 저장
        for j in range(len(data['data'][i]['body']['dialogue'])): # j번째 화자가 한 말
          text += data['data'][i]['body']['dialogue'][j]['utterance'] + " "
        train = pd.concat([train, pd.DataFrame({'Text' : text[:-1], 'Summary' : data['data'][i]['body']['summary'], 'Topic' : data_path.name.split('/')[6].split('.')[0]}, index = [i])])
  return train

valid = transformType(test_data_path)
train = transformType(train_data_path)

valid.to_csv('/content/drive/MyDrive/BOAZ_miniProject2/valid.csv', index = False)
train.to_csv('/content/drive/MyDrive/BOAZ_miniProject2/train.csv', index = False)