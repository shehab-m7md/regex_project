import re
import csv

class FileReader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> str:
        
        with open(self.file_path, "r", encoding="utf-8") as f:
                return f.read()
       


class PatternExtractor:
    def __init__(self, patterns: list[dict]):
        self.patterns = patterns

    def extract(self, text: str) -> list[dict]:
        
        results = []

        for p in self.patterns:
            for match in re.finditer(p["regex"], text):
                start= match.start()

                line_num = text.count("\n", 0, start) + 1
                last_newline_index = text.rfind("\n", 0, start)
                if last_newline_index == -1:
                    col_num = start + 1
                else:
                    col_num = start - last_newline_index

                results.append({
                    "type": p["type"],
                    "match": match.group(),
                    "line": line_num,
                    "column": col_num
                })

        return results


class ResultExporter:
    def __init__(self, output_path: str):
        self.output_path = output_path

    def export(self, results: list[dict]):
        if not results:
            print("no results to export.")
            return

        with open(self.output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["type", "match", "line", "column"])
            writer.writeheader()
            writer.writerows(results)



class RegexApp:
    def __init__(self, input_file: str, output_file: str, patterns: list[dict]):
        self.reader = FileReader(input_file)
        self.extractor = PatternExtractor(patterns)
        self.exporter = ResultExporter(output_file)

    def run(self):
        text = self.reader.read()
        results = self.extractor.extract(text)
        self.exporter.export(results)
