# LinkedIn Clone

## Build :

#### Use [requirements.txt](https://github.com/Twopersonwork/LinkedIn-Clone-Django/blob/main/requirements.txt) and Run :

```
pip install -r requirements.txt
```

#### It uses **Postgresql** so do the required setup for that.

#### Run Django side :

```
python3 manage.py runserver
```

#### It must be available at localhost:8000 by default.

### Frontend : [Repo Link](https://github.com/Twopersonwork/LinkedIn-Clone-React)

#### Main API for one user.

```http
GET /uapi/users/20
```

```JavaScript
{
    "id": 20,
    "username": "John",
    "email": "john@gmail.com",
    "date_joined": "2021-06-27T10:08:42.561870Z",
    "following": [
        {
            "id": 53,
            "following_user_id": 24,
            "username": "Amal khan",
            "created": "2021-06-30T10:10:23.373097Z"
        },
        {
            "id": 44,
            "following_user_id": 1,
            "username": "Prachi ",
            "created": "2021-06-30T08:37:22.438679Z"
        }
    ],
    "followers": [
        {
            "id": 52,
            "user_id": 25,
            "username": "Love Babbar",
            "created": "2021-06-30T10:01:59.799896Z"
        },
        {
            "id": 51,
            "user_id": 24,
            "username": "Amal khan",
            "created": "2021-06-30T10:01:35.025272Z"
        },
        {
            "id": 50,
            "user_id": 26,
            "username": "Nikhil Sharma",
            "created": "2021-06-30T10:01:17.013214Z"
        },
        {
            "id": 49,
            "user_id": 22,
            "username": "Neel Jain",
            "created": "2021-06-30T10:00:19.832824Z"
        }
    ],
    "posts": [
        {
            "id": 15,
            "body": "Google plus",
            "image": "https://res.cloudinary.com/mindflowingblog/image/upload/v1/media/post_images/evolving_google_identity_2x1_ggnpat",
            "user": 20,
            "likes": [],
            "comments": [
                {
                    "id": 7,
                    "comment": "nice",
                    "date": "2021-06-30T10:02:55.826009Z",
                    "post": 15,
                    "user": 20
                }
            ],
            "no_of_like": 0,
            "no_of_comment": 1
        }
    ],
    "profile_pic": "https://res.cloudinary.com/mindflowingblog/image/upload/v1/media/profile_images/57508_130120_15128802402522014267601_z9lj6p",
    "cover_pic": "https://res.cloudinary.com/mindflowingblog/image/upload/v1/media/defaults/cover.jpeg",
    "user_profile": {
        "id": 8,
        "firstName": "John Doe",
        "lastName": "",
        "headLine": "Python Developer",
        "education": "",
        "country": "India",
        "location": "Mumbai",
        "industry": "Software",
        "user": 20
    },
    "user_about": {
        "id": 4,
        "about": "Hey, I'm a Python Developer and react too",
        "user": 20
    },
    "user_education": [
        {
            "id": 6,
            "school": "University of San jose",
            "degree": "Bachelor of Engineering",
            "field_of_study": "Computer Engineering",
            "start_year": "2016",
            "end_year": "2020",
            "user": 20
        }
    ],
    "user_license": [
        {
            "id": 7,
            "name": "Machine Learning",
            "issuing_org": "Coursera",
            "issue_date": "2021-01-04",
            "expiration_date": "2021-04-16",
            "credential_id": "cvhvhvwd6g778",
            "user": 20
        }
    ],
    "user_skills": [
        {
            "id": 31,
            "skill": "HTML",
            "user": 20
        },
        {
            "id": 32,
            "skill": "Java",
            "user": 20
        },
        {
            "id": 33,
            "skill": "Python",
            "user": 20
        },
        {
            "id": 34,
            "skill": "Cloud Computing",
            "user": 20
        },
        {
            "id": 35,
            "skill": "Django REST Framework",
            "user": 20
        }
    ],
    "activities": [
        {
            "id": 7,
            "comment": "nice",
            "date": "2021-06-30T10:02:55.826009Z",
            "post": 15,
            "user": 20
        },
        {
            "id": 6,
            "comment": "Yeah actually it's a good framework",
            "date": "2021-06-30T09:31:31.005297Z",
            "post": 16,
            "user": 20
        },
        {
            "id": 19,
            "date": "2021-06-30T09:31:01.048293Z",
            "post": 16,
            "user": 20
        },
        {
            "id": 16,
            "date": "2021-06-30T09:04:01.785267Z",
            "post": 14,
            "user": 20
        }
    ],
    "waitFollowers": [
        {
            "id": 40,
            "user_id": 25,
            "username": "Love Babbar",
            "created": "2021-06-30T10:01:59.798654Z"
        },
        {
            "id": 37,
            "user_id": 22,
            "username": "Neel Jain",
            "created": "2021-06-30T10:00:20.105485Z"
        }
    ]
}
```

## Demo : [Our Work](https://ditto-linkedin.vercel.app/)

```
Use any credentials to use the web app.
[NOTE] It may load more, be patient.
```
