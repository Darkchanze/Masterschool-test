"""from PyPDF2 import PdfReader

reader = PdfReader('resume.pdf')
print(reader)
"""
countries = [{"name": "Spain",
             "capital_city": "Madrid",
             "currency": "EUR"
            },
            {"name": "United States",
             "capital_city": "Washington",
             "currency": "USD"
            },
            {"name": "Canada",
             "capital_city": "Ottawa",
             "currency": "CAD"
            }
           ]




for country_dict in countries:
    with open(f"{country_dict['name']}.txt", 'w') as new_data:
        new_data.write()