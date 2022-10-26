Feature: Validating the employee details from Dummy_API_link

  Scenario: Verify Employee API functionality
    Given the employee details needs to be fetch from the API call request
    When I execute the GetAPI method
    Then Validate the employee details

