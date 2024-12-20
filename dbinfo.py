def read_database_information(path: str) -> dict[str, any]:
    file = open(path, "rb")

    info = {
        "magic_string": file.read(16),
        "page_size": int.from_bytes(file.read(2)),
        "write_format": int.from_bytes(file.read(1)),
        "read_format": int.from_bytes(file.read(1)),
        "reserved_bytes": int.from_bytes(file.read(1)),
        "max_payload": int.from_bytes(file.read(1)),  #ignore
        "min_paylaod": int.from_bytes(file.read(1)),  #ignore
        "leaf_payload": int.from_bytes(file.read(1)), #ignore
        "file_change_counter": int.from_bytes(file.read(4)),  #unexpected
        "database_size_in_page": int.from_bytes(file.read(4)),
        "freelist_page_count": int.from_bytes(file.read(4)),
        "total_freelist_pages_count": int.from_bytes(file.read(4)),
        "schema_cookie": int.from_bytes(file.read(4)),
        "schema_format": int.from_bytes(file.read(4)),
        "default_cache_size": int.from_bytes(file.read(4)),
        "largest_root_btree_page": int.from_bytes(file.read(4)),
        "text_encoding": int.from_bytes(file.read(4)),
        "user_version": int.from_bytes(file.read(4)),
        "incremental_vacuum": int.from_bytes(file.read(4)),
        "application_id": int.from_bytes(file.read(4)),
        "reserved_for_expansion": int.from_bytes(file.read(20)),
        "version_valid_for": int.from_bytes(file.read(4)),
        "sqlite_version_number": int.from_bytes(file.read(4))
    }

    file.close()

    return info


if __name__ == "__main__":
    for key, val in read_database_information("database.db").items():
        print(key, '\t', val)