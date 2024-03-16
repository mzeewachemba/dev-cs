import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt

def svd_compression(img, num_components=10):
    """
    Perform Singular Value Decomposition (SVD) based image compression.

    Parameters:
    img (ndarray): Input image matrix.
    num_components (int): Number of principal components to retain for compression.

    Returns:
    None
    """
    print('\n-------------------------------------------------------------------------------------\n')

    # Perform Singular Value Decomposition (SVD) on the image matrix
    u, s, v = np.linalg.svd(img)
    print("Input image shape:", img.shape)
    
    # Retain only the specified number of components
    uc = u[:, :num_components]
    sc = s[:num_components]
    vc = v[:num_components, :]
    
    # Calculate original and compressed data size
    orig_size = img.shape[0] * img.shape[1]
    compressed_size = uc.shape[0] * uc.shape[1] + sc.shape[0] + vc.shape[0] * vc.shape[1]
    compressed_perc = compressed_size / orig_size * 100
    print("Storage needed for original data =", orig_size)
    print("Storage needed for compressed data =", compressed_size, " percentage of original size =",compressed_perc , "%")
    
    # Reconstruct the compressed image using the selected components
    compressed_img = np.matrix(u[:, :num_components]) * np.diag(s[:num_components]) * np.matrix(v[:num_components, :])
    
    # Display the compressed image
    plt.figure(figsize=(10,8))
    plt.title(f'Compressed Image with {num_components} number of components')
    plt.imshow(compressed_img, cmap='gray')
    plt.show()
    print("Compressed image shape:", compressed_img.shape)
    return  compressed_perc
    

def visualize_compressed_perc_vs_number_of_components(num_components_array, compressed_perce_array):
    # compressed % vs number of components
    plt.figure(figsize=(10, 8))
    plt.plot(num_components_array, compressed_perce_array, marker='o', linestyle='dashed', color='green', label='Compressed %')
    plt.title('Compressed percentage vs number of components')
    plt.xlabel('Number of components')
    plt.ylabel('Compressed %')
    plt.legend()
    plt.grid(True)
    plt.show()



def main():
    # Load the image file
    image_filename = 'E:/16.Data_for_assignments/Images/scenery1.jpg'
    img = cv2.imread(image_filename, 0)
    if img is None:
        print('Could not open or find the image:', image_filename)
        exit(0)
    
    # Display the original image
    plt.title('Original Image')
    plt.imshow(img, cmap='gray')
    plt.show()
    
    # Perform SVD compression with a specified number of components
    num_components = 50
    svd_compression(img, num_components)
    
    # -------------- Comparing the effect of number of components to the compression percentage ---------------
    num_components_array = [10 , 30 , 50 , 70 , 100 , 120 , 150 , 200 ]
    # num_components_array = [10 , 30 ]
    compressed_perce_array = []
    
    for num_comp in num_components_array:
        # see how compressed % change with respect to no of components
        compressed_perc = svd_compression(img, num_comp)
        compressed_perce_array.append(compressed_perc)
                
    visualize_compressed_perc_vs_number_of_components(num_components_array , compressed_perce_array)


if __name__ == "__main__":
    sys.exit(int(main() or 0))
