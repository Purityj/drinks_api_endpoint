# Drink API 
This repository contains a simple Drink API built with Django and Django Rest Framework. It provides endpoints for listing, creating, updating and deleting drink items in the database. A client script is also included to demonstrate how to consume the API. 

## Features 
- List all drinks
- Create a new drink
- Update an existing drink
- Delete a drink

## Installation 
1. **Clone the repository**:
```bash
git clone https://github.com/Purityj/drinks_api_endpoint.git
cd drink
```
2. Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
4. Install the required packages
```bash
pip install -r requirements.txt
```
6. Apply migrations
```bash
python manage.py migrate
```
8. Run server
```bash
python manage.py runserver
```
## API Endpoints
- GET /drinks: Retrieve a list of all drinks.
- POST /drinks: Create a new drink.
- GET /drinks/{id}: Retrieve a specific drink by ID.
- PUT /drinks/{id}: Update a specific drink by ID.
- DELETE /drinks/{id}: Delete a specific drink by ID.

## Usage
To interact with the API, you can run the consume.py script, which demonstrates how to send HTTP requests to the API. Make sure to have the server running before executing the script.
```bash
python consume.py
```
## Browser UI Results 
![image](https://github.com/user-attachments/assets/73354dca-4f70-4c65-bf03-adf3c85de29a)

## Results from running consume.py script 
![image](https://github.com/user-attachments/assets/26179766-57b0-49e3-bcfe-861fbca2866d)

