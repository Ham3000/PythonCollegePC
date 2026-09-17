from fastapi import FastAPI
from pydantic import BaseModel , computed_field , Field
from typing import Annotated , Literal

# post send info to server
# the info we send on server to create a new patent
# this info in API termenilogy know as a request body

#  A request body is the protion of HTTP request that
# contains data sent by the client to the server.
# It is typically used in http method such as post or put to
# transmit structured data eg.(JSON , XML , form-data)
# for the purpose of creating or updating  resource n the server
# the server parse the request body to extract the neccesary info
# and perform the intended operation.

# 🌟 we need understanding of pydantic for this tutorial
# post -> validate -> if correct -> insert in DB
#                  ↓
#                  if wrong -> throw error



app = FastAPI()

class Patient(BaseModel):
    # Now create the varaible/members to store data of 
    # Pateint see the patent.json file to see what what is
    # required

    # id : str
    # name : str
    # city : str
    # age : int
    # gender : str
    # height : float
    # weight : float 

    # bmi : float [computed]
    # verdict : str [computed]

    id : Annotated[
        str,
        Field(
            ...,
            description="Id of the patient",
            examples=["P001"]
        )
    ]

    name : Annotated[
        str,
        Field(
            ...,
            description="Name of Pateint",
            examples=["Mr. Timuthi"]
        )
    ]

    city : Annotated[
        str,
        Field(
            ...,
            description="Name of the city from where Pateint belong",
        )
    ]

    age : Annotated[
        int,
        Field(
            ...,
            gt=0,
            le=120,
            description="Age of the Pateint in numbers",
            examples=[18,20,35]
        )
    ]

    gender : Annotated[
        # only 3 options
        # M : male , F : Female , O : Other
        Literal["M","F","O"],
        Field(
            ...,
            description="Gender =  M : male , F : Female , O : Other"
        )
    ]

    height : Annotated[
        float,
        Field(
            ...,
            gt=0,
            description="Height of Patient in meters"
        )
    ]

    weight : Annotated[
        float,
        Field(
            ...,
            gt=0,
            description="Weight of Patient in Kg"
        )
    ]


    # computed fields
    @computed_field
    @property
    def bmi(self)->float:
        h = self.height
        w = self.weight
        bmi = h/(w**2)
        return bmi

    # another computed field
    @computed_field
    @property
    def verdict(self)->str:
        bmi = self.bmi
        if bmi < 18.8 : return "Under-Weight"
        elif  bmi>=18.5 and bmi<25.0: return "Healthy"
        elif  bmi>=25.0 and bmi<30.0 : return "Over-weight"
        else: return "obseity"



app = FastAPI()








    
    

