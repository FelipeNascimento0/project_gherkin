Feature: Car door functionality

  Scenario: Closing the car door correctly
    Given the car door is open
    When the user closes the car door
    Then the car door should be closed
    And the car should indicate the door is closed
