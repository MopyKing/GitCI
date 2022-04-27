About the Assignment :

The Purpose is to create a Jenkins job that is configured
to run a Build - triggered by changes in a specific repository
on GitHub

First i created a local & remote repository.

Then of Jenkins i created a new job that is configured as following :

- Source Code Management : Git
  then added the repository URL

- Build trigger : Poll SCM * * * * *
  for the job to be triggered when changes occur in the repository

- Build : Execute Shell
  for the job to run commands on the terminal once triggered

  javac shido.java
  java shido

to see that the file can be compiled and run


then i added a simple java file inside my local repository : 

public class shido{
  public static void main(String[] args) {
    for (int i=1;i<=10;i++){
      System.out.println("Shido V10.."+i);
    }
  }
}

compiled to create the .class file 

then pushed them into the remote repository

the Jenkins job has been triggered automatically, and finished as : SUCCESS
with the correct console output
