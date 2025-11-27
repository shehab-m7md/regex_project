from regex_tool import RegexApp
from patterns import PATTERNS   

if __name__ == "__main__":
    app = RegexApp(
        input_file="C:/Users/user/OneDrive/Desktop/regex/input.txt",
        output_file="C:/Users/user/OneDrive/Desktop/regex/results.csv",
        patterns=PATTERNS
    )
    app.run()


