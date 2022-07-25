import pandas as pd
df = pd.read_csv('train.csv')
df = df.dropna()
print(df.info())


df.drop(['Mjob', 'Fjob'], axis = 1, inplace = True)

def sex_apply(sex):
    if sex == 'M':
        return 0
    if sex == 'F':
        return 1

def edu_apply(edu):
    if edu == 'none':
        return 0
    if edu == 'primary education (4th grade)':
        return 1
    if edu == '5th to 9th grade':
        return 2
    if edu == 'secondary education':
        return 3
    if edu == 'higher education':
        return 4

def yes_no_apply(yesno):
    if yesno == 'yes':
        return 0
    if yesno == 'no':
        return 1

def address_apply(address):
    if address == 'Urban':
        return 0
    if address == 'Rural':
        return 1

def fam_size_apply(famsize):
    if famsize == 'greater than 3 persons':
        return 0
    if famsize == '3 persons or less':
        return 1

def reason_apply(reason):
    if reason == 'course':
        return 0
    if reason == 'home':
        return 1
    if reason == 'reputation':
        return 2
    if reason == 'other':
        return 3

def guardian_apply(guardian):
    if guardian == 'mother':
        return 0
    if guardian == 'father':
        return 1
    if guardian == 'other':
        return 2

def famrel_apply(famrel):
    if famrel == 'very bad':
        return 0
    if famrel == 'bad':
        return 1
    if famrel == 'normal':
        return 2
    if famrel == 'good':
        return 3
    if famrel == 'excellent':
        return 4

def freetime_apply(freetime):
    if freetime == 'very low':
        return 0
    if freetime == 'low':
        return 1
    if freetime == 'medium':
        return 2
    if freetime == 'high':
        return 3
    if freetime == 'very high':
        return 4

def traveltime_apply(traveltime):
    if traveltime == 'less than 15 min.':
        return 0
    if traveltime == '15 to 30 min.':
        return 1
    if traveltime == '30 min. to 1 hour':
        return 2
    if traveltime == 'more than 1 hour':
        return 3

def studytime_apply(studytime):
    if studytime == 'less than 2 hours':
        return 0
    if studytime == '2 to 5 hours':
        return 1
    if studytime == '5 to 10 hours':
        return 2
    if studytime == 'more than 10 hours':
        return 3

df['sex'] = df['sex'].apply(sex_apply)
df['Medu'] = df['Medu'].apply(edu_apply)
df['Fedu'] = df['Fedu'].apply(edu_apply)
df['address'] = df['address'].apply(address_apply)
df['famsize'] = df['famsize'].apply(fam_size_apply)
df['reason'] = df['reason'].apply(reason_apply)
df['guardian'] = df['guardian'].apply(guardian_apply)
df['schoolsup'] = df['schoolsup'].apply(yes_no_apply)
df['famsup'] = df['famsup'].apply(yes_no_apply)
df['paid'] = df['paid'].apply(yes_no_apply)
df['activities'] = df['activities'].apply(yes_no_apply)
df['nursery'] = df['nursery'].apply(yes_no_apply)
df['higher'] = df['higher'].apply(yes_no_apply)
df['internet'] = df['internet'].apply(yes_no_apply)
df['famrel'] = df['famrel'].apply(famrel_apply)
df['freetime'] = df['freetime'].apply(freetime_apply)
df['traveltime'] = df['traveltime'].apply(traveltime_apply)
df['studytime'] = df['studytime'].apply(studytime_apply)

print(df.info())



from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

i = 0
aver_result = 0

while i<5:
    x = df.drop('result', axis = 1)
    y = df['result']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.4)

    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)

    classifier = KNeighborsClassifier(n_neighbors = 5)
    classifier.fit(x_train, y_train)

    y_pred = classifier.predict(x_test)
    print('Процент правильно предсказанных исходов:', accuracy_score(y_test, y_pred) * 100)
    aver_result += accuracy_score(y_test, y_pred) * 100
    print('Confusion matrix:')
    print(confusion_matrix(y_test, y_pred))
    i+=1
print('Процент правильно предсказанных исходов:', aver_result/5)