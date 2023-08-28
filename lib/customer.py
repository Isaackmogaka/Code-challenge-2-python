class Customer:
    # A list to store all customer instances
    all_customers = []

    def __init__(self, given_name, family_name):
        # Initialize a customer with given name and family name
        self.given_name = given_name
        self.family_name = family_name
        # Add the customer instance to the list of all customers
        Customer.all_customers.append(self)
        # Print a message indicating that a customer has been created
        print(f"Customer '{self.full_name()}' created.")

    # Method to get the given name of the customer
    def given_name(self):
        return self.given_name

    # Method to get the family name of the customer
    def family_name(self):
        return self.family_name

    # Method to get the full name of the customer
    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    # Class method to get a list of all customer instances
    @classmethod
    def all(cls):
        return cls.all_customers

    # Method to get a list of restaurants reviewed by the customer
    def restaurants(self):
        reviewed_restaurants = set()
        from review import Review  
        for review in Review.all():
            if review.customer() == self:
                reviewed_restaurants.add(review.restaurant())
        return list(reviewed_restaurants)

    # Method to add a review made by the customer
    def add_review(self, restaurant, rating):
        from review import Review  
        review = Review(self, restaurant, rating)
        # Print a message indicating that a review has been added
        print(f"Review added by {self.full_name} for {restaurant.name}. Rating: {rating}")

    # Method to get the number of reviews made by the customer
    def num_reviews(self):
        return len(self.reviews())

    # Class method to find a customer by their full name
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all():
            if customer.full_name() == name:
                return customer
        return None

    # Class methods to find all customers with a given name
    @classmethod
    def find_all_by_given_name(cls, name):
        matching_customers = []
        for customer in cls.all():
            if customer.given_name == name:
                matching_customers.append(customer)
        return matching_customers




