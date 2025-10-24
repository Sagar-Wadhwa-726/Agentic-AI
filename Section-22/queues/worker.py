from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

# Vector embeddings
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embedding_model
)

openai_client = OpenAI()
 

def process_query(query: str):
    print("Searching Chunks ", query)
    search_results = vector_db.similarity_search(query=query)

    context = "\n\n\n".join([f"Page Content : {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile location: {result.metadata['source']}" for result in search_results])

    SYSTEM_PROMPT = f"""

    You are a helpful AI assistant who answers user query based on the available context retrieved from a PDF file along with page_contents and page number. You should only answer the user based on the following context and navigate the user to open the right page number to know more.

    Context : {context}

    """

    response = openai_client.chat.completions.create(
    model="gpt-5",
    messages=[
            {"role" : "system", "content" : SYSTEM_PROMPT},
            {"role" : "user", "content" : query}
        ]
    )
    
    print(f"🤖 : {response.choices[0].message.content}")
    return response.choices[0].message.content
