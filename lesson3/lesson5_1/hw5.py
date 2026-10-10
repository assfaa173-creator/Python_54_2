
import csv
import json


#  1.  ID

def save_test_ids(test_ids):
    with open("tests.txt", "w", encoding="utf-8") as file:
        for test_id in test_ids:
            file.write(test_id + "\n")


def add_test_id(test_id):
    with open("tests.txt", "a", encoding="utf-8") as file:
        file.write(test_id + "\n")


def load_test_ids(filename):
    test_ids = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            test_id = line.strip()

            if test_id:
                test_ids.append(test_id)

    return test_ids



save_test_ids(["QA-1001", "QA-1002", "QA-1003"])
add_test_id("QA-1004")

print("Test IDs:")
print(load_test_ids("tests.txt"))


# 2.  CSV

def get_test_statistics(filename):
    total = 0
    passed = 0
    failed = 0
    total_duration_ms = 0
    failed_ids = []

    with open(filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += 1

            if row["status"] == "PASSED":
                passed += 1

            if row["status"] == "FAILED":
                failed += 1
                failed_ids.append(row["test_id"])

            total_duration_ms += int(row["duration_ms"])

    result = {
        "total": total,
        "passed": passed,
        "failed": failed,
        "total_duration_ms": total_duration_ms,
        "failed_ids": failed_ids
    }

    return result


print("\nTest statistics:")
print(get_test_statistics("results.csv"))


# 3. JSON

def save_test_config(environment, base_url, timeout):
    config = {
        "environment": environment,
        "base_url": base_url,
        "timeout": timeout
    }

    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)


def load_test_config(filename):
    with open(filename, "r", encoding="utf-8") as file:
        config = json.load(file)

    return config

save_test_config("staging", "https://example.com", 30)

config = load_test_config("config.json")

print("\nTest config:")
print(config)

assert type(config["timeout"]) == int
print("Timeout type:", type(config["timeout"]))


#  4.

from pathlib import Path


def build_run_report(project_name, csv_filename):
    total = 0
    passed = 0
    failed = 0
    total_duration_ms = 0
    failed_ids = []

    with open(csv_filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += 1
            total_duration_ms += int(row["duration_ms"])

            if row["status"] == "PASSED":
                passed += 1
            elif row["status"] == "FAILED":
                failed += 1
                failed_ids.append(row["test_id"])

    report_dir = Path("reports") / project_name
    report_dir.mkdir(parents=True, exist_ok=True)

    summary = {
        "project": project_name,
        "total": total,
        "passed": passed,
        "failed": failed,
        "total_duration_ms": total_duration_ms
    }

    with open(report_dir / "summary.json", "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    with open(report_dir / "failed_tests.txt", "w", encoding="utf-8") as file:
        for test_id in failed_ids:
            file.write(test_id + "\n")

    return summary


print("\nQA report:")
print(build_run_report("Shop", "results.csv"))

