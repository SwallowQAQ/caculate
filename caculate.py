from fractions import *
import random
def main():
    print('输入题目的数量:')
    n = int(input())
    print('输入运算符的数量（建议2或3）:')
    fn = int(input())
    print("本次共 {} 题,满分 100 分".format(n))
    flag=0
    for i in range(n):
        while 1:
            ex = expression(fn)
            an=eval(js(ex))
            s=str(an)
            if '.' in s:
                continue
            if an>0:
                if '/'in s:
                    if an >1:
                        continue
                a=''.join(ex)
                print(a)
                if eval(input())==an:
                    flag+=1
                    print('回答正确！')
                else:
                    print("回答错误！,正确答案是{}".format(an))
                break
    print("共答对{}题,本次得分：{}".format(flag,round(100/n*flag)))
def expression(n):
    f = ['+','-','*','÷','/']
    fl = []
    ex = []
    pren = 0
    pre = ''
    for i in range(n+1):
        if pre == '÷':
            pren = random.randint(1, 20)
            pre = f[random.randint(0, 2)]
        elif pre == '/':
            pren = random.randint(1, 20)
            pre = f[random.randint(0, 2)]
            ex.append(str(pren))
            ex.append(pre)
            pren = random.randint(1, 20)
            pre = f[random.randint(0, 2)]
        else:
            pren = random.randint(1, 20)
            pre = f[random.randint(0, 4)]
        ex.append(str(pren))
        ex.append(pre)
    ex[-1] = '='
    return ex
def js(s):
    f = ['+', '-', '*', '÷', '/']
    l=len(s)
    jg=''
    for i in range(0,int(l/2)-1):

        if s[2*i+1] in f[:4]:
            if i==0:
                jg=jg+s[0]
            if s[2*i+3] =='/':
                if s[2*i+1] =='÷':
                    jg = jg + '/'
                else:
                    jg=jg+s[2*i+1]
            else:
                if s[2*i+1] =='÷':
                    jg = jg + '/'+ s[2*i+2]
                else:
                    jg = jg +s[2*i+1]+ s[2*i+2]
        else:
            jg=jg+'Fraction('+s[2*i]+','+s[2*i+2]+')'
    return str(jg)
main()

