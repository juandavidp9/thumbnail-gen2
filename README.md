# Thumbnail Generator App

This app allows you to generate thumbnails of images with custom sizes.
It provides an intuitive interface for uploading images, adjusting thumbnail dimensions, and downloading the result.

### Architecture 

![architecture](https://drive.google.com/uc?id=1QHcwubP07HWqoq01DK7NjINtIUzSJc32)

The solution consists of a Streamlit app as the front-end interface, an AWS API Gateway as the entry point, an AWS Lambda function for generating thumbnails, and an AWS S3 bucket for optionally storing the thumbnails.

The flow is as follows:

1. Streamlit App: Uploads image, gets thumbnail settings, and sends base64-encoded image data to API Gateway.
2. API Gateway: Receives request, and invokes Lambda function.
3. Lambda: Decodes image data, generates a thumbnail, saves to S3 bucket, and returns base64-encoded thumbnail data.
4. Streamlit app: Receives and decodes thumbnail data, displays the thumbnail, and allows download.

## Features
●   Upload images in JPG, PNG, and JPEG formats.  
●   Customize thumbnail width and height using sliders.  
●   Select the output format for the thumbnail (PNG or JPG).  
●   Preview the original image and the generated thumbnail.  
●   Download the thumbnail with a custom file name.  

Built with Streamlit https://docs.streamlit.io/

## Installation
Install libraries necessary for the project
```
pip install -r requirements.txt
```

## Run
Run this command to start the app. 
```bash
streamlit run main.py
```

