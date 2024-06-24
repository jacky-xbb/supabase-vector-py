# Supabase Vector Store

This project demonstrates how to use LangChain and Supabase to create a vector store for Documents using OpenAI embeddings. The text data is split into manageable chunks and stored in Supabase for efficient retrieval.

## Prerequisites

- Python 3.12
- Pipenv

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/supabase-vector-store.git
   cd supabase-vector-store
   ```

2. Install dependencies using Pipenv:

   ```bash
   pipenv install
   ```

3. Create a `.env` file in the root directory and add your Supabase and OpenAI credentials:

   ```plaintext
   SUPABASE_API_URL=your_supabase_api_url
   SUPABASE_API_KEY=your_supabase_api_key
   OPENAI_API_KEY=your_openai_api_key
   OPENAI_API_URL=your_openai_api_url
   ```

## Usage

1. Ensure you have a text file named `personal-info.txt` in the root directory with the content you want to process.

2. Install the dependencies using Pipenv:

   ```bash
   pipenv install
   ```

3. Run the script:

   ```bash
   pipenv run python vector.py
   ```

4. If the script runs successfully, you should see the message:

   ```plaintext
   Documents stored successfully.
   ```

## License

This project is licensed under the MIT License.

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [Supabase](https://supabase.io/)
- [OpenAI](https://openai.com/)
