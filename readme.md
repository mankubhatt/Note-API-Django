# NOTE API

To perform CRUD operations on the note.

## Try it on - https://notes-django-7tua.onrender.com/swagger/

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mankubhatt/Note-API-Django.git
   cd your-repository
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv env
   ```

3. Activate the virtual environment:

   On Windows:

   ```bash
   .\env\Scripts\activate
   ```

   On macOS/Linux:

   ```bash
   source env/bin/activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser (for accessing Django admin):

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

   Visit http://127.0.0.1:8000/ in your browser.

## API Endpoints

- **Create Note:**

  ```
  POST /api/v1/notes/
  ```

- **Retrieve Note:**

  ```
  GET /api/v1/notes/<note_id>/
  ```

- **Update Note:**

  ```
  PUT /api/v1/notes/<note_id>/
  ```

- **Share Note:**

  ```
  PUT /api/v1/notes/share/<note_id>/
  ```

- **Note Version History:**

  ```
  GET /api/v1/notes/version-history/<note_id>/
  ```

## Running Tests

Run the following command to execute the test suite:

```bash
python manage.py test
```

## API Documentation

To access the DRF Browsable API:

- Start the development server (`python manage.py runserver`)
- Visit http://127.0.0.1:8000/swagger/ in your browser.

## License

This project is licensed under the [MIT License](LICENSE).
