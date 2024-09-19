### **Lib requirements:**

  **-PyQT6**

  **-gradio_client**

  
### Other requirements:
  
  -Python 3.11
  
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
 
 -Select Image Button is for selecting an image on the computer
 
 -URL Input: If the image is on the internet, paste the URL of the image here
 
 -Prompt Input: Prompt for Background Generation function. **Required to run the function**
 
 -Run BgGeneration Button: run Background Generation function. Remember to type some prompt in the Prompt Input Box before running
 
 -Run BgRemoval: Run background removal function
 
 -Save picture: To save the image after background being removed or generated

### Credit: 

- https://huggingface.co/spaces/not-lain/background-removal

- https://huggingface.co/spaces/briaai/BRIA-Background-Generation


Sample images taken on Pexel and Unsplash
