// random password generater using python
improt.random
def.paswardGenerator():
lowerchars=['a','b','c','d']
upperchars=['A','B','C','D']
specialchars=['&','*',',','!']
numericchars=['1','2','3','4']
password =[random.choice(lowerchars)+random.choice(upperchars)+random.choice(specialchars)+random.choice(numericchars) ]
passward=password + password
return password
