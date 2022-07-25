#!---------------------------------------------------------------------------------
def SetNumEducationStatus(status):
    for i in statuses:
        if status == statuses[i]:
            return int(i)
def SetNumLifeMain(main):
    if main == "False":
        return -1
    if main == "0":
        return -1
    return int(main)
def occupation_type_int(type):
    if type == 'university':
        return 0
    elif type == 'work':
        return 1
    return -1
def career_int(year):
    if year == 'False':
        return -1
    if year == '666':
        return -1
    return int(year)
def get_year(date):
    date = str(date)
    date = date.split(".")
    date = date[-1]
    
    if len(date) >= 4:
        return int(date)
    return -1
def education_form_int(form):
    if form == 'Full-time':
        return 1
    if form == 'Distance Learning':
        return 2
    if form == 'Part-time':
        return 3
    return -1

# df['education_status'] = df['education_status'].apply(SetNumEducationStatus)
# df['life_main'] = df['life_main'].apply(SetNumLifeMain)
# df['occupation_type'] = df['occupation_type'].apply(occupation_type_int)
# df['career_start'] = df['career_start'].apply(career_int)
# df['career_end'] = df['career_end'].apply(career_int)
# df['byear'] = bdate.apply(get_year)
# df['education_form'] = df['education_form'].apply(education_form_int)
# df['has_mobile'] = df['has_mobile'].apply(int)
# df['followers_count'] = df['followers_count'].apply(int)
# df['graduation'] = df['graduation'].apply(int)
# df['relation'] = df['relation'].apply(int)

# print(df['life_main'].value_counts())
# print(df.info())
# #----------------------------------

# #> Часть 2
# #--------------------------------------------------
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import confusion_matrix, accuracy_score

# x = df.drop('result', axis=1)
# y = df['result']

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

# sc = StandardScaler()
# x_train = sc.fit_transform(x_train)
# x_test = sc.transform(x_test)

# classifier = KNeighborsClassifier(n_neighbors=3)
# classifier.fit(x_train, y_train)

# y_pred = classifier.predict(x_test)

# percent = accuracy_score(y_test, y_pred) * 100

# print(percent)
# print(confusion_matrix(y_test, y_pred))