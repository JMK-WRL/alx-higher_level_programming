# 0x0F-python-object_relational_mapping
n - Object-relational mapping

This project involves connecting Python with MySQL databases using both raw SQL queries and SQLAlchemy, an Object-Relational Mapping (ORM) library.

## Tasks

### 0. Get all states
- **File:** 0-select_states.py
- **Description:** This script connects to a MySQL database and lists all states from the table "states" in the "hbtn_0e_0_usa" database, ordered by state ID.

### 1. Filter states
- **File:** 1-filter_states.py
- **Description:** This script connects to a MySQL database and lists all states with names starting with 'N' from the "hbtn_0e_0_usa" database, ordered by state ID.

### 2. Filter states by user input
- **File:** 2-my_filter_states.py
- **Description:** This script takes a state name as user input and lists all values in the "states" table of the "hbtn_0e_0_usa" database where the state name matches the input, ordered by state ID.

### 3. SQL Injection...
- **File:** 3-my_safe_filter_states.py
- **Description:** Similar to Task 2 but with protection against SQL injection. The script takes a state name as user input and lists all values in the "states" table of the "hbtn_0e_0_usa" database where the state name matches the input, ordered by state ID.

### 4. Cities by states
- **File:** 4-cities_by_state.py
- **Description:** This script lists all cities from the "cities" table in the "hbtn_0e_4_usa" database, displaying city ID, city name, and state name. It uses only one execute() statement.

### 5. All cities by state
- **File:** 5-filter_cities.py
- **Description:** This script takes a state name as user input and lists all cities of that state from the "cities" table in the "hbtn_0e_4_usa" database, ordered by city ID.

### 6. First state model
- **File:** model_state.py
- **Description:** Defines a Python class `State` and an instance `Base` using SQLAlchemy. The class represents the "states" table in the database, with attributes `id` and `name`.

### 7. All states via SQLAlchemy
- **File:** 7-model_state_fetch_all.py
- **Description:** This script connects to a MySQL database using SQLAlchemy and lists all State objects from the "hbtn_0e_6_usa" database, ordered by state ID.

### 8. First state
- **File:** 8-model_state_fetch_first.py
- **Description:** This script connects to a MySQL database using SQLAlchemy and prints the first State object from the "hbtn_0e_6_usa" database, ordered by state ID.

### 9. Contains `a`
- **File:** 9-model_state_filter_a.py
- **Description:** This script connects to a MySQL database using SQLAlchemy and lists all State objects that contain the letter 'a' from the "hbtn_0e_6_usa" database, ordered by state ID.

### 10. Get a state
- **File:** 10-model_state_my_get.py
- **Description:** This script connects to a MySQL database using SQLAlchemy and prints the ID of the State object with the name passed as an argument from the "hbtn_0e_6_usa" database.

### 11. Add a new state
- **File:** 11-model_state_insert.py
- **Description:** This script connects to a MySQL database using SQLAlchemy and adds a new State object with the name "Louisiana" to the "hbtn_0e_6_usa" database.

### 12. Update a state
- **File:** 12-model_state_update_id_2.py
- **Description:** This script connects to a MySQL database using SQLAlchemy and changes the name of the State object with ID 2 to "New Mexico" in the "hbtn_0e_6_usa" database.

### 13. Delete states
- **File:** 13-model_state_delete_a.py
- **Description:** This script connects to a MySQL database using SQLAlchemy and deletes all State objects with a name containing the letter 'a' from the "hbtn_0e_6_usa" database.

### 14. Cities in state
- **File:** model_city.py
- **Description:** Defines a Python class `City` using SQLAlchemy. The class represents the "cities" table in the database, with attributes `id`, `name`, and `state_id`.


