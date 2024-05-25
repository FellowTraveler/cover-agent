# Generated by CodiumAI

import pytest
import yaml
from yaml.scanner import ScannerError

from cover_agent.utils import load_yaml


class TestLoadYaml:
    #  Tests that load_yaml loads a valid YAML string
    def test_load_valid_yaml(self):
        yaml_str = "name: John Smith\nage: 35"
        expected_output = {"name": "John Smith", "age": 35}
        assert load_yaml(yaml_str) == expected_output

    def test_load_invalid_yaml1(self):
        yaml_str = '''\
PR Analysis:
  Main theme: Enhancing the `/describe` command prompt by adding title and description
  Type of PR: Enhancement
  Relevant tests: No
  Focused PR: Yes, the PR is focused on enhancing the `/describe` command prompt.

PR Feedback:
  General suggestions: The PR seems to be well-structured and focused on a specific enhancement. However, it would be beneficial to add tests to ensure the new feature works as expected.
  Code feedback:
    - relevant file: pr_agent/settings/pr_description_prompts.toml
      suggestion: Consider using a more descriptive variable name than 'user' for the command prompt. A more descriptive name would make the code more readable and maintainable. [medium]
      relevant line: user="""PR Info: aaa
  Security concerns: No'''
        with pytest.raises(ScannerError):
            yaml.safe_load(yaml_str)

        expected_output = {
            "PR Analysis": {
                "Main theme": "Enhancing the `/describe` command prompt by adding title and description",
                "Type of PR": "Enhancement",
                "Relevant tests": False,
                "Focused PR": "Yes, the PR is focused on enhancing the `/describe` command prompt.",
            },
            "PR Feedback": {
                "General suggestions": "The PR seems to be well-structured and focused on a specific enhancement. However, it would be beneficial to add tests to ensure the new feature works as expected.",
                "Code feedback": [
                    {
                        "relevant file": "pr_agent/settings/pr_description_prompts.toml",
                        "suggestion": "Consider using a more descriptive variable name than 'user' for the command prompt. A more descriptive name would make the code more readable and maintainable. [medium]",
                        "relevant line": 'user="""PR Info: aaa',
                    }
                ],
                "Security concerns": False,
            },
        }
        assert (
            load_yaml(
                yaml_str,
                keys_fix_yaml=[
                    "relevant line:",
                    "suggestion content:",
                    "relevant file:",
                    "existing code:",
                    "improved code:",
                ],
            )
            == expected_output
        )

    def test_load_invalid_yaml2(self):
        yaml_str = """\
- relevant file: src/app.py:
  suggestion content: The print statement is outside inside the if __name__ ==: \
"""
        with pytest.raises(ScannerError):
            yaml.safe_load(yaml_str)

        expected_output = [
            {
                "relevant file": "src/app.py:",
                "suggestion content": "The print statement is outside inside the if __name__ ==:",
            }
        ]
        assert (
            load_yaml(
                yaml_str,
                keys_fix_yaml=[
                    "relevant line:",
                    "suggestion content:",
                    "relevant file:",
                    "existing code:",
                    "improved code:",
                ],
            )
            == expected_output
        )

# auto-generated by cover agent
def test_try_fix_yaml_snippet_extraction():
    from cover_agent.utils import try_fix_yaml
    yaml_str = "```yaml\nname: John Smith\nage: 35\n```"
    expected_output = {"name": "John Smith", "age": 35}
    assert try_fix_yaml(yaml_str) == expected_output

def test_try_fix_yaml_remove_all_lines():
    from cover_agent.utils import try_fix_yaml
    yaml_str = "name: John Smith\nage: 35\ninvalid_line"
    expected_output = {"name": "John Smith", "age": 35}
    assert try_fix_yaml(yaml_str) == expected_output
