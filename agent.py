import sys
import json

from openai import OpenAI


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


class Agent:
    client = OpenAI()
    conversation = []
    tools = [{
        "type": "function",
        "name": "read_file",
        "description": "Read the contents of a given relative file. Use this when you want to see what's inside a file.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string"}
            },
            "required": ["path"],
            "additionalProperties": False
        },
        "strict": True
    }]

    @staticmethod
    def get_user_message():
        try:
            return sys.stdin.readline()
        except KeyboardInterrupt:
            sys.exit()

    def get_response(self, user_input):
        self.conversation.append({
            "role": "user",
            "content": user_input
        })

        response = self.client.responses.create(
            model="gpt-4.1-nano",
            input=self.conversation,
            tools=self.tools
        )
        output_text = response.output_text

        if output_text != "":
            self.conversation.append({
                "role": "assistant",
                "content": output_text
            })

            return output_text

        tool_call = response.output[0]
        args = json.loads(tool_call.arguments)
        result = read_file(args["path"])
        self.conversation.append(tool_call)
        self.conversation.append({
            "type": "function_call_output",
            "call_id": tool_call.call_id,
            "output": str(result)
        })

        response = self.client.responses.create(
            model="gpt-4.1-nano",
            input=self.conversation,
            tools=self.tools
        )
        output_text = response.output_text
        self.conversation.append({
            "role": "assistant",
            "content": output_text
        })

        return output_text
