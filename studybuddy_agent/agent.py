import litellm
litellm.ssl_verify = False

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

#from .system_prompt import system_prompt
from .tools import split_time

q_model = LiteLlm(
    model="openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
)

root_agent = Agent(
    name= "studybuddy_agent",
    model=q_model,
    description="Helpful assistant",
    instruction="Помоги сформулировать первый выполнимый шаг. Разбей время на короткие рабочие блоки. Уточни задачу, если пользователь её не назвал.",
    tools=[split_time]
)
