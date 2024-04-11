import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Eat Healthy")

st.sidebar.success("Use this nav bar to navigate through the website.")

st.markdown(
    """
    A diet recommendation web application using content-based approach with Scikit-Learn, Flask and Streamlit.
    """
)

# Big text with attractive formatting
st.write(
    """
    <h2 style="text-align: center; color: #3498db; font-size: 30px;">Take Control of Your Health</h2>
    <h2 style="text-align: center; font-size: 40px;">With Our Tailored Diet Plans</h2>
    """,
    unsafe_allow_html=True
)

image_path = Path(__file__).parent / "images" / "diet_plan.jpg"
st.image(str(image_path), use_column_width=True)

# Dummy About Us page
st.markdown(
    """
    ## About Us

    Nutrients, vitamins and minerals are required by the human body in order to prevent diseases. Nutritional diseases occur when a body lacks proper amount of nutrients which can lead to multiple health problems. Excess or deficiencies of nutrients in the diet or eating disorder can lead to many catastrophic diseases such as diabetes, coeliac disease, Hypothyroidism, etc. A common example of nutritional deficiency is the lack of Protein. It is also known as Malnutrition. It is important for building and repairing tissues, producing enzymes and hormones, and supporting immune function. Therefore, in such condition it becomes very necessary to maintain a proper diet. A correct and balanced diet would allow the body to get the required amount of nutrients, vitamins, and minerals in order to work effectively. The paper is the framework that provides a proper diet plan to the user.

    EatHealthy is multiple disease-based diet recommendation system that provides a diet plan as output by taking all the relevant health related information as input. Our system can be used an effective tool in order to improve nutritional intake as well as to maintain and improve from the health conditions.
    """
)

# Creators section with GitHub icons and centered images
st.markdown("## Meet the Creators")

# Function to convert image to base64 for embedding
def img_to_html(img_path, width='100px', height='100px'):
    with open(img_path, "rb") as img_file:
        img_bytes = img_file.read()
        encoded = base64.b64encode(img_bytes).decode()
        return f"<img src='data:image/png;base64,{encoded}' style='display: block; margin-left: auto; margin-right: auto;' width='{width}' height='{height}'>"

# Display each creator in a separate column with centered name and image
cols = st.columns(4)

cols[0].markdown(f"<div style='text-align: center;'>{img_to_html(Path(__file__).parent / 'images' / 'image1.jpg')}</div>", unsafe_allow_html=True)
cols[0].markdown("<div style='text-align: center;'>Creator 1</div>", unsafe_allow_html=True)
cols[0].markdown("<div style='text-align: center;'><a href='https://github.com/creator1'><img src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white'></a></div>", unsafe_allow_html=True)

cols[1].markdown(f"<div style='text-align: center;'>{img_to_html(Path(__file__).parent / 'images' / 'image2.jpg')}</div>", unsafe_allow_html=True)
cols[1].markdown("<div style='text-align: center;'>Creator 2</div>", unsafe_allow_html=True)
cols[1].markdown("<div style='text-align: center;'><a href='https://github.com/creator2'><img src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white'></a></div>", unsafe_allow_html=True)

cols[2].markdown(f"<div style='text-align: center;'>{img_to_html(Path(__file__).parent / 'images' / 'image3.jpg')}</div>", unsafe_allow_html=True)
cols[2].markdown("<div style='text-align: center;'>Creator 3</div>", unsafe_allow_html=True)
cols[2].markdown("<div style='text-align: center;'><a href='https://github.com/creator3'><img src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white'></a></div>", unsafe_allow_html=True)

cols[3].markdown(f"<div style='text-align: center;'>{img_to_html(Path(__file__).parent / 'images' / 'image4.jpg')}</div>", unsafe_allow_html=True)
cols[3].markdown("<div style='text-align: center;'>Creator 4</div>", unsafe_allow_html=True)
cols[3].markdown("<div style='text-align: center;'><a href='https://github.com/creator4'><img src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white'></a></div>", unsafe_allow_html=True)
