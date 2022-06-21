FORMAT: 1A
#Lego
## Question Collection [/questions]

### List All Questions [GET]

+ Request (application/json)

    + Header

            Accept: application/json

    + Body

            {
                "question": "Favorite time of year?",
                "choices": [
                    "Autumn",
                    "winter",
                    "spring",
                    "summer"
                ]
            }

+ Response 201 (application/json)
