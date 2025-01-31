# HNG Stage 0 Backend Task

This is a simple public API built with FastAPI that returns basic information in JSON format.

### Setup Instructions

-CLone the repositiory 
git clone `https://github.com/iamthedarksaint/hng_stage_zero_public_api`

-Install Dependencies
pip install -r requirements.txt

-Run the application
uvicorn main:app --reload


### Back link 
- https://hng.tech/hire/python-developers


## API Documentation
- [API Docs](https://stage-zero-public-api.vercel.app/docs)

### Endpoint

- **URL**: `https://stage-zero-public-api.vercel.app/`
- **Method**: `GET`

### Response Format
```json
{
  "email": "bojzino128@example.com",
  "current_datetime": "2025-01-30T09:30:00Z", 
  "github_url": "https://github.com/iamthedarksaint/hng_stage_zero_public_api"
}

