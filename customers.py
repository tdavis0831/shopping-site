"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):

        return "<Customer: {}, {}, {}>".format(self.first_name, self.last_name, self.email)

tim=Customer("tim", "jones", "tim@gmail.com", "hello")

print(tim)

def read_customers(filepath):
    customers={}
    with open(filepath) as file:
        for line in file:
            first_name, last_name, email, password = line.strip().split("|")
            customers[email]= Customer(first_name, last_name, email, password)
        return(customers)

customers_dict = read_customers("customers.txt")

def get_by_email(hat):

    print(customers_dict[hat])

get_by_email("janet@hotmail.com")