# misc_code
small scripts from here and there
* chessboard.sh 
  * chess board visual on CLI(not the game). Using the characters or \e exscape sequence for black and white background

* countdown_timer.sh
  * shutdown counter before EOD. Reminder for those who forget

* create_user.sh
  * create the new user and configure ssh-key based authentication. Requires current access 

* airflow-useradd.sh
  * add new user for web UI password authentication
  ```[webserver]
  authenticate = True
  auth_backend = airflow.contrib.auth.backends.password_auth 
  ```
  Automates the commands for adding new user for Airflow WebUI
  
