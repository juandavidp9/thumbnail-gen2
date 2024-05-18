import streamlit as st
import requests
from PIL import Image
from streamlit_extras.add_vertical_space import add_vertical_space
import io
import base64
import json

def main():
    st.markdown("<h1 style='text-align: center;'>Thumbnail Generator</h1>", unsafe_allow_html=True)
    add_vertical_space(3)
    st.write("Upload an image and specify the desired thumbnail size.")
    uploaded_file = st.file_uploader("Upload your image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        original_width, original_height = image.size
        st.write(f"Original Size: {original_width} x {original_height} pixels")
        st.image(image, caption="Original Image")

        thumbnail_width = st.slider("Thumbnail Width", 10, original_width, 100)
        thumbnail_height = st.slider("Thumbnail Height", 10, original_height, 80)
        output_format = st.selectbox("Choose Image Format", ("PNG", "JPG"))
        file_name = st.text_input("Enter file name", value="thumbnail")

        if st.button("Generate Thumbnail"):
            
            image_data = base64.b64encode(uploaded_file.getvalue()).decode('utf-8')
            data = {
                "body": {
                    "file_name": file_name,
                    "output_format": output_format,
                    "image_data": image_data,
                    "width": thumbnail_width,
                    "height": thumbnail_height
                }
            }
            api_gateway_url = 'https://tncwqesy01.execute-api.us-east-1.amazonaws.com/prod/thumbnail'
            headers = {'Content-Type': 'application/json'}
            response = requests.post(api_gateway_url, headers=headers, data=json.dumps(data))

            if response.status_code == 200:
                response_data = response.json()
                response_body = json.loads(response_data['body'])
                thumbnail_base64 = response_body['thumbnail_base64']
                thumbnail_bytes = base64.b64decode(thumbnail_base64)
                thumbnail = Image.open(io.BytesIO(thumbnail_bytes))
                add_vertical_space(1)
                st.image(thumbnail, caption="Thumbnail Preview")

                
                download_button = st.download_button(
                    label="Download Thumbnail",
                    data=thumbnail_bytes,
                    file_name=f"{file_name}.{output_format.lower()}",
                    mime=f"image/{output_format.lower()}"
                )

if __name__ == "__main__":
    main()