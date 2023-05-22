from hanspell import spell_checker
import re

import pandas as pd

train = pd.read_csv('C:/Users/user/git/SpeedWagon/train.csv')
valid = pd.read_csv('C:/Users/user/git/SpeedWagon/valid.csv')

def preprocess(text):
  text = text.lower() # 영어 텍스트를 소문자로 변환
  text = re.sub(r'[ㄱ-ㅎㅏ-ㅣ]+[/ㄱ-ㅎㅏ-ㅣ]', '', text) # 반복되는 자음, 모음 제거 (ex. ㅋㅋ ㅠㅠ)
  text = spell_checker.check(text).checked # 맞춤법 검사
  text = re.sub(r'\.{3,}', '..', text) # .이 3개 이상 반복되면 2개로 변환 
  text = re.sub(r'\?{2,}', '?', text) # ?이 2개 이상 반복되면 1개로 변환
  text = re.sub(r'\!{2,}', '!', text) # !이 2개 이상 반복되면 1개로 변환
  text = re.sub(r'\~{2,}', '~', text) # ~이 2개 이상 반복되면 1개로 변환
  text = re.sub(r'[" "]+', " ", text) # 공백 여러 개를 1개로 변환
  text = text.strip() # 양쪽 공백 제거
  return text

preprocess(train.iloc[2,0])

for i in range(train.shape[0]):
  try:
    train.iloc[i,0] = preprocess(train.iloc[i,0])
  except:
    print(i, "번째 error")

for i in range(valid.shape[0]):
  try:
    valid.iloc[i,0] = preprocess(valid.iloc[i,0])
  except:
    print(i, "번째 error")

train.to_csv('C:/Users/user/git/SpeedWagon/train_전처리.csv', index = False)
valid.to_csv('C:/Users/user/git/SpeedWagon/valid_전처리.csv', index = False)