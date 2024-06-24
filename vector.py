import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import SupabaseVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter


from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

# Load environment variables
SUPABASE_API_URL = os.getenv("SUPABASE_API_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_URL = os.getenv("OPENAI_API_URL")

if not SUPABASE_API_URL or not SUPABASE_API_KEY:
    raise ValueError(
        "Supabase URL and API Key must be provided in the .env file")

if not OPENAI_API_KEY or not OPENAI_API_URL:
    raise ValueError(
        "OpenAI API Key and URL must be provided in the .env file")

# Create Supabase client
supabase: Client = create_client(SUPABASE_API_URL, SUPABASE_API_KEY)

# Read the input text file
with open("personal-info.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split the text into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, chunk_overlap=50, separators=["\n\n", "\n", " ", ""]
)

documents = splitter.create_documents([text])

# print("Text split into documents:", documents)

if not documents:
    raise ValueError("Text splitting did not produce any documents")

embeddings = OpenAIEmbeddings(
    openai_api_base=OPENAI_API_URL,
    openai_api_key=OPENAI_API_KEY,
)

# Store documents in Supabase
vector_store = SupabaseVectorStore.from_documents(
    documents,
    embeddings,
    client=supabase,
    table_name="personal_infos",
    query_name="match_personal_infos",
)

print("Documents stored successfully.")
