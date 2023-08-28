class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating_value):
        self.customer_instance = customer
        self.restaurant_instance = restaurant
        self.rating_value = rating_value
        Review.all_reviews.append(self)
        print(f"Review created for {self.restaurant_instance.name} by {self.customer_instance.full_name()}. Rating: {self.rating_value}")

    @classmethod
    def all(cls):
        return cls.all_reviews

    def customer(self):
        from customer import Customer  # Import Customer here to avoid circular dependency
        return self.customer_instance

    def restaurant(self):
        from restaurant import Restaurant  # Import Restaurant here to avoid circular dependency
        return self.restaurant_instance

    def get_rating(self):
        return self.rating_value






