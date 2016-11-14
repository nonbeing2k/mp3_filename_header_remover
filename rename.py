#-*- coding: utf-8 -*-

import os,sys, shutil

files = os.listdir('.')
for f in files:
    #print f
    t = f

    if ".mp3" in t:
        if ord(t[0]) < 65 :
            t = t[1:]
        if ord(t[0]) < 65 :
            t = t[1:]
        if ord(t[0]) < 65 :
            t = t[1:]
        if ord(t[0]) < 65 :
            t = t[1:]
        if ord(t[0]) < 65 :
            t = t[1:]
        if ord(t[0]) < 65 :
            t = t[1:]
        if ord(t[0]) < 65 :
            t = t[1:]

        print t
        os.rename (f,t)
