import os
import torch.nn as nn
from pytorch_pretrained_bert import BertModel, BertConfig


class BertClassification(nn.Module):
    def __init__(self, weight_path, num_labels=3):
        super(BertClassification, self).__init__()
        self.num_labels = num_labels
        self.bert = BertModel.from_pretrained(weight_path)
        self.config = BertConfig(os.path.join(weight_path, 'config.json'))
        self.dropout = nn.Dropout(self.config.hidden_dropout_prob)
        self.classifier = nn.Linear(self.config.hidden_size, num_labels)
        nn.init.xavier_normal_(self.classifier.weight)

    def forward(self, input_ids, token_type_ids=None, attention_mask=None):
        _, pooled_output = self.bert(input_ids,
                                     token_type_ids,
                                     attention_mask)

        pooled_output = self.dropout(pooled_output)

        logits = self.classifier(pooled_output)
        return logits
