import re

class QueryValidator:
    @staticmethod
    def is_safe_query(query: str) -> bool:
        dangerous_keywords = ["DROP", "DELETE", "UPDATE", "INSERT", "--", "/*", "*/"]
        return not any(keyword in query.upper() for keyword in dangerous_keywords)
