# Make the counter persistent

**As a:** User  
**I need:** the hit counter to persist the last known count  
**So that:** I don't loose track of the count after the service is restarted

**Assumptions:**

- We will use Redis as the persistent store
- A Redis image from Docker should be used

**Tasks:**

- [ ] Need to update the `Vagrantfile` with Redis Docker image
- [ ] Need to create a Model that uses Redis

**Acceptance Criteria:**

```gherkin
Given I have a persistent counter
When I advance the hit counter to 2
And I restart the hit counter service
And I call the hit /counter URL
Then I should see 3 returned from the service
```
