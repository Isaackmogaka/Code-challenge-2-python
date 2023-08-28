class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        # self.restaurant_name = name
        self.name = name
        Restaurant.all_restaurants.append(self)
        print(f"Restaurant '{self.name}' created.")

    def name(self):
        return self.restaurant_name

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def reviews(self):
        restaurant_reviews = []
        from review import Review  # Import Review here to avoid circular dependency
        for review in Review.all():
            if review.restaurant() == self:
                restaurant_reviews.append(review)
        return restaurant_reviews

    def customers(self):
        restaurant_customers = set()
        for review in self.reviews():
            restaurant_customers.add(review.customer())
        return list(restaurant_customers)

    def average_star_rating(self):
        total_ratings = 0
        num_reviews = len(self.reviews())
        for review in self.reviews():
            total_ratings += review.rating_value
        if num_reviews > 0:
            return total_ratings / num_reviews
        else:
            return 0.0

    def __str__(self):
        return f"Restaurant: {self.name()}"



      

