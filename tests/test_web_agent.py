from agents import Runner
from agents.items import ToolCallItem, MessageOutputItem, HandoffCallItem, HandoffOutputItem, MessageOutputItem 
from pulse.web_agent import web_agent
import pytest 

item_flow = [
    (ToolCallItem, 'web_agent'),
    (MessageOutputItem, 'web_agent'),
    (HandoffCallItem, 'web_agent'),
    (HandoffOutputItem, 'web_agent'),
    (MessageOutputItem, 'summary_agent'),
]

@pytest.mark.asyncio
async def test_web_agent_only():
    """Test web agent without handoff during testing - should raise MaxTurnsExceeded"""
    result = await Runner.run(web_agent, "What are the symptoms of a UTI?", ) 
    # check first 2 item flows 
    for step,item in enumerate(result.new_items[:2]): 
        assert isinstance(item, item_flow[step][0])
        assert item.agent.name == item_flow[step][1]
    print(result.raw_responses[0].output) # llm response from agent 
    assert result.raw_responses[0].output is not None

@pytest.mark.asyncio
async def test_web_agent_with_handoff():
    """Test web agent with handoff during testing"""
    result = await Runner.run(web_agent, "What are the symptoms of a UTI?", )
    # check all item flows 
    for step,item in enumerate(result.new_items): 
        assert isinstance(item, item_flow[step][0]), item
        assert item.agent.name == item_flow[step][1], item
    print(result) 
    assert result.final_output is not None
    assert isinstance(result.final_output, str)
    assert result._last_agent.name == "summary_agent"
