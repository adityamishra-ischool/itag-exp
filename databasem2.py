from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from sqlalchemy_declarative import Address, Base, Person
 
engine = create_engine('sqlite:///sqlalchemy_examplenew.db')
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
 
# Insert a Person in the person table
#new_person = Person(name='AdminMan',id=1,isit='No',role='Admin',password='password')
new_person = Person(name='Player1',id=2,isit='No',role='Player',password='password')
new_person = Person(name='Player2',id=3,isit='No',role='Player',password='password')
new_person = Person(name='Player3',id=4,isit='Yes',role='Player',password='password')
new_person = Person(name='Player4',id=5,isit='No',role='Player',password='password')
new_person = Person(name='Player5',id=6,isit='No',role='Player',password='password')
new_person = Person(name='Player6',id=7,isit='No',role='Player',password='password')
new_person = Person(name='Player7',id=8,isit='No',role='Player',password='password')
session.add(new_person)
session.commit()
 
