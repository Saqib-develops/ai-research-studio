'''
 zero shot prompt template
 - Interface prompt
 - this interface will be constant for all prompt template
'''

class ZeroShotPrompt():

    @staticmethod
    def build(user_prompt:str) -> str:
        return user_prompt