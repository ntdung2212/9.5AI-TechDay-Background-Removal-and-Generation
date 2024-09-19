### **Lib requirements:**

  **-PyQT6**

  **-gradio_client**

  **-qrcode**

  **-httpx**

  
### Other requirements:
  
  -Python 3.10 or 3.11
  
  -Internet


### This is a small python program that remove and generate background from images. It calls API from not-lain/background-removal and briaai/BRIA-Background-Generation project on HuggingFace/Spaces


## **Description:**

  -CallAPI.py: Upload the image and get the response from server
  
  -BgRemoval&Generation.py: Main program file
  
  -form.ui: UI file

## **How to run:**

  -Open the 'BgRemoval&Generation.py' file in any IDE and run. (Remember to install all the requirement lib)
  
  or
  
  -Run the file directlty with command line in Terminal or CMD

 ## **Description**
 
 -Select Image button is for selecting an image on the computer
 
 -URL Input: If the image is on the internet, paste the URL of the image here
 
 -Prompt Input: Prompt for Background Generation function. **Required to run the function**
 
 -Run BgGeneration button: run Background Generation function. Remember to type some prompt in the Prompt Input Box before running
 
 -Run BgRemoval button: Run background removal function
 
 -Save picture: To save the image after background being removed or generated

 -Generate QR button: Upload the processed image to imgur.com and generate a QR code for other user to download the image

### **Note:**

- Free GPU quota from HuggingFace is quiet limited, only fits ~10-12 images. If you exceeded, you have to wait for a long time.

### Credit: 

- https://huggingface.co/spaces/not-lain/background-removal

- https://huggingface.co/spaces/briaai/BRIA-Background-Generation


Sample images taken on Pexel and Unsplash
