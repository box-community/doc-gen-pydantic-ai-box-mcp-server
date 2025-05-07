import asyncio
import os
import textwrap
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.agent import AgentRunResult
from pydantic_ai.mcp import MCPServerStdio
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from console_utils import type_writer_effect_machine, print_markdown

# Load environment variables from .env file
load_dotenv()

TEMPLATE = "data/nda_template.docx"
DATA = "data/NDA.json"


def print_tools_used(agent_result: AgentRunResult):
    all_messages = agent_result.all_messages()
    for message in all_messages:
        for part in message.parts:
            if part.part_kind == "tool-call":
                type_writer_effect_machine(
                    f"  {part.tool_name}", is_dim=True, delay=0.01
                )


async def main() -> None:
    mcp_box = MCPServerStdio(
        command="uv",
        args=[
            "--directory",
            "/Users/rbarbosa/Documents/code/python/box/mcp-server-box",
            "run",
            "src/mcp_server_box.py",
        ],
    )

    model = OpenAIModel("gpt-4.1-mini", provider=OpenAIProvider())

    agent = Agent(
        model,
        system_prompt=(
            "You are a Box Agent. Your job is to answer questions and complete actions with Box using the tools available."
        ),
        mcp_servers=[mcp_box],
    )
    prompt = "Who am I logged in as in Box?"
    print_markdown("**Human:**")
    type_writer_effect_machine(f"{prompt}", is_dim=False, delay=0.05)
    print_markdown("---")

    async with agent.run_mcp_servers():
        result = await agent.run(prompt)

    print_markdown("**Tools used::**")
    print_tools_used(result)
    print_markdown("---")
    print_markdown("**AI:**")
    type_writer_effect_machine(f"{result.output}", is_dim=False, delay=0.01)
    print_markdown("---")

    prompt = f"""
        Upload this local file  {os.path.abspath(TEMPLATE)} to the Box Folder called OpenAI Doc Gen and mark it as a doc gen template.
        Wait a few seconds for the doc gen tags to be processed by Box.
        Then upload the data file {os.path.abspath(DATA)} to the same folder, and  generate a new document with the template using the data file.
        """
    prompt = textwrap.dedent(prompt)

    print_markdown("**Human:**")
    type_writer_effect_machine(f"{prompt}", is_dim=False, delay=0.05)
    print_markdown("---")

    async with agent.run_mcp_servers():
        result = await agent.run(prompt)

    print_markdown("**Tools used::**")
    print_tools_used(result)
    print_markdown("---")
    print_markdown("**AI:**")
    type_writer_effect_machine(f"{result.output}", is_dim=False, delay=0.01)
    print_markdown("---")


if __name__ == "__main__":
    asyncio.run(main())
