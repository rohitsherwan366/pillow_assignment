# pillow_assignment
1. A user makes a request to the API with the X-USER-ID and X-REQUEST-ID headers.
2. The middleware receives the request and extracts the X-USER-ID and X-REQUEST-ID headers.
3. The middleware checks if the X-USER-ID and X-REQUEST-ID combination exists in the database.
4. If the combination does not exist, the middleware creates a new entry in the database with the X-USER-ID, X-REQUEST-ID, and a timestamp.
5. If the combination does exist, the middleware updates the timestamp for the existing entry.
6. The middleware calculates the aggregated statistics for the past 5 minutes, 1 hour, 6 hours, 12 hours, and 24 hours based on the timestamps in the database.
7. The middleware returns a JSON response with the aggregated statistics to the user.
