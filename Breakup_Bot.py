from chatbot import ChatBot


class Breakup_Bot(ChatBot):
    """A simple chatbot that directs students to office hours of CS professors."""

    STATES = [
        'waiting',
        'advice',
        'listening'
        'love'
        'move_on'
        
    ]
#weeeeee
    TAGS = {

        #listen
        'listening': 'listen',
        'listen': 'listen',

        
        #advice
        'advice': 'advice',
        'talk': 'advice',
        'help': 'advice',

        #problems
        'still love':'love',
        'still in love': 'love'
        
        

    }

 
    def __init__(self):
        """Initialize the OxyCSBot.

              
        """
        super().__init__(default_state='waiting')


    def respond_from_waiting(self, message, tags):
        """ find out if they want advice or someone to vent to
        """
        if 'advice' in tags:
            return self.go_to_state('advice')

        elif 'listening' in tags:
            return self.go_to_state('listen')

        else:
            return self.finish('confused')



    def on_enter_advice(self):
        """Send a message when entering the "advice" state."""
        return "what do you need help with"

    """def respond_from_advice(self, message, tags):"""


    def finish_confused(self):
        """Send a message and go to the default state."""
        return "Sorry, I'm just a simple bot that can't understand much."


if __name__ == '__main__':
    Breakup_Bot().chat()
