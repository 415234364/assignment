
from numpy.lib.npyio import loadtxt
import utils

class Glacier:
    def __init__(self, glacier_id, name, unit, lat, lon, code):
        self.glacier_id=glacier_id
        self.name=name
        self.unit=unit
        self.lat=lat
        self.lon=lon
        self.code=code
        self.mass_balance_measurement=[]

        

    def add_mass_balance_measurement(self, year, mass_balance,partial_measurement):
        if validation_for_year(float(year)):
            balance_measure=[year,mass_balance,partial_measurement]
            self.mass_balance_measurement.append(balance_measure)


    def plot_mass_balance(self, output_path):
        raise NotImplementedError
    
    def get_id(self):
        return self.glacier_id
    
    def get_code(self):
        return self.code
    def get_latitude(self):
        return self.lat
    def get_lontitude(self):
        return self.lon
    def get_name(self):
        return self.name
    def get_mass(self):
        return self.mass_balance_measurement
        

from pathlib import Path
import csv

def validation_for_glacier(id,latitude,lontitude,unit):
    def is_number(s):
            try:
                int(s)
            except ValueError:
                return False
            return True
    if not(is_number(id)):
        return False
    if is_number(id):
        if len(id)!=5:
            raise ValueError("id should be a number with length of 5")
    if latitude>90 or latitude<-90 or lontitude>180 or lontitude<-180:
        raise ValueError("latitude should be in range of (-90,90),lontitude should be in range of (-180,180) ")
    if len(unit)!=2 and unit!=99:
        return False
    return True

def validation_for_measurement(unit,id,year):
    def is_number(s):
            try:
                int(s)
            except ValueError:
                return False
            return True
    if not(is_number(id)):
        return False
    if is_number(id):
        if len(id)!=5:
            return False
    if len(unit)!=2 and unit!=99:
        return False
    if year>2021 or not(year.is_integer()):
        return False
    return True

def validation_for_year(year):
    if year>2021 or not(year.is_integer()):
        return False
    return True
class GlacierCollection:

    def __init__(self, file_path):
        self.file_path=file_path
        self.collectionObject=[]
        with file_path.open() as file:          
             reader = csv.reader(file)
             next(reader)
            #  lines=len(list(reader))
             for row in reader:
                digit_str=row[7]+row[8]+row[9]
                digit=int(digit_str)
                if(validation_for_glacier(row[2],float(row[5]),float(row[6]),row[0])):
                    Glacier_object=Glacier(row[2],row[1],row[0],float(row[5]),float(row[6]),digit)
                    self.collectionObject.append(Glacier_object)
                
        print(0)
                
        
        

                
        

    def read_mass_balance_data(self, file_path):
        match_indication=0
        with file_path.open() as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                id=row[2]
                for glacier in self.collectionObject:
                    if glacier.get_id()==id:
                        if validation_for_measurement(row[0],row[2],float(row[3])):
                            glacier.add_mass_balance_measurement(row[3],row[11],row[6])
                        match_indication=1
                if match_indication==0:
                    print("no matching id for ",id)
                match_indication=0
                
        print(0)



    def find_nearest(self, lat, lon, n):
        """Get the n glaciers closest to the given coordinates."""
        temp_collection=[]
        for glacier in self.collectionObject:
            
            lat_2=glacier.get_latitude()
            lon_2=glacier.get_lontitude()
            temp=[glacier,utils.haversine_distance(lat,lon,lat_2,lon_2)]
            temp_collection.append(temp)
        
        def takeSecond(elem):
            return elem[1]
        temp_collection.sort(key=takeSecond)
        topn=temp_collection[:n]
        name=[]
        for entry in topn:
            name.append(entry[0].get_name())
        return name


    
    def filter_by_code(self, code_pattern):
        """Return the names of glaciers whose codes match the given pattern."""
        code_pattern=str(code_pattern)
        first_digit=code_pattern[0]
        second_digit=code_pattern[1]
        third_digit=code_pattern[2]
        first_iteration=[]
        second_iteration=[]
        third_iteration=[]
        for entry in self.collectionObject:
            code=entry.get_code()
            code_str=str(code)
            first_code=code_str[0]
            if(first_code==first_digit or first_code=='?'):
                first_iteration.append(entry)
        for entry in first_iteration:
            code=entry.get_code()
            code_str=str(code)
            second_code=code_str[1]
            if(second_code==second_digit or second_code=='?'):
                second_iteration.append(entry)
        for entry in second_iteration:
            code=entry.get_code()
            code_str=str(code)
            third_code=code_str[2]
            if(third_code==third_digit or third_code=='?'):
                third_iteration.append(entry)
        
        return third_iteration


    def sort_by_latest_mass_balance(self, n, reverse):
        """Return the N glaciers with the highest area accumulated in the last measurement."""
        temp_collection=[]
        def sortbyyear(elem):
            return int(elem[0])
        def is_number(s):
            try:
                float(s)
            except ValueError:
                return False
            return True
        for glacier in self.collectionObject:
            if glacier.get_mass() :
                mass_measurement=glacier.get_mass()
                mass_measurement.sort(key=sortbyyear,reverse=True)
                value=mass_measurement[0][1]
                if is_number(value):
                    temp=[glacier,float(value)]
                    temp_collection.append(temp)

        def sortbySecond(elem):
            return elem[1]
        if reverse==0:
            temp_collection.sort(key=sortbySecond)
        else :
            temp_collection.sort(key=sortbySecond,reverse=True)
        topn=temp_collection[:n]
        glacier_object=[]
        for entry in topn:
            glacier_object.append(entry[0])
        return glacier_object



    def summary(self):
        def sortbyyear(elem):
            return int(elem[0])
        def is_number(s):
            try:
                float(s)
            except ValueError:
                return False
            return True
        number=len(self.collectionObject)
        print("this collection has ",number," glaciers")
        earliest_year=3000
        number_of_decay=0
        number_of_recording=0
        for glacier in self.collectionObject:
            if glacier.get_mass():
                number_of_recording=number_of_recording+1
                mass_measurent=glacier.get_mass()
                for entry in mass_measurent:
                    year=entry[0]
                    if is_number(year):
                        if(int(year)<earliest_year):
                            earliest_year=int(year)
               
                mass_measurent.sort(key=sortbyyear,reverse=True)
                value=mass_measurent[0][1]
                if is_number(value):
                     if float(value)<0:
                        number_of_decay=number_of_decay+1

        percent=round(number_of_decay/number_of_recording*100)
        print("The earliest measurement was in ",earliest_year)
        print(percent,"% of glacier shrunk in their last measurement ")

    def plot_extremes(self, output_path):
        raise NotImplementedError


def main():
    file_path = Path("sheet-A.csv")
    collection = GlacierCollection(file_path)
    file_path_2=Path("sheet-EE.csv")
    collection.read_mass_balance_data(file_path_2)
    # collection.filter_by_code(638)
    # collection.find_nearest(0,0,5)
    # collection.sort_by_latest_mass_balance(5,1)
    collection.summary()

if __name__ == "__main__":
    main()