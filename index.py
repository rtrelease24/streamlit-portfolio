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
    st.write("- Python\n- JavaScript\n- PHP\n- Web Development (HTML, CSS, Bootstrap)\n- SQL")
    st.write("## Frameworks and Technologies")
    st.write("- Streamlit\n- Bootstrap")



with tab3:
    st.title("Major Projects")
    st.write("## [Store POS](http://areawebsites.org/rtrelease/Portfolio/PHP/Store_POS/index.php)")
    st.write("A point-of-sale system for the school store.")
    st.write ("## [Pampered Pups](http://areawebsites.org/rTrelease/Portfolio/PHP/Pampered%20Pups/index.php)")
    st.write("A website for a dog grooming business.")
    st.write("## [Real Estate](http://areawebsites.org/rTrelease/Portfolio/PHP/Real%20Estate/index.php)")
    st.write("A website for a real estate business.")
    
        

