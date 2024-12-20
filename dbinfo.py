def read_database_information(path: str) -> dict[str, any]:
    file = open(path, "rb")
    page = file.read(4096)

    info = {
        "magic_string": page[:16],
        "page_size": int.from_bytes(page[16: 18]),
        "write_format": int.from_bytes(page[18: 19]),
        "read_format": int.from_bytes(page[19: 20]),
        "reserved_bytes": int.from_bytes(page[20: 21]),
        "max_payload": int.from_bytes(page[21: 22]),  #ignore
        "min_paylaod": int.from_bytes(page[22: 23]),  #ignore
        "leaf_payload": int.from_bytes(page[23: 24]), #ignore
        "file_change_counter": int.from_bytes(page[24: 28]),  #unexpected
        "database_size_in_page": int.from_bytes(page[28: 32]),
        "freelist_page_count": int.from_bytes(page[32: 36]),
        "total_freelist_pages_count": int.from_bytes(page[36: 40]),
        "schema_cookie": int.from_bytes(page[40: 44]),
        "schema_format": int.from_bytes(page[44: 48]),
        "default_cache_size": int.from_bytes(page[48: 52]),
        "largest_root_btree_page": int.from_bytes(page[52: 56]),
        "text_encoding": int.from_bytes(page[56: 60]),
        "user_version": int.from_bytes(page[60: 64]),
        "incremental_vacuum": int.from_bytes(page[64: 68]),
        "application_id": int.from_bytes(page[68: 72]),
        "reserved_for_expansion": int.from_bytes(page[72: 92]),
        "version_valid_for": int.from_bytes(page[92: 96]),
        "sqlite_version_number": int.from_bytes(page[96: 100]),
        "number of tables": page.count(b"CREATE TABLE")
    }

    file.close()

    return info


if __name__ == "__main__":
    for key, val in read_database_information("database.db").items():
        print(key, '\t', val)