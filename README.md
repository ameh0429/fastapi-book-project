# FastAPI Book Project. My Stage 2 Task 

## Overview
The **FastAPI Book Project** is a simple REST API built using FastAPI. It provides endpoints for retrieving book details and is designed with best practices in CI/CD, containerization, and deployment.

This project's repository was forked from `hng12-devbot/fastapi-book-project` with the task to add a missing endpoint, set up a test pipeline, and configure the deployment process. The application should be served using Nginx.

## Features
- Retrieve book details by ID
- CI pipeline using `pytest`
- Automated deployment pipeline
- Dockerized FastAPI application
- Reverse proxy setup with Nginx
- Hosted on AWS

## Technologies Used
- **FastAPI** - Web framework for building APIs
- **Python** - Programming language
- **Docker** - Containerization
- **Nginx** - Reverse proxy server
- **GitHub Actions** - CI/CD pipeline
- **AWS** - Cloud deployment

## Project Structure
```
fastapi-book-project/
├── api/
│   ├── db/
│   │   ├── __init__.py
│   │   └── schemas.py      # Data models and in-memory database
│   ├── routes/
│   │   ├── __init__.py
│   │   └── books.py        # Book route handlers
│   └── router.py           # API router configuration
├── core/
│   ├── __init__.py
│   └── config.py           # Application settings
├── tests/
│   ├── __init__.py
│   └── test_books.py       # API endpoint tests
├── main.py                 # Application entry point
│── Dockerfile
│── .github/workflows/
│   ├── ci.yml
│   ├── cd.yml
├── requirements.txt        # Project dependencies
└── README.md
```

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.9+
- Docker
- FastAPI
- Uvicorn
- Git

### Setup
- Clone the repository:
   ```sh
   git clone https://github.com/ameh0429/fastapi-book-project.git
   cd fastapi-book-project
   ```
- Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
- Run the application:
   ```sh
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```
- Access the API documentation at:
   - Swagger UI: `http://localhost:8000/docs`
   

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ebuleugqgbkmcraxduo0.png)

## API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/api/v1/books/{book_id}` | Retrieve book details |

## Running Tests
Run unit tests using pytest:
```sh
pytest tests/
```

## Docker Deployment
1. Build the Docker image:
   ```sh
   docker build -t fastapi-book-app .
   ```
2. Run the container:
   ```sh
   docker run -p 8000:8000 fastapi-book-app
   ```

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/g8pvt85dlkq0t3pypqny.png)

## CI/CD Pipeline
The project includes GitHub Actions for:
- Running tests on PRs
- Deploying automatically on merge

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/netgnkm2iperunj8u2uc.png)

## AWS Deployment
- Deploy the container using AWS EC2.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nfb6lpq38bkxehl5cdim.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gqiuyp1jp0vaewdy91e4.png)

- Configure Nginx as a reverse proxy.
Run `sudo nano /etc/nginx/sites-available/fastapi` to configure nginx

```
server {
    listen 80;
    server_name YOUR_EC2_PUBLIC_IP;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

```

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zzd5emghwh68manawyq1.png)

## Test from Your Browser
Try accessing the correct API endpoint in your browser. 
`http://54.164.65.253/api/v1/books/`

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1jvuzmmnztewyvlcgy3b.png)

## The Result

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0jccs0bqa5bn8rmo5mo5.png)

## Error Handling
The API includes proper error handling for:
- Non-existent books
- Invalid book IDs
- Invalid genre types
- Malformed requests

## Challenges and Lessons Learned
I faced numerous challenges as the deadline for submitting this task was tight. I encountered errors at various stages but was able to debug them with the help of my #HNG peers and by consulting AI. Through this experience, I gained deeper insights into FastAPI, Docker, CI/CD pipelines, and AWS deployment. I also improved my debugging skills and learned the importance of collaboration in software development.

## Future Improvements 
- Implement authentication and authorization
- Add database integration for persistent storage
- Enhance test coverage with additional unit and integration tests
- Improve error handling and logging
- Deploy using AWS Lambda and API Gateway for a serverless architecture


## License
This project is licensed under the MIT License.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, please open an issue in the GitHub repository.
