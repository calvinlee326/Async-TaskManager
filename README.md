# Async Task Manager (Using FastAPI and Heroku)

This is an asynchronous task manager built with FastAPI and deployed on Heroku. It allows users to create and track long-running tasks that are processed asynchronously in the background using `BackgroundTasks` and `asyncio`.

## Features

- Asynchronous task management using `asyncio` and FastAPI's `BackgroundTasks`.
- Deploys on Heroku using `uvicorn` as the ASGI server.
- Real-time API documentation and interactive testing through FastAPI's Swagger UI.

## Technologies Used

- **FastAPI**: Web framework for building APIs.
- **Uvicorn**: ASGI server to run FastAPI.
- **Python**: Programming language for writing the application.
- **Heroku**: Cloud platform for deployment.

## Getting Started

### Prerequisites

Ensure that you have the following installed on your local development machine:

- Python 3.x
- FastAPI
- Uvicorn
- Git
- Heroku CLI (for deployment)

### Setup Instructions

1. **Clone the Repository**

   First, clone the repository to your local machine using Git:

   ```bash
   git clone https://github.com/yourusername/async-task-manager.git
   cd async-task-manager
   ```

2. **Create and Activate Virtual Environment**

   Create a Python virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Mac/Linux
   venv\Scripts\activate  # For Windows
   ```

3. **Install Dependencies**

   Install all the dependencies listed in the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Development Server**

   Start the Uvicorn development server locally:

   ```bash
   uvicorn app:app --reload
   ```

   Open your browser and visit:

   ```
   http://localhost:8000
   ```

   You should see a JSON message returned by the FastAPI application.

5. **Access Swagger Documentation**

   To explore and test the API using FastAPI's Swagger documentation, open your browser and visit:

   ```
   http://localhost:8000/docs
   ```

### Deployment to Heroku

1. **Login to Heroku**

   Make sure you have Heroku CLI installed. Then, login to Heroku:

   ```bash
   heroku login
   ```

2. **Create a Heroku App**

   Create a new Heroku app using the following command:

   ```bash
   heroku create your-app-name
   ```

3. **Deploy the App**

   Push the code to Heroku and deploy the FastAPI app:

   ```bash
   git push heroku main
   ```

4. **Visit the Live App**

   Once the deployment is successful, you can open the live application using:

   ```bash
   heroku open
   ```

   Your app should now be live on the web!

### Live Application

The live application is available at:
![Screenshot 2024-09-13 at 2 54 40 PM](https://github.com/user-attachments/assets/36f4d9be-7171-42de-9b78-a3834d115c0c)

[https://async-task-4e020a9578b4.herokuapp.com/](https://async-task-4e020a9578b4.herokuapp.com/)

### Project Structure

```
async-task-manager/
├── app.py
├── task_manager/
│   ├── __init__.py
│   └── background_tasks.py
├── venv/
├── requirements.txt
├── Procfile
├── README.md
└── runtime.txt (optional)
```

## Future Improvements

- Task status tracking (e.g., `pending`, `in_progress`, `completed`).
- Integration with databases for task persistence.
- WebSocket integration for real-time task progress updates.

## License

This project is open-source and available under the [MIT License](LICENSE).

