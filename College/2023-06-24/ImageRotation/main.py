import cv2


def main():
    image = cv2.imread("image.png")
    cv2.imshow("Original", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    (height, width) = image.shape[:2]
    imageMatrix = cv2.getRotationMatrix2D((width // 2, height // 2), 45, 1)

    rotatedImage = cv2.warpAffine(image, imageMatrix, (height, width))

    cv2.imshow("Rotated", rotatedImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
