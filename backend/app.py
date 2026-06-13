from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np
import os
import  json
from charts import create_pie_chart
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
from fastapi.staticfiles import StaticFiles
app.mount("/outputs", StaticFiles(directory="outputs"), name="outputs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create folders
os.makedirs("images", exist_ok=True)
os.makedirs("outputs", exist_ok=True)


# ================= HELPER FUNCTIONS =================

def calculate_stats(img):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Vegetation
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([90, 255, 255])

    # Water
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([140, 255, 255])

    # Urban
    lower_gray = np.array([0, 0, 50])
    upper_gray = np.array([180, 50, 220])

    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    gray_mask = cv2.inRange(hsv, lower_gray, upper_gray)

    total_pixels = img.shape[0] * img.shape[1]

    vegetation = round(np.count_nonzero(green_mask) / total_pixels * 100, 2)
    water = round(np.count_nonzero(blue_mask) / total_pixels * 100, 2)
    urban = round(np.count_nonzero(gray_mask) / total_pixels * 100, 2)

    return vegetation, water, urban


def generate_report(vegetation, water, urban):

    report = ""

    if vegetation > 50:
        report += "Vegetation dominates the region. "
    elif vegetation < 20:
        report += "Low vegetation cover detected. "

    if water > 30:
        report += "Water resources are abundant. "
    else:
        report += "Water coverage is limited. "

    if urban > 40:
        report += "Highly urbanized area detected."
    else:
        report += "Urbanization is moderate."

    return report

def calculate_landcover(mask):
    total_pixels = mask.shape[0] * mask.shape[1]

    vegetation_pixels = np.sum(mask == 1)
    water_pixels = np.sum(mask == 2)
    urban_pixels = np.sum(mask == 3)

    vegetation_percent = round(vegetation_pixels * 100 / total_pixels, 2)
    water_percent = round(water_pixels * 100 / total_pixels, 2)
    urban_percent = round(urban_pixels * 100 / total_pixels, 2)

    return {
        "vegetation_percent": vegetation_percent,
        "water_percent": water_percent,
        "urban_percent": urban_percent
    }

def create_change_heatmap(img1, img2):

    img1 = cv2.resize(img1, (512, 512))
    img2 = cv2.resize(img2, (512, 512))

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(gray1, gray2)

    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    change_percent = round(
        np.sum(thresh > 0) * 100 / (512 * 512),
        2
    )

    heatmap = cv2.applyColorMap(diff, cv2.COLORMAP_JET)

    cv2.imwrite("outputs/change_heatmap.jpg", heatmap)

    return change_percent
def generate_caption(vegetation, water, urban):

    if vegetation > 50:
        return "Dense vegetation with limited urban development."

    elif urban > 50:
        return "Highly urbanized region with sparse vegetation."

    elif water > 30:
        return "Region contains significant water bodies."

    else:
        return "Mixed landscape with moderate vegetation and urban coverage."

# ================= HOME =================

@app.get("/")
def home():
    return {
        "message": "Earth Observation System Running"
    }


# ================= UPLOAD =================

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):

    contents = await file.read()

    path = os.path.join("images", file.filename)

    with open(path, "wb") as f:
        f.write(contents)

    return {
        "message": "Image saved successfully",
        "filename": file.filename
    }


# ================= GRAYSCALE =================

@app.post("/grayscale")
async def grayscale(file: UploadFile = File(...)):

    contents = await file.read()

    img = cv2.imdecode(
        np.frombuffer(contents, np.uint8),
        cv2.IMREAD_COLOR
    )

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("outputs/grayscale.jpg", gray)

    return {
        "message": "Grayscale image saved"
    }


# ================= RESIZE =================

@app.post("/resize")
async def resize(file: UploadFile = File(...)):

    contents = await file.read()

    img = cv2.imdecode(
        np.frombuffer(contents, np.uint8),
        cv2.IMREAD_COLOR
    )

    resized = cv2.resize(img, (512, 512))

    cv2.imwrite("outputs/resized.jpg", resized)

    return {
        "message": "Resized image saved"
    }


# ================= EDGE DETECTION =================

@app.post("/edges")
async def edges(file: UploadFile = File(...)):

    contents = await file.read()

    img = cv2.imdecode(
        np.frombuffer(contents, np.uint8),
        cv2.IMREAD_COLOR
    )

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edge = cv2.Canny(gray, 100, 200)

    cv2.imwrite("outputs/edges.jpg", edge)

    return {
        "message": "Edge image saved"
    }


# ================= THRESHOLD =================

@app.post("/threshold")
async def threshold(file: UploadFile = File(...)):

    contents = await file.read()

    img = cv2.imdecode(
        np.frombuffer(contents, np.uint8),
        cv2.IMREAD_GRAYSCALE
    )

    _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    cv2.imwrite("outputs/threshold.jpg", thresh)

    return {
        "message": "Threshold image saved"
    }


# ================= SEGMENT =================

@app.post("/segment")
async def segment(file: UploadFile = File(...)):

    contents = await file.read()

    img = cv2.imdecode(
        np.frombuffer(contents, np.uint8),
        cv2.IMREAD_COLOR
    )

    if img is None:
        return {
            "error": "Cannot load image"
        }

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Vegetation
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([90, 255, 255])

    # Water
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([140, 255, 255])

    # Urban
    lower_gray = np.array([0, 0, 50])
    upper_gray = np.array([180, 50, 220])

    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    gray_mask = cv2.inRange(hsv, lower_gray, upper_gray)

    cv2.imwrite("outputs/vegetation_mask.jpg", green_mask)
    cv2.imwrite("outputs/water_mask.jpg", blue_mask)
    cv2.imwrite("outputs/urban_mask.jpg", gray_mask)

    total_pixels = img.shape[0] * img.shape[1]

    vegetation_percent = round(
        np.count_nonzero(green_mask) / total_pixels * 100, 2)

    water_percent = round(
        np.count_nonzero(blue_mask) / total_pixels * 100, 2)

    urban_percent = round(
        np.count_nonzero(gray_mask) / total_pixels * 100, 2)

    create_pie_chart(
        vegetation_percent,
        water_percent,
        urban_percent
    )

    report = generate_report(
        vegetation_percent,
        water_percent,
        urban_percent
    )

    return {
        "vegetation_percent": vegetation_percent,
        "water_percent": water_percent,
        "urban_percent": urban_percent,
        "report": report,
        "segmented_image": "outputs/segment.jpg"

    }


# ================= COMPARE =================

@app.post("/compare")
async def compare(
        image1: UploadFile = File(...),
        image2: UploadFile = File(...)
):

    contents1 = await image1.read()
    contents2 = await image2.read()

    img1 = cv2.imdecode(
        np.frombuffer(contents1, np.uint8),
        cv2.IMREAD_COLOR
    )

    img2 = cv2.imdecode(
        np.frombuffer(contents2, np.uint8),
        cv2.IMREAD_COLOR
    )

    veg1, water1, urban1 = calculate_stats(img1)
    veg2, water2, urban2 = calculate_stats(img2)

    vegetation_change = round(veg2 - veg1, 2)
    water_change = round(water2 - water1, 2)
    urban_change = round(urban2 - urban1, 2)

    if vegetation_change < 0:
        status = "Forest loss detected"
    else:
        status = "Vegetation increased"

    return {

        "image1": {
            "vegetation": veg1,
            "water": water1,
            "urban": urban1
        },

        "image2": {
            "vegetation": veg2,
            "water": water2,
            "urban": urban2
        },

        "changes": {
            "vegetation_change": vegetation_change,
            "water_change": water_change,
            "urban_change": urban_change
        },

        "status": status
    }
@app.post("/landcover")
async def landcover(file: UploadFile = File(...)):

    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    vegetation_mask = cv2.inRange(hsv, (35, 40, 40), (85, 255, 255))
    water_mask = cv2.inRange(hsv, (90, 50, 50), (130, 255, 255))
    urban_mask = cv2.inRange(hsv, (0, 0, 50), (180, 50, 200))

    mask = np.zeros(img.shape[:2], dtype=np.uint8)

    mask[vegetation_mask > 0] = 1
    mask[water_mask > 0] = 2
    mask[urban_mask > 0] = 3

    return calculate_landcover(mask)

@app.post("/timeseries")
async def timeseries():

    vegetation = [62, 58, 54, 49]

    years = [2020, 2021, 2022, 2023]

    return {
        "years": years,
        "vegetation_percent": vegetation
    }

@app.post("/change_heatmap")
async def change_heatmap(
    file1: UploadFile = File(...),
    file2: UploadFile = File(...)
):

    contents1 = await file1.read()
    contents2 = await file2.read()

    nparr1 = np.frombuffer(contents1, np.uint8)
    nparr2 = np.frombuffer(contents2, np.uint8)

    img1 = cv2.imdecode(nparr1, cv2.IMREAD_COLOR)
    img2 = cv2.imdecode(nparr2, cv2.IMREAD_COLOR)

    if img1 is None or img2 is None:
        return {"error": "Cannot load image"}

    change_percent = create_change_heatmap(img1, img2)

    return {
        "change_percentage": change_percent,
        "heatmap_saved_as": "change_heatmap.jpg"
    }

@app.post("/caption")
async def caption(file: UploadFile = File(...)):

    contents = await file.read()

    nparr = np.frombuffer(contents, np.uint8)

    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    vegetation_mask = cv2.inRange(hsv, (35,40,40), (85,255,255))
    water_mask = cv2.inRange(hsv, (90,50,50), (130,255,255))
    urban_mask = cv2.inRange(hsv, (0,0,50), (180,50,200))

    total_pixels = img.shape[0]*img.shape[1]

    vegetation = round(np.sum(vegetation_mask>0)*100/total_pixels,2)
    water = round(np.sum(water_mask>0)*100/total_pixels,2)
    urban = round(np.sum(urban_mask>0)*100/total_pixels,2)

    description = generate_caption(
        vegetation,
        water,
        urban
    )

    return {
        "description": description
    }

@app.post("/geojson")
async def geojson(file: UploadFile = File(...)):

    contents = await file.read()

    nparr = np.frombuffer(contents, np.uint8)

    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    vegetation_mask = cv2.inRange(
        hsv,
        (35,40,40),
        (85,255,255)
    )

    contours, _ = cv2.findContours(
        vegetation_mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    features = []

    for cnt in contours:

        coords = []

        for p in cnt:
            x, y = p[0]
            coords.append([int(x), int(y)])

        if len(coords) > 2:

            features.append({
                "type": "Feature",
                "properties": {
                    "class": "vegetation"
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [coords]
                }
            })

    geojson_data = {
        "type": "FeatureCollection",
        "features": features
    }

    with open("vegetation.geojson", "w") as f:
        json.dump(geojson_data, f, indent=4)

    return {
        "message": "GeoJSON file saved",
        "features": len(features)
    }
