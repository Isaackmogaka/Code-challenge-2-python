class Restaurant:
    # A list to store all restaurant instances
    all_restaurants = []

    def __init__(self, name):
        # Initialize a restaurant with a given name
        self.name = name
        # Add the restaurant instance to the list of all restaurants
        Restaurant.all_restaurants.append(self)
        # Print a message indicating that a restaurant has been created
        print(f"Restaurant '{self.name}' created.")

    # Method to get the name of the restaurant
    def name(self):
        return self.restaurant_name

    # Class method to get a list of all restaurant instances
    @classmethod
    def all(cls):
        return cls.all_restaurants

    # Method to get all reviews for the restaurant
    def reviews(self):
        restaurant_reviews = []
        from review import Review  # Import Review here to avoid circular dependency
        for review in Review.all():
            if review.restaurant() == self:
                restaurant_reviews.append(review)
        return restaurant_reviews

    # Method to get a list of customers who reviewed the restaurant
    def customers(self):
        restaurant_customers = set()
        for review in self.reviews():
            restaurant_customers.add(review.customer())
        return list(restaurant_customers)

    # Method to calculate the average star rating of the restaurant
    def average_star_rating(self):
        total_ratings = 0
        num_reviews = len(self.reviews())
        for review in self.reviews():
            total_ratings += review.rating_value
        if num_reviews > 0:
            return total_ratings / num_reviews
        else:
            return 0.0

    # Method to provide a human-readable string representation of the restaurant
    def __str__(self):
        return f"Restaurant: {self.name()}"




      

