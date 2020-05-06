## Banking System Process Simulation

This project tries to simulate the real world banking system operations.

It has the following features:

- Basic user authentication

    - We validate the user by matching it with a pre-stored user account details in a text file.
    
    - We try to automate creation of user sessions by creating a session text file upon successful authentication.

- Creating an account

    - We accept user creation account details
    through the **stdin**, generate a unique account number and store customer details in the existing customers text file.
      

    > **STDIN** - Standard Input Stream

    - We automate the process of preventing users from using thesame email for creating multiple accounts by matching it with the existing record of customer details saved in a text file.

- Check account details

    - Our system is able to retrieve the account details for a particular customer by accepting the account number and searching through the stored customer details for a match. If a match is found, the customer's details is display in **stdout**.


    > **STDOUT** - Standard Output Stream

- Logout

    - When users log out, our system deletes the session text file created when they logged in.