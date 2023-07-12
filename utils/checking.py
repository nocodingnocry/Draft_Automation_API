"""Methods for check response"""
import json


class Checking():

    """Method for check status code"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        print("Success, status code: " + str(result.status_code))

    """Method for check reqirement field in response"""
    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)  # Get response in format JSON
        assert list(token) == expected_value
        print("Required fields: " + str(expected_value) +" received")

    """Method for check values of reqirement fields"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert expected_value in check_info
        print(expected_value + " is true!")