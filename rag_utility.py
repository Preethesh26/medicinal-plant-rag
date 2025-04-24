# import pandas as pd
# from langchain.schema import Document
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import Chroma
# from langchain_huggingface import HuggingFaceEmbeddings

# # Path to dataset
# dataset_path = "plants.xlsx"

# def load_dataset():
#     """Loads the dataset, converts it into LangChain Documents, and splits it into chunks."""
#     df = pd.read_excel(dataset_path)

#     # Convert each row to a LangChain Document
#     documents = []
#     for _, row in df.iterrows():
#         text = "\n".join([f"{col}: {row[col]}" for col in df.columns if pd.notna(row[col])])
#         doc = Document(page_content=text, metadata={"source": "plants_cleaned.xlsx"})
#         documents.append(doc)

#     # Split documents into smaller chunks
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
#     texts = text_splitter.split_documents(documents)
    
#     return texts

# def create_vector_db(texts):
#     """Embeds text data and stores it in a Chroma vector database."""
#     embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
#     # Create a vector store with the embeddings
#     vectordb = Chroma.from_documents(texts, embedding)
#     return vectordb

# # Load and process dataset
# texts = load_dataset()
# vectordb = create_vector_db(texts)

# def answer_question(query):
#     """Retrieves the most relevant document chunks and formats them for readability."""
#     docs = vectordb.similarity_search(query, k=3)
    
#     if not docs:
#         return "No relevant information found."

#     formatted_response = "## 🌿 Medicinal Plant Information\n\n"
#     unique_responses = set()  # Avoid duplicate answers

#     for doc in docs:
#         content = doc.page_content.strip()

#         if content not in unique_responses:
#             unique_responses.add(content)

#             formatted_response += "### 🏺 Preparation Method\n"
#             for line in content.split("\n"):
#                 if ":" in line:
#                     key, value = line.split(":", 1)
#                     formatted_response += f"- **{key.strip()}**: {value.strip()}\n"
#                 else:
#                     formatted_response += f"- {line.strip()}\n"
#             formatted_response += "\n---\n"

#     return formatted_response





# import os
# import pandas as pd
# from langchain.schema import Document
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import Chroma
# from langchain_huggingface import HuggingFaceEmbeddings

# # Path to dataset and ChromaDB directory
# dataset_path = "plants.xlsx"
# chroma_db_dir = "chroma_db"

# def load_dataset():
#     """Loads the dataset, converts it into LangChain Documents, and splits it into chunks."""
#     df = pd.read_excel(dataset_path)

#     # Convert each row to a LangChain Document
#     documents = []
#     for _, row in df.iterrows():
#         text = "\n".join([f"{col}: {row[col]}" for col in df.columns if pd.notna(row[col])])
#         doc = Document(page_content=text, metadata={"source": "plants_cleaned.xlsx"})
#         documents.append(doc)

#     # Split documents into smaller chunks
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
#     texts = text_splitter.split_documents(documents)
    
#     return texts

# def create_vector_db(texts):
#     """Creates or loads a Chroma vector database with embeddings."""
#     embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#     # Create the directory if it does not exist
#     if not os.path.exists(chroma_db_dir):
#         os.makedirs(chroma_db_dir)

#     # Load or create the database
#     vectordb = Chroma.from_documents(texts, embedding, persist_directory=chroma_db_dir)
#     vectordb.persist()  # Ensure data is stored persistently
#     return vectordb

# # Load and process dataset
# texts = load_dataset()
# vectordb = create_vector_db(texts)
# def answer_question(query):
#     """Retrieves the most relevant document chunks and formats them for readability."""
#     if not os.path.exists(chroma_db_dir):
#         return "Error: Vector database not found. Please rerun data processing."

#     docs = vectordb.similarity_search(query, k=3)
    
#     if not docs:
#         return "No relevant information found."

#     formatted_response = "## 🌿 Medicinal Plant Information\n\n"
#     preparation_method = ""
#     unique_responses = set()

#     for doc in docs:
#         content = doc.page_content.strip()

#         if content not in unique_responses:
#             unique_responses.add(content)
#             lines = content.split("\n")

#             for line in lines:
#                 if not line.strip():
#                     continue
#                 if "Preparation Method" in line:
#                     # Store preparation for later
#                     preparation_method += f"- **{line.strip().split(':')[0]}**: {line.strip().split(':',1)[1].strip()}\n"
#                 elif ":" in line:
#                     key, value = line.split(":", 1)
#                     formatted_response += f"- **{key.strip()}**: {value.strip()}\n"
#                 else:
#                     formatted_response += f"- {line.strip()}\n"

#     # Add Preparation Method section last
#     if preparation_method:
#         formatted_response += "\n### 🏺 Preparation Method\n"
#         formatted_response += preparation_method
#         formatted_response += "\n---\n"

#     return formatted_response




# import os
# import pandas as pd
# from langchain.schema import Document
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import Chroma
# from langchain_huggingface import HuggingFaceEmbeddings

# # Paths
# dataset_path = "plants.xlsx"
# chroma_db_dir = "chroma_db"

# def load_dataset():
#     """Loads Excel and converts each row into a LangChain Document with all text fields."""
#     df = pd.read_excel(dataset_path)

#     documents = []
#     for _, row in df.iterrows():
#         text_parts = []
#         for col in df.columns:
#             if pd.notna(row[col]):
#                 # Avoid putting binary image or unreadable data types
#                 if isinstance(row[col], (str, int, float)):
#                     text_parts.append(f"{col}: {row[col]}")
#         text = "\n".join(text_parts)
#         doc = Document(page_content=text, metadata={"source": "plants.xlsx"})
#         documents.append(doc)

#     splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
#     return splitter.split_documents(documents)

# def create_vector_db(texts):
#     """Creates vector store and persists it."""
#     embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
#     if not os.path.exists(chroma_db_dir):
#         os.makedirs(chroma_db_dir)
#     vectordb = Chroma.from_documents(texts, embedding, persist_directory=chroma_db_dir)
#     vectordb.persist()
#     return vectordb

# texts = load_dataset()
# vectordb = create_vector_db(texts)

# def answer_question(query):
#     """Generates the answer with formatted markdown from relevant chunks."""
#     if not os.path.exists(chroma_db_dir):
#         return "Vector database not found."

#     docs = vectordb.similarity_search(query, k=3)
#     if not docs:
#         return "No relevant information found."

#     formatted_response = "## 🌿 Medicinal Plant Information\n\n"
#     preparation_method = ""
#     unique_responses = set()

#     for doc in docs:
#         content = doc.page_content.strip()
#         if content not in unique_responses:
#             unique_responses.add(content)
#             lines = content.split("\n")

#             for line in lines:
#                 if not line.strip():
#                     continue
#                 if "Preparation Method" in line:
#                     preparation_method += f"- **{line.strip().split(':')[0]}**: {line.strip().split(':',1)[1].strip()}\n"
#                 elif ":" in line:
#                     key, value = line.split(":", 1)
#                     formatted_response += f"- **{key.strip()}**: {value.strip()}\n"
#                 else:
#                     formatted_response += f"- {line.strip()}\n"

#             formatted_response += "\n"

#     if preparation_method:
#         formatted_response += "\n### 🏺 Preparation Method\n"
#         formatted_response += preparation_method
#         formatted_response += "\n---\n"

#     return formatted_response


import os
import pandas as pd
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings


# Paths
dataset_path = "plants.xlsx"
chroma_db_dir = "chroma_db"

def load_dataset():
    """Loads Excel and converts each row into a LangChain Document with all text fields."""
    df = pd.read_excel(dataset_path)

    documents = []
    for _, row in df.iterrows():
        text_parts = []
        for col in df.columns:
            if pd.notna(row[col]):
                if isinstance(row[col], (str, int, float)):
                    text_parts.append(f"{col}: {row[col]}")
        text = "\n".join(text_parts)
        doc = Document(page_content=text, metadata={"source": "plants.xlsx"})
        documents.append(doc)

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(documents)

def create_vector_db(texts):
    """Creates vector store and persists it."""
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    if not os.path.exists(chroma_db_dir):
        os.makedirs(chroma_db_dir)
    vectordb = Chroma.from_documents(texts, embedding, persist_directory=chroma_db_dir)
    vectordb.persist()
    return vectordb

texts = load_dataset()
vectordb = create_vector_db(texts)

def answer_question(query):
    """Generates the answer with formatted markdown from relevant chunks."""
    if not os.path.exists(chroma_db_dir):
        return "Vector database not found."

    docs = vectordb.similarity_search(query, k=3)
    if not docs:
        return "No relevant information found."

    formatted_response = "## 🌿 Medicinal Plant Information\n\n"
    preparation_method = ""
    unique_responses = set()

    for doc in docs:
        content = doc.page_content.strip()
        if content not in unique_responses:
            unique_responses.add(content)
            lines = content.split("\n")

            for line in lines:
                if not line.strip():
                    continue
                if "Preparation Method" in line:
                    preparation_method += f"- **{line.strip().split(':')[0]}**: {line.strip().split(':',1)[1].strip()}\n"
                elif ":" in line:
                    key, value = line.split(":", 1)
                    formatted_response += f"- **{key.strip()}**: {value.strip()}\n"
                else:
                    formatted_response += f"- {line.strip()}\n"

            formatted_response += "\n"

    if preparation_method:
        formatted_response += "\n### 🏺 Preparation Method\n"
        formatted_response += preparation_method
        formatted_response += "\n---\n"

    location_link = "https://maps.app.goo.gl/cPghnzW23zHydnGq7?g_st=aw"
    formatted_response += f'\n**Location**: ["{location_link}"]({location_link})'

    return formatted_response



