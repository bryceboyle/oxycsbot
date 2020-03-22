from chatbot import ChatBot
import random


class Breakup_Bot(ChatBot):
    """A chatbot that offers help with a breakup"""

    
    STATES = [
        'waiting',
        'generic',
        'healthy',
        'unhealthy',
        'move_on',
        'upset',
        'doubt',
        'questioning',
        #'insecure',
        'done',
        'm_advice'
    ]

    PROMPT = [
        'how does the situation make you feel?',
        'why is the situation a problem',
        'what do you do when you feel that way',
        ]


    upsetList = [
        'Do you think you have a healthy way to express that feeling?',
        'Is it internal or do you think it’s from the situation?',
        'Does that work well for you? Do you feel like it’s healthy?'
        ]

    unhealthyList = [
        'outside of this situation what do you do when you feel this emotion',
        'trying to distance yourself from what triggers you can prevent falling into unhealthy patterns, how can you try to remove yourself from the situation',
        

        ]

    adviceList = ['You should make sure you reclaim the things of yours that they have, so you won\'t feel dependent on them.',
                  'Keep your distance from them. I understand that this is difficult, but you need time to heal on your own.',
                  'Try not to seek them out, which is easier said than done if you see them frequently, but it will be good for you.',
                  'Find distractions in other people or things you love to help you through this.',
                  'If you have tried many things already, it is also possible that no one can help you move on completely. You will just need more time, which is perfectly okay.']

    questionList = ['How long have you felt this way?',
                    'Do you think you were with them for the right reasons?',
                    'Do you think you were with them for who they are or who they had the potential to be?',
                    'How do you feel about being unhappy for so long?',
                    'Were the highs of the relationship worth the lows?']
    
    TAGS = {


        #problems
        'still love':'love',
        'still in love': 'love',
        'cant forget them': 'love',
        'keep thinking about them': 'love',
        'i love': 'love',
        'move on': 'love',
        'get over': 'love',

        'frustrated': 'bothered',
        'angry': 'bothered',
        'annoying': 'bothered',
        'annoyed': 'bothered',
        'bothering me': 'bothered',
        'upset': 'bothered',
        'mad': 'bothered',
        'driving me crazy': 'bothered',
        'uncomfortable': 'bothered',
        'anxious': 'bothered',
        'sad': 'bothered',
        'bad': 'bothered',
        'not great': 'bothered',
        'hurts': 'bothered',
        'pisses me off': 'bothered',
        'pissed': 'bothered',

        'better': 'better',
        'I have healthy':'better',
        'good': 'worse',
        'worse': 'worse',
        'the same': 'worse',
        'bad': 'worse',
        'don\'t have healthy': 'worse',

        'am happy': 'happy',
        'was happy': 'happy',
        'i feel happy': 'happy',
        'i felt happy': 'happy',
        'i feel good': 'happy',
        'pretty good': 'happy',
        'i felt good': 'happy',
        'i feel okay': 'bad',
        'i felt okay': 'bad',
        'i felt ok': 'bad',
        'i feel ok': 'bad',
        'unhappy': 'bad',
        'worried': 'bad',
        'upset': 'bad',
        'anxious': 'bad',
        'anxiety': 'bad',
        'stress': 'bad',
        'stressed': 'bad',
        'angry': 'bad',
        'mad': 'bad',
        'frustrated': 'bad',
        'sad' : 'bad',
        'lonely': 'bad',
        'worthless': 'bad',
        'felt bad': 'bad',
        'feel bad': 'bad',
        'feels bad': 'bad',

        'regret': 'unsure',
        'unsure': 'unsure',
        'i don\'t know': 'unsure',
        'not sure': 'unsure',
        'confused': 'unsure',
        'lost': 'unsure',
        'mistake': 'unsure',
        
        
        
        #yes and no
        'im good':'no',
        'nope': 'no',
        'i dont think': 'no',
        'not really': 'no',
        'guess not':'no',
        'no': 'no',
        'nah': 'no',
        'i don\'t know': 'no',
        
        'yes': 'yes',
        'yea': 'yes',
        'i still': 'yes',
        'maybe': 'yes',
        'i think so': 'yes',
        'sure': 'yes',
        'i guess': 'yes'
    }

 
    def __init__(self):
        """Initialize the OxyCSBot.

              
        """
         
        super().__init__(default_state='waiting')


    print( "Hi Im the breakup chatbot: made for your breakup problems!" +
           "\nWhat can I help you with?")

    def respond_from_waiting(self, message, tags):

        if 'love' in tags:
            return self.go_to_state('move_on')
        elif 'bothered' in tags:
            return self.go_to_state('upset')
        elif 'thanks' in tags:
            return self.finish('thanks')
        elif 'unsure' in tags:
            return self.go_to_state('doubt')
        else:
            return self.go_to_state('generic')


    def on_enter_generic(self):
        prompt = random.choice(self.PROMPT)
        return prompt

    def respond_from_generic(self,message,tags):
        if 'love' in tags:
            return self.go_to_state('move_on')
        elif 'bothered' in tags:
            return self.go_to_state('upset')
        elif 'unsure' in tags:
            return self.go_to_state('doubt')
        else:
            return self.go_to_state('generic')

    def on_enter_upset(self):
        response = '\n'.join([
            f'I can understand how you would feel that way',
            'what do you do when that feeling arises?',
            'and how do you feel after?',
        ])
        return response


    def respond_from_upset(self,message,tags):
        if len(self.upsetList) != 0:
            item = random.choice(self.upsetList)
            self.upsetList.remove(item)
            return item
        else:
            if 'better' in tags:
                return self.go_to_state('healthy')
            elif 'worse' in tags:
                return self.go_to_state('unhealthy')
            else:
                return self.finish('confused')
            

    def on_enter_healthy(self):
        response = '\n'.join([
            f'how are ways you can utilize your coping mechanisms and distance yourself from what bothers you',
            'its important to know that sometimes you cant control what others do and instead you should focus on what you can control',
        ])
        return response

    def respond_from_healthy(self,message,tags):
        response = '\n'.join([
            f'Figuring out ways to overcome stressful emotions and relationships isnt easy and cant be solved instantaneously',
            'but it is important to spend the time thinking of how to find these outlets and distance for yourself',
            'make sure to give yourself that time'
        ])

        print (response)
        return self.go_to_state('done')
        
    def on_enter_unhealthy(self):
        return 'do you think you have or can think of good ways to cope when you are struggling with this situation?' 

    def respond_from_unhealthy(self,messages,tags):
        if 'yes' in tags:
            response = '\n'.join([
            f'Figuring out ways to overcome stressful emotions and relationships isnt easy and cant be solved instantaneously',
            'but it is important to spend the time thinking of how to find these outlets and distance for yourself',
            'make sure to give yourself that time'
            ])
            print (response)
            return self.go-to_state('done')
        
        else:
            if len(self.unhealthyList) != 0:
                item = random.choice(self.unhealthyList)
                self.unhealthyList.remove(item)
                return item

            else:
                return self.go_to_state('done')

    def on_enter_doubt(self):
        return 'Do you feel happy most of the time or unhappy most of the time when you are around them?'

    def respond_from_doubt(self,messages,tags):
        if 'happy' in tags:
            return self.go_to_state('move_on')
        
        if 'bad' in tags:
            return self.go_to_state('questioning')

        else:
            return self.finish('confused')

    def on_enter_questioning(self):
        return 'Why are you putting yourself in a situation where you are often worried or unhappy?'

    def respond_from_questioning(self,messages,tags):
        if len(self.questionList) > 0:
            item = random.choice(self.questionList)
            self.questionList.remove(item)
            if len(self.questionList) == 3:
                return '\n'.join(['I can understand that. ', item])
            if len(self.questionList) == 1:
                return '\n'.join(['I see, that must be difficult. ', item])
            else:
                return item
        else:
            print('I think it\'s important to prioritize your happiness. It might be hard to know what will do that,but if you are trying things and are still not satisfied, maybe it\’s time to let the relationship go.')
            print('\n')
            return self.go_to_state('unhealthy')
        

    def on_enter_move_on(self):
        return 'Do you feel like you’ve had closure in this relationship?'

    def respond_from_move_on(self,messages,tags):
        if 'yes' in tags:
            print('\n'.join([random.choice(['You should to take more time for yourself to work through it', 'We all move on at our own pace, some of us may take a little longer',
                                  'This relationship was clearly an important part of your life. It is natural to need time to process']), ' How do you feel when you think about them?']))
            return self.go_to_state('upset')
        if 'no' in tags:
            print('Its important not to judge yourself too harshly for the things you feel or do. I think working towards getting over them would be good for you.')
            return self.go_to_state('m_advice')
        else:
            return self.finish('confused')

    def on_enter_m_advice(self):
        return 'Would you like some advice that could help you move on?'

    def respond_from_m_advice(self,messages,tags):
        if 'no' in tags:
            return self.go_to_state('done')

        if 'yes' in tags:
            if len(self.adviceList) > 0:
                item = random.choice(self.adviceList)
                self.adviceList.remove(item)
                if len(self.adviceList) > 0:
                    return '\n'.join([item, ' Do you want more advice?']) #maybe randomize varied versions of this if theres time
                else:
                    return item
            else:
                return self.go_to_state('done')
        else:
            if len(self.adviceList) > 0:
                return self.finish('confused')
            else:
                return self.go_to_state('done')
        
       
    def on_enter_done(self):
        return 'is there anything else I can help you with'

    def respond_from_done(self,messages,tags):
        if 'yes' in tags:
            print('whats troubling you')
            return self.go_to_state('waiting')
        else:
            return self.finish('thanks')
        
    def finish_thanks(self):
        """Send a message and go to the default state."""
        return "Im glad I could help, if you ever need someone to talk to I'm here."
    
    def finish_confused(self):
        """Send a message and go to the default state."""
        return "Sorry, I'm just a simple bot that can't understand much. can you try to explain again?"


if __name__ == '__main__':
    Breakup_Bot().chat()
