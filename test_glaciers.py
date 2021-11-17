from glaciers import *
from pytest import raises

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

def test_validation_for_glacier_fail_on_non_5_length_id():
      with raises(ValueError) as exception: 
          validation_for_glacier('1444',0,0,0)
    
def test_validation_for_glacier_fail_on_non_valid_latitude():
      with raises(ValueError) as exception: 
         validation_for_glacier('14444',-190,0,0)
def test_validation_for_glacier_fail_on_non_number_id():
    with raises(TypeError) as exception:
         validation_for_glacier('jimmy',0,0,0)
def test_validation_for_glacier_fail_on_non_valid_unit():
    with raises(ValueError) as exception:
         validation_for_glacier('14444',0,0,'aed')
def test_validation_for_measurement_fail_on_non_number_id():
    with raises(TypeError) as exception:
        validation_for_measurement('sr','jimmy',2002)
def test_validation_for_measurement_fail_on_non_5_length_id():
    with raises(ValueError) as exception:
        validation_for_measurement('sr','12',2002)
def test_validation_for_measurement_fail_on_non_valid_unit():
    with raises(ValueError) as exception:
         validation_for_measurement('srs','12',2002)
def test_validation_for_measurement_fail_on_future_year():
    with raises(ValueError) as exception:
        validation_for_measurement('srs','12',20222)
def test_validation_for_measurement_fail_on_non_integer_year():
    with raises(ValueError) as exception:
        validation_for_measurement('srs','12',2020.2)
def test_validation_for_year_fail_on_future_year():
    with raises(ValueError) as exception:
        validation_for_year(20222)
def test_validation_for_year_fail_on_non_integer_year():
    with raises(ValueError) as exception:
        validation_for_year(2020.2)
    