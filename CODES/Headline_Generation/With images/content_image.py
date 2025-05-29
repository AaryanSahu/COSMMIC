l="Bangla"
def generate_headline(text, img_url=None):
    # Ensure the text is a string
    if not isinstance(text, str):
        return None
    
    # Encode the text to get tokens
    tokens = tokenizer.encode(text)
    token_count = len(tokens)
    
    # Token limit
    token_limit = 128000
    
    # Trim the text if the token count exceeds the limit
    if token_count > token_limit:
        text = text[:110000]
        tokens = tokenizer.encode(text)
        while len(tokens) > token_limit:
            text = text[:-1]
            tokens = tokenizer.encode(text)
    
    # Prepare the messages for the API call
    messages = [
        {
            "role": "system",
            "content": "You are an expert news editor. Your primary task is to create headlines that accurately reflect the main content of news articles and images."
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"""Craft a precise and engaging news headline in {l} that primarily summarizes the main point of the article or image. Follow these guidelines:

1. Focus predominantly (about 80-90%) on the key information and main message from the article or image.
2. Keep the headline concise, ideally under 15 words.
3. Use active voice and clear, impactful language.
4. Ensure the headline is factual and directly related to the article's main content or the key elements of the image.

Article content: {text}

Headline:"""
                }
            ],
        }
    ]
    
    # Try to add the image URL if it's provided and valid
    if img_url:
        try:
            messages[1]["content"].append({
                "type": "image_url",
                "image_url": {
                    "url": img_url,
                },
            })
        except Exception as e:
            print(f"Error processing image URL: {e}. Continuing without image.")
    
    try:
        # Call the model with the prepared messages
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=50,
        )
        
        headline = completion.choices[0].message.content
        print("headline_generated")
        return headline
    except Exception as e:
        print(f"Error generating headline: {e}")
        
        return None

# Now update your DataFrame
data['GPT_headline_with_images'] = data.apply(
    lambda row: generate_headline(
        row['Content'], 
        row.get('Image URL', None)  # Pass None if 'Image URL' column doesn't exist
    ), 
    axis=1
)

# Save the DataFrame
data.to_csv(f'/Users/aryansahu/Desktop/IIT-P/GPT-4o/with images/{l}_headlineswithimages.csv', index=False)
print("DataFrame saved to 'headlines_with_content_images.csv'")