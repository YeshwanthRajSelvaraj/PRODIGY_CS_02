from PIL import Image
import numpy as np

class ImageEncryptor:
    def __init__(self):
        self.key = 42  # Simple encryption key (can be modified)

    def encrypt_image(self, input_path, output_path):
        try:
            # Open and convert image to RGB
            img = Image.open(input_path).convert('RGB')
            # Convert image to numpy array
            img_array = np.array(img, dtype=np.uint8)
            
            # Apply XOR operation with key to each pixel value
            encrypted_array = img_array ^ self.key
            
            # Convert back to image
            encrypted_img = Image.fromarray(encrypted_array)
            encrypted_img.save(output_path)
            print(f"Image encrypted and saved as {output_path}")
            
            return True
        except Exception as e:
            print(f"Error during encryption: {str(e)}")
            return False

    def decrypt_image(self, input_path, output_path):
        try:
            # Open encrypted image
            img = Image.open(input_path).convert('RGB')
            # Convert to numpy array
            img_array = np.array(img, dtype=np.uint8)
            
            # Apply XOR operation with same key to decrypt
            # XOR with same key reverses the encryption
            decrypted_array = img_array ^ self.key
            
            # Convert back to image
            decrypted_img = Image.fromarray(decrypted_array)
            decrypted_img.save(output_path)
            print(f"Image decrypted and saved as {output_path}")
            
            return True
        except Exception as e:
            print(f"Error during decryption: {str(e)}")
            return False

def main():
    encryptor = ImageEncryptor()
    
    print("Image Encryption Tool")
    print("--------------------")
    
    while True:
        print("\n1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == '3':
            print("Goodbye!")
            break
            
        if choice not in ['1', '2']:
            print("Invalid choice! Please select 1, 2, or 3.")
            continue
            
        input_path = input("Enter input image path: ")
        output_path = input("Enter output image path: ")
        
        if choice == '1':
            encryptor.encrypt_image(input_path, output_path)
        else:
            encryptor.decrypt_image(input_path, output_path)

if __name__ == "__main__":
    # Make sure you have Pillow installed: pip install Pillow
    main()


# output 

#Image Encryption Tool
--------------------

#1. Encrypt an image
#2. Decrypt an image
#3. Exit
#Enter your choice (1-3): 1
#Enter input image path: input.jpg
#Enter output image path: encrypted.jpg
#Image encrypted and saved as encrypted.jpg

#1. Encrypt an image
#2. Decrypt an image
#3. Exit
#Enter your choice (1-3): 2
#Enter input image path: encrypted.jpg
#Enter output image path: decrypted.jpg
#Image decrypted and saved as decrypted.jpg
#Image decrypted and saved as decrypted.jpg
#Image decrypted and saved as decrypted.jpg
