# Flask Blog Application

This is a simple blog web application built using Flask. It allows users to create, read, update, and delete blog posts. The application is structured to follow best practices for Flask development.

## Project Structure

```
flask-blog-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   └── post.html
│   └── static
│       ├── css
│       │   └── styles.css
│       ├── js
│       │   └── scripts.js
│       └── images
├── migrations
├── tests
│   ├── __init__.py
│   └── test_app.py
├── .gitignore
├── requirements.txt
├── config.py
├── run.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-blog-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Edit the `config.py` file to set up your database connection and other configuration settings.

## Running the Application

To run the application, execute the following command:
```
python run.py
```

The application will be available at `http://127.0.0.1:5000`.

## Testing

To run the tests, use the following command:
```
pytest
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.