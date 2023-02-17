from src.models.base import *

class ModelBookType(Base):
    __tablename__ = "t_book_types"
    type_id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    name = Column(String, nullable=False)
    description = Column(Text)
    active_flag = Column(Boolean, default=True)
    inactive_date = Column(DateTime(timezone=True))
    last_update_date = Column(DateTime(timezone=True))

    relationship("src.models.book.ModelBook")