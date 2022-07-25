import pandas as pd
from textformat import ct
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')
#----------------------------------

langs = df['langs']
bdate = df['bdate']
ID = df['id']
last_seen = df['last_seen']
df.drop(['langs', 'bdate', 'last_seen'], axis=1, inplace=True)
df.drop(['id', 'city', 'people_main', 'has_photo', 'occupation_name'], axis=1, inplace=True)
#----------------------------------

statuses = {
    1: "Student (Bachelor's)",
    2: "Student (Specialist)",
    3: "Student (Master's)",
    4: "Alumnus (Bachelor's)",
    5: "Alumnus (Specialist)",
    6: "Alumnus (Master's)",
    7: "PhD",
    8: "Undergraduate applicant",
    9: "Candidate of Sciences",
}
life_mains = {
    0: "не указано",
    1: "семья и дети",
    2: "карьера и деньги",
    3: "развлечения и отдых",
    4: "наука и исследования",
    5: "совершенствование мира",
    6: "саморазвитие",
    7: "красота и искусство",
    8: "слава и влияние",
}


def divide(color=2, title=None):
    text = ct("=======================================================", color=color)
    if title != None:
        print(ct(f"\n[{title}]", c=3))
    print(text)
#----------------------------------------

print(df.head())

def SetTextMobile(has):
    if has == 1:
        return "Имеет"
    return "Не имеет"

def SetTextResult(result):
    if result == 1:
        return 'Купил'
    return "Не купил"

df['has_mobile'] = df['has_mobile'].apply(SetTextMobile)
df['result'] = df['result'].apply(SetTextResult)

test = df.groupby(by='education_form')['result'].value_counts()
print(test.plot(kind='pie'))

plt.show()
