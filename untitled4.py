# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 11:32:49 2017

@author: lenovo_pc
"""

weight = float(input("Enter weight: "))
height = float(input("Enter height: "))
bmi = weight/height**2
print("Body mass index= ", bmi)
print(type(bmi))
bmi_int = int(bmi)
print(type(bmi_int))
print("BMI in integer: ", bmi_int)
