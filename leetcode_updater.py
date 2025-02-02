import requests
import os
import argparse
from pathlib import Path

# LeetCode GraphQL API endpoint
LEETCODE_API_URL = "https://leetcode.com/graphql"

# GraphQL query to fetch problem details
PROBLEM_QUERY = """
query getQuestionDetail($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
        questionId
        title
        titleSlug
        difficulty
        content
        likes
        dislikes
        isPaidOnly
        topicTags {
            name
            slug
        }
        codeSnippets {
            lang
            langSlug
            code
        }
        hints
        exampleTestcases
        stats
        similarQuestions
        contributors {
            username
            profileUrl
        }
    }
}
"""

# Headers for the request
HEADERS = {
    "Content-Type": "application/json",
}

CPP_HEAD = (
    "#include <iostream> \n" +
    "#include <vector> \n" +
    "#include <string> \n" +
    "#include <algorithm> \n" +
    "#include <unordered_map> \n" +
    "#include <map> \n" +
    "#include <unordered_set> \n" +
    "#include <set> \n" +
    "#include <queue> \n" +
    "#include <stack> \n" +
    "#include <deque> \n" +
    "#include <cmath> \n" +
    "#include <limits> \n" +
    "\nusing namespace std; \n \n"
)

CPP_MAIN = (
    "\n\n" +
    "int main(){ \n" +
    "\n\n" +
    "  return 0;\n" +
    "}\n"
)

PYTHON_MAIN = (
    "if __name__ == '__main__':\n" +
    "    pass"
    "\n"
)


def fetch_problem_details(title_slug):
    """Fetch problem details from Leetcode API."""
    payload = {
        "operationName": "getQuestionDetail",
        "variables": {"titleSlug": title_slug},
        "query": PROBLEM_QUERY,
    }

    response = requests.post(
        LEETCODE_API_URL, 
        json=payload,
        headers=HEADERS
    )

    if response.status_code == 200:
        return response.json()["data"]["question"]
    else:
        raise Exception(
            f"Failed to fetch problem details: {response.status_code}"
        )


def get_code_snippet(language, p):
    return [
        code_snippet["code"]
        for code_snippet in p["codeSnippets"]
        if code_snippet['lang'] == language
    ][0]


def create_problem_file(problem, lang):
    """Create a markdown file for the problem with Python and C++ solutions."""
    problem_id = problem["questionId"]
    title = problem["title"]
    title_slug = problem["titleSlug"]
    difficulty = problem["difficulty"]
    content = problem["content"]
    folder_name = f"{problem_id.zfill(4)}-{title.lower().replace(' ', '-')}"
    folder_path = Path(f'leetcode/{folder_name}')
    folder_path.mkdir(exist_ok=True)

    # Create README.md
    readme_content = f"""# {problem_id}. {title}
## Problem Statement
{content}


## Difficulty
**{difficulty}**
"""

    if lang == "py":
        extension = "py"
        author = "# Amir Mukhtarov, mukhtarov.amir.a@gmail.com \n"
        snippet_lang = "Python3"
        code_snippet = get_code_snippet(snippet_lang, problem)
        solution_content = f'{author}{code_snippet}\n\n{PYTHON_MAIN}'
    elif lang == "cpp":
        extension = "cpp"
        author = "// Amir Mukhtarov, mukhtarov.amir.a@gmail.com \n"
        snippet_lang = "C++"
        code_snippet = get_code_snippet(snippet_lang, problem)
        solution_content = f'{author}{CPP_HEAD}{code_snippet}\n{CPP_MAIN}'
    else:
        Exception("Incorrect programing language")

    with open(folder_path / "README.md", "w") as f:
        f.write(readme_content)

    # save solution files
    with open(folder_path / f"{title_slug}.{extension}", "w") as f:
        f.write(solution_content)

    return folder_name


def update_readme_table(problem, lang):
    """Update the main README.md with a table of solutions."""
    problem_id = problem["questionId"]
    title = problem["title"]
    title_slug = problem["titleSlug"]
    difficulty = problem["difficulty"]
    folder_name = f"{problem_id.zfill(4)}-{title.lower().replace(' ', '-')}"
    readme_path = Path("README.md")

    if lang == "py":
        extension = "py"
        # author = "# Amir Mukhtarov, mukhtarov.amir.a@gmail.com \n"
        # snippet_lang = "Python3"
        # code_snippet = get_code_snippet(snippet_lang, problem)

    elif lang == "cpp":
        extension = "cpp"
        # author = "// Amir Mukhtarov, mukhtarov.amir.a@gmail.com \n"
        # snippet_lang = "C++"
        # code_snippet = get_code_snippet(snippet_lang, problem)

    else:
        Exception("Incorrect programing language") 

    # Solution links
    link = f"[Python](leetcode/{folder_name}/{title_slug}.{extension})" 
    print(link)
    
    # if "python" in solutions else ""
    # cpp_link = f"[C++](leetcode/{folder_name}/solution.cpp)" if "cpp" in solutions else ""
    
    # solution_links = " | ".join(link)

    # Create table entry
    table_entry = f"| {problem_id} | [{title}](leetcode/{folder_name}/README.md) | {difficulty} | {link} |\n"

    # Add table entry to README.md
    if not readme_path.exists():
        with open(readme_path, "w") as f:
            f.write("# LeetCode Solutions\n\n")
            f.write("| # | Title | Difficulty | Solutions |\n")
            f.write("|---|-------|------------|-----------|\n")

    with open(readme_path, "a") as f:
        f.write(table_entry)


def get_multi_line_input(lang):
    """Capture multi-line input from the user."""
    print(f"Paste your {lang} solution code (Press Enter twice to finish):")
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "":  # Stop reading on an empty line
                break
            lines.append(line)
        except EOFError:  # Handle Ctrl+D (EOF) for some terminals
            break
    return "\n".join(lines) if lines else None



def main():
    parser = argparse.ArgumentParser(description="Leetcode auto filling")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-c",
        action="store_true", 
        help="Enable option C (Create problem)"
    )
    group.add_argument(
        "-d",
        action="store_true",
        help="Enable option D (Done problem)"
    )

    parser.add_argument("lang", type=str, help="Programming language")
    parser.add_argument("title_slug", type=str, help="Problem title slug") 
    args = parser.parse_args()

    # Fetch problem details
    problem = fetch_problem_details(args.title_slug)
    lang = args.lang

    if args.c:
        # Create solution folder and markdown file
        create_problem_file(problem, lang)

    elif args.d:
        print("Option -d was selected.")
        # Update README.md
        update_readme_table(problem, lang)

    # Input: Problem title slug
    # title_slug = input("Enter the problem title slug (e.g., two-sum): ").strip()
    
    # solutions = {}

    # # Get Python solution
    # python_solution = get_multi_line_input("Python")
    # if python_solution:
    #     solutions["python"] = python_solution

    # # Get C++ solution
    # cpp_solution = get_multi_line_input("C++")
    # if cpp_solution:
    #     solutions["cpp"] = cpp_solution





    

    print(f"Successfully added solution for problem: {problem['title']}")


if __name__ == "__main__":
    main()
