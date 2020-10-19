# DevOps for Software Engineers Workshop 2020

This repository represents the starting point for a 3 hour workshop on **DevOps for Software Engineers**. It is menant to be forked to your own GitHub account so that you can create Issues and Pull Requests and push software updates as you follow along with the hands-on workshop.

## Overview

Many job postings consider DevOps to consist largely of operation skills, but what about the software engineers that provide the Dev? This tutorial will give attendees first hand experience in building a microservice and deploying it as a container on Kubernetes using DevOps practices and methods. An overview of DevOps culture and cloud native microservice architecture will be presented as a backdrop to the hands-on exercise. 

Attendees will build a RESTful Python Flask microservice using Test Driven Development techniques and run it locally. Then we will introduce the concepts of Docker and wrap that service in a Docker container and re-run our tests proving that the behavior has not changed. We will then set up a CI/CD pipeline and deploy the microservice to a local Kubernetes cluster. Finally we will add persistence to our microservice and deploy a Redis service in our Kubernetes cluster for our microservice to use showing how to use secrets for storing sensitive information like database credentials. 

The tutorial will switch between lecture and lab several times as new concepts are introduced and then quickly demonstrated and implemented in the hands-on exercise. Attendees will come away with a good understanding of how modern software is delivered using DevOps tools and practices with a programmable containerized infrastructure like Kubernetes.

## Prerequisites

To successfully follow along with this workshop you will need to have VirtualBox and Vagrant installed on your computer. The lab will be using an Ubuntu 18.04 virtual machine configured by Vagrant.

## Agenda

The workshop Agenda is as follows:

### Introduction and Setup

Overview of how the workshop will be run. Get Vagrant and VirtualBox installed and setup and building during the DevOps Overview section if you haven't done that before the workshop.

Follow these instructions to [Install Prerequisite Software](docs/install-prereqs.md)

Instructions on [Working with Vagrant and VirtualBox](docs/working-with-vagrant.md)

### DevOps Overview

Brief  Overview of DevOps with an emphasis on the Software Developer perspective. Attendees will be introduced to the practices that are covered in this workshop and also learn why culture is the most critical aspect of DevOps to get right.

### Agile Planning

Introduction to Agile Planning concepts. Create an agile plan for the remainder of the workshop. Attendees will create Stories that they will execute during workshop. They will also use a Burndown chart to track their progress.

Stories include:

1. Create a skeleton **Flask** service
2. Add a counter where each `GET` increments the counter
3. Make the counter persistent
4. Add ability for multiple counters that are RESTful
5. Setup Continuous Integration
6. Add ability to delete a counter
7. Add Docker support
8. Add Kubernetes support

Full stories for planning are [here](docs/user-stories.md)

### Social Coding

Introduction to the **Git Feature Branch Workflow**. Attendees will assign the first [Story #1](docs/stories/01-skeleton-flask.md) from their Sprint Backlog to themselves, create a feature branch to work on the story, and issue a pull request to merge their code back into master.

### Test Driven Development

Introduction to Test Driven Development. Attendees will write the test cases for the code they wish they had, and then implement that code following Agile Planning and Feature Branch Workflow. They will implement [Story #2](docs/stories/02-add-counter.md) to add a non-persistent counter where each `GET` increments the counter.

### Microservices and REST APIs

Introduction to Microservice Architecture and REST APIs. Attendees will begin to code their first REST API for the hit counter application starting with test cases that follow good RESTful coding standards. Stories include [Story #3](docs/stories/03-add-persistence.md) and [Story #4](docs/stories/04-restful-counters.md) adding persistence to the counter in the form of a **Redis** database.

### Continuous Integration and Continuous Delivery

Attendees will be introduced to the concepts of CI/CD and in particular Travis CI. They will connect their git repo to Travis CI so that their test cases run with every Pull Request. Stories include added Redis to their Travis CI in [Story #5](docs/stories/05-setup-ci.md) and implementing the remainder of the REST interface in [Story #6](docs/stories/06-delete-counter.md).

### Introduction to Docker

Overview of Docker containers. Attendees will create a Dockerfile for their microservices and run it in a Docker container. They will implement Story #6 and update Travis CI to run tests for the Dockerized version.

### Introduction to Kubernetes

Overview of Kubernetes. Attendees will deploy the Docker version of their microservice in a Kubernetes cluster. They will implement Story #7 and will also have to deploy a Redis service in Kubernetes for their microservice.

## Copyright
(c) 2019, 2020 John Rofrano, All Rights Reserved
