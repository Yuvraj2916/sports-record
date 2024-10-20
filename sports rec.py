import pickle
def writerecords():
    f=open("sports.dat","wb")
    for i in range(5):
        sprtno=int(input("Enter sports number:"))
        sprtnm=input("Enter sports name:")
        players=int(input("Enter the numbers of players:"))
        rec=[sprtno,sprtnm,players]
        pickle.dump(rec,f)
        print(rec)
    f.close()
writerecords()
