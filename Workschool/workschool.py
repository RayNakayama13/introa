# import pandas as pd
# school_df = pd.read_csv('/Users/raynakayama/Downloads/school.csv')
# print(school_df)
# school_df.info()
# Bob = school_df.query("name == 'Bob'")
# print(Bob)
# Age = school_df['age']
# MeanAge = Age.mean()
# MeanAge = MeanAge.round()
# print(MeanAge)
#
# school_df['weight'] = [29, 31, 33, 28, 29, 31, 27]
# print(school_df.head())
#
# school_df.to_csv('/Users/raynakayama/Downloads/school_add_weight.csv', index=False)
#

# import pandas as pd
# game1 = pd.read_csv('/Users/raynakayama/Downloads/game1.csv')
# game1 = game1.rename(columns={'cellphone': 'device_type'})
# print(game1.isnull().sum())
# print(game1)
# game1 = game1.dropna()
# print(game1)
# game1.to_csv('/Users/raynakayama/Downloads/game1_formatted.csv', index=False)
#
#
# import pandas as pd
#
# game2 = pd.read_csv('/Users/raynakayama/Downloads/game2.csv')
# game2 = game2.drop('ranking', axis=1)
# game2 = game2.fillna(0)
# print(game2)
# game2 = game2.sort_values('billing_amount(¥)', ascending=False)
# print(game2)
# game2.to_csv('/Users/raynakayama/Downloads/game2_formatted.csv', index=False)


# import pandas as pd
# kanto = pd.read_csv('/Users/raynakayama/Downloads/kanto.csv')
# kansai = pd.read_csv('/Users/raynakayama/Downloads/kansai.csv')
# # print(kanto)
# # print(kansai)
# kanto_kansai = pd.concat([kanto, kansai], sort=False)
# kanto_kansai2 = pd.concat([kanto, kansai], sort=True)
# kanto_kansai = kanto_kansai.reset_index(drop=True)
# kanto_kansai2 = kanto_kansai2.reset_index(drop=True)
# print(kanto_kansai)
# print(kanto_kansai2)
# kanto_kansai.to_csv('/Users/raynakayama/Downloads/kanto_kansai.csv', index=False)

#
# import pandas as pd
#
# class_ = pd.read_csv('Users/raynakayama/Downloads/class.csv')
# grade = pd.read_csv('Users/raynakayama/Downloads/grade.csv')
# print(class_)
# print(grade)
# class_grade = pd.merge(class_, grade, on=['student_number', 'name'], how='inner')
# print(class_grade)
# class_grade.to_csv('Users/raynakayama/Downloads/class_grade.csv', index=False)






#"titanic RandomForestClassifier"

# import numpy as np
# import pandas as pd
# import sklearn
#
# titanic = pd.read_csv('/Users/raynakayama/Downloads/titanic_text.csv')
# print(titanic.head())
# y = titanic['Survived']
# x = np.array(titanic.drop(["Survived", "PassengerId"], axis=1))
# y_array = np.array(y)
# # x_array = np.array(x)
# x_array = x
#
# # print(y_array.shape)
# # print(x_array.shape)
#
# from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test = train_test_split(x_array, y_array, test_size= 0.28, random_state=0)
# print(x_train.shape)
# print(y_train.shape)
# print(x_test.shape)
# print(y_test.shape)
# from sklearn.ensemble import RandomForestClassifier
#
# rfc = RandomForestClassifier(random_state=0)
#
# rfc.fit(x_train, y_train)
#
# y_pred = rfc.predict(x_test)
#
# from sklearn.metrics import accuracy_score
#
# result = accuracy_score(y_pred, y_test)
# print(result)


#"RandomForestClassifier Assignment::::"

# import numpy as np
# import pandas as pd
# import sklearn
#
# titanic = pd.read_csv('/Users/raynakayama/Downloads/titanic_text.csv')
# y = titanic['Survived']
# x = np.array(titanic.drop(['Survived', 'PassengerId'], axis=1))
# y_array = np.array(y)
# x_array = x
#
# from sklearn.model_selection import train_test_split
#
# x_train, x_test, y_train, y_test = train_test_split(x_array, y_array, test_size=0.2, random_state=0)
#
# from sklearn.ensemble import RandomForestClassifier
#
# rfc = RandomForestClassifier(random_state=0)
# rfc.fit(x_train, y_train)
# y_pred = rfc.predict(x_test)
#
#
#
# from sklearn.metrics import accuracy_score
#
# new_data = pd.read_csv('/Users/raynakayama/Downloads/titanic_assignment_question.csv')
# print(new_data.head())
# new_x = np.array(new_data.drop(['PassengerId'], axis=1))
# y_pred1 = rfc.predict((new_x))
# print(y_pred1.shape)
# print(y_pred)
# #y_predはPassengerId順で予測されたからそのままの順番でDateFrameを作ることができる。
#
# y_pred_assigment_submit = pd.DataFrame({'PassengerId': new_data['PassengerId'], 'Survived' : y_pred1})
# print(y_pred_assigment_submit.head())
# y_pred_assigment_submit.to_csv('/Users/raynakayama/Downloads/Y_pred.csv', index=False)


import pandas as pd
import numpy as np
import sklearn
#
houseprice = pd.read_csv('/Users/raynakayama/Downloads/houseprice_text.csv')
# print(houseprice.head())

y = houseprice['SalePrice']
x = np.array(houseprice.drop(['Id','SalePrice'], axis=1))
y_array = np.array(y)
x_array = x

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x_array, y_array, test_size=0.2, random_state=0)
# print(x_train.shape)
# print(x_test.shape)
# print(y_train.shape)
# print(y_test.shape)

from sklearn.ensemble import RandomForestRegressor

rfr = RandomForestRegressor(random_state=0)
rfr.fit(x_train, y_train)

y_pred = rfr.predict(x_test)

from sklearn.metrics import mean_squared_error
#二乗平均平方根誤差=root mean squared error
mse = np.sqrt(mean_squared_error(y_pred, y_test))
print(mse)
#この誤差内で価格を予測することができるという意味

x_test1 = pd.read_csv('/Users/raynakayama/Downloads/houseprice_assignment_question.csv')
print(x_test1.head())
x_test2 = np.array(x_test1.drop(['Id'], axis=1))
y_pred1 = rfr.predict(x_test2)

y_pred_assigment_submit = pd.DataFrame({'Id': x_test1['Id'], 'SalePrice': y_pred1})
print(y_pred_assigment_submit.head())

y_pred_assigment_submit.to_csv('/Users/raynakayama/Downloads/y_pred_assigment_submit.csv', index=False)
