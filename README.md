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
   python manage.py migrate
   ```

3. Run Django Project
    - Start the local development server to view the project in your browser.

    ```bash
    python manage.py runserver
    ```

    - Once the server is running, you can access the application at: http://127.0.0.1:8000/

4. Create a Superuser (Optional)

    - To access the Django Admin interface, create an admin account:
    Bash

    ```bash
    python manage.py createsuperuser
    ```

    - Follow the prompts to set a username, email, and password, then navigate to /admin to log in.