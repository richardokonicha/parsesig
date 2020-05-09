import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

SQLITE = "sqlite:///db.db"
engine = create_engine(SQLITE, echo=True, connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class MessagePair(Base):
    __tablename__ = "message_pair"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    pair_name = Column(String)
    api_id = Column(String)
    api_hash = Column(String)
    bot_token = Column(String)
    channel_input = Column(String)
    channel_output = Column(String)

    
    def __init__(self, pair_name, user_id=None, channel_input=None, channel_output=None):
        self.user_id = user_id
        self.pair_name = pair_name
        self.channel_input = channel_input
        self.channel_output = channel_output
    
    def commit(self):
        session.add(self)
        session.commit()
    
    def delete(self):
        session.delete(self)
        session.commit()
    
    @classmethod
    def get_name(cls, name):
        return session.query(MessagePair).filter_by(pair_name=name).first()

    @classmethod
    def get_id(cls, id):
        return session.query(MessagePair).filter_by(user_id=id).first()

    
    def __repr__(self):
        return f"MessagePair {self.pair_name}"


Base.metadata.create_all(engine)