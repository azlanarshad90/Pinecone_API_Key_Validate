from pinecone import Pinecone, PodSpec

def validate_pinecone_key(api_key):
  pc = Pinecone(api_key=api_key)
  try:
    response = pc.list_indexes()
    if response.indexes:
        print("Your API key is Valid")
        return
    else:
        try:
            pc.create_index(
              name="starter-index",
              dimension=1536,
              metric="cosine",
              spec=PodSpec(
                environment="gcp-starter"
              )
            )
            response = pc.list_indexes()
            if response.indexes:
              print("Your API key is valid")
              pc.delete_index("starter-index")
              return
        except:
          print("Error, the API key is Invalid. Try another !!!")
          return
  except:
    print("Error, the API key is Invalid. Try another !!!")
    return
  
def main():
    try:
        #Enter your Pinecone API key Here
        pinecone_api_key = "PINECONE_API_KEY"
        validate_pinecone_key(pinecone_api_key)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
