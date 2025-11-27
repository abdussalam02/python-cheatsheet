#!/usr/bin/env python3
"""
从 Unsplash 下载随机图片并更新所有 blog 文章的头图
"""
import os
import re
import random
import requests
import time
from pathlib import Path
from typing import Dict, List, Optional

# Unsplash API 配置
UNSPLASH_API_BASE = "https://api.unsplash.com"
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")
UNSPLASH_SECRET_KEY = os.getenv("UNSPLASH_SECRET_KEY")

# 图片尺寸（适合社交媒体分享）
IMAGE_WIDTH = 1200
IMAGE_HEIGHT = 630

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent
BLOG_DIR = PROJECT_ROOT / "docs" / "blog"
PUBLIC_BLOG_DIR = PROJECT_ROOT / "public" / "blog"

# 文章名称到图片文件名的映射
ARTICLE_IMAGE_MAP = {
    "python-3-14-breaking-free-from-gil": "python-gil.jpg",
    "python-comprehensions-step-by-step": "python-comprehensions.png",
    "python-data-types": "python-data-types.jpg",
    "python-decorators-for-beginners": "python-decorators.jpg",
    "python-easy-args-kwargs": "kwargs.jpg",
    "python-pathlib-essentials": "path-lib-essentials.jpg",
    "python-projects-with-poetry-and-vscode-part-1": "poetry-1.jpg",
    "python-projects-with-poetry-and-vscode-part-2": "poetry-2.jpg",
    "python-projects-with-poetry-and-vscode-part-3": "poetry-3.jpg",
    "python-sets-what-why-how": "sets.jpg",
    "python-uv-package-manager": "python-uv-package-manager.jpg",
}

# 语言列表
LANGUAGES = ["en", "de", "es", "fr", "ja", "ko", "pt", "ru", "zh"]


def get_random_photo_url(query: Optional[str] = None) -> Optional[str]:
    """从 Unsplash API 获取随机图片的下载 URL"""
    if not UNSPLASH_ACCESS_KEY:
        raise ValueError("UNSPLASH_ACCESS_KEY 环境变量未设置")

    headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}

    params = {"orientation": "landscape"}

    if query:
        params["query"] = query

    try:
        response = requests.get(
            f"{UNSPLASH_API_BASE}/photos/random",
            headers=headers,
            params=params,
            timeout=30,
        )
        response.raise_for_status()

        photo_data = response.json()

        # 使用 API 返回的 urls 对象中的 URL
        urls = photo_data.get("urls", {})
        if not urls:
            print("API 响应中未找到 urls 对象")
            print(f"响应数据：{photo_data}")
            return None

        # 获取基础图片 URL（优先使用 raw，因为它通常最大）
        base_url = urls.get("raw") or urls.get("full") or urls.get("regular")
        if not base_url:
            print("API 响应中未找到有效的图片 URL")
            return None

        # 使用 Unsplash 图片服务的参数来调整尺寸，避免图像被拉伸
        # fit=crop 会保持宽高比并裁剪到指定尺寸，不会拉伸变形
        # 如果 URL 已经有参数，使用 & 连接，否则使用 ?
        separator = "&" if "?" in base_url else "?"
        image_url = (
            f"{base_url}{separator}w={IMAGE_WIDTH}&h={IMAGE_HEIGHT}"
            f"&fit=crop&auto=format&q=80"
        )

        return image_url
    except requests.exceptions.HTTPError as e:
        print(f"HTTP 错误：{e}")
        if hasattr(e.response, "text"):
            print(f"响应内容：{e.response.text[:200]}")
        return None
    except Exception as e:
        print(f"获取随机图片失败：{e}")
        return None


def download_image(url: str, save_path: Path) -> bool:
    """从 URL 下载图片并保存到指定路径

    注意：URL 应该已经包含 Unsplash 的尺寸参数（w, h, fit=crop），
    这样可以避免图像被拉伸变形。Unsplash 会自动处理图片裁剪和尺寸调整。
    """
    try:
        print(f"正在下载：{url}")
        response = requests.get(url, timeout=30, allow_redirects=True)
        response.raise_for_status()

        # 确保目录存在
        save_path.parent.mkdir(parents=True, exist_ok=True)

        # 直接保存图片（Unsplash 已经通过 URL 参数处理了尺寸和裁剪）
        with open(save_path, "wb") as f:
            f.write(response.content)

        print(f"已保存：{save_path}")
        return True

    except Exception as e:
        print(f"下载失败 {url}: {e}")
        return False


def update_markdown_file(file_path: Path, old_image: str, new_image: str) -> bool:
    """更新 markdown 文件中的图片路径"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 替换 frontmatter 中的 socialImage
        content = re.sub(
            rf"socialImage:\s*{re.escape(old_image)}",
            f"socialImage: {new_image}",
            content,
        )

        # 替换 route meta 中的 socialImage
        content = re.sub(
            rf"socialImage:\s*{re.escape(old_image)}",
            f"socialImage: {new_image}",
            content,
        )

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"已更新：{file_path}")
        return True
    except Exception as e:
        print(f"更新失败 {file_path}: {e}")
        return False


def get_article_name_from_file(file_path: Path) -> str:
    """从文件路径提取文章名称"""
    return file_path.stem


def main():
    """主函数"""
    print("开始下载 blog 文章头图...")
    print(f"项目根目录：{PROJECT_ROOT}")
    print(f"Blog 目录：{BLOG_DIR}")
    print(f"Public Blog 目录：{PUBLIC_BLOG_DIR}")

    # 确保目录存在
    PUBLIC_BLOG_DIR.mkdir(parents=True, exist_ok=True)

    # 检查环境变量
    if not UNSPLASH_ACCESS_KEY:
        print("错误：UNSPLASH_ACCESS_KEY 环境变量未设置")
        return

    # 为每篇文章下载新图片
    downloaded_images = {}

    # 使用不同的搜索关键词来获取不同主题的图片
    # 注意：避免使用 "python" 关键词，因为它可能返回蛇的图片
    keywords = [
        "technology",
        "code",
        "programming",
        "computer",
        "laptop",
        "development",
        "software",
        "digital",
        "innovation",
        "coding",
        "tech",
        "developer",
        "code editor",
        "computer science",
        "algorithm",
        "data",
        "web development",
        "software engineering",
        "computer programming",
        "coding workspace",
    ]

    # 只更新 python-decorators-for-beginners 这一篇文章
    target_article = "python-decorators-for-beginners"
    
    if target_article not in ARTICLE_IMAGE_MAP:
        print(f"错误：未找到文章 '{target_article}'")
        return
    
    image_filename = ARTICLE_IMAGE_MAP[target_article]
    image_path = PUBLIC_BLOG_DIR / image_filename

    # 随机选择关键词
    keyword = random.choice(keywords)
    print(f"\n为文章 '{target_article}' 获取图片 (关键词：{keyword})...")

    # 从 Unsplash API 获取随机图片 URL
    photo_url = get_random_photo_url(query=keyword)

    if photo_url and download_image(photo_url, image_path):
        downloaded_images[target_article] = image_filename
    else:
        print(f"跳过文章 '{target_article}'，下载失败")
        return

    print(f"\n成功下载 {len(downloaded_images)} 张图片")

    # 更新所有语言版本的 markdown 文件
    print("\n开始更新 markdown 文件...")

    updated_count = 0
    for lang in LANGUAGES:
        lang_dir = BLOG_DIR / lang
        if not lang_dir.exists():
            print(f"跳过不存在的语言目录：{lang_dir}")
            continue

        for article_name, image_filename in downloaded_images.items():
            md_file = lang_dir / f"{article_name}.md"
            if not md_file.exists():
                print(f"文件不存在：{md_file}")
                continue

            # 读取文件以获取旧的图片路径
            try:
                with open(md_file, "r", encoding="utf-8") as f:
                    content = f.read()

                # 查找旧的 socialImage
                match = re.search(r"socialImage:\s*(/blog/[^\s]+)", content)
                if match:
                    old_image = match.group(1)
                    new_image = f"/blog/{image_filename}"

                    if update_markdown_file(md_file, old_image, new_image):
                        updated_count += 1
                else:
                    print(f"未找到 socialImage 字段：{md_file}")
            except Exception as e:
                print(f"处理文件失败 {md_file}: {e}")

    print(f"\n完成！已更新 {updated_count} 个文件")


if __name__ == "__main__":
    main()
