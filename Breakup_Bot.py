from chatbot import ChatBot
import random


class Breakup_Bot(ChatBot):
    """A chatbot that offers help with a breakup"""

    upsetConf = 0
    moveOnConf = 0
    doubtConf = 0
    adviceConf = 0
    careConf = 0

    waitCount = 0

    
    STATES = [
        'waiting',
        'generic',
        'healthy',
        'unhealthy',
        'move_on',
        'upset',
        'doubt',
        'questioning',
        'insecure',
        'done',
        'm_advice',
        'self_care'
    ]

    PROMPT = [
        'How does the situation make you feel?',
        'Why is the situation a problem?',
        'What do you do when you feel that way?',
        'Can you tell me more about it?',
        'Can you elaborate?',
        "What's your thought process when this happens?"
        ]


    upsetList = [
        'Do you think you have a healthy way to express that feeling?',
        "Is it internal or do you think it’s from the situation?",
        "Does that work well for you? Do you feel like it’s healthy?"
        ]

    unhealthyList = [
        'Outside of this situation, what do you do when you feel this emotion?',
        'Trying to distance yourself from what triggers you can prevent falling into unhealthy patterns. How can you try to remove yourself from the situation?',
        ]

    adviceList = ["You should make sure you reclaim the things of yours that they have, so you won't feel dependent on them.",
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
        "can't forget them": 'love',
        'keep thinking about them': 'love',
        'i love': 'love',
        'move on': 'love',
        'get over': 'love',
        'not over': 'love',

        'frustrated': 'bad',
        'angry': 'bad',
        'annoying': 'bad',
        'annoyed': 'bad',
        'bothering me': 'bad',
        'upset': 'bad',
        'driving me crazy': 'bad',
        'uncomfortable': 'bad',
        'anxious': 'bad',
        'sad': 'bad',
        'badly': 'bad',
        'not great': 'bad',
        'hurts': 'bad',
        'pisses me off': 'bad',
        'pissed': 'bad',
        'unhappy': 'bad',
        'worried': 'bad',
        'upset': 'bad',
        'anxiety': 'bad',
        'stress': 'bad',
        'stressed': 'bad',
        'mad': 'bad',
        'sad' : 'bad',
        'lonely': 'bad',
        'worthless': 'bad',
        'felt bad': 'bad',
        'feel bad': 'bad',
        'feels bad': 'bad',
        'i feel okay': 'bad',
        'i felt okay': 'bad',
        'i felt ok': 'bad',
        'i feel ok': 'bad',
        'cry' : 'bad',
        'crying' : 'bad',
        'scream': 'bad',
        'yell' : 'bad',

        'better': 'better',
        'i have healthy':'better',
        'i think i have healthy':'better',
        'good': 'worse',
        'worse': 'worse',
        'the same': 'worse',
        'bad': 'worse',
        "dont have healthy": 'worse',
        "don't have healthy": 'worse',
        "dont think i have healthy": 'worse',
        "don't think i have healthy": 'worse',

        'am happy': 'happy',
        'was happy': 'happy',
        'i feel happy': 'happy',
        'i felt happy': 'happy',
        'i feel good': 'happy',
        'pretty good': 'happy',
        'i felt good': 'happy',


        'regret': 'unsure',
        'unsure': 'unsure',
        'i dont know': 'unsure',
        "i don't know": 'unsure',
        'not sure': 'unsure',
        'confused': 'unsure',
        'lost': 'unsure',
        'mistake': 'unsure',

        'never find love' : 'insecure',
        'unlovable' : 'insecure',
        'forever alone' : 'insecure',
        'lonely forever' : 'insecure',
        'alone forever' : 'insecure',
        'single forever' : 'insecure',
        'am ugly' : 'insecure',
        'am so ugly' : 'insecure',
        'im ugly' : 'insecure',
        "i'm ugly" : 'insecure',
        'im so ugly' : 'insecure',
        "i'm so ugly" : 'insecure',
        'am stupid' : 'insecure',
        'am so stupid' : 'insecure',
        'im stupid' : 'insecure',
        'im so stupid' : 'insecure',
        "i'm stupid" : 'insecure',
        "i'm so stupid" : 'insecure',
        'am dumb' : 'insecure',
        'am so dumb' : 'insecure',
        'im dumb' : 'insecure',
        'im so dumb' : 'insecure',
        "i'm dumb" : 'insecure',
        "i'm so dumb" : 'insecure',
        'feel stupid' : 'insecure',
        'feel so stupid' : 'insecure',
        'feel dumb' : 'insecure',
        'feel so dumb' : 'insecure',
        'feel ugly' : 'insecure',
        'feel so ugly' : 'insecure',
        'cant believe i' : 'insecure',
        "can't believe i" : 'insecure',
        'can not believe i' : 'insecure',
        'hate myself' : 'insecure',
        'replaceable' : 'insecure',
        
        
        #yes and no
        
        'im good':'no',
        "i'm good":'no',
        'nope': 'no',
        'i dont think': 'no',
        "i don't think": 'no',
        'not really': 'no',
        'not necessarily': 'no',
        'not particularly': 'no',
        'guess not':'no',
        'no': 'no',
        'nah': 'no',
        'i dont know': 'no',
        "i don't know": 'no',
        
        'yes': 'yes',
        'yea': 'yes',
        'yeah': 'yes',
        'yee': 'yes',
        'yas': 'yes',
        'yuh': 'yes',
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


    def respond_from_waiting(self, message, tags):
        self.waitCount += 1
        if self.waitCount == 1:
            
            return '\n'.join(["Hi I'm the breakup chatbot: made for your breakup problems!", self.finish('continue')])

        if 'love' in tags:
            return self.go_to_state('move_on')
        elif 'insecure' in tags:
            return self.go_to_state('insecure')
        elif 'bad' in tags:
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
        elif 'insecure' in tags:
            return self.go_to_state('insecure')
        elif 'bad' in tags:
            return self.go_to_state('upset')
        elif 'unsure' in tags:
            return self.go_to_state('doubt')
        else:
            return self.go_to_state('generic')

    def on_enter_upset(self):
        response = '\n'.join([
            f'I can understand how you would feel that way.',
            'What do you do when that feeling arises,',
            'and how do you feel after?',
        ])
        return response


    def respond_from_upset(self,message,tags):
        if len(self.upsetList) != 0:
            item = random.choice(self.upsetList)
            self.upsetList.remove(item)
            return item
        else:
            if 'better' or 'happy' in tags:
                return self.go_to_state('healthy')
            elif 'worse' or 'bad' in tags:
                return self.go_to_state('unhealthy')
            else:
                if self.upsetConf < 1:
                    self.upsetConf += 1
                    return '\n'.join(["I'm sorry, I'm not sure I understand. Can you try explaining again?", self.go_to_state('upset')])
                else:
                    self.upsetConf = 0
                    return self.finish('confused')
            

    def on_enter_healthy(self):
        response = '\n'.join([
            f'What are ways you can utilize your coping mechanisms and distance yourself from what bothers you?',
            "It's important to know that sometimes you can't control what others do and instead you should focus on what you can control."
        ])
        return response

    def respond_from_healthy(self,message,tags):
        response = '\n'.join([
            f"Figuring out ways to overcome stressful emotions and relationships isn't easy and can't be solved instantaneously,",
            'but it is important to spend the time thinking of how to find these outlets and distance for yourself.',
            'Make sure to give yourself that time.'
        ])
        return '\n'.join([response,  '\n', self.go_to_state('done')])
        
    def on_enter_unhealthy(self):
        return 'Do you think you have or can think of good ways to cope when you are struggling with this situation?' 

    def respond_from_unhealthy(self,messages,tags):
        if 'yes' in tags:
            response = '\n'.join([
            f"Figuring out ways to overcome stressful emotions and relationships isn't easy and can't be solved instantaneously,",
            'but it is important to spend the time thinking of how to find healthy outlets and distance for yourself.',
            'Make sure to give yourself that time and make sure that you are safe. that should be your priority.'
            ])
            return '\n'.join([response, '\n', self.go_to_state('done')])
        
        else:
            if len(self.unhealthyList) != 0:
                item = random.choice(self.unhealthyList)
                self.unhealthyList.remove(item)
                return item

            else:
                return self.go_to_state('done')

    def on_enter_insecure(self):
        return 'Why do you think that?'

    def respond_from_insecure(self,messages,tags):
        return '\n'.join(["That does sound awful. But the future is filled with so much opportunity. I know you’re dealing with this now. But it's not forever.",  '\n', self.go_to_state('self_care')])

    def on_enter_self_care(self):
        return 'Would you like some ideas that could help you work on appreciating yourself?'

    def respond_from_self_care(self,messages,tags):
        if 'no' in tags:
            return '\n'.join(["I'm sorry you are dealing with this.", '\n', self.go_to_state('unhealthy')])
            
        if 'yes' in tags:
            return '\n'.join(['Maybe instead of focusing on a relationship, you could use this as an opportunity to learn how to love yourself. That will make you more happy long term.',
                              "One thing that helps me is to try to list one thing I like about myself everyday. Even if they're little things.", '\n',self.go_to_state('done')])
        else:
            if self.careConf < 1:
                self.careConf += 1
                return '\n'.join(["Could you repeat that? I didn't quite grasp what you were saying.", self.go_to_state('self_care') ])
            else:
                self.careConf = 0
                return self.finish('confused')


    def on_enter_doubt(self):
        return 'Do you feel happy most of the time or unhappy most of the time when you are around them?'

    def respond_from_doubt(self,messages,tags):
        if 'happy' in tags:
            return self.go_to_state('move_on')
        
        if 'bad' in tags:
            return self.go_to_state('questioning')

        else:
            if self.doubtConf < 1:
                self.doubtConf += 1
                return '\n'.join(["I'm a little lost, sorry. Could you rephrase that?", self.go_to_state('doubt')])
            else:
                self.doubtConf = 0
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
            return '\n'.join(["I think it's important to prioritize your happiness. It might be hard to know what will do that, but if you are trying things and are still not satisfied, maybe it's time to let the relationship go.", '\n', self.go_to_state('unhealthy')])
        

    def on_enter_move_on(self):
        return "Do you feel like you’ve had closure in this relationship?"

    def respond_from_move_on(self,messages,tags):
        if 'yes' in tags:
            return '\n'.join([random.choice(['You should to take more time for yourself to work through it', 'We all move on at our own pace, some of us may take a little longer',
                                  'This relationship was clearly an important part of your life. It is natural to need time to process']), ' How do you feel when you think about them?', '\n', self.go_to_state('upset')])
        if 'no' in tags:
            return '\n'.join(["It's important not to judge yourself too harshly for the things you feel or do. I think working towards getting over them would be good for you.", '\n', self.go_to_state('m_advice')])
        else:
            if self.moveOnConf < 1:
                    self.moveOnConf += 1
                    return '\n'.join(['What exactly do you mean by that? I am a little confused.', self.go_to_state('move_on')])
            else:
                self.moveOnConf = 0
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
                    return '\n'.join([item, ' Do you want more advice?'])
                else:
                    return item
            else:
                return self.go_to_state('done')
        else:
            if len(self.adviceList) > 0:
                if self.adviceConf < 1:
                    self.adviceConf += 1
                    return '\n'.join(["I'm not sure what you are trying to say. Could you explain it a little differently?", self.go_to_state('m_advice')])
                else:
                    self.adviceConf = 0
                    return self.finish('confused')
            else:
                return self.go_to_state('done')
        
       
    def on_enter_done(self):
        return 'Is there anything else I can help you with?'

    def respond_from_done(self,messages,tags):
        if 'yes' in tags:
            return self.finish('continue')
        else:
            return self.finish('thanks')

    def finish_continue(self):
        upsetConf = 0
        moveOnConf = 0
        doubtConf = 0
        adviceConf = 0
        careConf = 0
        return "What's troubling you?"
        
    def finish_thanks(self):
        """Send a message and go to the default state."""
        waitCount = 0
        
        upsetConf = 0
        moveOnConf = 0
        doubtConf = 0
        adviceConf = 0
        careConf = 0
        
        return "I'm glad I could help, if you ever need someone to talk to I'm here."
    
    def finish_confused(self):
        """Send a message and go to the default state."""
        return "Sorry, I'm just a simple bot that can't understand much. Can you try to explain again?"


if __name__ == '__main__':
    Breakup_Bot().chat()
