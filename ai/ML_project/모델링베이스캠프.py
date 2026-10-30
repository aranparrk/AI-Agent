import pandas as pd

# 조건1. 학습 데이터를 읽어서 최초 2개 데이터 출력
print("=" * 50)
df = pd.read_csv("모델링베이스캠프.csv")
print("최초 2개 데이터 출력")
print(df.head(2))
print("=" * 50)

# 조건2. 전체 데이터 수 출력
print("전체 데이터 수 : ", len(df))
print("=" * 50)

# 조건3. 분류 모델 학습 및 성능 평가
x = df.drop(columns=["result"])
y = df["result"]

from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    x, y, stratify=y, random_state=42
)

from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()
kn.fit(train_input, train_target)

from sklearn.metrics import f1_score

pred = kn.predict(test_input)

f1 = f1_score(test_target, pred, pos_label="good")

print("F1 점수 :", f1)

from sklearn.model_selection import cross_val_score
from sklearn.metrics import make_scorer

scores = cross_val_score(
    kn, train_input, train_target,
    cv=5,
    scoring=make_scorer(f1_score, pos_label="good")
)

print("교차검증 평균 F1 점수 :", scores.mean())
print("=" * 50)

# 조건4. 임의의 데이터로 good/bad 예측
new_data = pd.DataFrame(
    [[6, 85, 80, 5, 7]],
    columns=x.columns
)

result = kn.predict(new_data)

print("예측 결과 :", result[0])
