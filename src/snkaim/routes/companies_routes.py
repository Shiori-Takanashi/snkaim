from flask import Blueprint, render_template, request

from snkaim.services.companies_service import get_pagination


companies_bp = Blueprint("companies", __name__, url_prefix="/companies")


@companies_bp.route("/")
def company_list():
    pagination = get_pagination(
        request.args.get("total_companies", 50, type=int),
        request.args.get("page", 1, type=int),
        request.args.get("per_page", 10, type=int),
    )
    return render_template("companies.html", pagination=pagination)
