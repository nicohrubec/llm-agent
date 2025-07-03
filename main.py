from agent import Agent


def main():
    agent = Agent()

    print("Chat with ChatGPT (use 'crl-c' to quit)")

    while True:
        user_input = agent.get_user_message()
        response = agent.get_response(user_input)
        print(response)


if __name__ == '__main__':
    main()
