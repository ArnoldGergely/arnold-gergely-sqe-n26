#!/usr/bin/env python3

import requests
from automation.src.base.base_tc import BaseTestCase


class BaseAPIBuilders(object):

    PRODUCTS = "/products"
    STORES = "/stores"
    CATEGORIES = "/categories"
    SERVICES = "/services"

    default_header = {
        'Accept': 'application/json'
    }

    product_payload = {
        "name": "string",
        "type": "string",
        "price": 1,
        "shipping": 1,
        "upc": "string",
        "description": "string",
        "manufacturer": "string",
        "model": "string",
        "url": "string",
        "image": "string"
    }

    store_payload = {
        "name": "string",
        "type": "string",
        "address": "string",
        "address2": "string",
        "city": "string",
        "state": "string",
        "zip": "string",
        "lat": 0,
        "lng": 0,
        "hours": "string",
        "services": {}
    }

    service_payload = {
        "name": "string"
    }

    category_payload = {
        "name": "string",
        "id": "string"
    }


class BaseApi(object):

    def __init__(self):
        self.base_api_builder = BaseAPIBuilders
        self.base_tc = BaseTestCase()

    """
        API url builders
    """

    def api_url(self):
        return self.base_tc.get_base_link()

    def products_url(self):
        return self.api_url() + self.base_api_builder.PRODUCTS

    def stores_url(self):
        return self.api_url() + self.base_api_builder.STORES

    def categories_url(self):
        return self.api_url() + self.base_api_builder.CATEGORIES

    def services_url(self):
        return self.api_url() + self.base_api_builder.SERVICES

    # In case ID is passed as integer not string, ensuring casting str(id)
    def product_by_id_url(self, id):
        return self.api_url() + self.base_api_builder.PRODUCTS + "/" + str(id)

    def store_by_id_url(self, id):
        return self.api_url() + self.base_api_builder.STORES + "/" + str(id)

    def service_by_id_url(self, id):
        return self.api_url() + self.base_api_builder.SERVICES + "/" + str(id)

    def category_by_id_url(self, id):
        return self.api_url() + self.base_api_builder.CATEGORIES + "/" + str(id)

    """
        API functions
    """

    # PRODUCTS

    def get_all_products(self):
        response = requests.get(self.products_url())
        return response

    def create_new_product(self, payload):
        response = requests.post(self.products_url(), json=payload)
        return response

    def get_product_by_id(self, product_id):
        response = requests.get(self.product_by_id_url(product_id))
        return response

    def update_product_by_id(self, product_id, payload):
        response = requests.patch(self.product_by_id_url(product_id), json=payload)
        return response

    def delete_product_by_id(self, product_id):
        response = requests.delete(self.product_by_id_url(product_id))
        return response

    # STORES

    def get_all_stores(self):
        response = requests.get(self.stores_url())
        return response

    def create_new_store(self, payload):
        response = requests.post(self.stores_url(), json=payload)
        return response

    def get_store_by_id(self, store_id):
        response = requests.get(self.store_by_id_url(store_id))
        return response

    def update_store_by_id(self, store_id, payload):
        response = requests.patch(self.store_by_id_url(store_id), json=payload)
        return response

    def delete_store_by_id(self, store_id):
        response = requests.delete(self.store_by_id_url(store_id))
        return response

    # SERVICES

    def get_all_services(self):
        response = requests.get(self.services_url())
        return response

    def create_new_service(self, payload):
        response = requests.post(self.services_url(), json=payload)
        return response

    def get_service_by_id(self, service_id):
        response = requests.get(self.service_by_id_url(service_id))
        return response

    def update_service_by_id(self, service_id, payload):
        response = requests.patch(self.service_by_id_url(service_id), json=payload)
        return response

    def delete_service_by_id(self, service_id):
        response = requests.delete(self.service_by_id_url(service_id))
        return response

    # CATEGORIES

    def get_all_categories(self):
        response = requests.get(self.categories_url())
        return response

    def create_new_category(self, payload):
        response = requests.post(self.categories_url(), json=payload)
        return response

    def get_category_by_id(self, category_id):
        response = requests.get(self.category_by_id_url(category_id))
        return response

    def update_category_by_id(self, category_id, payload):
        response = requests.patch(self.category_by_id_url(category_id), json=payload)
        return response

    def delete_category_by_id(self, category_id):
        response = requests.delete(self.category_by_id_url(category_id))
        return response
