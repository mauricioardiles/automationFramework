
Feature: I want to search for products

  Scenario : Search
    Given I am on home page
    When I search for "phone"
    Then I should see list of matching products in search results