from customer import Customer
from restaurant import Restaurant
from review import Review

if __name__ == "__main__":
 # Create instances of Customer and Restaurant
 customer1 = Customer("Dilan", "Ariana")
 customer2 = Customer("Farouk", "Smithson")
 customer3 = Customer("Peter", "Michael")
 customer4 = Customer("Jael", "Monreal")
 restaurant1 = Restaurant("Tasty Burgers")
 restaurant2 = Restaurant("Pizza Delight")
 restaurant3 = Restaurant("Pizza Inn")
 restaurant4 = Restaurant("Pizza Hut")

# Create reviews with instances of Customer and Restaurant
 review1 = Review(customer1, restaurant1, 4)
 review2 = Review(customer2, restaurant2, 5)
 review3 = Review(customer3, restaurant3, 3)
 review = Review (customer4, restaurant4, 45)
   # Retrieving and printing customer information
for customer in Customer.all():
        print(f"Customer: {customer.full_name()}")
        print(f"Reviewed Restaurants: {[restaurant.name for restaurant in customer.restaurants()]}")
        print()

    # Retrieving and printing restaurant information
for restaurant in Restaurant.all():
        print(f"Restaurant: restaurant.name")
        print(f"Reviews: {len(restaurant.reviews())}")
        print(f"Customers: {[customer.full_name() for customer in restaurant.customers()]}")
        print(f"Average Rating: {restaurant.average_star_rating()}")
        print()

    # Retrieving and printing reviews
for review in Review.all():
        print(f"{review.customer().full_name()} reviewed {review.restaurant().name()} with a rating of {review.rating()}")

