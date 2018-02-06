code=input('Enter your code here: ')
#I canT DAnCE i CANt TAlK Hey
code_a=code.replace(" ","")
print(code_a)
from textwrap import wrap
code_b=wrap(code_a, 5)
if len(code_b[-1])<5:
    del code_b[-1]
print(code_b)
new_code=''
for a in code_b:
    for i in a:
        if i.islower()==True:
            new_code=new_code+'a'
        else:
            new_code=new_code+'b'
print(new_code)
res=''
def result(code):
    res=wrap(code,5)
    print(res)
    for ind in res:
        if ind=="baaab":
            print('w', end='')
        elif ind=="bbabb":
            print('i', end='')
        elif ind=="abbba":
            print('k', end='')
        else:
            break;
result(new_code)


