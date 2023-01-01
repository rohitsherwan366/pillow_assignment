# pillow_assignment
1. A request with a user ID and request ID is received by the middleware.
2. The middleware checks the dictionary to see if there is an entry for the user ID.
3. If there is an entry, the middleware increments the count for that user ID in the dictionary and adds the current timestamp to the queue.
4. If there is no entry for the user ID in the dictionary, the middleware creates a new entry and sets the count to 1. It also adds the current timestamp to the queue.
5. The middleware calculates the aggregated statistics for the past 5 minutes, 1 hour, 6 hours, 12 hours, and 24 hours by iterating through the queue and counting the number of timestamps that fall within each respective time period.
6. The middleware constructs the response object with the success status, data, and metadata, and returns it to the client.
