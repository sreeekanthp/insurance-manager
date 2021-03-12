# Insurance Manager


Insurance manager is a django application to create customers and insurance policies for the customers.

## Major frameworks/libraries used

- django
- django rest framework
- pytest
- flake8

## Development

**Clone repo locally**

    git clone https://github.com/srkanth/insurance-manager.git

	cd insurance-manager

**Install requirements**

    pip install -r requirements/development.txt

**Run migrations**

    python manage.py migrate

**Create a super user**

    python manage.py createsuperuser

**Run app locally**

    python manage.py runserver

app should be up and running at http://localhost:8000/

**Login to admin**

Got to http://localhost:8000/admin/ and login using your credentials.

## API Endpoints

 - Create new customer - http://127.0.0.1:8000/api/v1/create_customer/
 - Create new policy - http://127.0.0.1:8000/api/v1/create_policy/

Django rest framework UI is enabled for the endpoints and the Raw data form can be used to create customers/policy using respective apis.

New customers/policies created can be verified from the admin.
