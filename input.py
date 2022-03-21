#radius = int(input("dairenin yaricapini giriniz:"))
#alan = 3*(radius**2)
#print("dairenin alani : ",alan)



'''
adi = input("adiniz")
soyadi = input("Soyadiniz")
adresi = input("adresiniz")
sehir = input("sehriniz")

print("adi: {}\nSoyadi: {}\nAdres: {}\nSehir: {}".format(adi,soyadi,adresi,sehir))
'''


time = float(input("give second: "))

day = time//(60*60*24)
time = time%(60*60*24)
hour = time//(60*60)
time = time%(60*60)
minute = time//(60)
time %= (60)
second = time

print("day: {}\nhours: {}\nminutes: {}\nsecond: {}".format(day,hour,minute,second))
print("day:hour:minute:second->%d:%d:%d:%d"%(day,hour,minute,second))