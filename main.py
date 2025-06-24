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





# try:
#     # 2. Create the engine
#     engine= create_engine(os.environ["DATABASE_URL"], echo=True)
#     # 3. Test the connection (optional, but good practice)
#     # This will attempt to connect and raise an exception if it fails

#     with engine.connect() as connection:
#         print("Successfully connected to the database!")
#         # You can execute a simple query to further verify
#         # result = connection.execute(text("SELECT 1"))
#         # print(f"Query result: {result.scalar()}")
        
#     # 4. Create a sessionmaker for interacting with the database (for ORM)
#     SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# except Exception as e:
#     print(f"Error connecting to the database: {e}")

# Base = declarative_base()

# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     email = Column(String, unique=True, nullable=False)
#     age = Column(Integer)

# class Product(Base):
#     __tablename__ = 'products'

#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     price = Column(Integer, nullable=False)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

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





