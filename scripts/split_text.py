import pandas as pd

def slice_text_into_fragments(df, window_length, step_size, df_type = "twitter"):
    """
    Slice text into fragments based on the specified window length and step size.

    Parameters:
    - df: DataFrame containing columns 'author', 'date', 'text_all', and 'tweet_id'.
    - window_length: Number of words in one window.
    - step_size: Number of words that the window moves.

    Returns:
    - DataFrame 
    """

    result_list = []

    # Iterate through each row in the input DataFrame
    for _, row in df.iterrows():
        if df_type == "twitter":
            author = row['username']
            tweet_id = row['tweet_id']
            text_all = row['text']
        else: 
            author = row['author']
            date = row['date']
            place = row['place']
            tbl_s = row['TextBlob_Subjectivity']
            tbl_p = row['TextBlob_Polarity']
            herbert = row['sentiment_herbert']
            text_all = row['text']

        # Tokenize the text into words
        words = text_all.split()

        # Generate text fragments based on the specified window length and step size
        for i in range(0, len(words) - window_length + 1, step_size):
            start_idx = i
            end_idx = i + window_length
            text_fragment = ' '.join(words[start_idx:end_idx])

            # Append the result to the new DataFrame
            if df_type =="twitter":
                result_list.append({
                    'username': author,
                    'tweet_id': tweet_id, # type: ignore
                    'text_all': text_all,
                    'text': text_fragment,
                }) # type: ignore
            else: 
                result_list.append({
                    'author': author,
                    'date': date, # type: ignore
                    'text_all': text_all,
                    'place': place, # type: ignore
                    'TextBlob_Subjectivity': tbl_s, # type: ignore
                    'TextBlob_Polarity': tbl_p, # type: ignore
                    'sentiment_herbert': herbert, # type: ignore
                    'text': text_fragment
                }) # type: ignore
    result_df = pd.DataFrame(result_list)
    return result_df

