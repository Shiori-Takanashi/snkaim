from flask import Blueprint, render_template, request

from ..services.items import get_paginated_items


items_bp = Blueprint("items", __name__, url_prefix="/items")


@items_bp.route("/")
def list_items():
    page = request.args.get("page", 1, type=int)
    per_page = 12

    pagination_data = get_paginated_items(page, per_page)

    return render_template("items.html", pagination=pagination_data)
