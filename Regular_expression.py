my_list=[]
file = open("regular.txt","r")
data=file.read()
numbers=[]
pattern = re.compile("(010|012)\d{7}")
matches=pattern.finditer(data)
for match in matches :
    start=match.span()[0]
    end = match.span()[1]
    numbers.append(data[start:end])
print(numbers)


mails=[]
pattern2 = re.compile("[a-zA-Z]+@[a-zA-Z]+\.[a-z]+")
matches2 = pattern2.finditer(data)
for match in matches2 :
    start=match.span()[0]
    end = match.span()[1]
    mails.append(data[start:end])
print(mails)


names=[]
pattern3 = re.compile(r"([a-zA-Z]+\s[a-zA-Z]+)")
matches3 = pattern3.finditer(data)
for match in matches3 :
    start=match.span()[0]
    end = match.span()[1]
    names.append(data[start:end])
print(names)




