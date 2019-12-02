# Rest API: Implementation with Django Rest Framework
 API simulating Marvel **Characters* endpoints (https://developer.marvel.com/docs#!/public)
  
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Must have the following
```
Python >= 3.6
```


### Installing

Follow the steps below to set up the project

Clone the project
```
 git clone https://github.com/nacpacheco/RestAPI_Django.git
```

From root folder, install dependencies (no internet connection required)
```
pip install --no-index --find-links ./dependencies/ -r requirements.txt
```

After successfully installing packages, build application
```
python manage.py runserver
```

You must receive the message:
```
Starting development server at http://127.0.0.1:8000/
```
And it's up and running! 

## Using the API

Some examples of requests to try and use the endpoints. 
 
 ps: The database contains three characters (id 1 to 3)

### List all Characters 
```
GET: http://127.0.0.1:8000/characters/
```

```
RESPONSE: [
    {
        "id": 2,
        "name": "Captain Marvel",
        "description": "Near death, Carol Danvers was transformed into a powerful warrior for the Kree.",
        "modified": "2019-12-01T19:03:11.492244Z",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSCTE",
        "uri": "https://www.marvel.com/characters/captain-marvel-carol-danve",
        "comic_set": [
            {
                "id": 1,
                "name": "Ms. Marvel (1977) #1",
                "uri": "https://www.marvel.com/comics/issue/10287/ms_marvel_1977_1"
            },
            {
                "id": 2,
                "name": "Ms. Marvel (2006) #1",
                "uri": "https://www.marvel.com/comics/issue/3949/ms_marvel_2006_1"
            }
        ],
        "storie_set": [
            {
                "id": 1,
                "name": "CMStorie #1",
                "uri": "www.cmstorie.com",
                "type": "storie"
            }
        ],
        "event_set": [
            {
                "id": 1,
                "name": "Captain Marvel Event #1",
                "uri": "www.cmevent.com"
            }
        ],
        "serie_set": [
            {
                "id": 1,
                "name": "CM Serie #1",
                "uri": "www.cmserie1.com"
            }
        ],
        "url_set": [
            {
                "id": 1,
                "uri": "https://pt.wikipedia.org/wiki/Captain_Marvel_(Marvel_Comics)",
                "type": "wiki Captain Marvel"
            }
        ]
    },
    {
        "id": 1,
        "name": "Hulk",
        "description": "Green guy",
        "modified": "2019-12-01T19:00:42.141893Z",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQXeP",
        "uri": "https://www.marvel.com/characters/hulk-bruce-banner",
        "comic_set": [
            {
                "id": 3,
                "name": "Hulk (1977) #59",
                "uri": "https://hulkcomic.com/59"
            }
        ],
        "storie_set": [],
        "event_set": [],
        "serie_set": [],
        "url_set": []
    },
    {
        "id": 3,
        "name": "Spider-Man",
        "description": "Bit by a spider",
        "modified": "2019-12-01T22:09:01.292684Z",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR1sJ",
        "uri": "https://www.marvel.com/characters/spider-man-peter-parker",
        "comic_set": [
            {
                "id": 4,
                "name": "Superior Spider-Man (2013) #1",
                "uri": "https://www.marvel.com/comics/issue/46462/superior_spider-man_2013_1"
            }
        ],
        "storie_set": [],
        "event_set": [],
        "serie_set": [],
        "url_set": []
    }
]
```

### List character by id
 [ID] = id of character 
```
GET: http://127.0.0.1:8000/characters/[ID]
```
```
RESPONSE: {
    "id": 2,
    "name": "Captain Marvel",
    "description": "Near death, Carol Danvers was transformed into a powerful warrior for the Kree.",
    "modified": "2019-12-01T19:03:11.492244Z",
    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSCTE",
    "uri": "https://www.marvel.com/characters/captain-marvel-carol-danve",
    "comic_set": [
        {
            "id": 1,
            "name": "Ms. Marvel (1977) #1",
            "uri": "https://www.marvel.com/comics/issue/10287/ms_marvel_1977_1"
        },
        {
            "id": 2,
            "name": "Ms. Marvel (2006) #1",
            "uri": "https://www.marvel.com/comics/issue/3949/ms_marvel_2006_1"
        }
    ],
    "storie_set": [
        {
            "id": 1,
            "name": "CMStorie #1",
            "uri": "www.cmstorie.com",
            "type": "storie"
        }
    ],
    "event_set": [
        {
            "id": 1,
            "name": "Captain Marvel Event #1",
            "uri": "www.cmevent.com"
        }
    ],
    "serie_set": [
        {
            "id": 1,
            "name": "CM Serie #1",
            "uri": "www.cmserie1.com"
        }
    ],
    "url_set": [
        {
            "id": 1,
            "uri": "https://pt.wikipedia.org/wiki/Captain_Marvel_(Marvel_Comics)",
            "type": "wiki Captain Marvel"
        }
    ]
}
```

### List Comics related to character
 [ID] = id of character 
```
GET: http://127.0.0.1:8000/characters/[ID]/comics
```
```
RESPONSE:[
    {
        "id": 1,
        "name": "Ms. Marvel (1977) #1",
        "uri": "https://www.marvel.com/comics/issue/10287/ms_marvel_1977_1"
    },
    {
        "id": 2,
        "name": "Ms. Marvel (2006) #1",
        "uri": "https://www.marvel.com/comics/issue/3949/ms_marvel_2006_1"
    }
]
```

### Other endpoints:
```
GET: http://127.0.0.1:8000/characters/[ID]/events
GET: http://127.0.0.1:8000/characters/[ID]/stories
GET: http://127.0.0.1:8000/characters/[ID]/series
```
   
## Running the tests

To run automated test on this application:

```
python manage.py test
```

## Built With

* [Django Rest Framework](https://www.django-rest-framework.org/) 