import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dts

# csv 파일을 Pandas DataFrame으로 받고,
df = pd.read_csv('./fitbit_data.csv')
print(df.head())

# 1. 수집 기간동안의 평균 소모 칼로리, 평균 이동거리, 평균 step수를 출력해 보세요.
cals_mean = df['calories'].mean()
dist_mean = df['distances'].mean()
step_mean = df['steps'].mean()

print("The average of 'Calories' is", cals_mean)
print("The average of 'Distances' is", dist_mean)
print("The average of 'Steps' is", step_mean)

# 2. x축은 date, y축은 calories로 꺾은선 그래프를 그려 보세요.
fig = plt.figure(figsize = (15,9)) #글자가 다 보일 정도의 창 크기
graph_first = fig.add_subplot() #도화지를 만들어준다.
df['date'] = pd.to_datetime(df['date']) #인식하기 쉽도록 index를 datetime으로 바꾸어준다.

graph_first.plot(df['date'], df['calories'], marker = 'o', markersize=3 ) #x,y축에 해당하는 데이터들 넣어준다.

graph_first.set_title('<Calories Per Date>') #그래프의 제목
graph_first.set_xlabel('<Date>') #x축 레이블
graph_first.set_ylabel('<Calories>') #y축 레이블
graph_first.grid() #그래프에 격자 설정
graph_first.xaxis.set_major_locator(dts.MonthLocator(interval=1)) #x축 눈금이 너무 많아 한달 간격으로 하나씩만 그려지도록 함수 작성
plt.show()

# 3. 이동한 거리(distance)와 소모된 칼로리(calories)와의 관계를 알아보고자 합니다.
# x축은 distance, y축은 calories로 산점도를 그려보세요. (scatter plotting)
fig = plt.figure(figsize = (7,4))
graph_second = fig.add_subplot()
graph_second.scatter(df['distances'], df['calories'])
graph_second.set_title('<Calories Per Distance>') #그래프의 제목
graph_second.set_xlabel('<Distances>') #x축 레이블
graph_second.set_ylabel('<Calories>') #y축 레이블
graph_second.grid() #그래프에 격자 설정
plt.show()

# 요일 별로 소모 칼로리, 이동거리, 평균 steps 수를 분석해 보고 나름대로의 결론을 내려보세요.

#"요일별"이라는 단어 확인 -> weekday 함수 이용하여 요일 칼럼 추가
df['weekday'] = df['date'].dt.weekday
print(df.head())
df_dayname = df.groupby(by = 'weekday').mean()#요일을 인덱스로 가지는 df_dayname 데이터 프레임 만든다.
print(df_dayname)


fig = plt.figure(figsize = (13,5)) #그래프가 두개이므로 가로로 길게 생성한다.
fig.subplots_adjust(wspace=1)

graph_third_cal1 = fig.add_subplot(1,2,1) #첫번째 그래프를 위한 도화지 생성
graph_third_cal1.set_title('<Calories Per Steps>') #그래프 제목 설정
graph_third_cal1.grid() #그래프에 격자 설정
graph_third_cal1.plot(['Mon','Tue','Wed','Thu','Fri','Sat','Sun',], df_dayname['calories'], marker = 's', color = 'cornflowerblue', markersize=5, label = 'Calories')
graph_third_cal1.set_ylabel('<Calories>', fontsize = 15, color = 'cornflowerblue') #겹치지 않게 label 색, 폰트 지정

graph_third_steps = graph_third_cal1.twinx() # 한 그래프에 출력
graph_third_steps.plot(['Mon','Tue','Wed','Thu','Fri','Sat','Sun',], df_dayname['steps'], marker = 'o', color = 'lightpink', markersize=5, label = 'Steps')
graph_third_steps.set_ylabel('<Steps>', fontsize = 15, color = 'lightpink') #겹치지 않게 label 색, 폰트 지정

graph_third_cal1.legend(loc='upper left') #그래프별 이름 태그
graph_third_steps.legend(loc='upper right') #그래프별 이름 태그

graph_third_cal2 = fig.add_subplot(1,2,2) #두번째 그래프를 위한 도화지 생성
graph_third_cal2.set_title('<Calories Per distances>')#그래프 제목 설정
graph_third_cal2.grid() #그래프에 격자 설정
graph_third_cal2.plot(['Mon','Tue','Wed','Thu','Fri','Sat','Sun',], df_dayname['calories'], marker = 's', color = 'cornflowerblue', markersize=5, label = 'Calories')
graph_third_cal2.set_ylabel('<Calories>', fontsize = 15, color = 'cornflowerblue') #label 색, 폰트 지정

graph_third_distances = graph_third_cal2.twinx() # 한 그래프에 출력
graph_third_distances.plot(['Mon','Tue','Wed','Thu','Fri','Sat','Sun',], df_dayname['distances'], marker = 'o', color = 'orange', markersize=5, label = 'Distances')
graph_third_distances.set_ylabel('<Distances>', fontsize = 15, color = 'orange') #겹치지 않게 label 색, 폰트 지정

graph_third_cal2.legend(loc='upper left') #그래프별 이름 태그
graph_third_distances.legend(loc='upper right') #그래프별 이름 태그

plt.show()