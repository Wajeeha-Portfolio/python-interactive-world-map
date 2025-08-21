from io import StringIO
from openai import OpenAI
import pandas as pd

# Initialize the OpenAI client
client = OpenAI(api_key="your-api-key") 

def validate_indicator(indicator_value):
    prompt = f"You are an expert in global development metrics and international statistics. Your task: Determine whether the given text exactly matches the name of a recognized global development indicator that is officially tracked by organizations such as the United Nations (SDGs), the World Bank, OECD, or other reputable statistical agencies. If the text is a valid indicator and measurable statistics exist globally for it, return 'true' (without quotes). If it is not a recognized global indicator with collectable statistics, return exactly 'false'. Text:{indicator_value}"
    # prompt = f"Is '{indicator_value}' a recognized global development indicator with measurable statistics? Respond with 'true' or 'false'."
    response = client.chat.completions.create(
        model="gpt-4.1-mini",  # You can change to gpt-4.1 or gpt-4o
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    print(f"Prompt sent to OpenAI: {prompt}")
    print(f"Response from OpenAI: {response.choices[0].message.content.strip()}")
    return response.choices[0].message.content.strip()

def fetch_data(stat_type):
    """
    Fetch data for the specified statistic type from OpenAI.
    Returns a DataFrame with the data.
    """
    prompt = f"""Provide a structured dataset for all recognized countries with the following columns:
    Country, Country Code, {stat_type}

    - Use 3 letter country codes for Country Code that is compatible with choropleth maps.
    - The indicator values must be numeric only. 
    - If exact up-to-date data is not available, provide the most recent reliable estimates or use representative sample values.
    - Do not ask me for a dataset; instead, return the values directly in the requested format.
    - Output only the table in plain text (CSV style), no explanations.
"""
    # Send a simple prompt to the latest model
    response = client.chat.completions.create(
        model="gpt-4.1-mini",  # You can change to gpt-4.1 or gpt-4o
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    print(f"Prompt sent to OpenAI: {prompt}")
    print(f"Response from OpenAI: {response.choices[0].message.content.strip()}")
    
    # Combine header and API response content into CSV text
    data = response.choices[0].message.content.strip()

    # Read the CSV text into a DataFrame
    df = pd.read_csv(StringIO(data))

    # Save to file
    df.to_csv(f"{stat_type}.csv", index=False)

    return df
