from flask import Blueprint, render_template


home_bp = Blueprint("home", __name__)


@home_bp.get("/")
def home():
    page_title = "Jinja2 サンプルページ"
    description = "ループと条件分岐を含むHTMLテンプレートの例である。"

    user = {
        "name": "Taro",
        "is_admin": False,
        "is_active": True,
    }

    articles = [
        {
            "title": "Flaskの基本",
            "summary": "Flaskでルーティングとテンプレートを扱う。",
            "is_published": True,
            "tags": ["Flask", "Python", "SSR"],
            "updated_at": "2026-05-06",
        },
        {
            "title": "Jinja2の条件分岐",
            "summary": "if文を使って表示内容を切り替える。",
            "is_published": False,
            "tags": ["Jinja2", "Template"],
            "updated_at": None,
        },
        {
            "title": "Bootstrapのカード表示",
            "summary": "カードUIで一覧を整える。",
            "is_published": True,
            "tags": [],
            "updated_at": "2026-05-01",
        },
    ]

    categories = [
        {"name": "Python", "count": 5},
        {"name": "HTML", "count": 2},
        {"name": "未分類", "count": 0},
    ]

    messages = [
        {
            "level": "success",
            "text": "ページを正常に読み込んだ。",
        },
        {
            "level": "warning",
            "text": "一部の記事は下書き状態である。",
        },
    ]

    return render_template(
        "home.html",
        page_title=page_title,
        description=description,
        user=user,
        articles=articles,
        categories=categories,
        messages=messages,
    )
