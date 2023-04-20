import sys
import math

sys.path.append('../../')

from svm_model.predict import make_prediction
from svm_model.processing.data_manager import load_dataset


def test_make_single_prediction():
    # Given
    test_data = load_dataset(file_name='test.csv')
    single_test_input = test_data[0:1]

    # When
    subject = make_prediction(input_data=single_test_input)

    print(subject.get('predictions'))
    
test_make_single_prediction()

def test_make_multiple_predictions():
    # Given
    test_data = load_dataset(file_name='test.csv')
    original_data_length = len(test_data)
    multiple_test_input = test_data

    # When
    subject = make_prediction(input_data=multiple_test_input)

    # Then
    print(subject.get('predictions'))

test_make_multiple_predictions()