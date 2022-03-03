[![Django CI/CD](https://github.com/devopslecturer/awpgdip2022/actions/workflows/django.yml/badge.svg?branch=Dev)](https://github.com/devopslecturer/awpgdip2022/actions/workflows/django.yml)
[![Release Wicked-Adventure](https://github.com/devopslecturer/awpgdip2022/actions/workflows/release.yml/badge.svg?branch=Dev&event=release)](https://github.com/devopslecturer/awpgdip2022/actions/workflows/release.yml)
[![Sonar Cloud Scanning](https://github.com/devopslecturer/awpgdip2022/actions/workflows/sonar_scan.yml/badge.svg?branch=Dev)](https://github.com/devopslecturer/awpgdip2022/actions/workflows/sonar_scan.yml)

# awpgdip2022
Wednesday Assignment PgDip Group 2021-2022

## Table of Contents

       Table of Contents
        Preamble
            Product Owner
            Rockstars
        Project Deadline
        Project Specification
        Considerations
        Useful Links
            For more information visit our other sections
        Risk Register
        Tenants of Design
        Social Contract

## Preamble

This is the online repository for the https://github.com/devopslecturer/awpgdip2022. 

Summary:
The end customer would like an online booking system for range of horror themed adventure parks. 
Their most popular product is Risky Rollercoaster. The system must take details of customer map them 
to the themed adventure park of their choice along with a single box for extra set of health and 
warning checkboxes. The system should be clean and simple. Your team has been tasked with creating 
the pipeline for the SDLC. You have also been asked to provide a simple prototype page(s) to test the 
pipeline. The system needs to take into account the usual security requirements. The administrator of 
the end system (Wednesday or Pugsley) should be able to access detailed information and edit as 
appropriate. Once the client enters details it should not be able to be changed by the holiday maker.


Our product will be delivered using an Agile methodology that embraces the DevOps culture. Please note that our culture embraces change and these documents are treated as living, breathing artefacts that will be continuously updated.

### Scrum Master
-Vitalijus Baseckas    


### Product Owner
-Muhammad Anwar

### Team Members
-Neha Tripathi
-Panagiotis Drakos
-Wagner Ribeiro
-Rodrigo Lima

Lecturer: Paul Greaney
  
### Project Deadline
1st April - TBD
Refer to Blackboard for the most up to date information on deadlines.
  
## Project Specification  
<!-- <team must agree specifications here - below are samples for discussion purposes>     -->
    Clean and simple design
    User access levels (client, administrator)
    Includes at least one self developed api and one webservice
    To be run over Amazon AWS

    Frameworks
    Database
    Database persistence technology
    Define the buisness Requirements
    Named queries and database triggers for security
    Regex for cleansing and validation of data before sending to the database.

## Useful Links

    DC Slack:https://lyit.slack.com/archives/C02PJK31GUD
    Jira: 
    GitHub: https://github.com/devopslecturer/awpgdip2022
    Project close out presentation: 

### More Information
For more information visit our other sections
Section     Description
Process     Describes the companies process
Project Log     Log of project activities
Costings    Overview of the project cost
Architecture    Outlines the architecture
Environments    Overview of the environment set-up
DR Plan     Disaster Recovery Plan and procedures
Requirements    Overview of the requirements for the project
SLAs    Service level agreements
Risk Management     How we manage risk
Security    Overview of security
Project Log     Team log for the project

To be Decided on meetings:
      - Performance Management Tool(s)
      - Unit Testing – automated Sonarqube or similar
      - Issue ticketing & boards
      - Security Tools (SAST/DAST) 
      - Binary repositories (eg. Artifactory)
      - Automated documentation
      - Code Created (include consideration for security, performance, etc.)
      - Automated Pipeline

## Risk Register

These are the current Risks on the project, re-aligned on a weekly basis

    Infrastructure proving to be a real problem, may block being able to release software
    Team is finding itself to be running short on time due to other work and study commitments
    No PO feedback on software
    Unknown technology choices has led to a lot of upskilling required
    Changing / ambiguous requirements
    Talk of the company being bought out has raised concerns
    Lack of rights for toolsets chosen has hindered progress and ability to deliver

## Tenants of Design
<pick from the sample sections below and add your own>
    Dedication to clean, secure, performant and self documented code
        code Frameworks used
        code coverage tool used
        Secure code: Regex for cleansing and validation, Named queries and database triggers
        performance testing tool to be used
    Documentation / code commenting (javadoc)/separate branch
    Datastore for persistance
    Testing:
        Unit testing
        integretation testing
        UA
    Environments:
        staging and production
        tight configuration management for consistency and reproducibility
        automated creation and deployments
        integrated and automated pipeline (commit -> test -> deploy)
    Github version control:
        branches used
        version/release management
    Agile project management methods/principles (jira)

## Social Contract

### Meetings 
       
    Stand-ups will occur on <Monday 20:30>.
    The order that people give their updates will be based on <<define the order>> of those present at the meeting.
    Updates will be in the form: What I've done, What I plan to do, Impediments
    Sprint planning will occur every other <<day and time>>.
    Please add and update items within Jira prior to the sprint planning session.
    Sprint retro will occur once a month, <<Date and time>>.
    The order that people present their sprint retro updates will be based on alphabetical order of those present at the meeting.
    Points raised in the sprint retro will be noted and posted on the slack channel by the Scrum Master.
    Backlog refinement?
    Task estimation will be done using <<what method>>. 
    Come prepared to meetings.
    Be on time for Stand Ups and meetings.
    Mobile phones on silent.
    Everyone has equal voice and valuable contribution.
    Keep your language and tone professional at all times.
    Be honest.
       
    1st week tasks 2021.07.12
       - Jira was decided to be used
       - Python was decided to be the main language
       - Create Jira project Neha and Vitalijus
	   
	2nd week meeting minutes 2021 December 13th
		- On this meeting Django has been selected as framework for our project. 
			Flask was also considered to use in this project, but we did go with this. 
			Django is better integration and easier to use than Flask. 
			Django is more professional in terms web development.
		- Add comments inside the script. The code is pretty much functioning.
		- On the meeting was discussed to review on (14/12/2021) the progress of the project. 
		- The code is already on Git Hub. Looking for a person who will be responsible to implement CI.
    
Long holidays.

6th week meeting minutes 2022 January 10th
	Participants:
	Vitaliy 
	Niha
	Panagiotis

	During this meeting the following things were done.
	1.	Moved uncompleted tasks to Sprint 2
	2.	Some tasks are close for Sprint 1
	3.	Added values for the tasks on Sprint 2

	Subjects to discuss on the next team meeting:
	1. Set the priority of the tasks
	2. Discuss the Test strategy
	3. Discuss with the Team about the AWS steps or Heroku. What we go with?
	4. Obtain Admin right for everyone 
	5. Add values to the tasks on Sprint 1 to use this statistic for future use.

	Issues discussed:
	Niha had an issue on PD-4 probably due to permissions
	The team did not gather on this meeting. We need to work together hard on this.


7th week meeting minutes 2022 January 17th
No records

8th week meeting minutes 2022 January 24th
No records

9th week meeting minutes 2022 January 31th
No records

10th week meeting minutes 2022 February 7th
Meeting did not happened. The team did not gather.

11th week meeting minutes 2022 Febrary 14th
Meeting did not happened. The team did not gather. Happy Valentines day.
	

### Communication

    Slack is the preferred method of communication.
    If a demonstration is required use << ?>>, record the session and upload to the Slack channel.
    No Slack communications between "<Time and Timezone>".
    Raise a problem as soon as you see it.
    Respect each other and understand differences in knowledge.
    All team documents are to be created using Markdown language and shared on GitHub.
    There are no silly questions, if you don’t understand, ask.
    Share success stories.
    Focus on the positives.
    Don’t make assumptions.
    Don’t interrupt and cut another person off while they are talking.
    Listen when someone is talking, don’t interject.
    Zero tolerance for bullying.
    Communication in this order: <<list in order of preference for the team>>
    Agile way of working.
    If are assigned a job, take ownership of it and keep it up to date.
    Stick to your agreed working patterns. Let the team know when you are late or going early.
    Keep JIRA board updated at all times.
    Update the Scrum Board as you progress the story i.e. don’t update at standup.
    Don't be afraid to ask for help.
    Don't be afraid to give constructive critism, as long as it is constructive.
    Solve roadblocks within the team. If the impediment can’t be solved within the team then give it to the Scrum Master.

## Other

    Sprints will start <<check with lecturer>>.
    The Scrum Master role rotates each week, the schedule is available on the on the process section
    The Product Owner role rotates each week, the schedule is available on the on the process section
    Jira will be used for task management and planning.
    Each member of the team will work <<? story points>> per week, unless they are on vacation.

### Branching Strategy
       Master __ Main 
       
       Dev _____ Feature
             |__ Bugfix


### Estimating Story Points Within Jira

The teams team's velocity is calculated by dividing the the number of points burned each sprint divided by no of sprints. The Velocity chart from Jira (below) is used for this calculation.

The teams current story point velocity is "<Choose the number!>".
	

[![Code scanning](https://github.com/devopslecturer/awpgdip2022/actions/workflows/codeql-analysis.yml/badge.svg?branch=Dev)](https://github.com/devopslecturer/awpgdip2022/actions/workflows/codeql-analysis.yml)
