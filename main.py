from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel
import json
# from sqlalchemy import create_engine , Column, Integer, String, Sequence
import os
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy_cockroachdb import run_transaction
from fastapi.testclient import TestClient
app= FastAPI()

#automatically load datasets on server start
with open('assets/accounts.json') as fp:
    accounts = json.load(fp)

with open('assets/transactions.json') as fp:
    tx = json.load(fp)

# class input(BaseModel):
#     account_id: str
    
@app.get("/",  status_code=status.HTTP_200_OK)
async def read_root(account_id: str ):   
    try:
        #get user account assuming unique account id
        account= [x for x in accounts if x['id']== account_id]

        if not len(account):
            #halt the func if there is no account_id match
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= 'No account found')

        # filter for all user's transactions
        usertxs= [x for x in tx if x['accountId']== account_id]
        
        #list all currencies txs under user account
        currencies= list(set([ x['currency'] for x in usertxs]))


        #recurring func for summations 
        settled= {}
        chargeback={}
        refunded={}

        #balance calculation -- settled txs - chargeback txs- refunded txs
        balance={}

        for curr in currencies:
            settled[curr]= sum([float(x['amount']) for x in tx if x['type']=='Settled' and x['currency']== curr])
            chargeback[curr]= sum([float(x['amount']) for x in tx if x['type']=='Chargeback' and x['currency']== curr])
            refunded[curr]= sum([float(x['amount']) for x in tx if x['type']=='Refunded' and x['currency']== curr])
            balance[curr]= settled[curr]-chargeback[curr]-refunded[curr]

        #create the output json
        output={}        
        output['account']= account[0]
        #can optionally list all the Names under the account id
     
        output['transactions']= {'settled': settled, 'chargeback': chargeback, 'refunded': refunded}
        output['balance']= balance
        
        return output
    
    except HTTPException as e:
        # FastAPI's internal handlers will catch this and format the response.
        raise e
    
    except Exception as e :
         
         raise HTTPException(status_code=  status.HTTP_500_INTERNAL_SERVER_ERROR , detail= e )  # Return an appropriate error status code


    

    
    



    # settled_eur= sum([float(x['amount']) for x in tx if x['type']=='Settled' and x['currency']== 'EUR'])

    # Chargeback_gbp= [float(x['amount']) for x in tx if x['type']=='Chargeback' and x['currency']== 'GBP']
    # Chargeback_eur= [float(x['amount']) for x in tx if x['type']=='Chargeback' and x['currency']== 'EUR']

    # Refunded_gbp= [float(x['amount']) for x in tx if x['type']=='Refunded' and x['currency']== 'GBP']
    # Refunded_eur= [float(x['amount']) for x in tx if x['type']=='Refunded' and x['currency']== 'EUR']




    
    # db= SessionLocal()
    # db.query("SELECT * FROM users")
    
    return {"Hello": "World"}





