from dataclasses import dataclass


@dataclass
class Item:
    id: int
    name: str


@dataclass
class PaginationData:
    items: list[Item]
    page: int
    per_page: int
    total_count: int
    total_pages: int

    # デフォルト値を設定したり、プロパティ化することも可能です
    @property
    def has_prev(self) -> bool:
        return self.page > 1

    @property
    def has_next(self) -> bool:
        return self.page < self.total_pages


def get_paginated_items(page: int, per_page: int) -> PaginationData:
    # ダミーデータ生成
    # 辞書ではなく Item クラスのインスタンスを作成します
    all_items = [Item(id=i, name=f"アイテム {i}") for i in range(1, 106)]

    total_count = len(all_items)
    total_pages = (total_count + per_page - 1) // per_page

    if page < 1:
        page = 1
    elif page > total_pages and total_pages > 0:
        page = total_pages

    offset = (page - 1) * per_page
    items = all_items[offset : offset + per_page]

    # PaginationData クラスのインスタンスを返す
    return PaginationData(
        items=items,
        page=page,
        per_page=per_page,
        total_count=total_count,
        total_pages=total_pages,
    )
