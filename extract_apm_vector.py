from transformers import BertTokenizer, BertModel
        import torch

        tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        model = BertModel.from_pretrained('bert-base-uncased')

        text = "Error: Database connection failed."
        encoded_input = tokenizer(text, return_tensors='pt')

        with torch.no_grad():
            output = model(**encoded_input)

        log_vector = output.last_hidden_state.mean(dim=1).squeeze().numpy()
        print(log_vector[:5]) 
