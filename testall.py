# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:57:39 2018

@author: haodada
"""
import os,sys
import numpy
import matplotlib
import scipy
import argparse
import datetime
import imutils
import time
import cv2
#通过cv直接读取视频文件
camera=cv2.VideoCapture('myfile.avi')
# 创建参数解析器并解析参数
"""
#ap = argparse.ArgumentParser()
#ap.add_argument("-v", "--video", help="path to the video file")
##python testmotion.py -v D:\学习\毕业设计\myfile.avi
#args = vars(ap.parse_args())
## 如果video参数为None，那么我们从摄像头读取数据
#if args.get("video", None) is None:
#    camera = cv2.VideoCapture(0)#将camera指向第一个硬件相机
#    time.sleep(0.25)
## 否则我们读取一个视频文件
#else:
#    #通过cv直接读取视频文件
#    camera = cv2.VideoCapture(args["video"])
"""
firstFrame=None#初始化第一帧
fgbg=cv2.createBackgroundSubtractorMOG2()#初始化背景图
peoplenum=0
while True:
    ret1,frame=camera.read()#frame为当前帧
    if not ret1:#判断是否到视频的结尾，并跳出循环
        break
    frame=imutils.resize(frame,width=500,height=300)#调整图片压缩比
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)#调整高斯模糊
    if firstFrame is None:
        firstFrame=gray#第一帧的赋值
        continue
    #cv2.imshow('frame',gray)
    frameDelta=cv2.absdiff(firstFrame, gray)#计算当前帧与第一帧的差值
    ret2,thresh=cv2.threshold(frameDelta,25,255,cv2.THRESH_BINARY)#调整二值化
    thresh = cv2.dilate(thresh,None,iterations=2)#调整膨胀参数
    cnts=cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    print cnts
    cv2.imshow('frame',thresh)
    k=cv2.waitKey(300)&0xff
    if k==27:
        break
camera.release()
cv2.destroyAllWindows()