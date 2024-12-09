import pickle
class CarRecord:
    def __init__(self):
        self.VehicleID=""
        self.Registration=""
        self.DateOfRegistration=None
        self.EngineSize=0
        self.PurchasePrice=0.00
ThisCar=CarRecord()
#store records to the file by determining a hash value for each
CarFile=open('CarFile.DAT','rb+')
Address=hash(ThisCar.VehicleID)
CarFile.seek(Address)
pickle.dump(ThisCar,CarFile)
CarFile.close()
#load a record at a given hash value to the file
CarFile=open('CarFile.DAT','rb')
VehicleID=input("What is the vehicle id of the record you would like to access")
try:
    Address = hash(VehicleID)
    CarFile.seek(Address)
    ThisCar = pickle.load(CarFile)
except:
    print("VehicleID does not exist for a record")
CarFile.close()