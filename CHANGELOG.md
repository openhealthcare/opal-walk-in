### 0.2.1 Release

Symptoms is becoming a many to many relationship so a user can add in many symptoms
in a single field. There's a fix for some boolean logic that was leaking into other packages
in the episode detail view.


### 0.2 Release

Allows discharge summary letters to be re-generated from details pages.

### 0.1.2 Release

Fixes a bug whereby patients could not be readmitted. (openhealthcare/elcid#742)

### 0.1.1 Release

Resolves some pluralisation bugs in admin display.
Updates to Django 1.8.3
Sets discharge dates for end of appointment
Updates Javascript tests to Jasmine 2.x

Upgrade instructions:

    $ python manage.py migrate walkin --fake-initial
