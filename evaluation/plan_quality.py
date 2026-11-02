from deepeval.integrations.langchain import CallbackHandler
from deepeval.metrics import PlanQualityMetric
from model import eval_model
from dataset import dataset
import sys
from pathlib import Path
from uuid import uuid4
from dotenv import load_dotenv

load_dotenv()
sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "agents")
)
from agent import agent



metrics = [PlanQualityMetric(
    threshold=0.8, model=eval_model, include_reason=True)]


for golden in dataset.evals_iterator(metrics=metrics):
    response = agent.invoke(
        {"messages": [{"role": "user", "content": golden.input}]},
        config={"configurable": {"thread_id": str(uuid4())},
                "callbacks": [CallbackHandler()]}
    )
