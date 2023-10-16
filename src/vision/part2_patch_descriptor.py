#!/usr/bin/python3

import numpy as np


def compute_normalized_patch_descriptors(
    image_bw: np.ndarray, X: np.ndarray, Y: np.ndarray, feature_width: int
) -> np.ndarray:
    """Create local features using normalized patches.

    Normalize image intensities in a local window centered at keypoint to a
    feature vector with unit norm. This local feature is simple to code and
    works OK.

    Choose the top-left option of the 4 possible choices for center of a square
    window.

    Args:
        image_bw: array of shape (M,N) representing grayscale image
        X: array of shape (K,) representing x-coordinate of keypoints
        Y: array of shape (K,) representing y-coordinate of keypoints
        feature_width: size of the square window

    Returns:
        fvs: array of shape (K,D) representing feature descriptors
    """

    ###########################################################################
    # TODO: YOUR CODE HERE                                                    #
    ###########################################################################
    fvs = []

    for i in range(len(X)):
        fv = []
        x = X[i]
        y = Y[i]
        center_x = x - (feature_width // 2 - 1)
        center_y = y - (feature_width // 2 -  1)

        for r in range(center_y, center_y + feature_width):
            for c in range(center_x, center_x + feature_width):

                fv.append(image_bw[r][c])
        fv = np.array(fv)
        fv = np.float32(fv)
        fv = fv / np.linalg.norm(fv)
        fvs.append(fv)

    fvs = np.array(fvs)



    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################

    return fvs
