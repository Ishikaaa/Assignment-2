# Q1
import pandas as pd
for i in range(5):
    a = str( input( "enter name" ) )
    age = int( input( "enter age" ) )
    mail = input( "enter mail" )
    phoneno = int( input( "enter phone no" ) )
data={'name':a,'age':age,'mail id':mail,'phone no':phoneno}
df=pd.DataFrame(data,index=['rank1','rank2','rank3','rank4','rank5'])
print(df)

# Q2
import pandas as pd
d=pd.read_csv('sample1.csv')
print(d)
# a)
print(d.head(5))

#b)
print(d.head(10))

#c)
print(d.sum(axis=0))
print(d.sum(axis=1))
print(d.mean(axis=0))
print(d.mean(axis=0))
print(d.describe())
print(d.count())

#d)
print(d.tail(5))

#e)
print(d['Location'].sum())
print(d['Location'].describe())
print("Location"+str(d['Location'].count())+"times")