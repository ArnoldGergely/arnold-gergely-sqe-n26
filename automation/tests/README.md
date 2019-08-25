# Test cases for Task 3

Example test cases for API automation Best Buy - API Playground running locally

Examples are divided into 3 separate sections:  

    1. Smoke test candidates - simple check of endpoint responsiveness 
    2. Basic GET tests with data handling, e.g. print out some values from response
    3. Full CRUD test cases for each major endpoints - Products, Stores, Services, Categories 

##### Smoke test candidates

* Test GET /products endpoint, should return 200
    1. Call ../products
    2. Assert response has status 200
    
    
* Test GET /stores endpoint, should return 200
    1. Call ../stores
    2. Assert response has status 200
    
    
* Test GET /services endpoint, should return 200
    1. Call ../services
    2. Assert response has status 200
    
    
* Test GET /categories endpoint, should return 200
    1. Call ../categories
    2. Assert response has status 200


##### Basic GET tests with data handling

* Test GET product by ID
    1. Call ../products/{id} using id = '43900'
    2. Assert response has status 200
    3. Handle response body
    4. Print out name and id
    
    
* Test GET store by ID
    1. Call ../stores/{id} using id = '11'
    2. Assert response has status 200
    3. Handle response body
    4. Print out name and id
    
    
* Test GET service by ID
    1. Call ../services/{id} using id = '7'
    2. Assert response has status 200
    3. Handle response body
    4. Print out name and id
    
    
* Test GET category by ID
    1. Call ../categories/{id} using id = 'abcat0101001'
    2. Assert response has status 200
    3. Handle response body
    4. Print out name and id
    
##### Full CRUD test cases for each major endpoints
###### Note: Create and Update payloads are structured as same in the test environment 

* Test Product CRUD
    1. Create new Product payload
    2. Call POST call on ../products with payload
    3. Assert successful creation response 201
    4. Retrieve product ID from response
    5. Update payload with changes
    6. Call PATCH call on ../products/{id} with payload to update changes
    7. Assert successful creation response 200
    8. Handle response and verify changes
    9. Using product_id from step 4 call DELETE on ../products/{id} call
    10. Assert delete was successful, confirm call status 200
    11. Call GET on ../products/{id}
    12. Assert response should be status 404
    


* Test Store CRUD
    1. Create new Store payload
    2. Call POST call on ../stores with payload
    3. Assert successful creation response 201
    4. Retrieve store ID from response
    5. Update payload with changes
    6. Call PATCH call on ../stores/{id} with payload to update changes
    7. Assert successful creation response 200
    8. Handle response and verify changes
    9. Using product_id from step 4 call DELETE on ../stores{id} call
    10. Assert delete was successful, confirm call status 200
    11. Call GET on ../stores/{id}
    12. Assert response should be status 404


* Test Service CRUD
    1. Create new Service payload
    2. Call POST call on ../services with payload
    3. Assert successful creation response 201
    4. Retrieve product_ID from response
    5. Update payload with changes
    6. Call PATCH call on ../services/{id} with payload to update changes
    7. Assert successful creation response 200
    8. Handle response and verify changes
    9. Using product_id from step 4 call DELETE on ../services/{id} call
    10. Assert delete was successful, confirm call status 200
    11. Call GET on ../services/{id}
    12. Assert response should be status 404


* Test Category CRUD
    1. Create new Category payload that includes ID
    2. Call POST call on ../categories with payload
    3. Assert successful creation response 201
    4. Update payload with changes
    5. Call PATCH call on ../categories{id} with payload to update changes
    6. Assert successful creation response 200
    7. Handle response and verify changes
    8. Using product_id from step 1 call DELETE on ../categories{id} call
    9. Assert delete was successful, confirm call status 200
    10. Call GET on ../categories/{id}
    11. Assert response should be status 404

### There can be many other variations...

    That would combine usage of these basic calls, which would lead to more complex test cases such as: 
    Adding categories to products
    Adding services to stores 
    Etc 
    
    But as for example this should be sufficient
