from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    designation = Column(String)
    department = Column(String)
    checkin_timestamp = Column(DateTime)

    def __repr__(self):
        return "employee : {} - {}".format(self.id,
                                           self.name)
