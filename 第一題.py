

data = [] 
strlist = []
 
while True: 
 str = input()
 if str == "BREAK":
  break
 str = str.replace(" ","")
 strlist = str.split(",")
 data.append(strlist)
 
print(data)
#[['0.2', '1.1', '2.2', '3.3', '4.4'], ['1.3', '-1.1', '-3.3', '-2.2', '5.2'], ['3.5', '-0.7', '4', '3', '2'], ['-2.4', '8', '7', '2', '2'], ['1', '2', '3', '4'], ['2']]
d = int(data[-1][0])
print(d) #2
a = data[-2]
print(a) #['1', '2', '3', '4']
 
a2= []
for i in range(len(a)):
 a2.append(int(a[i]))
print(a2) #[1, 2, 3, 4]


total = 0
for i in a2:
 total += i
 
print(total) #

def discal(list): #丟入清單計算與A點距離
 sum = 0
 for i in range(1,len(list)):
  sum += 