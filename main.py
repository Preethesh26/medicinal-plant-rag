# import streamlit as st
# from rag_utility import answer_question

# # Streamlit app
# st.set_page_config(page_title="Medicinal Plant RAG System", layout="wide")

# st.title("🌿 Medicinal Plant RAG System")
# st.markdown("Ask about medicinal plants and their uses.")

# # Text input for user query
# user_question = st.text_input("🔍 **Ask your question about medicinal plants**")

# if st.button("Get Answer", use_container_width=True):
#     if user_question:
#         with st.spinner("🔍 Searching for the best answer..."):
#             answer = answer_question(user_question)
#         st.markdown(answer, unsafe_allow_html=True)
#     else:
#         st.warning("⚠️ Please enter a question.")




# import streamlit as st
# from rag_utility import answer_question

# # Streamlit app
# st.set_page_config(page_title="Medicinal Plant RAG System", layout="wide")

# st.title("🌿 Medicinal Plant RAG System")
# st.markdown("Ask about medicinal plants and their uses.")

# # Text input for user query
# user_question = st.text_input("🔍 **Ask your question about medicinal plants**")

# if st.button("Get Answer", use_container_width=True):
#     if user_question:
#         with st.spinner("🔍 Searching for the best answer..."):
#             answer = answer_question(user_question)
#         st.markdown(answer, unsafe_allow_html=True)
#     else:
#         st.warning("⚠️ Please enter a question.")




# import streamlit as st
# from rag_utility import answer_question
# import pandas as pd
# import os

# # Streamlit config
# st.set_page_config(page_title="Medicinal Plant RAG System", layout="wide")
# st.title("🌿 Medicinal Plant RAG System")
# st.markdown("Ask about medicinal plants and their uses.")

# # Ask a question
# user_question = st.text_input("🔍 **Ask your question about medicinal plants**")

# if st.button("Get Answer", use_container_width=True):
#     if user_question:
#         with st.spinner("🔍 Searching for the best answer..."):
#             answer = answer_question(user_question)
#         st.markdown(answer, unsafe_allow_html=True)

#         # Display image if related
#         df = pd.read_excel("plants.xlsx")
#         for _, row in df.iterrows():
#             combined_text = " ".join(str(row[col]) for col in df.columns if pd.notna(row[col])).lower()
#             if user_question.lower() in combined_text:
#                 image_path = row.get("Image")
#                 if pd.notna(image_path) and isinstance(image_path, str) and os.path.exists(image_path):
#                     st.image(image_path, caption="🌿 Matched Plant Image", use_column_width=True)
#                 break
#     else:
#         st.warning("⚠️ Please enter a question.")




# import streamlit as st
# import pandas as pd
# import os
# from rag_utility import answer_question

# # Page config
# st.set_page_config(page_title="Medicinal Plant RAG System", layout="wide")

# # Load dataset
# plants_df = pd.read_excel("plants.xlsx")

# # Title
# st.markdown("<h1>🌿 Medicinal Plant RAG System</h1>", unsafe_allow_html=True)
# st.write("Ask about medicinal plants and their uses.")

# # Input
# query = st.text_input("🔎 **Ask your question about medicinal plants**")

# # Button
# if st.button("Get Answer"):
#     if query:
#         # Get answer from RAG utility
#         answer = answer_question(query)
        
#         # Display markdown response
#         st.markdown(answer, unsafe_allow_html=True)

#         # Get image path from dataframe
#         matched_row = plants_df[plants_df['Plant Name'].str.lower() == query.strip().lower()]
#         if not matched_row.empty:
#             image_path = matched_row.iloc[0]['Image']
#             if image_path and os.path.exists(image_path):
#                 st.image(image_path, caption="🌿 Matched Plant Image", use_container_width=True)
#             else:
#                 st.warning("No image found for this plant.")
#     else:
#         st.warning("Please enter a plant name.")




import streamlit as st
import pandas as pd
import os
from rag_utility import answer_question


# Set Streamlit page configuration
st.set_page_config(page_title="Medicinal Plant RAG System", layout="wide")

# Load dataset
plants_df = pd.read_excel("plants.xlsx")

# Title and instructions
st.markdown("<h1>🌿 Medicinal Plant RAG System</h1>", unsafe_allow_html=True)
st.write("Ask about medicinal plants and their uses.")

# Input box
query = st.text_input("🔎 **Ask your question about medicinal plants**")

# Button to trigger the search
if st.button("Get Answer"):
    if query:
        with st.spinner("🔍 Searching for the best answer..."):
            answer = answer_question(query)
        st.markdown(answer, unsafe_allow_html=True)

        # Try to display the image
        matched_row = plants_df[plants_df['Plant Name'].str.lower() == query.strip().lower()]

        if not matched_row.empty:
            image_path = matched_row.iloc[0].get("Image", None)

            if pd.notna(image_path):
                try:
                    if image_path.startswith("http"):
                        st.image(image_path, caption="🖼️ Medicinal Plant Image", use_container_width=True)
                    else:
                        full_path = os.path.join("images", image_path) if not os.path.exists(image_path) else image_path
                        if os.path.exists(full_path):
                            st.image(full_path, caption="🖼️ Medicinal Plant Image", use_container_width=True)
                        else:
                            raise FileNotFoundError
                except Exception:
                    st.image("images/placeholder.jpg", caption="🖼️ No specific image found. Showing placeholder.", use_container_width=True)
            else:
                st.image("images/placeholder.jpg", caption="🖼️ No image provided for this plant.", use_container_width=True)
        else:
            st.warning("⚠️ No matching plant found.")
    else:
        st.warning("⚠️ Please enter a plant name.")






