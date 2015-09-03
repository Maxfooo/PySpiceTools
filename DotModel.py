'''
Created on Sep 3, 2015

@author: Max Ruiz
'''
from Tkinter import *
from DeviceParams import *


def mosfetDotModel(channel='NMOS',master=Toplevel()):
    mosfetTL = master
    cLabel = Label(mosfetTL,text = channel).pack()
    for params in mosfetParams:
        pFrame = Frame(mosfetTL)
        pLabel = Label(pFrame, text=params)
        pLabel.pack(side=LEFT)
        pEntry = Entry(pFrame, textvariable=mosfetParams[params])
        pEntry.pack(side=LEFT)
        pFrame.pack()
    pButton = Button(mosfetTL,text='Update',command= lambda: updateParams(mosfetParams))
    pButton.pack()
    mosfetTL.mainloop()


def updateParams(paramDict):
    for params in paramDict:
        print paramDict[params].get()


mosfetDotModel()
root.destroy()



