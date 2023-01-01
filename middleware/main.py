from datetime import datetime, timedelta
from collections import deque
from django.http import HttpResponse

class AggregationMiddleware:
    def __init__(self, get_response):
        # Dictionary to store API call counts keyed by user ID
        self.api_call_counts = {}
        # Queue to store timestamps of API calls
        self.timestamp_queue = deque()
        self.get_response = get_response
    
    def __call__(self, request):
        # Extract user ID and request ID from request headers
        user_id = request.headers.get("X-USER-ID")
        request_id = request.headers.get("X-REQUEST-ID")
        # Increment API call count for user
        if user_id in self.api_call_counts:
            self.api_call_counts[user_id] += 1
        else:
            self.api_call_counts[user_id] = 1
        
        # Add current timestamp to queue
        self.timestamp_queue.appendleft(datetime.utcnow())
        
        # Calculate aggregated statistics
        last_60_seconds = 0
        last_5_minutes = 0
        last_1_hour = 0
        last_6_hours = 0
        last_12_hours = 0
        last_24_hours = 0
        
        # Iterate through queue and count timestamps that fall within each time period
        for timestamp in self.timestamp_queue:
            if (datetime.utcnow() - timestamp) <= timedelta(seconds=60):
                last_60_seconds += 1
            if (datetime.utcnow() - timestamp) <= timedelta(minutes=5):
                last_5_minutes += 1
            if (datetime.utcnow() - timestamp) <= timedelta(hours=1):
                last_1_hour += 1
            if (datetime.utcnow() - timestamp) <= timedelta(hours=6):
                last_6_hours += 1
            if (datetime.utcnow() - timestamp) <= timedelta(hours=12):
                last_12_hours += 1
            if (datetime.utcnow() - timestamp) <= timedelta(hours=24):
                last_24_hours += 1
        
        # Construct response object with aggregated statistics
        data = {
            "user_id": user_id,
            "message": "Successfully called API"
        }
        metadata = {
            "last_60_seconds": last_60_seconds,
            "last_5_minutes": last_5_minutes,
            "last_1_hour": last_1_hour,
            "last_6_hours": last_6_hours,
            "last_12_hours": last_12_hours,
            "last_24_hours": last_24_hours
        }
        response = {
            "success": True,
            "data": data,
            "metadata": metadata,
        }
        print(response)
        return HttpResponse('api run successfully')
