from typing import List,Optional
import strawberry
from sqlmodel import Field, SQLModel, Session, create_engine, select, Relationship

class SQLPolitic(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	node: str
	temperature: str
	date: str
	time_interval: str
	location: str

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)


@strawberry.type
class Politic:
	id: int
	node: str
	temperature: str
	date: str
	time_interval:str
	location: str

def get_pols() -> List[Politic]:
	with Session(engine) as session:
		politics = session.query(SQLPolitic).all()
	return politics

@strawberry.type
class Query:
    politics: List[Politic] = strawberry.field(resolver=get_pols)
schema = strawberry.Schema(query=Query)
