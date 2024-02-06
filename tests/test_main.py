from pytest import CaptureFixture


def test_print(capfd: CaptureFixture[str]) -> None:
    import intro.main

    captured = capfd.readouterr()
    assert captured.out.strip().lower().removesuffix("!") == "hello world"
