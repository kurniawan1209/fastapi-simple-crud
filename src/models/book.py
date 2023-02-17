from src.models.base import *

class ModelBook(Base):
    __tablename__ = "t_books"
    book_id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    title = Column(String(100), nullable=False)
    description = Column(Text)
    type_id = Column(UUID(as_uuid=True), ForeignKey("t_book_types.type_id"))
    active_flag = Column(Boolean, default=True)
    inactive_date = Column(DateTime(timezone=True))
    last_update_date = Column(DateTime(timezone=True))

    relationship("src.models.book_type.ModelBookType")