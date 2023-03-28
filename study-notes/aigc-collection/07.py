from transformers import T5Tokenizer, T5Model
import torch
import pandas as pd
from sklearn.metrics import classification_report

# load the T5 tokenizer and model
# tokenizer = T5Tokenizer.from_pretrained('t5-small', model_max_length=512)
# model = T5Model.from_pretrained('t5-small')

# T5好评例子的评分 : -0.010294
# T5差评例子的评分 : -0.008990

tokenizer = T5Tokenizer.from_pretrained('t5-base', model_max_length=512)
model = T5Model.from_pretrained('t5-base')

# T5好评例子的评分 : 0.010347
# T5差评例子的评分 : -0.023935

# set the model to evaluation mode
model.eval()

# encode the input sentence
def get_t5_vector(line):
    input_ids = tokenizer.encode(line, return_tensors='pt', max_length=512, truncation=True)
    # generate the vector representation
    with torch.no_grad():
        outputs = model.encoder(input_ids=input_ids)
        vector = outputs.last_hidden_state.mean(dim=1)
    return vector[0]

positive_review_in_t5 = get_t5_vector("An Amazon review with a positive sentiment.")
negative_review_in_t5 = get_t5_vector('An Amazon review with a negative sentiment.')

def test_t5():
  positive_example_in_t5 = get_t5_vector(positive_text)
  negative_example_in_t5 = get_t5_vector(negative_text)

  def get_t5_score(sample_embedding):
    return cosine_similarity(sample_embedding, positive_review_in_t5) - cosine_similarity(sample_embedding, negative_review_in_t5)

  positive_score = get_t5_score(positive_example_in_t5)
  negative_score = get_t5_score(negative_example_in_t5)

  print("T5好评例子的评分 : %f" % (positive_score))
  print("T5差评例子的评分 : %f" % (negative_score))

test_t5()

datafile_path = "data/fine_food_reviews_with_embeddings_1k.csv"

df = pd.read_csv(datafile_path)

df["t5_embedding"] = df.Text.apply(get_t5_vector)
# convert 5-star rating to binary sentiment
df = df[df.Score != 3]
df["sentiment"] = df.Score.replace({1: "negative", 2: "negative", 4: "positive", 5: "positive"})

from sklearn.metrics import PrecisionRecallDisplay
def evaluate_embeddings_approach():
    def label_score(review_embedding):
        return cosine_similarity(review_embedding, positive_review_in_t5) - cosine_similarity(review_embedding, negative_review_in_t5)

    probas = df["t5_embedding"].apply(lambda x: label_score(x))
    preds = probas.apply(lambda x: 'positive' if x>0 else 'negative')

    report = classification_report(df.sentiment, preds)
    print(report)

    display = PrecisionRecallDisplay.from_predictions(df.sentiment, probas, pos_label='positive')
    _ = display.ax_.set_title("2-class Precision-Recall curve")

evaluate_embeddings_approach()


#               precision    recall  f1-score   support
#     negative       0.60      0.90      0.72       136
#     positive       0.98      0.90      0.94       789
#     accuracy                           0.90       925
#    macro avg       0.79      0.90      0.83       925
# weighted avg       0.93      0.90      0.91       925