# Coding Competition
This repository holds the problem set for the PACS x MCU Coding Competition. For this competition, we provisioned a UNIX server and created different users with different permissions in order to allow each team to participate as their own user. Each user was expected to log into the server with the credentials provided to them. This repository's contents are to be pre-added to each users local files. The users are then expected to edit each question's file in order to debug the issues with it and get the output expected. Different questions required different testers along with different setups for the server.

## SSH Into the Server
To SSH into the server, run:
```shell
ssh <USERNAME>@comp.usstm.ca
```
You will be prompted to enter a password. This password will be provided by the organizers during the event.

## Run the Code

### Python
To run the python questions, `cd` into the question directory and run:
```shell
python <PATH-TO-FILE>
```
All the python questions will run the `TestCases.py` file when they are run in the terminal.

### Java
To run the java questions, `cd` into the question directory and run:

```bash
javac <FILE-NAME>
```

Any errors will be shown during the compilation. After you compile successfully, run:

```
java <FILE-NAME>
```

This will run all the test cases automatically, and you can see which you passed or failed.
### SQL
For the SQL question, you will have to edit the `students.sql` file and then test it by doing a series of steps:

- Run MySQL by running

  ```shell
  mysql -p -u <USERNAME>
  ```
  
  `<USERNAME>` will be the same as your username to log into SSH. You will be prompted to enter a password. This password will also be the same one as the one you used to SSH.
  
- Once you are in MySQL, run
 
  ```mysql
  source <FILENAME>
  ```
  
  `<FILENAME>` will be the name of your SQL file (`students.sql` in this case).
  
- If you have everything correct, you will see a query result with 2 entries. Otherwise, you will see an error. Debug this to get the answer!
