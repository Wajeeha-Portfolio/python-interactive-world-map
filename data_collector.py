from io import StringIO
from openai import OpenAI
import pandas as pd

# Initialize the OpenAI client
client = OpenAI(api_key="your-api-key")  # Or set OPENAI_API_KEY in environment

def fetch_data(stat_type):
    """
    Fetch data for the specified statistic type from OpenAI.
    Returns a DataFrame with the data.
    """
    # Send a simple prompt to the latest model
    response = client.chat.completions.create(
        model="gpt-4.1-mini",  # You can change to gpt-4.1 or gpt-4o
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Give the {stat_type} for all countries. output must contain be 'Country,Country Code,{stat_type}' format. The {stat_type} should only contain numeric values. The country code should be 3 letter code that can be used in choropleth maps"}
        ]
    )
    
    # Combine header and API response content into CSV text
    data = f"Country,Country Code,{stat_type}\n" + response.choices[0].message.content.strip()

    # Read the CSV text into a DataFrame
    df = pd.read_csv(StringIO(data))

    # Save to file
    df.to_csv(f"{stat_type}.csv", index=False)

    return df
