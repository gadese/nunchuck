"""End-to-end CLI tests: exit codes, output format, error messages."""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from kg.cli import main


@pytest.fixture
def input_file(planted_graph_data: dict, tmp_path: Path) -> str:
    """Write planted graph data to a temp JSON file and return its path."""
    path = tmp_path / "input.json"
    path.write_text(json.dumps(planted_graph_data), encoding="utf-8")
    return str(path)


class TestValidateCommand:
    def test_valid_input(self, input_file: str) -> None:
        exit_code = main(["validate", input_file])
        assert exit_code == 0

    def test_invalid_input(self, tmp_path: Path) -> None:
        bad_file = tmp_path / "bad.json"
        bad_file.write_text('{"nodes": [1], "edges": []}')
        exit_code = main(["validate", str(bad_file)])
        assert exit_code == 2

    def test_missing_file(self) -> None:
        with pytest.raises(SystemExit) as exc_info:
            main(["validate", "/nonexistent/file.json"])
        assert exc_info.value.code == 2

    def test_malformed_json(self, tmp_path: Path) -> None:
        bad_file = tmp_path / "malformed.json"
        bad_file.write_text("{not valid json")
        with pytest.raises(SystemExit) as exc_info:
            main(["validate", str(bad_file)])
        assert exc_info.value.code == 2


class TestAnalyzeCommand:
    def test_text_output(
        self, input_file: str, capsys: pytest.CaptureFixture[str]
    ) -> None:
        exit_code = main(["analyze", input_file])
        assert exit_code == 0
        captured = capsys.readouterr()
        assert "KNOWLEDGE GRAPH ANALYSIS REPORT" in captured.out
        assert "COMMUNITIES" in captured.out

    def test_json_output(
        self, input_file: str, capsys: pytest.CaptureFixture[str]
    ) -> None:
        exit_code = main(["analyze", input_file, "--format", "json"])
        assert exit_code == 0
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert "communities" in data
        assert "gaps" in data
        assert "bridges" in data
        assert "modularity" in data
        assert "node_count" in data
        assert "edge_count" in data

    def test_visualization(self, input_file: str, tmp_path: Path) -> None:
        html_path = str(tmp_path / "graph.html")
        exit_code = main(["analyze", input_file, "--visualize", html_path])
        assert exit_code == 0
        assert os.path.exists(html_path)
        content = Path(html_path).read_text()
        assert "<html>" in content.lower() or "<!doctype" in content.lower()

    def test_seed_flag(
        self, input_file: str, capsys: pytest.CaptureFixture[str]
    ) -> None:
        exit_code = main(["analyze", input_file, "--seed", "123", "--format", "json"])
        assert exit_code == 0
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["node_count"] == 48

    def test_invalid_input_exit_code(self, tmp_path: Path) -> None:
        bad_file = tmp_path / "bad.json"
        bad_file.write_text('{"nodes": ["a"], "edges": [{"source": "x"}]}')
        exit_code = main(["analyze", str(bad_file)])
        assert exit_code == 2

    def test_missing_file_exit_code(self) -> None:
        with pytest.raises(SystemExit) as exc_info:
            main(["analyze", "/nonexistent/file.json"])
        assert exc_info.value.code == 2


class TestModuleEntryPoint:
    def test_python_m_kg(self, input_file: str) -> None:
        """Test that `python -m kg` works."""
        result = subprocess.run(
            [sys.executable, "-m", "kg", "validate", input_file],
            capture_output=True,
            text=True,
            cwd=str(Path(__file__).parent.parent),
        )
        assert result.returncode == 0
