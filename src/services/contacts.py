from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas import ContactCreate, ContactUpdate
from src.repository.contacts import ContactRepository

class ContactService:
    def __init__(self, db: AsyncSession):
        self.repository = ContactRepository(db)

    async def get_contacts(self, skip: int = 0, limit: int = 100):
        return await self.repository.get_contacts(skip, limit)

    async def get_contact(self, contact_id: int):
        return await self.repository.get_contact_by_id(contact_id)

    async def create_contact(self, body: ContactCreate):
        return await self.repository.create_contact(body)

    async def update_contact(self, contact_id: int, body: ContactUpdate):
        return await self.repository.update_contact(contact_id, body)

    async def remove_contact(self, contact_id: int):
        return await self.repository.remove_contact(contact_id)

    async def search_contacts(self, query: str):
        return await self.repository.search_contacts(query)

    async def get_upcoming_birthdays(self, days: int = 7):
        return await self.repository.upcoming_birthdays(days)