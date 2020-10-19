# Add a counter where each GET increments the counter

**As a:** User  
**I need:** a way to register a hit on the counter
**So that:** it increments with every access

**Assumptions:**

- Calling the `GET /counter` URl will increment the counter
- No need for the counter to be persistent for now

**Acceptance Criteria:**

```gherkin
Given I have a counter
When I call the /counter URL
Then I should see the counter increment
```
