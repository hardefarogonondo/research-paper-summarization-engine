# Import Libraries
from config.config import SummarizeRequest
from fastapi import FastAPI, HTTPException
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

# Initialization
model_dir = '/app/models/pegasus_model'
tokenizer = PegasusTokenizer.from_pretrained(model_dir)
model = PegasusForConditionalGeneration.from_pretrained(model_dir)
app = FastAPI()


@app.post("/summarize")
def summarize(request: SummarizeRequest):
    try:
        input_ids = tokenizer.encode(request.text, return_tensors='pt', add_special_tokens=True, truncation=True, max_length=1024)
        summary_ids = model.generate(input_ids, max_length=200, min_length=30, length_penalty=1.5, num_beams=6, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return {"summary": summary}
    except Exception as error_msg:
        raise HTTPException(status_code=500, detail=str(error_msg))