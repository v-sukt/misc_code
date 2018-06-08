### bash scripts/functions

* sizeof.sh : converts size from bytes to human readable string .. remember to append B in the end :)

* chessboard.sh : chess board visual on CLI(not the game). Using the characters or \e exscape sequence for black and white background

* countdown_timer.sh : shutdown counter before EOD. Reminder for those who forget

* create_user.sh : create the new user and configure ssh-key based authentication. Requires current access

* duration.sh : the duration conversion from the no. of seconds
  - useful to get
    - [x] difference between two files creation :
           ```
            file1_date=$(stat --format +%Z file1)    # This generated the last modified time since epoch
            file2_date=$(stat --format +%Z file2)    # generates as the number of seconds
            echo $(duration $(expr $(file1_date) - $(file2_date)))
           ```
    - [x] Time since the epoch :
           ```
             echo -e "Since epoch\t: $(duration $(date +%s))"
           ```
* session-checks.sh : To check on remote server if there are any connections active more than x time and then possibly do:
   - inform user to close them about active sessions (if it's not desired to have user active sessions from a server for longer time say,
      - token based access. But the sessions are kept alive even after end of token-expiry to allow users to continue working :: to inform them)
      - your team forgets their active sessions on server and they are left on server forever
   - terminate the sessions/connections based on PIDs (not coded in script)

