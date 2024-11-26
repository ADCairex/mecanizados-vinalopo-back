from fastapi_camelcase import CamelModel

class OTDetail(CamelModel):
    quantity: int
    client: str
    contact: str
    proyect: str
    business_name: str
    business_unit: str
    order: int
    claim: int
    material: str
    location: str


class OTTime(CamelModel):
    date: str
    employee: str
    work_station: str
    start_time: str
    end_time: str
    notes: str


class OTPurchase(CamelModel):
    type: str
    description: str
    quantity: int
    cost: float