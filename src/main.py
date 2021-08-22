import pprint

# from sqlalchemy import create_engine

# from models import Base

print = pprint.pprint

# engine = create_engine("sqlite:///data.db", echo=True)

# Base.metadata.create_all(engine)

# menu = "Welcome to music-application! What would you like to do?
#           1. create new account
#           2. log into existing account
#           3. search music
#           4. exit aplication"
user_input = input("Welcome to music-application! What would you like to do?")
while user_input not in ['1', '2', '3', '4']:
    user_input = input("Your input was incorrect. Please provide the input again.")
