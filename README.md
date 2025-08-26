# ALX BE FINAL PROJECT
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
    "password": "StrongPassword123",
    "location": "Ethiopia",
    "date_of_birth": "1995-08-26"`
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
<br>
### B. Login

**Description:**
 Authenticates a user and returns a token with user details.


**Endpoint:** POST /api/users/login/

  
**Request (JSON):**  
```json
{
    "username": "mergashasho",
    "password": "StrongPassword123" 
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

**Description:**  This allows for obtaning movie using title using a queryset form. When you search for a movie if it is in database, you will be provided with the movie data else you will be given the movie obtained from OMDB wesite.

**Endpoint:**   GET /api/movies/search/

**Note:** You will have to append ?title=the_name_of_the_movie_you_want to the ENDPOINT. 

**Request (JSON):** None

So for request like this: 
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

What is happening in the back is if this movie is in database it will simply be obtained via the api and will be provided with the 5 recent reviews and average rating but if it is not in the database, the backend will just obtain it from OMDB via
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