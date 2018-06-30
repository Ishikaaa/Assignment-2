#Q1.
import re
A=[]
emails = "zuck26@facebook.com  page33@google.com  jeff42@amazon.com"
a=re.findall("([\w\d]{1,22}[\w]{1,22}[\w]{1,5})",emails)
A.extend((tuple(a[0:3]),tuple(a[3:6]),tuple(a[6:9])))
print(A)

#Q2.
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
ee=re.findall('[Bb][\w]{1,20}',text)
print(ee)

#Q3.
import re
sentence = "A, very very; irregular_sentence"
ee1=re.sub("[;_:,]"," ",sentence)
print(ee1)

#4.
import re
def show1(tweet):
    tweet=re.sub("http\S+\s"," ",tweet)
    tweet=re.sub("RT|cc"," ",tweet)
    tweet=re.sub("#\S+"," ",tweet)
    tweet=re.sub("@\S+"," ",tweet)
    tweet=re.sub("[%s]" % re.escape(":!")," ",tweet)
    tweet=re.sub("\s+"," ",tweet)
    return tweet
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
print(show1(tweet))

