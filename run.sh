#!/bin/bash

# 这里可以放入代码运行命令
echo "program start..."
cd /app
python agent_predict.py \
    --question_file_path 'data/question.json' \
    --answer_file_path 'data/answer.jsonl' \
    --random_seed 47