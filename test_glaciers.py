from glaciers import *

def main():
    file_path = Path("sheet-A.csv")
    collection = GlacierCollection(file_path)
    file_path_2=Path("sheet-EE.csv")
    collection.read_mass_balance_data(file_path_2)
    collection.filter_by_code(638)
    collection.find_nearest(0,0,5)
    collection.sort_by_latest_mass_balance(5,1)
    collection.summary()

def test_filter():
    file_path = Path("sheet-A.csv")
    collection = GlacierCollection(file_path)
    file_path_2=Path("sheet-EE.csv")
    collection.read_mass_balance_data(file_path_2)
    filter_collection=collection.filter_by_code('638')
    print(*filter_collection)
    filter_collection_2=collection.filter_by_code('6?8')

if __name__ == "__main__":
    # main()
    test_filter()