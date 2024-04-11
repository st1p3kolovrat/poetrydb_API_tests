# Sporty_api_tests_demo
Automated API tests example for demo purpose, using Behave Framework (Python)
This repo contains setup for the demo purpose of the Sporty. It consists of
sending requests to certain endpoint, and testing functionality of the same.  

For this task we used"
- [PoetryDB API](https://github.com/thundercomb/poetrydb#readme)
- Python 3.9 
- [Behave Framework](https://behave.readthedocs.io/en/stable/)


### Install all dependencies: 
`pip3 install -r requirements.txt`

## How to run tests?
Tests can be run in two ways. 
>Via Terminal 

Open up your terminal and write `behave`
This will run entire test suite. 
![running_tests.gif](gif%2Frunning_tests.gif)

>Via IDE

Simply in test runner configuration select `author.feature` file press play and it will run only this feature file. 


## Scenarios

| Scenario                                                    |
|-------------------------------------------------------------|
| I can get a list of all authors                             |
| I can get all titles from given author "<author_full_name>" |

### Scenario validation explanation

Scenario `I can get a list of all authors` is using two validations: 
- 1. response code - `Then the response code is "<status_code>"`
- 2. response body - `And response body is matching expected "<expected_response_body>"`

1. We expect that our GET request is successful and expected status code is 200. 
2. We assert that what we got in the GET request is equal to what we expect. For that we use method
of matching `context.response.json()` which is response body in json format, that we actually got, with
response body that we expect (which we have in a json file `list_of_all_authors.json` stored under `data/reponse/`)

These two steps are placed in common_steps.py as they are made generic and can be used on other endpoint.


Scenario: `I can get all titles from given author "<author_full_name>"` is also using two identical validations, 
only difference with this scenario is that it is a scenario outline, so we have added multiple scenarios iterations under one
scenario. 

Note: This can be expanded vastly into more positive scenarios, but also negative scenarios where we
would expect certain error message to occur in case of incorrect request method, invalid search query, and many more.
