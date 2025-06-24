# Coding assignment

To run enter into terminal these commands:

#create a virtual env

python3 -mvenv venv && source ./venv/bin/activate

# install dependancies -fast api pydantic httpx etc

pip install -r requirements.txt

To run server: 

uvicorn main:app --reload 

#you're ready to go!


#Assumptions
Assumption is that the json data types are consistently is str data type that can be converted to float().

#Considerations

I have used the float data type instead of int as I assume that is more appropriate for currency transactions.

My script lists ALL the currencies the account transacts in, not just eur and gbp.

The file retrieves all names/accounts associated with the account_id but only shows the first.


The script will :

1- Search the accounts json as requested for the all user accounts details associated with the account_id

2- Search for all txs of the account_id and return a formatted json of 'settled','refunded', 'chargeback' and 'balance' details for ALL currencies the acccount has transacted with.



#Error cases

The endpoint returns an error 404-NOT FOUND if there is no account found

The endpoint returns an error 505-SERVER ERROR if there is an error in the calculations i.e irregular formating in the tx.json etc


#TESTING

To run the unit tests in the test_tx file, type in 'pytest' into the terminal (outside of the server- press ctrl + C to exit server if it is running).

There is one test that checks:

1- the 404 response when no account is found for the req account_id

2- A valid 202 response for a particular account_id


#Future improvements

- For larger datasets I would use pandas/polars and load the csv/json into a dataframe for faster calculations

- I would also add a dependancy of a valid connection to the required database in production.