
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
        balance_measure=[year,mass_balance,partial_measurement]
        self.mass_balance_measurement.append(balance_measure)


    def plot_mass_balance(self, output_path):
        raise NotImplementedError
    
    def get_id(self):
        return self.glacier_id
    
    def get_code(self):
        return self.code

        

from pathlib import Path
import csv

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
                Glacier_object=Glacier(row[2],row[1],row[0],float(row[5]),float(row[6]),digit)
                self.collectionObject.append(Glacier_object)
                
        print(0)
                
        
        

                
        

    def read_mass_balance_data(self, file_path):
        with file_path.open() as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                id=row[2]
                for glacier in self.collectionObject:
                    if glacier.get_id()==id:
                        glacier.add_mass_balance_measurement(row[3],row[11],row[6])
                
        print(0)



    def find_nearest(self, lat, lon, n):
        """Get the n glaciers closest to the given coordinates."""
        raise NotImplementedError
    
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
        raise NotImplementedError

    def summary(self):
        raise NotImplementedError

    def plot_extremes(self, output_path):
        raise NotImplementedError


def main():
    file_path = Path("sheet-A.csv")
    collection = GlacierCollection(file_path)
    # file_path_2=Path("sheet-EE.csv")
    # collection.read_mass_balance_data(file_path_2)
    collection.filter_by_code(638)

if __name__ == "__main__":
    main()