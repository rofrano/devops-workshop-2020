# Add ability to delete a counter

**As a:** User  
**I need:** the ability to delete a counter  
**So that:** I can remove unwanted counters  

**Assumptions:**

- Deleting a counter will remove it from the database
- If the counter doesn't exist a `204_NO_CONTENT` will be returned

**Acceptance Criteria:**

```gherkin
Given I have counter named foo
When I delete the counter named foo
Then I should receive a 204_NO_CONTENT
And I retrieve the counter named foo
Then I should receive 404_NOT_FOUND
And I delete the counter named foo again
Then I should receive a 204_NO_CONTENT
```
