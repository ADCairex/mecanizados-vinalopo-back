from src.models.search_ot import OTDetail, OTTime, OTPurchase

OT_DETAILS = [
    {
        "ot_id": 1,
        "quantity": 1,
        "client": "La Barraca",
        "contact": "Luismi",
        "proyect": "Desempaquetadora",
        "business_name": "Mecanizados Ángel Martínez",
        "business_unit": "Mecanizado",
        "order": 123456,
        "claim": 654321,
        "material": "Aluminio",
        "location": "Av. Alfonso el Sabio 27 2ºA"
    },
    {
        "ot_id": 2,
        "quantity": 5,
        "client": "Neoflex",
        "contact": "Carlos",
        "proyect": "Desempaquetadora",
        "business_name": "Mecanizados Ángel Martínez",
        "business_unit": "Mecanizado",
        "order": 123456,
        "claim": 654321,
        "material": "Aluminio",
        "location": "Av. Alfonso el Sabio 48 2ºA"
    },
      {
        "ot_id": 3,
        "quantity": 10,
        "client": "La Llave",
        "contact": "Pedro",
        "proyect": "Lenadora de botellas",
        "business_name": "Mecanizados Ángel Martínez",
        "business_unit": "Mecanizado",
        "order": 10,
        "claim": 6,
        "material": "Aluminio",
        "location": "Av. Alfonso el Sabio 50 2ºA"
    }
]

OT_TIMES = [
    {
        "ot_id": 1,
        "date": "2024-11-25",
        "employee": "Ángel Martínez",
        "work_station": "Torno CNC",
        "start_time": "10:00",
        "end_time": "16:00",
        "notes": "Mecanizado de pieza"
    },
    {
        "ot_id": 3,
        "date": "2024-11-26",
        "employee": "Ángel Martínez",
        "work_station": "Centro de mecanizado",
        "start_time": "09:00",
        "end_time": "16:00",
        "notes": "Mecanizado de pieza"
    },
    {
        "ot_id": 3,
        "date": "2024-11-27",
        "employee": "Ernesto Martínez",
        "work_station": "Torno CNC",
        "start_time": "08:00",
        "end_time": "16:00",
        "notes": "Mecanizado de pieza"
    },
    {
        "ot_id": 3,
        "date": "2024-11-28",
        "employee": "Manuel Martínez",
        "work_station": "Torno CNC",
        "start_time": "08:00",
        "end_time": "16:00",
        "notes": "Mecanizado de pieza"
    },
    {
        "ot_id": 2,
        "date": "2024-11-29",
        "employee": "Ángel Martínez",
        "work_station": "Centro de mecanizado",
        "start_time": "09:00",
        "end_time": "16:00",
        "notes": "Mecanizado de pieza"
    },
    {
        "ot_id": 2,
        "date": "2024-11-30",
        "employee": "Ernesto Martínez",
        "work_station": "Torno CNC",
        "start_time": "08:00",
        "end_time": "16:00",
        "notes": "Mecanizado de pieza"
    }
]

OT_PURCHASES = [
    {
        "ot_id": 1,
        "type": "Material",
        "description": "Una descripción",
        "quantity": 10,
        "cost": 100,
    },
    {
        "ot_id": 1,
        "type": "Material",
        "description": "Una descripción",
        "quantity": 10,
        "cost": 0.9,
    },
    {
        "ot_id": 2,
        "type": "Material",
        "description": "Una descripción",
        "quantity": 10,
        "cost": 100,
    },
    {
        "ot_id": 3,
        "type": "Material",
        "description": "Una descripción",
        "quantity": 1,
        "cost": 10,
    },
    {
        "ot_id": 3,
        "type": "Material",
        "description": "Una descripción",
        "quantity": 30,
        "cost": 1,
    },
]


class SearchOTRepository:
    def fetch_details(self, ot_id: int) -> OTDetail:
        """Fetch OT details."""

        for ot_details in OT_DETAILS:
            if ot_details["ot_id"] == ot_id:
                return ot_details
        

    def fetch_times(self, ot_id: int) -> list[OTTime]:
        """Fetch OT times."""

        ot_times_list = []
        for ot_time in OT_TIMES:
            if ot_time["ot_id"] == ot_id:
                ot_times_list.append(ot_time)

        return ot_times_list
    

    def fetch_purchases(self, ot_id: int) -> list[OTPurchase]:
        """Fetch OT purchases."""

        ot_purchases_list = []
        for ot_purchase in OT_PURCHASES:
            if ot_purchase["ot_id"] == ot_id:
                ot_purchases_list.append(ot_purchase)

        return ot_purchases_list
        
