# onlineshop

step 1 : clone from master branch (git clone -b master  https://github.com/aravindls/onlineshop.git)

step 2 : create a virtual environment and activate

step 3 : pip install -r .\requirements.txt

step 4 : makemigrations and migrate

step 5 : runserver

step 6 : use following urls for required result

        all products : http://127.0.0.1:8000/products/
        specific product : http://127.0.0.1:8000/products/?product_id=<pk>
        filter using category : http://127.0.0.1:8000/products/filter/?category=<pk> single category
                                http://127.0.0.1:8000/products/filter/?category=<pk>,<pk> multiple category
                                
 Use admin panel for CRUD operations
 admin username : admin
 password       : admin
