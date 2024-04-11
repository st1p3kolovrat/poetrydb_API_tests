Feature: Author Endpoint

  Scenario: I can get a list of all authors
    When I make a "GET" request to the "/author"
    Then the response code is "200"
    And response body is matching expected "list_of_all_authors.json"

  Scenario Outline: I can get all titles from given author "<author_full_name>"
    When I make a "GET" request to the "/author/<author_full_name>/title"
    Then the response code is "<status_code>"
    And response body is matching expected "<expected_response_body>"

    Examples:
      | author_full_name    | status_code | expected_response_body          |
      | Ben Jonson          | 200         | ben_jonson_titles.json          |
      | Adam Lindsay Gordon | 200         | adam_lindsey_gordon_titles.json |
      | Jane Austen         | 200         | jane_austen_titles.json         |
