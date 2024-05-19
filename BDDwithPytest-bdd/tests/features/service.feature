@api
Feature: API testing
  As an application user,
  I want to get instant response for search terms via a REST API,
  So that my app can get answers anywhere.

  Scenario: Basic API Query
    Given the API is queried with "panda"
    Then the response status code is "200"
    And the response contains results for "panda"




