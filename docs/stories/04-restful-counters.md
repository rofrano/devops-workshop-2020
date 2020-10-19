# Add ability for multiple counters that are RESTful

**As a:** User  
**I need:** the ability to create multiple RESTful counters  
**So that:** I can keep track of multiple hit targets

**Assumptions:**

- We will implement using REST API guidelines
- Add ability to create multiple named counters
- Add ability to update counters by name

**Tasks:**

- [ ] Need to update root `/` URL to return `json` message
- [ ] Need to rename `/counter` to `/counters` 
- [ ] Need to change `GET` to only return the counter
- [ ] Need to implemtent `POST` to create new counters
- [ ] Need to implement `PUT` to update multiple counters

**Acceptance Criteria:**

```gherkin
Given I have a multi-counter ability
When I create a counter named foo
And I update the counter named foo to 1
And I call the hit /counters/foo URL
Then I should see 1 returned from the service
```
