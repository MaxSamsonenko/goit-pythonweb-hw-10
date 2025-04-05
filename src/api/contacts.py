from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.schemas import ContactCreate, ContactUpdate, ContactResponse
from src.services.contacts import ContactService

router = APIRouter(prefix="/contacts", tags=["contacts"])

@router.get("/", response_model=List[ContactResponse])
async def read_contacts(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    service = ContactService(db)
    return await service.get_contacts(skip, limit)

@router.get("/{contact_id}", response_model=ContactResponse)
async def read_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    service = ContactService(db)
    contact = await service.get_contact(contact_id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactCreate, db: AsyncSession = Depends(get_db)):
    service = ContactService(db)
    return await service.create_contact(body)

@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(contact_id: int, body: ContactUpdate, db: AsyncSession = Depends(get_db)):
    service = ContactService(db)
    contact = await service.update_contact(contact_id, body)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.delete("/{contact_id}", response_model=ContactResponse)
async def delete_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    service = ContactService(db)
    contact = await service.remove_contact(contact_id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.get("/search/", response_model=List[ContactResponse])
async def search_contacts(query: str, db: AsyncSession = Depends(get_db)):
    service = ContactService(db)
    return await service.search_contacts(query)

@router.get("/birthdays/", response_model=List[ContactResponse])
async def upcoming_birthdays(days: int = 7, db: AsyncSession = Depends(get_db)):
    service = ContactService(db)
    return await service.get_upcoming_birthdays(days)