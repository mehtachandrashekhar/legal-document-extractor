import spacy
from spacy.training import Example

def fine_tune_ner_model():
    # Load the pre-trained spaCy model
    nlp = spacy.load("en_core_web_sm")
    
    # Add a new text classifier pipe if it doesn't exist
    if "textcat" not in nlp.pipe_names:
        textcat = nlp.add_pipe("textcat", config={"architecture": "bow"}, last=True)
    else:
        textcat = nlp.get_pipe("textcat")
    
    # Add a custom label to the text classifier
    textcat.add_label("CUSTOM_LABEL")
    
    # Prepare training data (replace with your own data)
    train_data = [
        ("XYZ Act", {"entities": [(0, 8, "CUSTOM_LABEL")]}),
        # Add more training examples here
    ]
    
    # Convert training data to spaCy Example objects
    examples = [Example.from_dict(nlp.make_doc(text), annotation) for text, annotation in train_data]
    
    # Train the model
    nlp.begin_training()
    for epoch in range(10):
        random.shuffle(examples)
        losses = {}
        for batch in spacy.util.minibatch(examples, size=8):
            texts, annotations = zip(*batch)
            nlp.update(texts, annotations, drop=0.5, losses=losses)
        print(f"Epoch {epoch} - Losses: {losses}")
    
    # Save the fine-tuned model
    nlp.to_disk("fine_tuned_model")

if __name__ == "__main__":
    fine_tune_ner_model()
