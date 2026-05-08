from dataclasses import dataclass, field


@dataclass
class Company:
    index: int
    name: str


@dataclass
class Pagination:
    total_companies: int
    requested_page: int
    per_page: int
    companies: list[Company] = field(default_factory=list)

    @property
    def total_pages(self) -> int:
        if self.total_companies == 0:
            return 0
        return (self.total_companies + self.per_page - 1) // self.per_page

    @property
    def current_page(self) -> int:
        if self.requested_page < 1:
            return 1
        if self.total_pages > 0 and self.requested_page > self.total_pages:
            return self.total_pages
        return self.requested_page

    @property
    def has_prev(self) -> bool:
        return self.current_page > 1

    @property
    def has_next(self) -> bool:
        return self.current_page < self.total_pages

    @property
    def start_index(self) -> int:
        """このページで必要なデータの開始位置"""
        if self.total_companies == 0:
            return 0
        return (self.current_page - 1) * self.per_page + 1

    @property
    def end_index(self) -> int:
        """このページで必要なデータの終了位置"""
        if self.total_companies == 0:
            return 0
        return min(self.current_page * self.per_page, self.total_companies)


def get_companies(start: int, end: int) -> list[Company]:
    """ダミーデータの取得処理"""
    if start == 0 and end == 0:
        return []
    return [
        Company(index=i, name=f"company_of_{i}") for i in range(start, end + 1)
    ]


def get_pagination(
    total_companies: int, requested_page: int, per_page: int
) -> Pagination:
    """ページネーションの構築とデータ取得を調整するサービス関数"""
    # 1. ページネーションの計算枠だけを生成（データは空）
    pagination = Pagination(
        total_companies=total_companies,
        requested_page=requested_page,
        per_page=per_page,
    )

    # 2. オブジェクト自身に計算させたインデックスを使ってデータを取得し、格納
    pagination.companies = get_companies(
        pagination.start_index, pagination.end_index
    )

    return pagination
