class PEP8:

    def __init__(self, code: list):
        self.issues = set()
        self.code = code

    def check_length(self, ln_num, line):
        if len(line) > 79:
            self.issues.add(f"Line {ln_num}: S001 Too Long")

    def output_issues(self):
        for issue in self.issues:
            print(issue)

    def run_check(self):
        for ln_num, line in enumerate(self.code, 1):
            self.check_length(ln_num, line)


class StaticCodeAnalyzer:

    def __init__(self):
        self.directory = None
        self.code = None

    @staticmethod
    def read_file(file_location: str) -> list:
        with open(file_location, 'r') as file:
            return file.readlines()

    def main(self):
        self.directory = input()
        self.code = self.read_file(self.directory)

        pep8_obj = PEP8(self.code)
        pep8_obj.run_check()
        pep8_obj.output_issues()


program = StaticCodeAnalyzer()
program.main()

