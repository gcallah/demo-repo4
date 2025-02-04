# Requirements for Security System

## Features Needed

- Different users have different permissions
- Do we need group permissions? (Maybe later.)
- We should be fine-grained about access... someone might be able, e.g., to update a record but not delete it.
- We must be able to easily add different types of security checks as required, e.g.,
    - login
    - auth key
    - dual factor
    - biometrics
    - IP address
- If there is no security record for some feature, it is open to all.

## Design

- Security data should be in our DB.
- First cut: let's use CRUD.
- Having a dictionary of bools to specify checks needed will permit easily adding more later.
