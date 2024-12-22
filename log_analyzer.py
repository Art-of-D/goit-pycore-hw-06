import argparse

def parse_log_line(line: str) -> dict:
    """Парсить рядок логу на складові."""
    parts = line.split()
    return {
        "timestamp": " ".join(parts[:2]),
        "level": parts[2],
        "message": " ".join(parts[3:])
    }

def load_logs(file_path: str) -> list:
    """Завантажує логи з файлу."""
    with open(file_path, 'r') as f:
        return [parse_log_line(line) for line in f]

def filter_logs_by_level(logs: list, level: str) -> list:
    """Фільтрує логи за рівнем."""
    return [log for log in logs if log["level"] == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    """Підраховує записи за рівнем."""
    counts = {}
    for log in logs:
        counts[log["level"]] = counts.get(log["level"], 0) + 1
    return counts

def display_log_counts(counts: dict):
    """Виводить результати у вигляді таблиці."""
    print("Рівень\tКількість")
    for level, count in counts.items():
        print(f"{level}\t{count}")

def main():
    parser = argparse.ArgumentParser(description="Аналіз лог-файлів")
    parser.add_argument("log_file", help="Шлях до лог-файлу")
    parser.add_argument("level", nargs="?", help="Фільтрувати логи за рівнем")
    args = parser.parse_args()

    log = load_logs(args.log_file)

    if args.level:
        filtered_logs = filter_logs_by_level(log, args.level)
        counts = count_logs_by_level(filtered_logs)
    else:
        counts = count_logs_by_level(log)

    display_log_counts(counts)

if __name__ == "__main__":
    main()