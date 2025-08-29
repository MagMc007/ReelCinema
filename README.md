# REEL CINEMA

ReelCinema API is a fully functional RESTful backend service for a movie review platform. It allows users to register, log in, browse movies, and submit reviews while ensuring robust authentication, authorization, and data integrity.  
### Check it live on:
```json
https://reelcinema.onrender.com/
```
## Key Features
### A. User Management
- Users can register and log in via token-based authentication.
- User data is securely stored, and sensitive fields are protected.

### B. Movie Data Integration
- Fetches movie data from OMDb API when it is not already in the local database.
- Stores movie information including title, year, IMDb ID, type, and poster image.
- Allows searching for movies by title with case-insensitive queries.
- Returns up to 5 recent reviews alongside movie details.

### C. Reviews
- Users can post reviews for movies (one review per user per movie).
- Reviews include `review_text`, `rating`, and timestamps.
- Users can update or delete their own reviews; other users have read-only access.
- Response includes simplified user info (username only) and the movie title.

### D. API Design
- Built with Django REST Framework (DRF) for clean, maintainable code.
- Supports pagination, filtering, and ordering of review listings.
- Permissions ensure only authenticated users can create or modify reviews.
- Error handling provides user-friendly messages for invalid or duplicate actions.

### E. Tech Stack
- Python 3.12, Django, Django REST Framework, Django-filter 
- MySQL for storage  (changed to sqlite for deployment purposes)
- Requests library for external API calls (OMDb)  
- Token-based authentication for secure access  


## Purpose
ReelCinema API is designed to provide a robust backend for a movie review application, demonstrating a full-stack-ready API architecture with secure authentication, relational database design, and third-party API integration.

## 1. Authentication  

### A. Register  

**Description:**  
Creates a new user account. Returns a token for authentication on success. 


**Endpoint:**   POST /api/users/register/
 

**Request (JSON):**  
```json
{
    "username": "mergashasho",
    "email": "merga@example.com",
    "password": "A...L....X",
    "location": "Ethiopia",
    "date_of_birth": "1995-08-26"
}
```
Success Response (201 Created):
```json
{
    "TOKEN": "bf632d86115ee.....4fa3c0e6794154d19b5ff2d",
    "username": "mergashasho",
    "email": "merga@example.com",
    "location": "Ethiopia",
    "date_of_birth": "1995-08-26"
}
```


### B.Login

**Description:**
 Authenticates a user and returns a token with user details.


**Endpoint:** POST /api/users/login/

  
**Request (JSON):**  
```json
{
    "username": "mergashasho",
    "password": "A...L....X" 
}
```
Success Response (200 OK):
```json
{
    "TOKEN": "bf632d86115e....4fa3c0e6794154d19b5ff2d",
    "user_id": 4,
    "username": "mergashasho"
}
```
Error Response (400 Bad Request): In the case of wrong credentials
```json
{
    "non_field_errors": [
        "Invalid credential"
    ]
}
```

## 2. Movies

**Description:**  This allows for obtaning movie using title using a queryset form. When you search for a movie if it is in database, you will be provided with the movie data else you will be given the movie obtained from OMDB API.

**Endpoint:**   GET /api/movies/search/

**Note:** You will have to append **?title=the_name_of_the_movie_you_want** to the ENDPOINT. 

**Request (JSON):** None

So for a request like this: 
 ```json
  http://127.0.0.1:8000/api/movies/search/?title=Mission Impossible
 ```

Success Response (200 OK):
```json
{
    "id": 6,
    "title": "Mission: Impossible - Ghost Protocol",
    "year": "2011",
    "imdb_id": "tt1229238",
    "type": "movie",
    "poster": "https://m.media-amazon.com/images/M/MV5BMTY4MTUxMjQ5OV5BMl5BanBnXkFtZTcwNTUyMzg5Ng@@._V1_SX300.jpg",
    "average_rating": null,
    "reviews_count": 0,
    "recent_reviews": []
}
```

What is happening in the backend is if this movie is in database it will simply be obtained via the api and will be provided with the 5 recent reviews and average rating but if it is not in the database, the backend will just obtain it from OMDB via
```json
http://www.omdbapi.com/?apikey=[mykey123]&s=Mission Impossible
```
and provide the first result that appears in the response with no reviews and ratings.


If by chance the movie you are looking for does not exist in both the backend database and OMDB, you will be provided with 
Error Response (404 Not Found):
```json
{
    "error": "Movie not found"
}
```
## 3. Reviews and Ratings

**Note:** All the practices below will require authentication so setup authentication using the procedute below:

- Set Authorization → Type = No Auth.

- Go to the Headers tab.

- Add a header:

  - Key: Authorization

  - Value: Token 12...34 (replace with your actual token).

### Creating a review for a movie

**Description:** You can review a movie according to your opinion and also rate it out of 5. The backend enforces that one user has only one record tied to a movie.

**Endpoint:** POST /api/review/rev/

**Request (JSON):**  
```json
{
  "movie_id": 2,
  "rating": 5,
  "review_text": "Epic movie!"
}
```
Note that in this process you must obtain the ID of the movie first.

Success Response (201 Created):
```json
{
    "id": 2,
    "user": {
        "username": "mergashasho",
        "email": "merga@example.com",
    },
    "title": "Inception",
    "review_text": "Epic movie!",
    "rating": 5,
    "created_at": "2025-08-26T18:59:26.666224Z",
    "updated_at": "2025-08-26T18:59:26.666224Z"
}
```
This will also be added among the recent reviews of that movie for others to see.
### Editing your review
**Description:** You can edit your review by changing its json content 

**Endpoint (JSON):** PUT /api/review/rev/review_id/ or  PATCH /api/review/rev/review_id/

**Request (JSON):**  
```json
{
  "movie_id": 2,
  "rating": 4,
  "review_text": "Epic movie!"
    
}
```
Success Response (200 OK):
```json
{
    "id": 2,
    "user": {
        "username": "mergashasho",
        "email": "merga@example.com"
    },
    "title": "Mission: Impossible - Ghost Protocol",
    "review_text": "Epic movie!",
    "rating": 4,
    "created_at": "2025-08-26T18:59:26.666224Z",
    "updated_at": "2025-08-26T19:26:35.887215Z"
}
```
#### One user can only have one review data tied to a movie. If that use tries to review the movie again by the method POST 

Error Response (400 Bad Request):
```json
{
    "detail": "You have already reviewed this movie."
}
```

