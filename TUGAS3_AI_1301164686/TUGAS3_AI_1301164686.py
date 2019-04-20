DataSetKompetensi = [61, 71, 64, 60, 73.5, 66.5, 82.5, 61, 52.5, 57.5, 72.5, 73.5, 50.5, 62.5, 62.5, 62.5, 68, 38, 52.5, 81, 72]
DataSetKepribadian = [37.5, 58.3, 35.8, 51.7, 75, 62.5, 15, 37.5, 54.2, 79.2, 56.7, 75, 70.8, 58.3, 60, 20.8, 82.5, 70.8, 61.7, 67.5]
DataSetHasil = ["Tidak", "Ya", "Tidak", "Tidak", "Ya", "Ya", "Tidak", "Tidak", "Tidak", "Ya", "Ya", "Ya", "Ya", "Tidak", "Tidak", "Tidak", "Ya", "Tidak", "Ya", "Ya"]

DataTestKompetensi = [61.5, 66.5, 71, 64.5, 57.5, 80, 81.5, 61, 46, 78]
DataTestKepribadian = [52.5, 58.3, 45.8, 55, 79.2, 45.8, 53.3, 64.2, 65.8, 49.2]
DataTestHasil = ["Tidak", "Tidak", "Tidak", "Tidak", "Tidak", "Tidak", "Tidak", "Tidak", "Tidak", "Tidak"]

def Fuzzy(a, b):
    kompetensi = a
    kompetensiKurang = 0
    kompetensiSedang = 0
    kompetensiTinggi = 0
    
    kepribadian = b
    kepribadianKurang = 0
    kepribadianSedang = 0
    kepribadianTinggi = 0
    
    y = 0 #yes
    yTemp = 0
    n = 0 #no
    nTemp = 0
    
    #fuzzification
    if (kompetensi <= 52.5):
        kompetensiKurang = 1
        kompetensiSedang = 0
        kompetensiTinggi = 0
    elif (kompetensi >= 72):
        kompetensiKurang = 0
        kompetensiSedang = 0
        kompetensiTinggi = 1
    elif (kompetensi == 64):
        kompetensiKurang = 0
        kompetensiSedang = 1
        kompetensiTinggi = 0
    elif (kompetensi > 52.5 and kompetensi < 64):
        kompetensiKurang = -(kompetensi-64)/(64-52.5)
        kompetensiSedang = (kompetensi-52.5)/(64-52.5)
        kompetensiTinggi = 0
    elif (kompetensi > 64 and kompetensi < 72):
        kompetensiKurang = 0
        kompetensiSedang = -(kompetensi-72)/(72-64)
        kompetensiTinggi = (kompetensi-64)/(72-64)
        
    if (kepribadian <= 54.2):
        kepribadianKurang = 1
        kepribadianSedang = 0
        kepribadianTinggi = 0
    elif (kepribadian >= 71):
        kepribadianKurang = 0
        kepribadianSedang = 0
        kepribadianTinggi = 1
    elif (kepribadian == 60):
        kepribadianKurang = 0
        kepribadianSedang = 1
        kepribadianTinggi = 0
    elif (kepribadian > 54.2 and kepribadian < 60):
        kepribadianKurang = -(kepribadian-60)/(60-54.2)
        kepribadianSedang = (kepribadian-54.2)/(60-54.2)
        kepribadianTinggi = 0
    elif (kepribadian > 60 and kepribadian < 71):
        kepribadianKurang = 0
        kepribadianSedang = -(kepribadian-71)/(71-60)
        kepribadianTinggi = (kepribadian-60)/(71-60)
            
    #inference
    if (kompetensiKurang != 0):
        if (kepribadianKurang != 0):
            nTemp = min(kompetensiKurang, kepribadianKurang)
            if (n < nTemp):
                n = nTemp
        if (kepribadianSedang != 0):
            nTemp = min(kompetensiKurang, kepribadianSedang)
            if (n < nTemp):
                n = nTemp
        if (kepribadianTinggi != 0):
            yTemp = min(kompetensiKurang, kepribadianTinggi)
            if (y < yTemp):
                y = yTemp
                
    if (kompetensiSedang != 0):
        if (kepribadianKurang != 0):
            nTemp = min(kompetensiSedang, kepribadianKurang)
            if (n < nTemp):
                n = nTemp
        if (kepribadianSedang != 0):
            nTemp = min(kompetensiSedang, kepribadianSedang)
            if (n < nTemp):
                n = nTemp
        if (kepribadianTinggi != 0):
            yTemp = min(kompetensiSedang, kepribadianTinggi)
            if (y < yTemp):
                y = yTemp
                
    if (kompetensiTinggi != 0):
        if (kepribadianKurang != 0):
            nTemp = min(kompetensiTinggi, kepribadianKurang)
            if (n < nTemp):
                n = nTemp
        if (kepribadianSedang != 0):
            yTemp = min(kompetensiTinggi, kepribadianSedang)
            if (y < yTemp):
                y = yTemp
        if (kepribadianTinggi != 0):
            yTemp = min(kompetensiTinggi, kepribadianTinggi)
            if (y < yTemp):
                y = yTemp
                
    #defuzzification
    sugeno = ((y*40) + (n*20))/(y + n)
    
    if (sugeno >= 22):
        hasil = 'Ya'
    else:
        hasil = 'Tidak'
    return hasil


print("HASIL DATA TRAIN")
countSet = 0
true = 0
while countSet < 20:
    data = DataSetHasil[countSet]
    ID = "P" + str(1+countSet)
    print(ID +" "+ DataSetHasil[countSet])
    if (Fuzzy(DataSetKompetensi[countSet], DataSetKepribadian[countSet]) == data):
        true = true + 1
    countSet = countSet + 1
    
print("\n" + "NILAI AKURASI DATA TRAIN : " + str((true/20)*100) +"\n")

print("HASIL DATA TEST")
countTest = 0
file = open("TebakanTugas3.csv", "w")
file.write("ID, TesKompetensi, Kepribadian, Hasil\n")
while countTest < 10:
    ID = "P" + str(21+countTest)
    DataSetHasil[countTest] = Fuzzy(DataTestKompetensi[countTest], DataTestKepribadian[countTest])
    print(ID +" "+ DataSetHasil[countTest])
    DataTebakan = str(ID) +","+ str(DataTestKompetensi[countTest]) +","+ str(DataTestKepribadian[countTest]) +","+ str(DataSetHasil[countTest]) +"\n"
    file.write(DataTebakan)
    countTest = countTest + 1
file.close
    


