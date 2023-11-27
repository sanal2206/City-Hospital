# City-Hospital 
 Welcome to the City Hospital Web Application repository! This web application, built using the Django framework and bootstarp.

## Features of the application
 - Automated mail confirmation :The user will receive an automated email once the booking is confirmed.
 - Contact Page : The user can send feedback and messages.
 - Doctor Dashboard : A dedicated page for checking the doctor's details and the departments.
 - Department Page : A designated department page gives a brief idea of the different departments in the hospital.
 - About Page :tells about City Hospital's mission and the advanced technology available in the hospital.
 - Admin page : Dediacted admin page with user authentication for changes and manipulation with read and write permission.
 - Staff login : Access to backend staff for checking the patient details and conatct page details with read only permission


 ## Technologies Used
 - Backend: Django, Django
 - Frontend:Bootstarp
 - Database-sqLite
 - Host-pythonanywhere

  ## Languages Used
  - Backend: Python
  - Frontend: HTML,CSS


## Accessing the City Hospital Web Application

You can access the City Hospital Web Application by following the link below:

[City Hospital Web Application](https://sanal2206.pythonanywhere.com/about)


## Getting Started

### Prerequisites

Make sure you have the following installed on your machine:

- [Python](https://www.python.org/) (version 3.7 or higher)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [virtualenv](https://pypi.org/project/virtualenv/)

  ### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sanal2206/city-hospital-web-app.git
   cd city-hospital-web-app

2. **Create a Virtual Environment:**

    ```bash
    virtualenv venv
    ```

3. **Activate the Virtual Environment:**
   - On Windows:

        ```bash
        venv\Scripts\activate
        ```

   - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Run Migrations:**

    ```bash
    python manage.py migrate
    ```

2. **Create a Superuser (Admin):**

    ```bash
    python manage.py createsuperuser
    ```

3. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

   


  
  






