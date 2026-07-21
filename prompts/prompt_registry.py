from prompts.template.ZeroShot import ZeroShotPrompt
from prompts.template.OneShot import OneShotPrompt
from prompts.template.FewShot import FewShotPrompt

PROMPT_REGISTRY = {
    "zero_shot": ZeroShotPrompt(),
    "one_shot": OneShotPrompt(),
    "few_shot": FewShotPrompt()
}