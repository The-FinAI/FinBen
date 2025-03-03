import evaluate, re, string
from seqeval.metrics import f1_score as entity_score


# summarizaiton
def rouge1(items):
    """
    # passthrough for efficiency
    """
    return items


def rouge1_agg(items):
    """
    Higher is better
    """
    refs = list(zip(*items))[0]
    preds = list(zip(*items))[1]
    rouge_scorer = evaluate.load("rouge")
    return rouge_scorer.compute(predictions=preds, references=refs)["rouge1"]


# ner
def process_text(entity_string, text):
    # Initialize
    entity_list = [(", ".join(val.split(", ")[:-1]), val.split(", ")[-1]) for val in entity_string.split("\n")]
    text_words = list(filter(None, re.split(r'(\s+|[' + re.escape(string.punctuation).replace('%', '') + r'«»‘’“”€])', text)))
    # print(text_words)
    labels = ['O'] * len(text_words)
    # text_lower = text.lower()
    text_lower = text

    # Create a list to store the start index of each word
    word_indices = [0]
    for word in text_words[:-1]:
        word_indices.append(word_indices[-1] + len(word))

    # Iterate over the entity list
    # print (entity_list)
    for entity, entity_type in entity_list:
        entity_words = entity.split()
        entity_lower = entity

        # Find start and end index of each occurrence of the entity in the text
        start = 0
        while True:
            start = text_lower.find(entity_lower, start)
            if not entity or start == -1: break  # No more occurrence
            end = start + len(entity) - 1

            # Find the words included in this occurrence
            try:
                start_word = next(i for i, ind in enumerate(word_indices) if ind >= start)
                end_word = next(i for i, ind in enumerate(word_indices) if ind > end)

                # Label the words
                labels[start_word] = 'B-' + entity_type
                for i in range(start_word+1, end_word):
                    labels[i] = 'I-' + entity_type

                # Move to the next character after the occurrence
            except Exception:
                pass
            start = end + 1

    _, filtered_labels = bio_filter(text_words, labels)

    return filtered_labels


def bio_filter(text_list, label_list):
    processed_text = []
    processed_label = []

    for text, label in zip(text_list, label_list):
        if not re.search(r'(\s+|[' + re.escape(string.punctuation).replace('%', '') + r'«»‘’“”€])', text):
            processed_text.append(text)
            processed_label.append(label)

    # print(processed_text)
    return processed_text, processed_label


def process_results(doc, results):
    text = doc["text"]
    # print("\n" + text)

    ground_truths_string = doc["answer"]
    # print(ground_truths_string)
    ground_truths = process_text(ground_truths_string, text)
    # print(len(ground_truths))
    # print(ground_truths)

    prediction_string = results[0].strip()
    # print(prediction_string)
    prediction = process_text(prediction_string, text)
    # print(len(prediction))
    # print(prediction)

    f1 = entity_score([ground_truths], [prediction])
    return {"f1": f1}
