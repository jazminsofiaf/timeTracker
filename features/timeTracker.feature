Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      When we implement a test
      Then behave will test it for us!

  Scenario: run a project simple test
      Given a project with name p1
      When we look for the name
      Then it is p1

  Scenario: run a task simple test
      Given a task with name t1 and project name p1
      When we look for the task name
      Then it is t1


  Scenario: Setup Table
     Given a set of project:
        | proyecto  | tarea	|
        | proy1     | t1	|   		  
   
    When nothing happens
    Then we will find that "t1" belongs to the proyecto: "proy1"

  Scenario: add hours
      Given a developer
      When we add hour
      Then we will find an hour created
      

 Scenario: hour validation
      Given a developer
      When we try to add hours with not project
      Then it throws a ValidationError with message "El proyecto es obligatorio"