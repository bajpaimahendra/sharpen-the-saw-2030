### A -  Introductrion -----------------------------------
    1- Jenkins is an open-source DevOps tool
    2- to help developers integrate changes into different evironment(dev, staging, productio) 
    3- A project (also known as "jobs")  in Jenkins is an automated process to perform work
    4- Jenkins offers several different types of projects
         - Freestyle
         - Pipeline
         - Multibranch Pipeline
         - etc
         - The four main types of Jenkins pipelines are
         - Declarative, Scripted, Multibranch, and Shared Library

### B - Pipeline -------------------------------------------
     - Another way of job configuration through script rather than UI (Freestyle)
     - Through pipeline divide our job into multiple parts i.e. stages(build, test, deploy)
     - Parallel excution of stages are easy to configure 
     - Each stage can execute with different version of java/MVN
     - If any stage failed , we can start from that stage rather than from frist stage
     - Visualize the build flow
     - Build can hold for user input (e.g. if sonar coverage is 70% and manager allow to proced for next stage)
     - In Multibranch pipeline scrit will automatcally creates sub branches

### Pipeline Syntax 
     => Declarative -> Declarative Pipeline a more simplified syntax, should be written inside the `pipeline` block.

        pipeline {
            /* insert Declarative Pipeline here */
        }

     => Scripted -> traditionally written as scripted pipelines, should be written inside the `node` block   

        node {
            /* ----------- */
        } 

### C - Terminology --------------------------------

    pipeline {
        agent any
        stages {
            stage('Build') { 
                steps {
                }
            }
            stage('Test') { 
                steps {
                }
            }
            stage('Deploy') { 
                steps {
                }
            }
        }
    }

#### 1- Pipeline ->
    - is a set of instructions written as code.
    - It defines the entire build process
    - consists of different stages for building, testing, and delivering the application.
 

#### 2- Node ->
        - Node is  the "machine" on which a job runs.
        - Nodes can be physical machines, virtual machines, or containers.

#### 3- agent -> 
        -agent in a Jenkins pipeline refers to the location (machine, container, or environment) where the entire pipeline or a specific stage runs.
        - agent can be at pipeline level or stage level. 
        - It’s mandatory to define an agent.   
     



### How to Read Environment Variables -------------------------------
     There are two ways to read and access Jenkins environment variables:
     - Using the env object. ${env.BUILD_NUMBER}
     - Using the short variable name. ${BUILD_NUMBER}
     Note: better to use the env object ,
          to  reduces the chance of confusing the short variable name with another object.

### How to Set Environment Variable ---------------------------------------

#### Global Environment Variables
    Manage Jenkins -> System Configuration -> System
    Check the box next to 'Environment variables' 
    and click the 'Add' button to add a new variable.
#### Local Environment Variables
     uses the environment {} block
     environment {
        variable_name = "variable_value"
     }
     - inside of the pipeline means variable is available for any step
         pipeline{
            agent any
            environment {
                variable_name = "variable_value"
            }
         }
      - in particular stage means it is only available for that stage only. 
        pipeline{
            agent any
            environment {
                variable_name = "variable_value"
            }
            stages{
                stage('test'){
                     environment {
                      NAME = "Alex"
                    }

                }
            }
         } 
        - env object in a script{} can use to  define an environment variable:  
            script {
                    env.WEBSITE = "phoenixNAP KB"
                }
        - withEnv allows to define environment variables, which are available within the withEnv block. 

            withEnv(["VAR1=value1", "VAR2=value2"]) {
                // VAR1 and VAR2 available to only this block only
            }    
            Note : Environment variables in withEnv must not have spaces around the = and and spaces can lead to incorrect parsing.  

        - 'EnvInject' plugin to Jenkins allows you to inject environment variables during the build startup. This is particularly useful when creating a freestyle project in Jenkins.

### What is use of credentials()  in jenkins pipeline ?
     - credentials() function is used to securely retrieve, 
        credentials from the Jenkins Credentials Store (Manage Jenkins -> Credentials).

#### Parameters
    - used to pass the data dynamically
    Types of parameter 
            - String (can pass single line, )
            - text   (can pass multiple line)
            - boolean
            - password
            - file    
              


    








        






Dashboard -> Manage Jenkins -> System -> Environment variables

environment-variables-builtIn







