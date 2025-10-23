# Retreival Phase
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

openai_client = OpenAI()

# Vector embeddings
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embedding_model
)

# Take the user input
user_query = input("Ask something : ")

# Do a similarity search on the vector database for the user query, returns the relevant chunks from the vector database
search_results = vector_db.similarity_search(query=user_query)

context = "\n\n\n".join([f"Page Content : {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile location: {result.metadata['source']}" for result in search_results])

SYSTEM_PROMPT = f"""

You are a helpful AI assistant who answers user query based on the available context retrieved from a PDF file along with page_contents and page number. You should only answer the user based on the following context and navigate the user to open the right page number to know more.

Context : {context}

"""

response = openai_client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role" : "system", "content" : SYSTEM_PROMPT},
        {"role" : "user", "content" : user_query}
    ]
)

print(f"🤖 : {response.choices[0].message.content}")