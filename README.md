# Create-Project

## Project Setup

1. Initialize the Environment

    - First, create a virtual environment to manage your dependencies locally.

    macOS / Linux (Bash):
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

    Windows Powershell:
    ```powershell
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    ```

2. Migrate database
   - Once the environment is active and requirements are installed, you need to set up the database schema.
   
   ```bash
   python createproject/manage.py migrate
   ```

3. Run Django Project
    - Start the local development server to view the project in your browser.

    ```bash
    python createproject/manage.py runserver
    ```

    - Once the server is running, you can access the application at: http://127.0.0.1:8000/

4. Create a Superuser (Optional)

    - To access the Django Admin interface, create an admin account:
    Bash

    ```bash
    python createproject/manage.py createsuperuser
    ```

    - Follow the prompts to set a username, email, and password, then navigate to /admin to log in.

## Running Tests

To ensure the application is functioning correctly and all templates are rendering as expected, run the test suite:

```bash
python createproject/manage.py test
```

What is being tested?

 - URL Resolution: Confirms that the homepage and other routes are accessible (Status 200)
 - Template Integrity: Verifies that home.html is correctly extending base.html.
 - Content Validation: Ensures key UI elements, such as "Welcome to my Website!" and the project carousel, are appearing in the HTML output.
 - Context Data: Confirms that the features and projects lists are being passed from the view to the frontend.