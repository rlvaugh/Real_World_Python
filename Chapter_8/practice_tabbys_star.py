"""Simulate transit of alien array and plot light curve."""
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

IMG_HT = 400
IMG_WIDTH = 500
BLACK_IMG = np.zeros((IMG_HT, IMG_WIDTH), dtype='uint8')
STAR_RADIUS = 165
EXO_DX = 3
EXO_START_X = -250
EXO_START_Y = 150
NUM_FRAMES = 500

def main():
    intensity_samples = record_transit(EXO_START_X, EXO_START_Y)
    rel_brightness = calc_rel_brightness(intensity_samples)
    plot_light_curve(rel_brightness)
    
def record_transit(exo_x, exo_y):
    """Draw array transiting star and return list of intensity changes."""
    intensity_samples = []
    for _ in range(NUM_FRAMES):
        temp_img = BLACK_IMG.copy()
        # Draw star:
        cv.circle(temp_img, (int(IMG_WIDTH / 2), int(IMG_HT / 2)),
                  STAR_RADIUS, 255, -1)
        # Draw alien array:
        cv.rectangle(temp_img, (exo_x, exo_y),
                     (exo_x + 20, exo_y + 140), 0, -1)
        cv.rectangle(temp_img, (exo_x - 360, exo_y),
                     (exo_x + 10, exo_y + 140), 0, 5)
        cv.rectangle(temp_img, (exo_x - 380, exo_y),
                     (exo_x - 310, exo_y + 140), 0, -1)
        intensity = temp_img.mean()
        cv.putText(temp_img, 'Mean Intensity = {}'.format(intensity), (5, 390),
                   cv.FONT_HERSHEY_PLAIN, 1, 255)
        cv.imshow('Transit', temp_img)
        cv.waitKey(10)
        intensity_samples.append(intensity)
        exo_x += EXO_DX
    return intensity_samples

def calc_rel_brightness(intensity_samples):
    """Return list of relative brightness from list of intensity values."""
    rel_brightness = []
    max_brightness = max(intensity_samples)
    for intensity in intensity_samples:
        rel_brightness.append(intensity / max_brightness)
    return rel_brightness

def plot_light_curve(rel_brightness):
    """Plot changes in relative brightness vs. time."""
    plt.plot(rel_brightness, color='red', linestyle='dashed',
             linewidth=2)
    plt.title('Relative Brightness vs. Time')
    plt.xlim(-150, 500)
    plt.show()

if __name__ == '__main__':
    main()
