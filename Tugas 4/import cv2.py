import cv2
import numpy as np

# Load the image
image = cv2.imread('list kendaraan.png')  # Replace with the path to your image file

# Resize image for consistency
image = cv2.resize(image, (600, 600))

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise and improve contour detection
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Threshold the image
_, binary = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)

# Define kernels for morphological operations
kernelOpen = np.ones((5, 5), np.uint8)
kernelClose = np.ones((7, 7), np.uint8)

# Perform morphological operations
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernelClose)
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernelOpen)

# Segment the image
segment = cv2.Canny(opening, 30, 200)
contours, _ = cv2.findContours(segment, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
segment = cv2.cvtColor(segment, cv2.COLOR_GRAY2RGB)
cv2.drawContours(image, contours, -1, (0, 0, 255), 1)

# Segmentation, clustering, labeling, and calculating parameters
centers = []
for j in range(len(contours)):
    # Clustering and labeling
    moments = cv2.moments(contours[j])
    if moments['m00'] == 0:
        continue
    centers.append((int(moments['m10'] / moments['m00']), int(moments['m01'] / moments['m00'])))  # Find centroid
    cv2.circle(image, centers[-1], 1, (0, 0, 255), -1)  # Draw circle at centroid
    cv2.putText(image, str(j + 1), centers[-1], cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 255, 255), 1)  # Label centroid

    # Calculate parameters
    (x, y), (minorAxis, majorAxis), angle = cv2.fitEllipse(contours[j])  # Get minor and major axis
    eccentricity = np.sqrt(1 - (minorAxis**2 / majorAxis**2))
    area = cv2.contourArea(contours[j])
    perimeter = cv2.arcLength(contours[j], True)
    metric = (4 * np.pi * area) / perimeter**2
    print("----------------------")
    print(f'Eccentricity of object {j + 1} : {eccentricity}')
    print(f'Area of object {j + 1} : {area}')
    print(f'Perimeter of object {j + 1} : {perimeter}')
    print(f'Metric of object {j + 1} : {metric}')

    # Label shapes based on metric
    offset = (centers[-1][0], centers[-1][1] + 20)  # Offset for text placement
    form = "Round" if round(metric, 1) >= 0.7 else "Ellipse"
    cv2.putText(image, str(form), offset, cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 0), 1)

# Display the image
cv2.imshow('Detected Shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
