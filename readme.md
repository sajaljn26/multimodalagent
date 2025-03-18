# FastAPI Image Processing and Querying Service

## Overview
This FastAPI application allows users to upload an image and submit a query. The image and query are processed using Groq API models.

## Features
- Upload an image and send a text query.
- Uses **Groq API** models (`llama-3.2-11b-vision-preview` and `llama-3.2-90b-vision-preview`).
- Returns processed results as JSON responses.
- Includes basic error handling and logging.

## Requirements
| Dependency | Version |
|------------|---------|
| Python     | 3.x     |
| FastAPI    | Latest  |
| Uvicorn    | Latest  |
| Requests   | Latest  |
| Python-dotenv | Latest |
| Pillow     | Latest  |

## Setup Instructions
### 1. Clone the Repository
```sh
git clone https://github.com/your-repo-name.git
cd your-repo-name
