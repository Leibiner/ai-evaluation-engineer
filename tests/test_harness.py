from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path


ROOT = Path(__file__).parents[1]
MODULE_PATH = ROOT / "08-evaluation-engineering" / "harness" / "core.py"
spec = spec_from_file_location("harness_core", MODULE_PATH)
module = module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)

EvalCase = module.EvalCase
EvaluationHarness = module.EvaluationHarness


def test_harness_runs_cases_and_calculates_pass_rate():
    cases = [
        EvalCase("case-1", "hello", expected="HELLO"),
        EvalCase("case-2", "world", expected="WORLD"),
    ]

    harness = EvaluationHarness(
        target=lambda text: text.upper(),
        grader=lambda case, output: float(output == case.expected),
    )

    results = harness.run(cases)

    assert len(results) == 2
    assert harness.pass_rate(results) == 1.0
