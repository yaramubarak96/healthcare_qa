# CHOICES

## Naming 
My repo name will be called: 
pulse... edgy, cool, simple. Feel the pulse? 

## Model Choice:
- two agents ( web research --> summary ), sequential and simple 
- did not put the web research in the same tool as summary because I would like flexibility in how the research is done 
- could add a judgement model on top for future reference 
- OPENAI agents allows you to easily add guardrails, I would do that to add checks for question and answer safety
- For future I would like to finetune summary model for better clinical language and to match the tone/brevity/style of our desired output 
- I noticed our dataset has multiple different responses to the same questions... in different styles. That will affect our scoring and we would probably have to clean that to our desired response after cleaning.

## Evaluation Choices:
https://huggingface.co/docs/evaluate/index
- Traditional: BLEU (precision based), ROUGE (recall based), METEOR (~F1)

I'd like to evaluate exact language achievement of the model because we have golden examples for each user query. 
This is also clinical language and exact language matters a lot. 

I also would like to take a look at BLEURT:
https://huggingface.co/spaces/evaluate-metric/bleurt
which would take care of semantic similarity but I'd like to finetune that. 
My current laptop crashes when I try to even use it, so that's out for now. 

Given more budget (I do not have enough llm credits):
https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation
- Safety: do not give unsubstantiated advice or answer dangerous questions (suicide, emergency questions...) 
- Faithfulness: (if supported has medical journals, or only trusted sites, I would like to make sure only those are pulled from).

## Code choices:

### Agent library: 
chose openAI Agents (https://medium.com/@elisowski/top-ai-agent-frameworks-in-2025-9bcedab2e239): 
- simple
- lightweight 
- has built in web agents (useful :))
- I have openAI developer credits (fantastic...)
- only works for sequential stuff (which I am doing)

## Eval library 
Evaluate: for non-llm metrics... Easy to use, has traditional metrics. 

Deepeval: for llm metrics like faithfulness and safety and any llm as a judge metrics, and can be built into pytests :) 

## Deployment choices: 
- serverless 
  - no memory needed
  - I assume this traffic is cyclical and predictable so cold start wont be an issue

## I used AI to: 
- format this readme (not write but format)
- Setup my pyproject file 
- write fastapi skeleton
- write my gitignore and push my first commit 

# Setup 

## Installation
1. Create and activate your environment (use Python 3.9+, I used 3.11):

2. Navigate to your repo and install dependencies:
   ```bash
   cd your-repo
   pip install -e .
   ```

## Configuration
Export your OpenAI API key:
```bash
export OPENAI_API_KEY=your-key-here
```

## Running the App
Start the FastAPI server locally:
```bash
uvicorn pulse.app:app --host 0.0.0.0 --port 8000 --reload
```

## Testing
Test with curl examples:
```bash
curl -X POST http://localhost:8000/pulse/answer \
     -H "Content-Type: application/json" \
     -d '{
       "user_id": "123e4567-e89b-12d3-a456-426614174000",
       "user_name": "Test User",
       "query": "What are the symptoms of a UTI?"
     }'
``` 

# Results 
Look at evaluations.ipynb notebook, it will have batch running, scoring and final results for 400 examples 