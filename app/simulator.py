from utils import args
from api import pris
from time import sleep

args = args.parse("config.dat")

equipment = pris.get_equipment(args["base_url"], args["equipment_active_list"])

while True:
    pris.send_random_coordinates(args["base_url"], equipment = equipment)
    sleep(3)
