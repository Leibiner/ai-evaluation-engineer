from dataclasses import dataclass, field
from typing import Any, Callable, Iterable


@dataclass
class EvalCase:
    """A single evaluation task."""

    case_id: str
    input: Any
    expected: Any | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class TrialResult:
    """One execution of an EvalCase."""

    case_id: str
    output: Any
    score: float
    passed: bool
    trace: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


class EvaluationHarness:
    """Minimal runner: execute cases, grade outputs, aggregate results."""

    def __init__(
        self,
        target: Callable[[Any], Any],
        grader: Callable[[EvalCase, Any], float],
    ) -> None:
        self.target = target
        self.grader = grader

    def run(self, cases: Iterable[EvalCase]) -> list[TrialResult]:
        results: list[TrialResult] = []
        for case in cases:
            output = self.target(case.input)
            score = float(self.grader(case, output))
            results.append(
                TrialResult(
                    case_id=case.case_id,
                    output=output,
                    score=score,
                    passed=score >= 1.0,
                )
            )
        return results

    @staticmethod
    def pass_rate(results: Iterable[TrialResult]) -> float:
        results = list(results)
        if not results:
            return 0.0
        return sum(r.passed for r in results) / len(results)
