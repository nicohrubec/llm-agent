import sys
from openai import OpenAI


class Agent:
    client = OpenAI()
    conversation = []

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
            input=self.conversation
        ).output_text

        self.conversation.append({
            "role": "assistant",
            "content": response
        })

        return response
