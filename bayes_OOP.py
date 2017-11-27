#M Tafaquh Fiddin Al Islami
#2110151035 | 3 D4ITB
#Electronic Engineering Polytechnic Institute of Surabaya

#Bayes Method

from operator import attrgetter
from mpl_toolkits.mplot3d import Axes3D
import math
import struct
import matplotlib.pyplot as plt
import numpy as np

class Data(object):
    def __init__(self, weather, temperature, wind, sport):
        self.__weather = weather
        self.__temperature = temperature
        self.__wind = wind
        self.__sport = sport
        
    def printValue(self):
        weather = str(self.__weather)
        temperature = str(self.__temperature)
        wind = str(self.__wind)
        sport = str(self.__sport)
        return(weather+"\t\t"+temperature+"\t\t"+wind+"\t\t"+sport)

    def setWeather(self, weather):
        self.__weather = weather
    def getWeather(self):
        return self.__weather

    def setTemp(self, temperature):
        self.__temperature = temperature
    def getTemp(self):
        return self.__temperature

    def setWind(self, wind):
        self.__wind = wind
    def getWind(self):
        return self.__wind

    def setSport(self, sport):
        self.__sport = sport
    def getSport(self):
        return self.__sport

def probability(data, list_data):
    weatherYes = 0
    weatherNo = 0
    tempYes = 0
    tempNo = 0
    windYes = 0
    windNo = 0
    yes = 0
    no = 0
    
    for i in range(0, len(list_data)):
        if((list_data[i].getWeather() == data.getWeather())
           and list_data[i].getSport() == "Ya"): weatherYes += 1
        if((list_data[i].getWeather() == data.getWeather())
           and list_data[i].getSport() == "Tidak"): weatherNo += 1
        if((list_data[i].getTemp() == data.getTemp())
           and list_data[i].getSport() == "Ya"): tempYes += 1
        if((list_data[i].getTemp() == data.getTemp())
           and list_data[i].getSport() == "Tidak"): tempNo += 1
        if((list_data[i].getWind() == data.getWind())
           and list_data[i].getSport() == "Ya"): windYes += 1
        if((list_data[i].getWind() == data.getWind())
           and list_data[i].getSport() == "Tidak"): windNo += 1

        if(list_data[i].getSport()=="Ya"): yes += 1
        else: no += 1
        
    probYes = yes / len(list_data)
    probNo = no / len(list_data)

    if(not(data.getWeather() == "")):
        probYes = probYes * (weatherYes / yes)
        probNo = probNo * (weatherNo / no)
    if(not(data.getTemp() == "")):
        probYes = probYes * (tempYes / yes)
        probNo = probNo * (tempNo / no)
    if(not(data.getWind() == "")):
        probYes = probYes * (windYes / yes)
        probNo = probNo *(windNo / no)

    probYes *= 100
    probNo *= 100
    if(probNo == 0 and probYes > 0):
        print("We suggest you to Go.\n%.2f %% people will go to sport today"% probYes)
    elif(probNo > 0 and probYes == 0):
        print("We suggest you not to Go.\n%.2f %% people will not to go to sport today"% probNo)
    elif(probYes == 0 and probNo == 0):
        print("We suggest you 100%% not to go")
    else :
        print("We suggest you to %.2f %% Go and %.2f %% Not to Go for Sport Activities"%(probYes,probNo));


def main():
    list_training = []

    list_training.append(Data("Cerah", "Normal", "Pelan", "Ya"));
    list_training.append(Data("Cerah", "Normal", "Pelan", "Ya"));
    list_training.append(Data("Hujan", "Tinggi", "Pelan", "Tidak"));
    list_training.append(Data("Cerah", "Normal", "Kencang", "Ya"));
    list_training.append(Data("Hujan", "Tinggi", "Kencang", "Tidak"));
    list_training.append(Data("Cerah", "Normal", "Pelan", "Ya"));
    list_training.append(Data("Cerah", "Tinggi", "Kencang", "Tidak"));

    loop = True
    while loop:
        weather = input("Bagaimana cuaca hari ini <Cerah/Hujan/Abstain>? ")
        if(weather == "Abstain"):weather = str("")
        temp = input("Bagaimana suhu temperatur hari ini <Normal/Tinggi/Abstain>? ")
        if(temp == "Abstain"):temp = str("")
        wind = input("Bagaimana kecepatn angin hari ini <Pelan/Kencang/Abstain>? ")
        if(wind == "Abstain"):wind = str("")
        
        data_test = Data(str(weather), str(temp), str(wind), "")
        
        probability(data_test, list_training)

        if(input("\nWanna try more data training <y/n>? ") == 'y'): loop = True
        else: loop = False
    
    #data_test = Data("Cerah", "Normal", "", "")
    #probability(data_test, list_training)
    

if __name__ == '__main__':
    main()
