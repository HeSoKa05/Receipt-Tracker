# Receipt Tracker Django App README
a simple receipt tracker developed using Django framework by Soufyane Hedidi 

## Overview

This README provides instructions for setting up and running the Django app. Follow these steps to get your development environment up and running.

## Prerequisites

Ensure you have the following installed:

- Python (3.9 recommended)
- pip (Python package installer)
- Virtualenv (optional but recommended)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/HeSoKa05/Receipt-Tracker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Receipt-Tracker
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   virtualenv venv
   ```

   Activate the virtual environment:

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On Linux/Mac:

     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

## Running the App

To start the development server, run:

```bash
python manage.py runserver
```

Access the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Additional Configuration

- Customize the settings in `settings.py` according to your needs.
- Set up a database by modifying the database configurations in `settings.py`.
- Create a superuser account for admin access:

  ```bash
  python manage.py createsuperuser
  ```

Follow these steps, and your Django app should be up and running. Refer to the official Django documentation for more advanced configurations and deployment options.

## Testing

To run receipt_tracker_app's models and views tests, run:
```bash
python manage.py test receipt_tracker_app
```

This will run the tests I wrote before (see the receip_tracker_app/tests.py file).
you can add codes to the app and run your own tests to help find errors easily.
