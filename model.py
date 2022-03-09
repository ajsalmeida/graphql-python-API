from typing import Optional
from sqlmodel import Field, SQLModel, Session, create_engine

class Politic(SQLModel, table=True):
	id: Optional[int] = Field(default=none, primary_key=True)
	node: str
	temperature: str
	date: str
	time_interval: str
	location: str


engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

def get_pols():
	with Session(engine) as session:
		result = session.execute(query).scalars().all()
	return result