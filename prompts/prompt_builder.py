'''
  this is a dispatcher script which will automatically dispatch the 
  template as per the use case. 
'''

from prompts.template.zero_shot import ZeroShotPrompt

class PromptBuilder:

    @staticmethod
    def build(prompt_type:str, user_prompt:str)->str:
        if prompt_type == 'Zero Shot':
            return ZeroShotPrompt.build(user_prompt)
        raise ValueError(f"No such {prompt_type} prompt")