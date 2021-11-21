from typing import Collection
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

def test_validation_for_code_length_not_3():
    with raises(ValueError) as exception:
        validation_for_code_pattern(1234)

def test_validation_for_code_first_character_not_available():
    with raises(ValueError) as exception:
        validation_for_code_pattern(".12")

def test_validation_for_identifier():
    with raises(ValueError) as exception:
        validation_for_identifier("123456")
    with raises(ValueError) as exception:
        validation_for_identifier("12?45")

def test_validation_for_mass_balance():
    with raises(ValueError) as exception:
        validation_for_mass_balance_value("?100")

def test_add_partial_mass_balance_measurement():
    file_path = Path("test-sheet-A.csv")
    collection = GlacierCollection(file_path)
    file_path_2=Path("test-sheet-EE-partial.csv")
    collection.read_mass_balance_data(file_path_2)
    assert collection.collectionObject[0].get_mass()[0]==['2018','-778',1]

def test_add_whole_mass_balance_measurement():
    file_path = Path("test-sheet-A.csv")
    collection = GlacierCollection(file_path)
    file_path_2=Path("test-sheet-EE-whole.csv")
    collection.read_mass_balance_data(file_path_2)
    assert collection.collectionObject[0].get_mass()[0]==['2015','-793',0]

def test_add_whole_mass_and_partial_balance_measurement():
    file_path = Path("test-sheet-A.csv")
    collection = GlacierCollection(file_path)
    file_path_2=Path("test-sheet-EE-partial-whole.csv")
    collection.read_mass_balance_data(file_path_2)
    assert collection.collectionObject[0].get_mass()[0]==['2018','705',1]
    assert len(collection.collectionObject[0].get_mass())==1

def test_filter():
    file_path = Path("test-sheet-A-filter.csv")
    collection = GlacierCollection(file_path)
    sub_collection=collection.filter_by_code(638)
    assert sub_collection[0].get_glacier()==['04532','AGUA NEGRA','AR',-30.16490,-69.80940,638]
    assert len(sub_collection)==1
    sub_collection_2=collection.filter_by_code('?38')
    assert len(sub_collection_2)==2
    assert sub_collection_2[1].get_glacier()==['02851','AZUFRE','AR',-35.29000,-70.55000,538]

def test_sort_by_latest_mass_balance():
    file_path = Path("test-sheet-A-sort.csv")
    collection = GlacierCollection(file_path)
    file_path_2=Path("test-sheet-EE-sort.csv")
    collection.read_mass_balance_data(file_path_2)
    temp_object=collection.sort_by_latest_mass_balance(1,0)
    assert len(temp_object)==1
    assert temp_object[0].get_glacier()==['02851','AZUFRE','AR',-35.29000,-70.55000,538]
    temp_object_2=collection.sort_by_latest_mass_balance(1,1)
    assert len(temp_object_2)==1
    assert temp_object_2[0].get_glacier()==['04532','AGUA NEGRA','AR',-30.16490,-69.80940,638]

    
if __name__ == "__main__":
    test_filter()