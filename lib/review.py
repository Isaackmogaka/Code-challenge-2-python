class Review:
    # A list to store all review instances
    all_reviews = []

    def __init__(self, customer, restaurant, rating_value):
        # Initialize a review with customer, restaurant, and rating
        self.customer_instance = customer
        self.restaurant_instance = restaurant
        self.rating_value = rating_value
        # Add the review instance to the list of all reviews
        Review.all_reviews.append(self)
        # Print a message indicating that a review has been created
        print(f"Review created for {self.restaurant_instance.name} by {self.customer_instance.full_name()}. Rating: {self.rating_value}")

    # Class methods to get a list of all review instances
    @classmethod
    def all(cls):
        return cls.all_reviews

    # Method to get the customer who made the review
    def customer(self):
        from customer import Customer 
        return self.customer_instance

    # Method to get the restaurant that was reviewed
    def restaurant(self):
        from restaurant import Restaurant 
        return self.restaurant_instance

    # Method to get the rating value of the review
    def get_rating(self):
        return self.rating_value







