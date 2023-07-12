import requests

from utils.http_methods import Http_method


""""Methods for testing Google maps API"""

base_url = "https://rahulshettyacademy.com"  # Base URL
key = "?key=qaclick123" #Param for all requests




class Google_maps_api():

    @staticmethod
    def create_new_place():

        json_for_create_new_place= {

                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                },
                "accuracy": 50,
                "name": "Super Frontline house",
                "phone_number": "34324 (+91) 983 893 3937",
                "address": "32, Lenina street",
                "types": ["shoe park", "shop"],
                "website": "http://google.com",
                "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json" # resource for methods post
        post_url = base_url + post_resource + key
        print(post_url)

        result_post = Http_method.post(post_url, json_for_create_new_place)
        print(result_post.text)

        return result_post

    """Method for check location"""
    @staticmethod
    def get_new_place(place_id):

        get_resource = "/maps/api/place/get/json" # resource for methods get
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = Http_method.get(get_url)
        print(result_get.text)

        return result_get

    """Method for update location"""

    @staticmethod
    def put_new_place(place_id):

        put_resource = "/maps/api/place/update/json" # resource for methods put
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = Http_method.put(put_url, json_for_update_location)
        print(result_put.text)

        return result_put

    @staticmethod
    def delete_location(place_id):
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_location = {
            "place_id": place_id
        }

        result_delete = Http_method.delete(delete_url, json_for_delete_location)
        print(result_delete.text)

        return  result_delete
