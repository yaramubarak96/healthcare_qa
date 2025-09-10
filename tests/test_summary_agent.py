
from agents import Runner, RunConfig
from pulse.summary_agent import summary_agent
import pytest 

@pytest.fixture 
def web_agent_output():
    return """
A urinary tract infection (UTI) occurs when bacteria infect any part of the urinary system, including the kidneys, ureters, bladder, or urethra. The symptoms of a UTI can vary depending on the location and severity of the infection. Common symptoms include:

- **Pain or burning sensation during urination**: A frequent and painful urge to urinate, often accompanied by a burning feeling. ([mayoclinic.org](https://www.mayoclinic.org/diseases-conditions/urinary-tract-infection/symptoms-causes/syc-20353447?utm_source=openai))

- **Frequent urination**: An increased need to urinate, often producing only small amounts of urine. ([mayoclinic.org](https://www.mayoclinic.org/diseases-conditions/urinary-tract-infection/symptoms-causes/syc-20353447?utm_source=openai))

- **Cloudy or bloody urine**: Urine that appears cloudy, dark, or contains blood, which may indicate the presence of bacteria or blood cells. ([mayoclinic.org](https://www.mayoclinic.org/diseases-conditions/urinary-tract-infection/symptoms-causes/syc-20353447?utm_source=openai))

- **Strong-smelling urine**: Urine with a strong or foul odor. ([mayoclinic.org](https://www.mayoclinic.org/diseases-conditions/urinary-tract-infection/symptoms-causes/syc-20353447?utm_source=openai))

- **Pelvic pain**: Discomfort or pressure in the lower abdomen or pelvic area. ([mayoclinic.org](https://www.mayoclinic.org/diseases-conditions/urinary-tract-infection/symptoms-causes/syc-20353447?utm_source=openai))

- **Fever**: A high temperature, which may indicate that the infection has reached the kidneys. ([cdc.gov](https://www.cdc.gov/uti/about/?utm_source=openai))

- **Nausea and vomiting**: Feeling nauseous or vomiting, especially if the infection has spread to the kidneys. ([cdc.gov](https://www.cdc.gov/uti/about/?utm_source=openai))

- **Back or side pain**: Pain in the lower back or sides, which may suggest a kidney infection. ([cdc.gov](https://www.cdc.gov/uti/about/?utm_source=openai))

- **Fatigue**: Feeling unusually tired or weak. ([cdc.gov](https://www.cdc.gov/uti/about/?utm_source=openai))

- **Confusion or agitation**: Particularly in older adults, UTIs can cause mental changes such as confusion or agitation. ([nichd.nih.gov](https://www.nichd.nih.gov/health/topics/urinary/conditioninfo/symptoms?utm_source=openai))

It's important to note that some individuals, especially older adults, may experience atypical symptoms, such as confusion or agitation, rather than the more common signs listed above. ([nichd.nih.gov](https://www.nichd.nih.gov/health/topics/urinary/conditioninfo/symptoms?utm_source=openai))

If you experience any of these symptoms, especially a combination of them, it's advisable to consult a healthcare provider promptly. Early treatment with antibiotics can prevent the infection from spreading and causing more serious health issues. ([cdc.gov](https://www.cdc.gov/uti/about/?utm_source=openai)) 

"""

@pytest.mark.asyncio
async def test_web_agent_only(web_agent_output):
    """Test summary agent with both question and web agent output"""
    # Create input list with both the original question and web agent output
    input_list = [
        {"role": "user", "content": "What are the symptoms of a UTI?"},
        {"role": "assistant", "content": web_agent_output}
    ]
    
    result = await Runner.run(summary_agent, input_list, 
                           max_turns = 1) # dont want to handoff during testing
    print(result.final_output)
    assert result.final_output is not None
    assert isinstance(result.final_output, str)