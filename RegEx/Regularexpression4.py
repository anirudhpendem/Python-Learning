import re

text = 'python java ruby javascript HTML Css '
print(text.split() ,"\n")

text1 = 'python, java, ruby, javascript, HTML, Css '
print(text1.split(',') ,"\n")

text2 = 'python:java:ruby:javascript:HTML:Css '
print(text2.split(':') ,"\n")

text3 = 'CatBatSatDogTigerLigontFatRatShutCut'
print(text3.split('t'), "\n")

print(text1.split(',',0), "\n")
print(text1.split(',',4), "\n")
print(text1.split(',',3),"\n")


