from random import randint
import math

#------------------------------------------------------
"""
Essa função simula a estrutura a seguinte estrutura:
"SSID-1": ["mac-1","mac-2","mac-3","mac-4"]
"SSID-2": ["mac-2","mac-4","mac-6","mac-8"]
"""
#------------------------------------------------------
def lista_mac():
    listaMacs = []
    dicFreq = {}
    for m in range(1,1001):
       listaMacs.append("mac-" + str(m))
        #listaMacs = ["mac-1","mac-2","mac-3","mac-4","mac-5","mac-6","mac-7","mac-8","mac-9","mac-10"]
        

    #Crianando Dicionario com 10 SSIDs tendo valores Macs aleatórios.
    for i in range(1,500):
        listaMacs2 = []
        SSID = "SSID-" + str(i)

        for j in range(1,randint(2,500)):
            mac = listaMacs[randint(0,999)]
            
            if mac not in listaMacs2:
                if SSID == "SSID-2" and len(listaMacs2) > 1:
                    continue
                elif SSID == "SSID-6" and len(listaMacs2) > 1:
                    continue
                listaMacs2.append(mac) 
        dicFreq[SSID] = listaMacs2
        print(SSID +" - " +str(len(listaMacs2)))
    a = {"BD":dicFreq,"QTD_MACS":len(listaMacs)}
    print(len(listaMacs))
    return(a)

#Função que calcula a frequecia do SSID dada por fz = |Xz∈x| / |F| , onde F é o total de Fingersprint e um SSID pertencente a Fingersprint X
def calcular_Frequencia(ssid,dicionario_de_retorno):
    #dicionario_de_retorno = lista_mac()
    freq_SSID = dicionario_de_retorno["BD"] 
    qtdMacs = dicionario_de_retorno["QTD_MACS"] 
    return len(freq_SSID[ssid])/qtdMacs

def Psimq(fingersprint1,fingersprint2,dic):
    
    #
    fp_SSID1 = list(fingersprint1.values())[0]
    fp_SSID2 = list(fingersprint2.values())[0]
    print(fp_SSID1)
    print(fp_SSID2)
    intercessao = list(set(fp_SSID1) & set(fp_SSID2))

    if len(intercessao) > 0:
        metrica = 0
        for i in range(len(intercessao)):
            frequencia = calcular_Frequencia(intercessao[i],dic)
            print(frequencia)
            metrica+= 1/(frequencia)**3
            print(1/(frequencia)**3)
        print(metrica)



def IDF(fingersprint1,fingersprint2,dic):
    fp_SSID1 = list(fingersprint1.values())[0]
    fp_SSID2 = list(fingersprint2.values())[0]
    print(fp_SSID1)
    print(fp_SSID2)
    intercessao = list(set(fp_SSID1) & set(fp_SSID2))

    if len(intercessao) > 0:
        metrica = 0
        metrica2 = 0
        metrica3 = 0
        for i in range(len(intercessao)):
            frequencia = calcular_Frequencia(intercessao[i],dic)
            print(frequencia)
            metrica+= (math.log(frequencia))**2
            #print(1/(frequencia)**3)
        print("METRICA - 0")
        print(metrica)

        for i in range(len(fp_SSID1)):
            frequencia = calcular_Frequencia(fp_SSID1[i],dic)
            print(frequencia)
            metrica2+= (math.log(frequencia))**2
            #print(1/(frequencia)**3)
        print("METRICA - 1")
        print(metrica2)

        for i in range(len(fp_SSID2)):
            frequencia = calcular_Frequencia(fp_SSID2[i],dic)
            print(frequencia)
            metrica3+= (math.log(frequencia))**2
            #print(1/(frequencia)**3)
        print("METRICA - 3")
        print(metrica3)

        cosineIDF = metrica/(math.sqrt(metrica2)*math.sqrt(metrica3))
        print("COSINE IDF:")
        print(cosineIDF)

    

    
    
    
    #print("aaaaaaaaaaaaaa")
    #mac1 = mac1[0]
    #print("aaaaaaaaaaaaaa")
    #conjunto_SSID1 = fingersprint1[mac1]
   # print(conjunto_SSID1)


#calcular_Frequencia("SSID-1")
#calcular_Frequencia({"mac-1":["SSID-1","SSID-2","SSID-3","SSID-4","SSID-5","SSID-6"]},{"mac-2":["SSID-2","SSID-6","SSID-7","SSID-8","SSID-9"]})

#IDF({"mac-1":["SSID-1","SSID-2","SSID-3","SSID-4","SSID-5","SSID-6"]},{"mac-2":["SSID-2","SSID-6","SSID-7","SSID-8","SSID-9"]},lista_mac())
IDF({"mac-1":["SSID-1","SSID-2","SSID-3","SSID-4","SSID-5","SSID-6"]},{"mac-2":["SSID-1","SSID-2","SSID-3","SSID-4","SSID-5","SSID-9"]},lista_mac())

#Psimq({"mac-1":["SSID-1","SSID-2","SSID-3","SSID-4","SSID-5","SSID-6"]},{"mac-2":["SSID-2","SSID-6","SSID-7","SSID-8","SSID-9"]},lista_mac())
