import json

# Open the JSON file and load data into a list
with open('Cell_Phones_and_Accessories_5.json', 'r', encoding='utf-8') as file:
    data = [json.loads(line) for line in file]

# Create an empty list to store processed records
content_list = []

# Define common words
common_words = [
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves',
    'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their',
    'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
    'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an',
    'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
    'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
    'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when',
    'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no',
    'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don',
    'should', 'now'
]

# Define good and bad words with their respective weights
word_weights = {
    'good': 0.65,
    'great': 0.65,
    'excellent': 0.65,
    'awesome': 0.65,
    'fantastic': 0.65,
    'amazing': 0.65,
    'superb': 0.65,
    'wonderful': 0.65,
    'perfect': 0.65,
    'love': 0.65,
    'like': 0.65,
    'best': 0.65,
    'better': 0.65,
    'nice': 0.65,
    'beautiful': 0.65,
    'happy': 0.65,
    'satisfied': 0.65,
    'recommend': 0.65,
    'recommended': 0.65,
    'recommendable': 0.65,
    'recommendation': 0.65,
    'recommendations': 0.65,
    'recommending': 0.65,
    'admirable': 0.65,
    'brilliant': 0.65,
    'cool': 0.65,
    'delightful': 0.65,
    'enjoyable': 0.65,
    'fabulous': 0.65,
    'fun': 0.65,
    'genius': 0.65,
    'glad': 0.65,
    'impressive': 0.65,
    'incredible': 0.65,
    'loved': 0.65,
    'lovely': 0.65,
    'marvelous': 0.65,
    'outstanding': 0.65,
    'pleased': 0.65,
    'positive': 0.65,
    'bad': 0.05,
    'worst': 0.05,
    'worse': 0.05,
    'horrible': 0.05,
    'terrible': 0.05,
    'awful': 0.05,
    'disappointed': 0.05,
    'disappointing': 0.05,
    'disappointment': 0.05,
    'disappointments': 0.05,
    'disappoint': 0.05,
    'disappoints': 0.05,
    'disappointedly': 0.05,
    'disappointedly': 0.05,
    'disappointingly': 0.05,
    'disappointingly': 0.05,
    'didnt like': 0.05,
    'hate': 0.05,
    'hated': 0.05,
    'hates': 0.05,
    'hating': 0.05,
    'hateable': 0.05,
    'hatefully': 0.05,
    'hatefulness': 0.05,
    'hatefulness': 0.05,
    'hateworthy': 0.05,
    'hateworthy': 0.05,
    'unhappy': 0.05,
    'unhappily': 0.05,
    'unhappiness': 0.05,
    'unhappiness': 0.05,
    'unhappier': 0.05,
    'not good': 0.05,
    'not great': 0.05,
    'not excellent': 0.05,
    'not awesome': 0.05,
    'not fantastic': 0.05,
    'not amazing': 0.05,
    'dislike': 0.05,
    'disliked': 0.05,
    'dislikes': 0.05,
    'disliking': 0.05,
    'dislikeable': 0.05,
    'dislikeably': 0.05,
    'dislikeable': 0.05,
    'unbearable': 0.05,
    'unbearably': 0.05,
    'dont like': 0.05,
    'dont': 0.05,
    'irritating': 0.05,
    'irritated': 0.05,
    'irritates': 0.05,
    'irritatingly': 0.05
}

# Iterate over each record in the data
for item in data:
    # Check if 'asin' key exists in the record
    if 'asin' in item:
        # Lowercase the review text and summary
        review_text = item.get("reviewText", "").lower()
        summary = item.get("summary", "").lower()

        # Remove punctuations from the review text and summary
        review_text = review_text.translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))
        summary = summary.translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))

        # Remove common words from the review text and summary
        review_text = ' '.join([word for word in review_text.split() if word not in common_words])
        summary = ' '.join([word for word in summary.split() if word not in common_words])

        # Calculate sentiment score based on word weights
        sentiment_score = sum(word_weights.get(word, 0) for word in review_text.split())

        # Assign sentiment label based on sentiment score
        if sentiment_score > 0.5:
            sentiment_label = 'positive'
        elif sentiment_score < 0.5:
            sentiment_label = 'negative'
        else:
            sentiment_label = 'neutral'

        # Store the processed record in the list
        content_list.append({
            'asin': item['asin'],
            'reviewText': review_text,
            'summary': summary,
            'sentiment_score': sentiment_score,
            'sentiment_label': sentiment_label
        })

print(content_list[0:5])

#Save the end result in a text file, putting the review text next to its sentiment. The reviews next to the feedback should be the same as it was in the original file.
# with open('sentiment_analysis.txt', 'w', encoding='utf-8') as file:
#     for record in content_list:
#         file.write(f"{record['sentiment_label']}: {record['reviewText']}\n")



