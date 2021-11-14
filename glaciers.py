
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
        print(self.mass_balance_measurement[0])

    def plot_mass_balance(self, output_path):
        raise NotImplementedError
    
    def get_id(self):
        return self.glacier_id

        

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
        raise NotImplementedError

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
    file_path_2=Path("sheet-EE.csv")
    collection.read_mass_balance_data(file_path_2)

if __name__ == "__main__":
    main()