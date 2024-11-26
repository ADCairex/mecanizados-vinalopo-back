from src.repositories.search_ot import SearchOTRepository

class SearchOTService:
    def __init__(self, repository: SearchOTRepository):
        self.repository = repository

    def get_details(self, ot_id: int):
        """Get the details of an OT from the repository."""
        return self.repository.fetch_details(ot_id)

    def get_times(self, ot_id: int):
        """Get the times of an OT from the repository."""
        return self.repository.fetch_times(ot_id)
    
    def get_purchases(self, ot_id: int):
        """Get the buys of an OT from the repository."""
        return self.repository.fetch_purchases(ot_id)
