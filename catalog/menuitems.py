from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import User,States, Base, MenuItem

engine = create_engine('postgresql://catalog:catalog@localhost/catalog')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
user1=User(name="admin",email="jyoshnamaniaddala@gmail.com",)
session.add(user1)
session.commit()

# Menu for UrbanBurger
state1 = States(name="Andhra pradesh",user_id=1)

session.add(state1)
session.commit()

menuItem1 = MenuItem(name="pulihora",ingredients="rice,tamrind,oil",image_url="https://www.google.com/search?q=pulihora&client=firefox-b-d&source=lnms&tbm=isch&sa=X&ved=0ahUKEwit47ng-rrgAhWJgI8KHXzMDu0Q_AUIDigB#",description="made of rice",itemtype="rice item",link="http://youtube.com",state=state1,user_id=1)

session.add(menuItem1)
session.commit()


