import pandas as pd
import numpy as np

# data = pd.read_csv('./spam.csv')
# # print(data)

# # print(data.columns)

# data.info()

# data['Spam'] = data['Category'].apply(lambda x: 1 if x == 'spam' else 0)
# # print(data.head())

from sklearn.feature_extraction.text import CountVectorizer

# vect = CountVectorizer()
# X = vect.fit_transform(data['Message'])
# w = vect.get_feature_names_out()


from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

# model = Pipeline([('vect', CountVectorizer()), ('NB', MultinomialNB())])
# # model = Pipeline([('vect', CountVectorizer()), ('NB', GaussianNB())])

# X_train, X_test, y_train, y_test = train_test_split(data['Message'], data['Spam'], test_size=0.3)

# model.fit(X_train, y_train)
# y_predict = model.predict(X_test)

from sklearn.metrics import accuracy_score

# # print(accuracy_score(y_predict, y_test))

# msg = [
#     'Hi! How are you?', 'free', 'win call us', 'call me this evening'
# ]

# # print(model.predict(msg))


# ----------------------------------- фишинг ---------------------------------------------


# data = pd.read_csv('./phishing.csv')
# # print(data.head())

# X = data.drop(columns='class')
# Y = pd.DataFrame(data['class'])
# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

from sklearn.tree import DecisionTreeClassifier

# dt = DecisionTreeClassifier()
# model = dt.fit(X_train, y_train)

# dt_predict = model.predict(X_test)


# ------------------------------------------------ парсинг ------------------------------------------------------------------

# html_content = """
# <html>
# <title>Data Science is Fun</title>

# <body>
#     <h1>Data Science is Fun</h1>
#     <div id='paragraphs' class='text'>
#         <p id='paragraph 0'>Paragraph 0
#             Paragraph 0 Paragraph 0 Paragraph 0 Paragraph 0 Paragraph 0 Paragraph 0
#             Paragraph 0 Paragraph 0 Paragraph 0 Paragraph 0 Paragraph 0 Paragraph 0
#             Paragraph 0 Paragraph 0 Paragraph 0 Paragraph 0 Paragraph 0 Paragraph 0
#             Paragraph 0 Paragraph 0 Paragraph 0 Paragraph 0 Paragraph 0 Paragraph 0
#             Paragraph 0 Paragraph 0 Paragraph 0 Paragraph 0 Paragraph 0 Paragraph 0
#             Paragraph 0 Paragraph 0 Paragraph 0 Paragraph 0 Paragraph 0 Paragraph 0
#             Paragraph 0 Paragraph 0 Paragraph 0 </p>
#         <p id='paragraph 1'>Paragraph 1
#             Paragraph 1 Paragraph 1 Paragraph 1 Paragraph 1 Paragraph 1 Paragraph 1
#             Paragraph 1 Paragraph 1 Paragraph 1 Paragraph 1 Paragraph 1 Paragraph 1
#             Paragraph 1 Paragraph 1 Paragraph 1 Paragraph 1 Paragraph 1 Paragraph 1
#             Paragraph 1 Paragraph 1 Paragraph 1 Paragraph 1 Paragraph 1 Paragraph 1
#             Paragraph 1 Paragraph 1 Paragraph 1 Paragraph 1 Paragraph 1 Paragraph 1
#             Paragraph 1 Paragraph 1 Paragraph 1 Paragraph 1 Paragraph 1 Paragraph 1
#             Paragraph 1 Paragraph 1 Paragraph 1 </p>
#         <p id='paragraph 2'>Here is a link to <a href='https://www.mail.ru'>Mail ru</a></p>
#     </div>
#     <div id='list' class='text'>
#         <h2>Common Data Science Libraries</h2>
#         <ul>
#             <li>NumPy</li>
#             <li>SciPy</li>
#             <li>Pandas</li>
#             <li>Scikit-Learn</li>
#         </ul>
#     </div>
#     <div id='empty' class='empty'></div>
# </body>

# </html>
# """

# from bs4 import BeautifulSoup as bs

# soup = bs(html_content, 'lxml')

# title = soup.find('title')
# # print(title)

# pList = soup.body.find_all('p')
# for i, p in enumerate(pList):
#     print(p.text)

# # print([bullet.text for bullet in soup.body.find_all('li')])

# p2 = soup.find(id='paragraph 2')

# divAll=soup.find_all('div')
# print(divAll)

# divClassText = soup.find_all('div')
# print(divClassText)

# soup.body.find(id='paragraph 0').decompose()
# soup.body.find(id='paragraph 1').decompose()

# print(soup.body.find(id='paragraphs'))

# new_p = soup.new_tag('p')
# print(new_p)

# new_p.string = 'Новое содержание'
# print(new_p)

# soup.find(id='empty').append(new_p)

# from urllib.request import urlopen

# url = 'https://ya.ru'
# html_content = urlopen(url).read()
# print(html_content[:1000])

# sp = bs(html_content, 'lxml')
# print(sp.title.text)
