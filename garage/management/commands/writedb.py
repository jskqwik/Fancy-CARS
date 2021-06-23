from django.core.management.base import BaseCommand
from garage.models import Car
import json
import requests

car_file = open("/Users/kasare/WebScrapping/gaaclassiccars_must.txt", "r")

def fetch_img(url, model):
    file_path = "carsimage/"
    response = requests.get(url)
    response.raise_for_status()
    file_name = "{}.png".format(model)
    try:
        with open(file_path, "wb") as img_file:
            img_file.write(response.content)
            return file_name
    except:
        return " "

class Command(BaseCommand):
    def handle(self, *args, **options):
        json_data = json.load(car_file)
        alist = json_data["data"]

        for item in alist:
            vin = item["vin"]
            year = item["year"]
            make = item["make"]
            model = item["model"]
            ex_color = item["ex_color"]
            in_color = item["in_color"]
            description = item["description"]
            image_url = item["photos"]
            image = fetch_img(image_url, model)

        
            Car.objects.create(vin=vin, year=year, make=make, model=model, interior_color=in_color, body_color=ex_color, speed=3.0, image=image, image_url=image_url)