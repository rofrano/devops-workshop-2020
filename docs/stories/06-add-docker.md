# Add Docker support

**As a:** Service Provider  
**I need:** the ability to deploy my service using Docker  
**So that:** I can move with speed and agility  

**Assumptions:**

- Need to create a `Dockerfle` for the service
- Need to update GitHub Actions to use Docker version

**Acceptance Criteria:**

```gherkin
Given I have my service in a Docker image
When I user docker run
Then I should have my service running in a contatiner
```
