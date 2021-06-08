
import numpy as np
import matplotlib.pyplot as mpl


def grid(ls=np.array([[43.356819, 5.482127],[43.374439, 5.345074],[43.253117, 5.387901],[43.292301, 5.453946]])):
    mpl.subplot(1,2,1)
    mpl.scatter(ls[:,0],ls[:,1],s=[1,10,30,70])

    lst=[]
    P=ls[0,:]
    v1=ls[1,:]-ls[0,:]
    v2=ls[3,:]-ls[0,:]
    v3=ls[2,:]-ls[1,:]
    sv=0
    ss=[]
    for i in range(10):
        for j in range(10):
            q1=(P+i*v2/9)
            q2=(P+v1+i*v3/9)
            q3=q1+j*(q2-q1)/9
            lst.append(q3)
            sv+=1
            ss.append(sv)
    lst=np.array(lst)
    mpl.subplot(1,2,2)
    mpl.scatter(lst[:,0],lst[:,1],s=ss)
    mpl.scatter(ls[:,0],ls[:,1],c=["black"])