class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)
        print(f"Customer '{self.full_name()}' created.")

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def restaurants(self):
        reviewed_restaurants = set()
        from review import Review  # Import Review here to avoid circular dependency
        for review in Review.all():
            if review.customer() == self:
                reviewed_restaurants.add(review.restaurant())
        return list(reviewed_restaurants)

    def add_review(self, restaurant, rating):
        from review import Review  # Import Review here to avoid circular dependency
        review = Review(self, restaurant, rating)
        # print(f"Review added by {self.full_name()} for {restaurant.name()}. Rating: {rating}")
        print(f"Review added by {self.full_name} for {restaurant.name}. Rating: {rating}")


    def num_reviews(self):
        return len(self.reviews())

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all():
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        matching_customers = []
        for customer in cls.all():
            if customer.given_name == name:
                matching_customers.append(customer)
        return matching_customers



