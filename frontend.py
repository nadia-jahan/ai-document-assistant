import requests
import streamlit as st

API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Document Assistant")

st.write(
    "Upload a technical document and ask grounded questions using semantic retrieval and OpenAI generation."
)

uploaded_file = st.file_uploader(
    "Upload a PDF document",
    type=["pdf"]
)

if uploaded_file is not None:

    if st.button("Process Document"):

        with st.spinner("Processing document..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf"
                )
            }

            response = requests.post(
                f"{API_BASE_URL}/upload",
                files=files
            )

            if response.status_code == 200:

                data = response.json()

                st.success("Document processed successfully!")

                st.write(f"Filename: {data.get('filename')}")
                st.write(f"Chunks Created: {data.get('number_of_chunks')}")
                st.write(f"Embedding Dimension: {data.get('embedding_dimension')}")

            else:
                st.error("Failed to process document.")
                st.write(response.text)

st.divider()

query = st.text_input(
    "Ask a question about the uploaded document"
)

if st.button("Ask Question"):

    if not query:
        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating answer..."):

            response = requests.get(
                f"{API_BASE_URL}/ask",
                params={"query": query}
            )

            if response.status_code == 200:

                data = response.json()

                if "error" in data:
                    st.error(data["error"])

                else:

                    st.subheader("Answer")

                    st.write(data.get("answer"))

                    with st.expander("View Retrieved Source Chunks"):

                        for i, source in enumerate(data.get("sources", []), start=1):

                            st.markdown(f"### Source Chunk {i}")

                            st.write(source)

                            st.divider()

            else:
                st.error("Failed to generate answer.")
                st.write(response.text)