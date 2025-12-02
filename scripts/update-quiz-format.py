#!/usr/bin/env python3
"""
批量更新 md 文件中的 quiz 格式

将旧格式：
<base-quiz>
<base-quiz-question correct="A" id="...">
...
</base-quiz-question>
</base-quiz>

转换为新格式：
<BaseQuiz id="..." correct="A">
...
</BaseQuiz>
"""

import re
import os
from pathlib import Path


def extract_quiz_attributes(question_tag):
    """从 base-quiz-question 标签中提取 id 和 correct 属性"""
    id_match = re.search(r'id="([^"]+)"', question_tag)
    correct_match = re.search(r'correct="([^"]+)"', question_tag)
    
    quiz_id = id_match.group(1) if id_match else None
    correct = correct_match.group(1) if correct_match else None
    
    return quiz_id, correct


def convert_quiz_block(content):
    """转换单个 quiz 块"""
    # 匹配完整的 quiz 块
    pattern = r'<base-quiz>\s*<base-quiz-question\s+([^>]+)>\s*(.*?)\s*</base-quiz-question>\s*</base-quiz>'
    
    def replace_quiz(match):
        question_attrs = match.group(1)
        quiz_content = match.group(2)
        
        # 提取 id 和 correct
        quiz_id, correct = extract_quiz_attributes(question_attrs)
        
        # 构建新的 BaseQuiz 开始标签
        attrs = []
        if quiz_id:
            attrs.append(f'id="{quiz_id}"')
        if correct:
            attrs.append(f'correct="{correct}"')
        
        base_quiz_start = f'<BaseQuiz {" ".join(attrs)}>'
        
        # 转换内容
        # 移除 template #question 周围的空白（如果有）
        quiz_content = quiz_content.strip()
        
        # 转换 base-quiz-option 为 BaseQuizOption
        quiz_content = re.sub(
            r'<base-quiz-option\s+([^>]+)>(.*?)</base-quiz-option>',
            lambda m: convert_option(m.group(1), m.group(2)),
            quiz_content,
            flags=re.DOTALL
        )
        
        # 转换 base-quiz-answer 为 BaseQuizAnswer，移除 value 属性
        quiz_content = re.sub(
            r'<base-quiz-answer\s+value="[^"]+"\s*>(.*?)</base-quiz-answer>',
            r'<BaseQuizAnswer>\1</BaseQuizAnswer>',
            quiz_content,
            flags=re.DOTALL
        )
        
        # 如果没有 value 属性，也处理
        quiz_content = re.sub(
            r'<base-quiz-answer\s*>(.*?)</base-quiz-answer>',
            r'<BaseQuizAnswer>\1</BaseQuizAnswer>',
            quiz_content,
            flags=re.DOTALL
        )
        
        return f'{base_quiz_start}\n{quiz_content}\n</BaseQuiz>'
    
    return re.sub(pattern, replace_quiz, content, flags=re.DOTALL)


def convert_option(attrs, content):
    """转换 base-quiz-option 为 BaseQuizOption"""
    # 提取 value 和 correct
    value_match = re.search(r'value="([^"]+)"', attrs)
    correct_match = re.search(r'\bcorrect\b', attrs)
    
    value = value_match.group(1) if value_match else ''
    has_correct = correct_match is not None
    
    # 构建新标签
    new_attrs = f'value="{value}"'
    if has_correct:
        new_attrs += ' correct'
    
    return f'<BaseQuizOption {new_attrs}>{content}</BaseQuizOption>'


def process_file(file_path):
    """处理单个文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        content = convert_quiz_block(content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    """主函数"""
    # 查找所有 md 文件
    docs_dir = Path(__file__).parent.parent / 'docs'
    
    md_files = []
    for pattern in ['**/*.md']:
        md_files.extend(docs_dir.rglob(pattern))
    
    print(f"Found {len(md_files)} markdown files")
    
    updated_count = 0
    for md_file in md_files:
        if process_file(md_file):
            print(f"Updated: {md_file.relative_to(docs_dir.parent)}")
            updated_count += 1
    
    print(f"\nTotal files updated: {updated_count}")


if __name__ == '__main__':
    main()

