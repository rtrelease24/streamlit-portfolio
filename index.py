import streamlit as st

# Create tabs for different sections
tab1, tab2, tab3= st.tabs(["Home", "Skills", "Projects"])
with tab1:
    st.title("Welcome to my portfolio.")
    st.write("Here, you'll find information about my skills, projects, and resume.")
    st.write("## Resume")
    with open("resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label="Download Resume",
                       data=PDFbyte,
                       file_name="resume.docx",
                       mime='application/octet-stream')

with tab2:
    st.title("Skills")
    st.write("## Programming Languages")
    programming_languages = {
        "Python": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg",
        "JavaScript": "https://upload.wikimedia.org/wikipedia/commons/9/99/Unofficial_JavaScript_logo_2.svg",
        "PHP": "https://upload.wikimedia.org/wikipedia/commons/2/27/PHP-logo.svg",
        "Web Development (HTML, CSS, Bootstrap)": "https://upload.wikimedia.org/wikipedia/commons/d/d5/CSS3_logo_and_wordmark.svg",
        "SQL": "https://upload.wikimedia.org/wikipedia/commons/2/29/Postgresql_elephant.svg"
    }
    for language, image_url in programming_languages.items():
        col1, col2, col3 = st.columns([0.02, 0.1, 0.7])
        with col1:
            st.markdown("<style>img {pointer-events: none;} </style>", unsafe_allow_html=True)
            st.write("•")
        with col2:
            st.markdown(f'<img src="{image_url}" style="width: 70px;">', unsafe_allow_html=True)
        with col3:
            st.write(language)
        



with tab3:
    st.title("Highschool Projects")
    st.write("## [Store POS](http://areawebsites.org/rtrelease/Portfolio/PHP/Store_POS/index.php)")
    st.write("A point-of-sale system for the school store.")
    st.write ("## [Pampered Pups](http://areawebsites.org/rTrelease/Portfolio/PHP/Pampered%20Pups/index.php)")
    st.write("A website for a dog grooming business.")
    st.write("## [Real Estate](http://areawebsites.org/rTrelease/Portfolio/PHP/Real%20Estate/index.php)")
    st.write("A website for a real estate business.")
    st.write("## [Career Research](http://areawebsites.org/rTrelease/Portfolio/Powerpoint/Career%20Research.pdf)")
    st.write("A presentation on potential careers.")
    
    
        

