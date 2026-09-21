# Nested models: using one model inside another model as a field

from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    name: str
    age: int
    gender: str

    # address is a complex type of data that stores many things, like
    # street no, street name, area name, landmark, city, pincode.
    #
    # If we store it as a plain string and later want to fetch the city
    # or area name, that becomes messy.
    # So we use a separate model class (Address) to store it,
    # and use that model as a field in this Patient model.
    address: Address


address_dict = {"city": "ABC", "state": "NCT", "pin": "1100AB"}
address1 = Address(**address_dict)

p1 = Patient(name="Aman", age=17, gender="M", address=address1)

print(p1)
print(p1.address.city)  # access nested values directly