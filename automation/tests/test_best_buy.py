#!/usr/bin/env python

import unittest
import json
from automation.src.base.base_api import BaseApi, BaseAPIBuilders


class TestBestBuy(unittest.TestCase):

    __author__ = "Arnold Gergely"
    __email__ = "gergelj.arnold@gmail.com"

    def setUp(self):
        super(TestBestBuy, self).setUp()
        self.api = BaseApi()
        self.api_builders = BaseAPIBuilders()

    def tearDown(self):
        super(TestBestBuy, self).tearDown()

    """
        SMOKE TEST candidates, can be used as unit-tests as well for developers.
        Basic check are all the public endpoints returning proper response, simple confirmation that 
        endpoint is accessible
    """

    def test_products_response_code(self):
        response = self.api.get_all_products()
        assert response.status_code == 200

    def test_stores_response_code(self):
        response = self.api.get_all_stores()
        assert response.status_code == 200

    def test_services_response_code(self):
        response = self.api.get_all_services()
        assert response.status_code == 200
        content = json.loads(response.content)
        print(content)

    def test_categories_response_code(self):
        response = self.api.get_all_categories()
        assert response.status_code == 200
        content = json.loads(response.content)
        print(content)

    """
        Slightly complex test cases, example getting by ID - products, stores, services and categories
    """

    def test_get_product_by_id(self):
        # Handpicked id from the examples
        response = self.api.get_product_by_id(43900)
        assert response.status_code == 200
        product = json.loads(response.content)
        print("Product id: " + str(product['id']))
        print("Product name: " + str(product['name']))

    def test_get_store_by_id(self):
        # Handpicked id from the examples
        response = self.api.get_store_by_id('11')
        assert response.status_code == 200
        store = json.loads(response.content)
        print("Store id: " + str(store['id']))
        print("Store name: " + str(store['name']))

    def test_get_service_by_id(self):
        # Handpicked id from the examples
        response = self.api.get_service_by_id(7)
        assert response.status_code == 200
        service = json.loads(response.content)
        print("Service id: " + str(service['id']))
        print("Service name: " + str(service['name']))

    def test_get_category_by_id(self):
        # Handpicked id from the examples
        response = self.api.get_category_by_id('abcat0101001')
        assert response.status_code == 200
        category = json.loads(response.content)
        print("Category id: " + str(category['id']))
        print("Category name: " + str(category['name']))

    """
        Full cycle tests - Create - Update - Delete - Verify
    """

    def test_product_crud(self):
        # CREATE
        product_payload = self.api_builders.product_payload
        product_payload['name'] = 'ARNOLD PRODUCT1'
        product_payload['type'] = 'Testing'
        product_payload['price'] = 101
        product_payload['manufacturer'] = 'ARNOLD LOL Gmbh'
        create = self.api.create_new_product(payload=product_payload)
        assert create.status_code == 201
        product_content = json.loads(create.content)
        product_id = product_content['id']

        # UPDATE - same payload is sent as at create
        product_payload['name'] = 'ARNOLD RENAMED'
        product_payload['price'] = 500
        update = self.api.update_product_by_id(product_id=product_id, payload=product_payload)
        assert update.status_code == 200
        product_content = json.loads(update.content)
        assert product_content['name'] == 'ARNOLD RENAMED'
        assert product_content['price'] == 500

        # DELETE
        delete = self.api.delete_product_by_id(product_id)
        assert delete.status_code == 200

        # GET - verify the it has been deleted
        get_response = self.api.get_product_by_id(product_id)
        assert get_response.status_code == 404

    def test_store_crud(self):
        # CREATE
        store_payload = self.api_builders.store_payload
        store_payload['name'] = 'Store random'
        store_payload['type'] = 'Testing'
        store_payload['address'] = 'Vienna'
        create = self.api.create_new_store(payload=store_payload)
        assert create.status_code == 201
        store_content = json.loads(create.content)
        store_id = store_content['id']

        # UPDATE - same payload is sent as at create
        store_payload['name'] = 'Store RENAMED'
        store_payload['type'] = 'Working'
        update = self.api.update_store_by_id(store_id=store_id, payload=store_payload)
        assert update.status_code == 200
        store_content = json.loads(update.content)
        assert store_content['name'] == 'Store RENAMED'
        assert store_content['type'] == 'Working'

        # DELETE
        delete = self.api.delete_store_by_id(store_id)
        assert delete.status_code == 200

        # GET - verify the it has been deleted
        get_response = self.api.get_store_by_id(store_id)
        assert get_response.status_code == 404

    def test_service_crud(self):
        # CREATE
        service_payload = self.api_builders.service_payload
        service_payload['name'] = 'Service New'
        create = self.api.create_new_service(payload=service_payload)
        assert create.status_code == 201
        service_content = json.loads(create.content)
        service_id = service_content['id']

        # UPDATE - same payload is sent as at create
        service_payload['name'] = 'Service RENAMED'
        update = self.api.update_service_by_id(service_id=service_id, payload=service_payload)
        assert update.status_code == 200
        service_content = json.loads(update.content)
        assert service_content['name'] == 'Service RENAMED'

        # DELETE
        delete = self.api.delete_service_by_id(service_id)
        assert delete.status_code == 200

        # GET - verify the it has been deleted
        get_response = self.api.get_service_by_id(service_id)
        assert get_response.status_code == 404

    def test_category_crud(self):
        # CREATE
        category_payload = self.api_builders.category_payload
        category_payload['name'] = 'Category Check'
        category_payload['id'] = 'abcat123arnold'
        create = self.api.create_new_category(payload=category_payload)
        assert create.status_code == 201
        category_content = json.loads(create.content)
        category_id = category_content['id']

        # UPDATE - same payload is sent as at create
        category_payload['name'] = 'Category RENAMED'
        update = self.api.update_category_by_id(category_id=category_id, payload=category_payload)
        assert update.status_code == 200
        category_content = json.loads(update.content)
        assert category_content['name'] == 'Category RENAMED'

        # DELETE
        delete = self.api.delete_category_by_id(category_id)
        assert delete.status_code == 200

        # GET - verify the it has been deleted
        get_response = self.api.get_category_by_id(category_id)
        assert get_response.status_code == 404

    """
        More test cases can be added e.g. adding products to stores, updating categories in products, trying adding 
        request payload that should call out negative results (example cannot create or update if some mandatory 
        parameter is missing or there are additional unexpected keys) but it is repetitive already as such and for 
        current example these examples should be sufficient...
    """
