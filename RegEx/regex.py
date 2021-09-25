import re
#find the hidden word
string=""" Papu aaj sath tere aayega """
regex=r'\b[a-z|A-Z]'  #here we use \b
# r here represents raw string
numbers=re.findall(regex,string)
print(numbers)

regex=r'^\d{2}[a-z]{4}[A-Z]{2}$'
string="66ahgjAJ"

#starts with 2 digits, is followed by 4 lowercase letters, ends with 2 upper case letters'
if(re.match(regex,string)):
  print("Valid")
else:
  print("Invalid")

#replace a with @
string="rashi ravan rohan"
list=re.sub(r'a','@',string) #syntax=re.sub(regex,replacement,string)
print(list)
ls=re.sub(r'a','@',string,2) #syntax=re.sub(regex,replacement,string,count) count=number of times u wanna replace
print(ls)

#split the string at a .
string="This is a sring. It is an array of characters."
regex=r'\.'
ls=re.split(regex,string)
print(ls)

# EXERCISES:

# 1)find code here: key= pick last letter of every word "antartica arm asia buzz zindagi modern bag "

# 2)replace all z with % "I crossed the road using zebra crossing on a zebra"

#Q1)
string=" antartica arm asia buzz zindagi modern bag "
regex=r'[a-z | A-Z]\s'
ls=re.findall(regex,string)
print(ls)

#2)
string="I crossed the road using zebra crossing on a zebra"
ls=re.sub(r'z','%',string)
print(ls)

# QUESTION

# Extract Phone numbers(10 digit) and Emails and save them in two different lists. Print those lists.

# """Rashi Number: 8291883287 Email: rashi@gmail.com Rahul Number: 9930665880 Email: rahul@gamil.com Rutuja Number: 9822365478 Email: rutuja@gmail.com 
# RIshi Number: 8766343265 Email: rishi@somaiya.edu"""

import re
string="""Rashi Number: 8291883287 Email: rashi250@gmail.com
          Rahul Number: 9930665880 Email: rahul58@curiosity.org 
          Rutuja Number: 9822365478 Email: rutu54ja@gmail.com 
          Rishi Number: 8766343265 Email: 290rishi@somaiya.edu """
regex=r'\d{10}'
regex2=r'\S+@\S*\.\S{3}'

numbers=re.findall(regex,string)
emails=re.findall(regex2,string)

print(numbers)
print("\n")
print(emails)

