# from .llm import *
from .llm.qwen import Qwen
from config.model_config import LLM_MODEL_DICT


def get_llm_cls(llm_type):
    if llm_type == "qwen":
        return Qwen  # 这里从.llm.qwen初始化了一个Qwen
    # elif llm_type == 'baichuan':
    #     return Baichuan
    # elif llm_type == 'chatglm':
    #     return ChatGLM
    # elif llm_type == 'test':
    #     return TestLM
    else:
        raise ValueError(f"Invalid llm_type {llm_type}")


class LLMFactory:

    @staticmethod
    def build_llm(model_name, additional_cfg):
        cfg = LLM_MODEL_DICT.get(
            model_name, {"type": "test"}
        )  # 如果 model_name 不存在，则使用默认配置 {'type': 'test'}
        cfg.update(additional_cfg)  # 然后将 additional_cfg 字典合并到配置字典中
        llm_type = cfg.pop("type")  # 从配置字典中取出 'type' 键对应的值
        llm_cls = get_llm_cls(llm_type)
        llm_cfg = cfg
        return llm_cls(cfg=llm_cfg)
