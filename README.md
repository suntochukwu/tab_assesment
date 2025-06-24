# Coding assignment

To run install :
fastapi
httpx
pytest

To run server: 

uvicorn main:app --reload 

Assumption is that the json data is str data type that can be converted to float().

#Considerations

I have used the float data type instead of int as I assume that is more appropriate for currency tx.


The script lists ALL the currencies the account transacts in, not just eur and gbp.


The file retrieves all names/accounts associated with the account_id but only shows the first.

The script will :
1- Search the accounts json as requested for the user accounts associated with the account_id


2- Search for all txs of the account_id and return a formatted json of settled,refunded, chargeback and balance details for ALL currencies the acccount has transacted with.



#Error cases

The endpoint returns an error 404-NOT FOUND if there is no account found

The endpoint returns an error 505-SERVER ERROR if there is an error in the calculations

#TESTING

TO run the unit tests in the test_tx file, type in 'pytest' into the terminal.

There is one test that checks:

1- the 404 response when no account is found for the req account_id

2- A valid 202 response for a particular account_id


#Future improvements

- For large datasets I would use pandas/polars and load the csv/json into a dataframe for faster calculations

- I would also add a dependancy of a valid connection to the required database in production.