# Pulse - Healthcare Q&A Agents

*Edgy, cool, simple. Feel the pulse?*

A healthcare agents project with ML screening capabilities using sequential web search and summarization agents.

## Architecture Design

### Model Choice
- **Two-agent architecture**: Web research → Summary (sequential and simple)
- **Separation of concerns**: Web research and summary are separate tools for flexibility
- **Future enhancements**: 
  - Add judgment model on top for quality assessment
  - Implement guardrails for question and answer safety checks
  - Fine-tune summary model for clinical language matching our dataset's tone/brevity/style

### Dataset Observations
Our dataset contains multiple different responses to the same questions in varying styles. This will affect scoring and may require response cleaning to achieve our desired output format.

## Evaluation Strategy

### Traditional Metrics
Reference: [Hugging Face Evaluate Documentation](https://huggingface.co/docs/evaluate/index)
- **BLEU**: Precision-based evaluation
- **ROUGE**: Recall-based evaluation  
- **METEOR**: F1-like metric

### Advanced Metrics
- **BLEURT**: [Semantic similarity evaluation](https://huggingface.co/spaces/evaluate-metric/bleurt)
  - Would benefit from fine-tuning for medical domain
  - Currently limited by hardware constraints

### Evaluation Goals
We prioritize exact language achievement evaluation since we have golden examples for each user query. Clinical language precision is critical where exact language matters significantly.

### Future Evaluations (Budget Permitting)
Reference: [LLM Evaluation Metrics Guide](https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation)
- **Safety**: Prevent unsubstantiated advice or dangerous responses (suicide, emergency questions)
- **Faithfulness**: Ensure information sourcing from trusted medical journals and verified sites only

## Technology Stack

### Agent Framework: OpenAI Agents
**Why OpenAI Agents?** ([Reference](https://medium.com/@elisowski/top-ai-agent-frameworks-in-2025-9bcedab2e239))
- Simple and lightweight architecture
- Built-in web agents functionality
- Available OpenAI developer credits
- Perfect for sequential workflows
- Easy guardrail implementation

### Evaluation Libraries
- **Evaluate**: Non-LLM metrics with traditional evaluation methods
- **ROUGE-Score**: Recall-based text evaluation
- **BLEURT**: Learned evaluation metrics
- **NLTK**: Text processing and tokenization

### Deployment Strategy
- **Serverless architecture**
  - No memory requirements
  - Assumes cyclical and predictable traffic patterns
  - Cold start not expected to be an issue

## Development Notes

*AI assistance used for:*
- README formatting (not content creation)
- pyproject.toml setup
- FastAPI skeleton structure
- .gitignore creation and initial commit 

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