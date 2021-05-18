import torch
import torch.nn.functional as F
from transformers import BertTokenizer
from tqdm import tqdm

LABELS = {0: 'neutral', 1: 'positive', 2: 'negative'}
MAX_SEQ_LENGTH = 64

if torch.cuda.is_available():
    device = torch.device("cuda")
    print('Using GPU', torch.cuda.get_device_name(0))

else:
    device = torch.device("cpu")
    print('Using CPU')


def preprocess_for_finbert(data, vocab_file, max_length=MAX_SEQ_LENGTH):
    tokenizer = BertTokenizer(vocab_file=vocab_file, do_lower_case=True)

    input_ids = []
    token_type_ids = []
    attention_masks = []

    for sent in data:
        encoded_sent = tokenizer.encode_plus(
            text=sent,
            add_special_tokens=True,
            max_length=max_length,
            truncation=True,
            padding='max_length',
            return_token_type_ids=True,
            return_attention_mask=True
        )

        input_ids.append(encoded_sent.get('input_ids'))
        token_type_ids.append(encoded_sent.get('token_type_ids'))
        attention_masks.append(encoded_sent.get('attention_mask'))

    # Convert lists to tensors
    input_ids = torch.tensor(input_ids)
    token_type_ids = torch.tensor(token_type_ids)
    attention_masks = torch.tensor(attention_masks)

    return input_ids, token_type_ids, attention_masks


def finbert_predict(model, dataloader):
    model.to(device).eval()

    all_logits = []

    for batch in tqdm(dataloader):
        b_input_ids, b_type_ids, b_attn_mask = tuple(
            t.to(device) for t in batch)[:3]

        with torch.no_grad():
            logits = model(b_input_ids, b_type_ids, b_attn_mask)
        all_logits.append(logits)

    # Concatenate logits from each batch
    all_logits = torch.cat(all_logits, dim=0)

    # Apply softmax to calculate probabilities
    probs = F.softmax(all_logits, dim=1)
    output = [LABELS[i.item()] for i in torch.argmax(probs, axis=1)]
    return output
