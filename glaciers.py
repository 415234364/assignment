
class Glacier:
    def __init__(self, glacier_id, name, unit, lat, lon, code):
        self.glacier_id=glacier_id
        self.name=name
        self.unit=unit
        self.lat=lat
        self.lon=lon
        self.code=code

        

    def add_mass_balance_measurement(self, year, mass_balance,partial_measurement):
        raise NotImplementedError

    def plot_mass_balance(self, output_path):
        raise NotImplementedError

        

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
                Glacier_object=Glacier(row[2],row[1],row[0],row[5],row[6],row[14])
                self.collectionObject.append(Glacier_object)
                
        
        

                
        

    def read_mass_balance_data(self, file_path):
        raise NotImplementedError

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

if __name__ == "__main__":
    main()