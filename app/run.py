#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk
from utils import args
from api import pris
import threading
from time import sleep

args = args.parse("config.dat")

equipment = pris.get_equipment(args["base_url"], args["equipment_active_list"])
print(equipment)
positions = pris.get_coordinates(args["base_url"], args["function"])
print(positions)

no_gps = []

# No GPS signal
def NoGPS():
    fd = open("equipment_with_no_gps_signla.txt", "w")
    fd.write("EQUIPMENT WITH NO GPS SIGNAL:\n")
    for ie in no_gps:
        fd.write(ie);
        fd.write("\n")
    fd.close()

def update_ui(win):
    canvas= Canvas(win, width=1280, height=1280)
    canvas.pack()
    #Load an image in the script
    map = ImageTk.PhotoImage(Image.open(args["map"]))
    truck = ImageTk.PhotoImage(Image.open(args["truck_image"]).convert("RGBA").resize((40,40), Image.ANTIALIAS))

    #Add image to the Canvas Items
    # X - the horizontal direction
    # Y - is the vertical direction
    # (x, y) top left corner is (0,0)
    # latitude is the horizontal lines
    # longitude is the vertical lines
    canvas.create_image(0,0,anchor=NW,image=map)

    btn = Button(canvas, text='No GPS',
        bd='1', command=NoGPS)
    btn.place(x=0, y=0) 
    
    # Get GPS positions of the trucks
    trucks_img = []

    
    
    while True:
        #positions = pris.get_coordinates(args["base_url"], args["function"], simulate = bool(args["simulation"]), equipment = equipment)

        positions = pris.get_coordinates(args["base_url"], args["function"])

        #canvas.delete("all")
        #Create a canvas and button
        
        for img in trucks_img:
            canvas.delete(img);

        trucks_img = []       
        active = []

        y_scale = (float(args["bbox_nw_lat"]) - float(args["bbox_se_lat"])) / float(args["image_height"])
        x_scale = (float(args["bbox_se_lng"]) - float(args["bbox_nw_lng"]))  / float(args["image_width"])
        
        print("Max diff x: " + str(float(args["bbox_se_lng"]) -float(args["bbox_nw_lng"])))
        print("Max diff y: " + str(float(args["bbox_nw_lat"]) -float(args["bbox_se_lat"])))

        print("X scale: " + str(x_scale))
        print("Y scale: " + str(y_scale))

        print("----------------------------------")
        for p in positions:
            found = False
            for eq in equipment:
                if p["code"] == eq["code"]:
                    
                    ann = eq["description"]
                    if len(p["positions"]) == 0:
                        continue
                    found = True
                    if eq["description"] in no_gps:
                        no_gps.remove(eq["description"])
                    print(str(p["positions"][0]["x"]) + ", " + str(p["positions"][0]["y"]))
                    y = (float(args["bbox_nw_lat"]) - float(p["positions"][0]["y"])) / y_scale
                    x = (float(p["positions"][0]["x"]) - float(args["bbox_nw_lng"])) / x_scale
                    #print("Difference x: " + str((p["positions"][0]["y"] - float(args["bbox_nw_lng"]))))
                    #print("Difference y: " + str((float(args["bbox_nw_lat"]) - p["positions"][0]["x"])))

                    active.append({
                        "desc": ann,
                        "x": x,
                        "y": y
                    })
                    break;
            if not found:
                no_gps.append(eq["description"])
        print("----------------------------------")  
        print(active)
        for point in active:
            print("Drawing an image @ (" + str(point["x"]) + ", " + str(point["x"]) + ")")
            id = canvas.create_text(point["x"] - 20, point["y"] - 20, text=point["desc"], fill="white", font=('Helvetica 12 bold'))
            trucks_img.append(id)
            id = canvas.create_image(point["x"], point["y"], anchor=NW, image=truck)
            trucks_img.append(id)
        sleep(int(args["update_interval"]))

#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
win.geometry("1280x1280")

main_thread = threading.Thread(target=update_ui, args=(win,))
main_thread.start()

win.mainloop()

