Parallel Deployment  ? 

##### Jenkins Complete Referenece (DevOpsSchool)
https://www.youtube.com/watch?v=yZn-kOjLSXw&list=PLDhScTEBdP8xhrtiXNbm1Wla1u77GhF3O&index=1

https://www.youtube.com/watch?v=RgELCs-gyz4&list=PL7qItE4wuWkv7G1hqcU6ICzyKk61lFaTz

https://www.devopsschool.com/blog/category/jenkins/

Objective of DevOps ?
    Immediate Release 
    Improve Quality of word

---- SDLC -----------------------
    Plan -> Code -> Code Review -> Build -> test

### What is jenkins ?
    - old name is hudson
    - is CI (Continuous Integration) tool
    - is integration tool, to integrate code
    - automate manual setup
    - scheduling
    - immediate feedback
    - written in java
### Release
     - Community (free and opensource)
     - Enterprise (paid) 
#### Alternate of jenkins
    - teamciy
    - Bamboo
    - Ubuild         

### What is Continuous Integration ?    
    Automatically Build -> Aut Test
    Immimmediate Feedback to dev team
    benefit -> Quantity and Quality of work will improve


### architecture of Jenkins


#### formula to work with jenkins ?
    you have to ask some question to team ?

     what is your technology and version ?
      - java
      - .net
      - node
      - python

    Where is code ? give the access of repository ?
    - github
    - svn 

    what is your builder(main file) ?
    - .sln, solution file of .net project ?
    - index.js , node js project
    - how frequently you want this job to be triggered ?
        - hourly

    How you want a feedback of this job ?
        - on email

### How you will organize your jenkins jobs
    - view
    - folder
### How you will schedule (trigger) a jenkins job ?
    - at certain time
    - at regurlar interval
    - using command line
    - trigger this job if other job is triggered 
    - trigger a job when there is PUSH in to gihub/bitbucket
##### IMP Plugnin
    https://www.devopsschool.com/blog/top-33-free-jenkins-plugins-and-their-tutorials-with-step-by-step-guide/

    - Job Config History

#### How to See Environment Variables in Jenkins
    - through a web browser
        [Jenkins URL]/env-vars.html
    - through command in pipeline
        steps{
            //====== PreDefined Environment Variables for this job
            sh "printenv" // on Linux 
            //bat "set" // on windows
        }

#### difference between ${env.VAR}, ${VAR} or $VAR way of defining Jenkins declarative pipeline env varaibles?

     - "${VAR}" and "$VAR" are equivalent
     - You use the curly braces to separate the variable name from the rest of the string
     - you can use env.VAR or just VAR

### Security
    https://www.youtube.com/watch?v=6sgJ5cL21I4&list=PLDhScTEBdP8wVaiL-rlxvEY26aIPC4KCa&index=3

### Jenkins Advance Tutorials Part-2 - 2024
 https://www.youtube.com/watch?v=bdf2NryeZIA&list=PLDhScTEBdP8xAA3wx30LCE5A6EaSt_jAY   



### Diff b/w Scripted and Declarative pipeline

https://www.youtube.com/watch?v=yl3a4jnf0jA




