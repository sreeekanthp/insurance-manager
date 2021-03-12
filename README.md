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

**Create a super user**

    python manage.py createsuperuser


**Run app locally**

    python manage.py runserver

app should be up and running at http://localhost:8000/

## API Endpoints

 - Create new customer - http://127.0.0.1:8000/api/v1/create_customer/
 - Create new policy - http://127.0.0.1:8000/api/v1/create_policy/

Django rest framework UI is enabled for the endpoints and can be used to hit the api with given payload.
