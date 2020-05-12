import numpy as np
import cv2

MIN_NUM_KEYPOINT_MATCHES = 150

img1 = cv2.imread('montage_left.JPG', cv2.IMREAD_COLOR)  # queryImage
img2 = cv2.imread('montage_right.JPG', cv2.IMREAD_COLOR) # trainImage

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  # Convert to grayscale.
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create(nfeatures=700) 

# Find the keypoints and desc with ORB.
kp1, desc1 = orb.detectAndCompute(img1, None)
kp2, desc2 = orb.detectAndCompute(img2, None)

# Find keypoint matches using Brute Force Matcher.
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(desc1, desc2, None)

# Sort matches in ascending order of distance.
matches = sorted(matches, key=lambda x: x.distance)
          
# Draw best matches.
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:MIN_NUM_KEYPOINT_MATCHES],
                       None)

cv2.namedWindow('Matches', cv2.WINDOW_NORMAL)
img3_resize = cv2.resize(img3, (699, 700))
cv2.imshow('Matches', img3_resize)
cv2.waitKey(7000)  # Keeps window open 5 seconds.
cv2.destroyWindow('Matches')

# Keep only best matches.
best_matches = matches[:MIN_NUM_KEYPOINT_MATCHES]

if len(best_matches) >= MIN_NUM_KEYPOINT_MATCHES:
    src_pts = np.zeros((len(best_matches), 2), dtype=np.float32)
    dst_pts = np.zeros((len(best_matches), 2), dtype=np.float32)

    for i, match in enumerate(best_matches):
        src_pts[i, :] = kp1[match.queryIdx].pt
        dst_pts[i, :] = kp2[match.trainIdx].pt
        
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC)

    # Get dimensions of image 2.
    height, width = img2.shape
    img1_warped = cv2.warpPerspective(img1, M, (width, height))

    cv2.imwrite('montage_left_registered.JPG', img1_warped)
    cv2.imwrite('montage_right_gray.JPG', img2)

else:
    print("\n{}\n".format('WARNING: Number of keypoint matches < 10!'))
                                  






