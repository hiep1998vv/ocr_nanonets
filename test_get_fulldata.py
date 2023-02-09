import requests
import base64
import json
import cv2
import numpy as np
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



url = "https://app.nanonets.com/api/v2/OCR/FullText"

payload={'urls': ['/home/adveng/Downloads/test.JPG']}
files=[
  ('file',('test',open('/home/adveng/Downloads/test.JPG','rb'),'application/pdf'))
]
# proxies={"http:/150.61.8.70"}
headers = {}

response = requests.request("POST", url, headers=headers, data=payload,  files=files, auth=requests.auth.HTTPBasicAuth('56f01a9f-a69e-11ed-a7a5-be63bfe23141', ''))

# print(response.text)

# file = open("json_data.txt", 'r')
# content = file.read()
content = response.text

jsondata = json.loads(content)["results"][0]

# jsondata2 = json.loads(jsondata["results"][0])
# print(jsondata["page_data"])
words = jsondata["page_data"][0]["words"]

# img_3 = np.zeros([30000,30000,3],dtype=np.uint8)
# img_3.fill(255)
img_3 = cv2.imread("./code/image/test.JPG")

for i in range(len(words)):
    text = words[i]["text"]
    x1 = words[i]["xmin"]
    y1 = words[i]["ymin"]
    x2 = words[i]["xmax"]
    y2 = words[i]["ymax"]
    cv2.rectangle(img_3, (x1, y1), (x2, y2), (255,0,0), 1)
    cv2.putText(img_3, text, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

# or img[:] = 255
cv2.imwrite("./code/image/after_2.png", img_3)
cv2.imshow('3 Channel Window', img_3)
print("image shape: ", img_3.shape)
cv2.waitKey()

cv2.destroyAllWindows()