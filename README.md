# HierarchyHelper

HierarchyHelper is a Django project designed to visualize hierarchical structures, like department trees.
## Installation

1. **Clone the Repository**: 

    ```bash
    git clone https://github.com/yourusername/hierarchy_helper.git
    cd hierarchy_helper
    ```

2. **Set Up a Virtual Environment** (Optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Requirements**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser** (Optional):

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**:

    ```bash
    python manage.py runserver
    ```

    Visit `http://127.0.0.1:8000/units` in your browser.

## Contributing

Contributions are welcome!

1. **Fork the Repository**: Click the "Fork" button on the top-right of the repository's page.
2. **Clone Your Fork**: 

    ```bash
    git clone https://github.com/yourusername/hierarchy_helper-fork.git
    cd hierarchy_helper-fork
    ```

3. **Create a Branch**: 

    ```bash
    git checkout -b feature-branch
    ```

4. **Make Your Changes**: Add, edit, or remove files as needed.
5. **Commit Your Changes**: 

    ```bash
    git add .
    git commit -m "Describe your changes"
    ```

6. **Push to GitHub**: 

    ```bash
    git push origin feature-branch
    ```

7. **Create a Pull Request**: Go to your fork on GitHub and click the "Compare & pull request" button. Fill out the form and submit.
