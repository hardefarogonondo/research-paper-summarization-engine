# Import Libraries
from config.config import SummarizeRequest
from fastapi import FastAPI, HTTPException
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Initialization
tokenizer = T5Tokenizer.from_pretrained('../../models/t5_tokenizer')
model = T5ForConditionalGeneration.from_pretrained('../../models/t5_model')
app = FastAPI()


@app.post("/summarize")
def summarize(request: SummarizeRequest):
    try:
        input_ids = tokenizer.encode(request.text, return_tensors='pt', add_special_tokens=True)
        summary_ids = model.generate(input_ids, num_beams=5, max_length=200, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return {"summary": summary}
    except Exception as error_msg:
        raise HTTPException(status_code=500, detail=str(error_msg))