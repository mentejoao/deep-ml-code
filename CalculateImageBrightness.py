
# Task: Image Brightness Calculator
# In this task, you will implement a function calculate_brightness(img) that calculates the average brightness of a grayscale image.
# The image is represented as a 2D matrix, where each element represents a pixel value between 0 (black) and 255 (white).

# Your Task: Implement the function calculate_brightness(img) to return the average brightness rounded to two decimal places.
# If the image matrix is empty, has inconsistent row lengths, or contains invalid pixel values (outside the range 0-255), the function should return -1.

def calculate_brightness(img):
    if not img or not img[0]:
        return -1

    row_length = len(img[0])
    for row in img:
        if len(row) != row_length:
            return -1

    total_sum = 0
    num_elements = len(img) * row_length

    for row in img:
        for element in row:
            if element < 0 or element > 255:
                return -1
            total_sum += element

    avg = total_sum / num_elements
    return round(avg, 2)