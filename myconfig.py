# point spread function stored as a flattened 3x3 array
#psf: [0.5, 1.0, 0.5, 1.0, 3.0, 1.0, 0.5, 1.0, 0.5]
psf: [0.0, 0.0, 0.0, 0.0, 9.0, 0.0, 0.0, 0.0, 0.0]


# directory, where generated low resolution images are stored
samples_folder: '/tmp/input_images'

# offset stored in (x,y) form for each low resolution image
# XXX should we include [0,0] image here? I'm not sure 
offsets_of_captured_imgs: [[-2, -2], [0, -1], [1, -2],
                           [-1,  0], [0, 0],  [1,  0],
                           [-2,  1], [0,  1], [2,  1]]


# number of iteration of SR algorithm
iterations: 10
