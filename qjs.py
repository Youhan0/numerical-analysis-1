# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:36:57 2018

@author: 23116207 Youhan0
"""


'''秦九韶算法'''
'''令y=3*x^5-2*x^3+x+7
   则y=((3*x^2-2)*x^2+1)*x+7'''
x=int(input("输入x:"))
N=5
a=[3,0,-2,0,1,7]
b=[3,0,0,0,0,0]
i=0
while i<N:
    b[i+1]=b[i]*x+a[i+1]
    i=i+1
print(b[N])


