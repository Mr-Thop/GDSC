import streamlit as st


st.set_page_config(layout="wide")


st.sidebar.write("Created with  ❤  by Team Eco")

# Set a title for your site
col1,col4,col2,col3=st.columns([1,0.3,5,2])
with col1:
     st.image("2.jpg")

with col2:
     st.write(" ")
     st.write(" ")
     st.header("Eco Harmony Innovators")

st.text(" ")
st.text("")

# Add an introduction
st.write(
     """Welcome to Eco Harmony Innovators.A pioneering platform dedicated to fostering a harmonious balance across Health, Agriculture, and Education sectors.In the realm of Health, we leverage cutting-edge technologies to develop innovative solutions for medical diagnostics and personalized healthcare.
          Our commitment to sustainable Agriculture is evident through intelligent farming practices, predictive analytics, and crop recommendations that empower farmers with data-driven insights.
          In the realm of Education, we strive to bridge gaps by providing accessible and inclusive learning experiences, utilizing technology to enhance educational outcomes.
          At Eco Harmony Innovators, we envision a world where health, agriculture, and education seamlessly coalesce for the betterment of individuals and communities alike.""")

st.write( '''Embark on a transformative journey with Eco Harmony Innovators, where groundbreaking technologies converge to revolutionize health, agriculture, and education.
                    Discover a future where innovation meets sustainability, fostering a harmonious balance for a brighter tomorrow.''')

st.write("---")
# Explain why the website was built
col1,_,col2=st.columns([5,0.3,3])

with col1:
     st.header("Who Are We ?")
     st.write(
          '''Eco Harmony Innovators is a visionary team committed to harnessing the power of technology for positive societal impact. We are dedicated to crafting innovative solutions that address critical challenges in health, agriculture, and education.''')

     st.markdown("1. Smart Health Solutions")
     st.markdown("2. Agrotech Revolution")
     st.markdown("3. Educational Empowerment")
     st.markdown("4. Community Collaboration")
     st.markdown("5. Sustainability Hub")

     st.write("---")
     
with col2:
     st.write(" ")
     st.write(" ")
     st.image("1.png",width=300)

st.header("Why we're Better")

# Column 3: Competitive Analysis
col3,col1=st.columns(2)
with col3:
     st.write(" ")
     st.write(" ")
     st.write(" ")
     st.write(" ")
     st.write(" ")
     st.write(" ")
     st.image("3.png")

with col1:
    st.header("Competitive Analysis")
    st.write(
        "In our competitive analysis, we have evaluated Eco Harmony Innovators alongside two notable competitors. Each player brings a unique set of strengths and focus areas to the table.")
    st.subheader("Competitor A")
    st.write("Strengths: Recognized for their robust environmental monitoring systems, GreenTech Solutions excels in providing sustainable solutions for urban planning and waste management.")
    st.write("Challenges: While their focus on urban sustainability is commendable, they might benefit from expanding their scope to include rural and agricultural initiatives.")
    st.subheader("Competitor B")
    st.write("Strengths: AgriTech Ventures has carved a niche in precision agriculture, leveraging advanced data analytics and IoT devices to optimize crop yields.")
    st.write("Challenges: The emphasis on high-tech solutions might pose accessibility challenges for smaller-scale farmers and rural communities.")
    st.subheader("Eco Harmony Innovators")
    st.write("Strengths: Distinguished by a holistic approach, Eco Harmony Innovators uniquely addresses health, agriculture, and education. The platform aims to foster collaboration and community engagement.")
    st.write("Challenges: Balancing diverse sectors may pose initial challenges, but the integrated approach enhances overall societal impact.")

st.write("---")
# Highlight key features
st.header("Key Features")
st.write("Our platform offers a range of features, including:")
st.write("- Integrated Health Monitoring")
st.write("- Smart Agriculture Solutions")
st.write("- Educational Empowerment")
st.write("- Community Collaboration Hub")
st.write("- Data Security and Privacy")



