import json
import allure

from utils.checking import Checking
from utils.api import Google_maps_api

""""Create,Change,Delete new location"""
@allure.epic("Test create place")
class Test_create_place():

    allure.description("Create,Change,Delete new location")
    def test_create_new_place(self):

        print('Method POST:')
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        #token = json.loads(result_post.text)
        #print(list(token))
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

        print("Method GET:")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name',
                                               'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '32, Lenina street')


        print("Method PUT:")
        result_put = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', "Address successfully updated")

        print("Method GET:")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name',
                                               'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', "100 Lenina street, RU")

        print("Method DELETE:")
        result_delete = Google_maps_api.delete_location(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', "OK")

        print("Method GET:")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")

        print("Create, update and delete test is completed")