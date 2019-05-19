employe_list = ['warisha','sundus','ramsha','shayan','talha',3,5,7]
print("employe name is "+str(employe_list[6]))
employ_det=['warisha',21,'karachi']
print("Employe name is" +employ_det[0] +"Employe age is" +str(employ_det[1]) +"employe city is" +employ_det[2])
employ_det.append('Pakistan')
print(employ_det)
employ_det[2]='lahore'
print(employ_det)
employ_det.insert(1,'khan')
print(employ_det)
employ_det.pop()
print(employ_det)
del employ_det[2] #indexwise
print(employ_det)
employ_det.remove('khan') #valuewise
print(employ_det)
employ_det.pop(0)
print(employ_det)
city = employ_det.pop(0)
print(city)