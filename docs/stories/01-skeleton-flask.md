# Create a skeleton Flask service

**As a:** Service Provider  
**I need:** a minimal Flask service  
**So that:** my developers have a starting point to add code

**Assumptions:**

- Only the root `/` URl needs to be defined
- Call it `app.py` for now

**Acceptance Criteria:**

```gherkin
Given I have a skeleton Flask app
When I call the / URL
Then I should see "Hello from Flask" returned
```
