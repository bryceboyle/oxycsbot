from chatbot import ChatBot
import random


class Breakup_Bot(ChatBot):
    """A chatbot that offers help with a breakup"""

    
    STATES = [
        'waiting',
        'advice',
        'prompt',
        #'healthy'
        #'unhealthy'
        #'listening',
        'move_on',
        'upset'
        
    ]

    PROMPT = [
        'test how does the sitaution make you feel?',
        'test why is that a problem',
        'test what do you do when you feel that way',
    ]

    upsetList = ['Do you think you have a healthy way to express that feeling?',
                     'Is it internal or do you think it’s from the situation?',
                     'Does that work well for you? Do you feel like it’s healthy?']

    
    TAGS = {

        #listen
        'listening': 'listen',
        'listen': 'listen',
        'dont want advice': 'listen',
        'dont need advice': 'listen',
        

        
        #advice
        'advice': 'advice',
        'talk': 'advice',
        'help': 'advice',

        #problems
        'still love':'love',
        'still in love': 'love',
        'cant forget them': 'love',
        'keep thinking about them': 'love',

        'frustrated': 'bothered',
        'angry': 'bothered',
        'annoying': 'bothered',
        'annoyed': 'bothered',
        'bothering me': 'bothered',
        'upset': 'bothered',
        'mad': 'bothered',
        'driving me crazy': 'bothered',
        'uncomfrtable': 'bothered',
        'anxious': 'bothered',

        'better': 'better',
        'good': 'worse',
        'worse': 'worse',
        'the same': 'worse',
        'bad': 'worse',
        
        

    }

 
    def __init__(self):
        """Initialize the OxyCSBot.

              
        """
        super().__init__(default_state='waiting')


    print( "Hi Im the breakup chatbot: made for your breakup problems!" +
           "\nDo you want advice or just someone to listen?")

    def respond_from_waiting(self, message, tags):
        """ find out if they want advice or someone to listen to them """
        
        if 'advice' in tags:
            return self.go_to_state('advice')

        elif 'listening' in tags:
            return self.go_to_state('listen')
        elif 'thanks' in tags:
            return self.finish('thanks')
        else:
            return self.finish('confused')

    def on_enter_advice(self):
        """Send a message when entering the "advice" state."""
        return "whats troubling you?"

        """def respond_from_advice(self, message, tags):"""


    def respond_from_advice(self,message,tags):
        if 'love' in tags:
            return self.go_to_state('move_on')
        elif 'bothered' in tags:
            return self.go_to_state('upset')
        else:
            return self.go_to_state('prompt')



    def on_enter_prompt(self):
        prompt = random.choice(self.PROMPT)
        return prompt

    def respond_from_prompt(self,message,tags):
        if 'love' in tags:
            return self.go_to_state('move_on')
        elif 'bothered' in tags:
            return self.go_to_state('upset')
        else:
            return self.go_to_state('prompt')

    def on_enter_upset(self):
        response = '\n'.join([
            f'I can understand how you would feel that way', 'what do you do when that feeling arises?',
            'and how do you feel after?',
        ])
        return response


    def respond_from_upset(self,message,tags):
        
        if 'better' in tags:
            return self.go_to_state('healthy')
        elif 'worse' in tags:
            return self.go_to_state('unhealthy')
        else:
            if len(self.upsetList) != 0:
                item = random.choice(self.upsetList)
                self.upsetList.remove(item)
                return item
            else:
                return 'i am out of things to say oops change topics?'

    #def on_enter_move_on(self)
    
        
    def finish_thanks(self):
        """Send a message and go to the default state."""
        return "Im glad I could help, if you ever need someone to talk to I'm here."
    
    def finish_confused(self):
        """Send a message and go to the default state."""
        return "Sorry, I'm just a simple bot that can't understand much."


if __name__ == '__main__':
    Breakup_Bot().chat()
