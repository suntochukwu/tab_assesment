# Coding assignment

# To run enter into terminal these commands:

#create a virtual env

python3 -mvenv venv && source ./venv/bin/activate

Install dependancies by typing in the terminal:

pip install -r requirements.txt

To run server type into the terminal : 

uvicorn main:app --reload 




The script will :

1- Search the accounts json as requested for the all user accounts details associated with the account_id

2- Search for all txs of the account_id and return a formatted json of 'settled','refunded', 'chargeback' and 'balance' details for ALL currencies the acccount has transacted with.

# Testing using postman

Upon starting the server in the terminal will be a line:

INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

Open postman and paste in the http string after starting the uvicorn server

* According to the line above the port is:  http://127.0.0.1:8000

Remember it's a GET request ie .get('/') should be used in Postman.

In Postman enter the port and as params: key: 'account_id' and the value: '1234' and press send to get a response.


# Assumptions

Assumption is that the json data types are consistently is str data type that can be converted to float().
If this is not the case the endpoint with return a 505 error.

# Considerations

- I have used the float data type instead of int as I assume that is more appropriate for currency transactions.

- My script lists ALL the currencies the account transacts in, not just eur and gbp.

- The file retrieves all names/accounts associated with the account_id but only shows the first.


# Error cases

- The endpoint returns an error 404-NOT FOUND if there is no account found

- The endpoint returns an error 505-SERVER ERROR if there is an error in the calculations i.e irregular formating in the tx.json etc


#TESTING

To run the unit tests in the test_tx file, type in 'pytest' into the terminal (outside of the server- press ctrl + C to exit server if it is running).

There is one test that checks:

1- the 404 response when no account is found for the req account_id

2- A valid 202 response for a particular account_id


#Future improvements

- For larger datasets I would use pandas/polars and load the csv/json into a dataframe for faster calculations

- I would also add a dependancy of a valid connection to the required database in production.