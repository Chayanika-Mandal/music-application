from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, User
from utils import get_input, print_menu

engine = create_engine("sqlite:///data.db", echo=True)

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


# menu = "Welcome to music-application! What would you like to do?
#           1. create new account
#           2. log into existing account
#           3. search music
#           4. exit application"

print("Welcome to music-application! What would you like to do?")
print_menu(
    [
        "Create new account",
        "Login into existing account",
        "Search music",
        "Exit application",
    ]
)
while True:
    user_input = get_input(4, input())
    if user_input == 1:
        session = Session()
        print("You chose to create new account")
        username = input("Enter username: ")
        password = input("Enter password: ")
        confirm_password = input("Confirm password: ")
        num_already_existing_user = (
            session.query(User).filter_by(username=username).count()
        )
        if num_already_existing_user != 0:
            print("This username already exists")
        if password == confirm_password:
            now = datetime.now()
            new_user = User(
                username=username, hashed_password=password, date_of_joining=now
            )
            session.add(new_user)
            session.commit()
            print("Your account was created successfully")
            break
    elif user_input == 4:
        print("Goodbye!")
        break
